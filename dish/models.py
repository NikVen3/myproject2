from django.db import models as m
from django.urls import reverse


class CategoryDish(m.Model):
    name = m.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return f"Категория: {self.name}, slug{self.slug}"

    class Meta:
        verbose_name = 'Категория коктейля'
        verbose_name_plural = 'Категории коктейлей'
        ordering = ("id",)


class CategoryIngredient(m.Model):
    name = m.CharField(max_length=120, unique=True, verbose_name='Название')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return f"Категория: {self.name}, slug{self.slug}"

    class Meta:
        verbose_name = 'Категория ингредиента'
        verbose_name_plural = 'Категории ингредиентов'
        ordering = ("id",)


class Ingredient(m.Model):
    name = m.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = m.TextField(blank=True, null=True, verbose_name='Описание')
    image = m.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    categories = m.ManyToManyField(CategoryIngredient, verbose_name='Категория ингредиента')

    def __str__(self):
        return f"Название: {self.name}, Описание: {self.description}"

    def display_id(self):
        return f"{self.id:05}"

    class Meta:
        db_table = 'ingredient'
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ("id",)


class Dish(m.Model):
    title = m.CharField(max_length=128, unique=True, verbose_name='Название')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = m.TextField(verbose_name='Описание')
    preparation_steps = m.TextField(verbose_name='Шаги приготовления')
    preparation_time = m.PositiveIntegerField(verbose_name='Время приготовления (в минутах)')
    image = m.ImageField(upload_to='recipe_images', blank=True, null=True, verbose_name='Изображение')
    author = m.CharField(max_length=128, verbose_name='Автор')
    categories = m.ManyToManyField(CategoryDish, verbose_name='Категория блюда')
    ingredients = m.ManyToManyField(Ingredient, verbose_name='Ингридиенты')
    date_register = m.DateField(auto_now=True, verbose_name='Дата регистрации')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


    def __str__(self):
        return f"Название: {self.title}, Описание: {self.description}"

    def display_id(self):
        return f"{self.id:05}"

    class Meta:
        db_table = 'dish'
        verbose_name = 'Рецепт блюда'
        verbose_name_plural = 'Рецепты блюд'
        ordering = ("id",)


