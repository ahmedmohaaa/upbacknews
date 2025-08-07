from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class News(models.Model):
    class C(models.TextChoices):
        SPORTS = 'رياضى', 'رياضى'
        ARTICLE = 'مقالى', 'مقالى'
        other='اخر','اخر'

    title = models.CharField(max_length=2000, blank=True, null=True)  
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/news/', blank=True, null=True)

    category = models.CharField(
        max_length=10,
        choices=C.choices,
        default=C.ARTICLE
    )
    created_at = models.DateTimeField(default=timezone.now)  # التاريخ والوقت الحالي تلقائيًا


    def __str__(self):
        return self.title
