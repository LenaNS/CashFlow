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
    search_fields:
        Список полей по которым выполняется поиск.
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
        ('created_at', DateFieldListFilter),          # Фильтрация по дате создания
        'status',              # Фильтрация по статусу
        'transaction_type',    # Фильтрация по типу транзакции
        'category',            # Фильтрация по категории
        'subcategory',         # Фильтрация по подкатегории
    )


@register(Status)
class StatusAdmin(ModelAdmin):
    list_display = (
        "name",
    )


@register(TransactionType)
class TransactionTypeAdmin(ModelAdmin):
    list_display = (
        "name",
    )
    filter_horizontal = ['categories']


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = (
        "name",
    )
    filter_horizontal = ['subcategories']

@register(Subcategory)
class SubcategoryAdmin(ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = (
        "name",
    )
