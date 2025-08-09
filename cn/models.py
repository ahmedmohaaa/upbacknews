from django.db import models
from django.utils import timezone

class News(models.Model):
    class C(models.TextChoices):
        SPORTS = 'رياضى', 'رياضى'
        ARTICLE = 'مقالى', 'مقالى'
        OTHER = 'اخر', 'اخر'

    title = models.CharField(
        max_length=2000, 
        blank=True, 
        null=True,
        verbose_name="عنوان الخبر"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="وصف الخبر"
    )

    is_featured = models.BooleanField(default=False, verbose_name="خبر مميز")

    image = models.ImageField(
        upload_to='uploads/news/', 
        blank=True, 
        null=True,
        verbose_name="الصورة الرئيسية"
    )

    category = models.CharField(
        max_length=10,
        choices=C.choices,
        default=C.OTHER,
        verbose_name="التصنيف"
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاريخ الإضافة"
    )

    def __str__(self):
        return self.title
    
