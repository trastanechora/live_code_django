from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('item_description/<int:requested_id>', views.get_page_description, name="item_description"),
   path('new_item', views.model_form_upload, name="new_item"),
]
