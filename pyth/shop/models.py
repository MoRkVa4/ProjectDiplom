from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def str(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    image = models.ImageField(verbose_name="Фото", blank=True, null=True)
    title = models.CharField(verbose_name="Название Товара", max_length=150)
    price = models.CharField(verbose_name="Цена", max_length=150)
    description = models.TextField(verbose_name="Описание Техники", max_length=200)
    publisher = models.CharField(verbose_name="Издатель", max_length=150, null=True)
    data = models.DateField(verbose_name="Дата выхода", auto_now_add=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def str(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Продук"
        verbose_name_plural = "Продукты"

