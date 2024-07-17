from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CategoryDish, CategoryIngredient, Ingredient, Dish

admin.site.site_header = 'Verre - сайт рецептов алкогольных напитков'
admin.site.site_title = 'Администрирование сайта'
admin.site.index_title = 'Администрирование сайта'


@admin.register(CategoryDish)
class CategoryDishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', "slug")
    list_display_links = ('name',)
    list_editable = ["slug", ]
    search_fields = ('name', "slug")
    fields = [
        "name",
        "slug",
    ]


@admin.register(CategoryIngredient)
class CategoryIngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', "slug")
    list_display_links = ('name',)
    list_editable = ["slug", ]
    search_fields = ('name', "slug")
    fields = [
        "name",
        "slug",
    ]


class CategoryModelInline(admin.TabularInline):
    model = Ingredient.categories.through
    extra = 0  # если указать 1, то в админке сразу подтягивается название 1‑го ингредиента(если он есть)
    verbose_name = "Ингридиент"
    verbose_name_plural = "Ингридиенты"
    can_delete = False
    can_change = False


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    list_filter = ["name", "slug"]

    def image(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.photo.url))
        else:
            return 'No image'

    image.allow_tags = True
    fields = [
        "name",
        "slug",
        "description",
        "image",
    ]
    # Отображение "categories" через "through"
    inlines = (CategoryModelInline,)


class CategoryDishModelInline(admin.TabularInline):
    model = Dish.categories.through
    extra = 0
    verbose_name = "Ингридиент"
    verbose_name_plural = "Ингридиенты"
    can_delete = False
    can_change = False


class CategoryCocktailTwoModelInline(admin.TabularInline):
    model = Dish.ingredients.through
    extra = 0
    verbose_name = "Ингридиент"
    verbose_name_plural = "Ингридиенты"
    can_delete = False
    can_change = False




@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'description', 'preparation_time','preparation_steps', 'preparation_time']
    search_fields = ['title', 'author']
    list_filter = ['title', 'author']
    fields = [
        "title",
        "slug",
        "description",
        "preparation_steps",
        "preparation_time",
        "image",
        "author",
    ]

    def image(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.photo.url))
        else:
            return 'No image'

    image.allow_tags = True
    # Отображение "categories" через "through"
    inlines = (CategoryDishModelInline,)