from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey


class Status(models.Model):
    """
    Модель статуса ДДС.

    Поля
    ----
    name:
        Название статуса.
    """
    name = models.CharField(verbose_name="Название статуса", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус ДДС"
        verbose_name_plural = "Статусы ДДС"


class Subcategory(models.Model):
    """
       Модель подкатегории.

       Поля
       ----
       category:
           Категория, к которой относится подкатегория.
       name:
           Название подкатегории.
       """
    name = models.CharField(verbose_name="Название подкатегории", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Category(models.Model):
    """
    Модель категории расхода/дохода.

    Поля
    ----
    name:
        Название категории.
    """
    name = models.CharField(verbose_name="Название категории", max_length=100, unique=True)
    subcategories = models.ManyToManyField(verbose_name="Подкатегории", to=Subcategory, related_name="categories")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class TransactionType(models.Model):
    """
    Модель типа ДДС.

    Поля
    ----
    name:
        Название типа транзакции.
    """
    name = models.CharField(verbose_name="Название типа", max_length=50, unique=True)
    categories = models.ManyToManyField(verbose_name="Категории", to=Category, related_name="types")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип ДДС"
        verbose_name_plural = "Типы ДДС"


class CashFlow(models.Model):
    """
        Модель записей о движении денежных средств.

        Поля
        ----
        created_at:
            Дата и время создания записи о ДДС. Заполняется автоматически.
        status:
            Статус ДДС.
        transaction_type:
            Тип ДДС.
        category:
            Категория, к которой относится ДДС.
        subcategory:
            Подкатегория, к которой относится ДДС.
        amount:
            Сумма ДДС в рублях.
        comment:
            Необязательное текстовое поле для комментария.
        """
    created_at = models.DateField(verbose_name="Дата создания записи", default=timezone.now)
    status = models.ForeignKey(verbose_name="Статус ДДС", to=Status, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(verbose_name="Тип ДДС", to=TransactionType, on_delete=models.CASCADE)
    category = ChainedForeignKey(verbose_name="Категория", to=Category, on_delete=models.CASCADE, chained_field="transaction_type", chained_model_field="types")
    subcategory = ChainedForeignKey(verbose_name="Подкатегория", to=Subcategory, on_delete=models.CASCADE, chained_field="category", chained_model_field="categories")
    amount = models.DecimalField(max_digits=10, decimal_places=2,blank=False, null=False,  verbose_name="Сумма ДДС (в рублях)")
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)

    def __str__(self):
        return f'{self.transaction_type.name} - {self.amount} руб.'

    class Meta:
        verbose_name = "ДДС"
        verbose_name_plural = "ДДС"
