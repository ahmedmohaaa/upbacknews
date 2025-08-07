from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import News

class NewsForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'
