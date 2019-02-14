from django.shortcuts import render
from .models import Product
from .forms import PostForm

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'home/home.html', {'products':product})

def get_page_description(request, requested_id):
    content = Product.objects.get(pk=requested_id)
    return render(request, 'item.html', {'content': content})

def model_form_upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'new_item.html', {
        'form': form
    })