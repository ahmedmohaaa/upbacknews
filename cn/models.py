from django.db import models
from ckeditor.fields import RichTextField
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
    description = RichTextField(
        blank=True, 
        null=True,
        verbose_name="وصف الخبر"
    )
    image = models.ImageField(
        upload_to='uploads/news/', 
        blank=True, 
        null=True,
        verbose_name="الصورة الرئيسية"
    )

    category = models.CharField(
        max_length=10,
        choices=C.choices,
        default=C.ARTICLE,
        verbose_name="التصنيف"
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاريخ الإضافة"
    )

    def __str__(self):
        return self.title
    
class NewsImage(models.Model):
      news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
      image = models.ImageField(upload_to='uploads/news/more/')
      def __str__(self):
         return f"صورة لـ {self.news.title}"
