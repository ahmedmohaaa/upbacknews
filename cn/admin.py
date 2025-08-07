from django.contrib import admin
from .models import News, NewsImage

class NewsImageInline(admin.TabularInline):  # أو admin.StackedInline حسب التنسيق المفضل
    model = NewsImage
    extra = 10  # عدد الصفوف الفارغة لإضافة صور جديدة

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline]

admin.site.register(News, NewsAdmin)
