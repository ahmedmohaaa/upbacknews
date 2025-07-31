from django.shortcuts import render, redirect,get_object_or_404
from .forms import NewsForm
from .models import News


def index(request):
    all_news=News.objects.all().order_by('-created_at')
    news = News.objects.filter(category='رياضى').order_by('-created_at')
    articales = News.objects.filter(category='مقالى').order_by('-created_at')
    lnews = News.objects.order_by('-created_at').first() 
    return render(request, 'index.html', {'news': news,'allnews':all_news,'arts':articales,'lnews':lnews})

def details(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'details.html', {'news': news_item})


def crud(request, pk=None):
    if pk:
        instance = get_object_or_404(News, pk=pk)
    else:
        instance = None

    if request.method == 'POST':
        if 'delete_id' in request.POST:
            # حذف
            news = get_object_or_404(News, pk=request.POST['delete_id'])
            news.delete()
            return redirect('crud')

        form = NewsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = NewsForm(instance=instance)

    all_news = News.objects.all()
    return render(request, 'crud.html', {'form': form, 'all_news': all_news})