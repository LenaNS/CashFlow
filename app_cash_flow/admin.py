from django.contrib import admin
from django.contrib.admin import ModelAdmin, register, DateFieldListFilter
from .models import *


@register(CashFlow)
class CashFlowAdmin(ModelAdmin):
    """
    Панель администрирования ДДС.

    Поля
    ----
    list_display:
        Список отображаемых полей.
    list_filter:
        Список полей, по которым доступны фильтры.
    """

    list_display = (
        "created_at",
        "status",
        "transaction_type",
        "category",
        "subcategory",
        "amount",
        "comment",
    )

    list_filter = (
        'created_at',
        'status',
        'transaction_type',
        'category',
        'subcategory',
    )


@register(Status)
class StatusAdmin(ModelAdmin):
    """
    Панель администрирования Статусов.

    Поля
    ----
    list_display:
        Список отображаемых полей.
    """
    list_display = (
        "name",
    )


@register(TransactionType)
class TransactionTypeAdmin(ModelAdmin):
    """
    Панель администрирования Типов.

    Поля
    ----
    list_display:
        Список отображаемых полей.
    filter_horizontal:
        Интерфейс для выбора категорий (Many-to-Many).
    """
    list_display = (
        "name",
    )
    filter_horizontal = ['categories']


@register(Category)
class CategoryAdmin(ModelAdmin):
    """
    Панель администрирования Категорий.

    Поля
    ----
    list_display:
        Список отображаемых полей.
    search_fields:
        Указывает, по каким полям можно выполнять поиск.
    filter_horizontal:
        Интерфейс для выбора категорий (Many-to-Many).
    """
    list_display = (
        "name",
    )
    search_fields = (
        "name",
    )
    filter_horizontal = ['subcategories']


@register(Subcategory)
class SubcategoryAdmin(ModelAdmin):
    """
    Панель администрирования Покатегорий.

    Поля
    ----
    list_display:
        Список отображаемых полей.
    search_fields:
        Указывает, по каким полям можно выполнять поиск.
    """
    list_display = (
        "name",
    )
    search_fields = (
        "name",
    )
