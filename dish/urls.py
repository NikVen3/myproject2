from django.urls import path
from . import views
from .views import AddIngredientView, AddDishView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cocktail'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_ingredients/', AddIngredientView.as_view(), name='add_ingredient'),
    path('add_receipt/', AddDishView.as_view(), name='add_recipe'),
    path('all_cocktails/', views.all_dishs, name='all_dish'),
    path('cocktails/<slug:slug>/', views.dish_detail, name='dish_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)