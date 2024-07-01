from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = RichTextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    old_price = models.PositiveIntegerField(default=0, blank=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name='Product Image', upload_to='product/product_image/', blank=True, )

    datetime_created = models.DateTimeField(default=timezone.now())
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])



class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',)
    body = models.TextField(verbose_name='Text')
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name='Rating')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])

    def get_queryset(self):
        return Comment.objects.all().order_by(-'datetime_created')
