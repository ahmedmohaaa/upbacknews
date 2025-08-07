from django.shortcuts import render, redirect,get_object_or_404
from .forms import NewsForm
from .models import News
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_change_done')  # ← هنا بتحدد صفحة النجاح


def index(request):
    all_news_list = News.objects.all().order_by('-created_at')
    
    # تحديد عدد الأخبار في كل صفحة
    paginator = Paginator(all_news_list, 15)  # 25 خبر في الصفحة

    # الحصول على رقم الصفحة المطلوبة من الرابط (GET parameter)
    page_number = request.GET.get('page')

    # الحصول على الصفحة المطلوبة
    all_news = paginator.get_page(page_number)

    news = News.objects.filter(category='رياضى').order_by('-created_at')
    articales = News.objects.filter(category='مقالى').order_by('-created_at')
    lnews = News.objects.order_by('-created_at').first() 
    
    return render(request, 'index.html', {
        'news': news,
        'allnews': all_news,
        'arts': articales,
        'lnews': lnews
    })

def details(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'details.html', {'news': news_item})

@login_required(login_url='login')
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


def all_articles_view(request):
    articles = News.objects.filter(category='مقالى').order_by('-created_at')
    return render(request, 'articles.html', {'arts': articles})


def sports_news_view(request):
    news = News.objects.filter(category='رياضى').order_by('-created_at')
    return render(request, 'sports.html', {'sports': news})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('crud')  # غيرها حسب الصفحة الرئيسية عندك
            else:
                messages.error(request, 'بيانات الدخول غير صحيحة.')
        else:
            messages.error(request, 'خطأ في البيانات المُدخلة.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
