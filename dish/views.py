from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .forms import IngredientForm, DishForm, CategoryIngredientForm
from .models import Dish


def home_page(request):
    # Получаем 5 случайных блюд, не зависимо от авторизации
    recipes = Dish.objects.order_by('?')[:5]
    return render(request, 'dish/home.html', {'dish': recipes})


def add_category(request):
    if request.method == 'POST':
        form = CategoryIngredientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана! 🎉')
            return render(request, 'dish/add_category.html', {'form': form})
    else:
        form = CategoryIngredientForm()
    return render(request, 'dish/add_category.html', {'form': form})


class AddIngredientView(View):
    def get(self, request):
        form = IngredientForm()
        return render(request, 'dish/add_ingredient.html', {'form': form})

    def post(self, request):
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            messages.success(request, 'Ингредиент успешно создан! 🎉')
            return render(request, 'dish/add_ingredient.html', {'form': form})
        return render(request, 'dish/add_ingredient.html', {'form': form})




class AddDishView(View):
    model = Dish

    def get(self, request):
        form = DishForm()
        return render(request, 'dish/add_category.html', {'form': form})

    def post(self, request):
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, 'блюдо успешно создан! 🎉')
            return render(request, 'dish/add_category.html', {'form': form})
        return render(request, 'dish/add_category.html', {'form': form})


def all_dishs(request):
    dish = Dish.objects.all()
    context = {
        'dish': dish
    }
    return render(request, 'dish/all_dish.html', context)


def dish_detail(request, slug):
    dish = get_object_or_404(Dish, slug=slug)

    context = {
        'dish': dish
    }
    return render(request, 'dish/dish_detail.html', context)


