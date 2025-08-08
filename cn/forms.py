from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'image', 'category']
        labels = {
            'title': 'عنوان الخبر',
            'image': 'الصورة الرئيسية',
            'category': 'التصنيف',
        }
        widgets = {
            'description': SummernoteWidget(),
            'title': forms.TextInput(attrs={'style': 'width: 100%; padding:10px;'}),
            'image': forms.ClearableFileInput(attrs={'style': 'width: 100%; padding:10px;'}),
            'category': forms.Select(attrs={'style': 'width: 100%; padding:10px;'}),
        }
