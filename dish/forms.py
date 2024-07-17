from django import forms

from dish.models import Ingredient, Dish, CategoryIngredient, CategoryDish


class CategoryIngredientForm(forms.ModelForm):
    class Meta:
        model = CategoryIngredient
        fields = ['name', 'slug']


class CategoryDishForm(forms.ModelForm):
    class Meta:
        model = CategoryDish
        fields = ['name', 'slug']


class IngredientForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=CategoryIngredient.objects.all(),
        widget=forms.SelectMultiple,
        required=False
    )

    class Meta:
        model = Ingredient
        fields = [
            'name',
            'slug',
            'description',
            'image',
            'categories'
        ]


class DishForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=CategoryDish.objects.all(),

        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = [
            'title',
            'slug',
            'description',
            'preparation_steps',
            'preparation_time',
            'image',
            'author',
            'categories',
        ]