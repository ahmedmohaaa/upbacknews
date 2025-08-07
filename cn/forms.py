from django import forms
from .models import News
from ckeditor.widgets import CKEditorWidget

class NewsForm(forms.ModelForm):
    description = forms.CharField(
        widget=CKEditorWidget(), 
        label="وصف الخبر"
    )

    # ❌ حذفنا MultiFileInput واستخدمنا حقل FileField عادي بدون ويدجت مخصص


    class Meta:
        model = News
        fields = ['title', 'description', 'image', 'category']
        labels = {
            'title': 'عنوان الخبر',
            'image': 'الصورة الرئيسية',
            'category': 'التصنيف',
        }
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 100%; padding:10px;'}),
            'image': forms.ClearableFileInput(attrs={'style': 'width: 100%; padding:10px;'}),
            'category': forms.Select(attrs={'style': 'width: 100%; padding:10px;'}),
        }
