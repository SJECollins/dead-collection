from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='uploads/', null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added_on',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'https://8000-sjecollins-deadcollecti-hqlw5hgkfnf.ws-eu82.gitpod.io' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'https://8000-sjecollins-deadcollecti-hqlw5hgkfnf.ws-eu82.gitpod.io' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'https://8000-sjecollins-deadcollecti-hqlw5hgkfnf.ws-eu82.gitpod.io' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail