from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from DM.models import Blog, Category
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

class YeniKullaniciView(TemplateView):
    template_name = 'yeni_kullanici.html'

class KayitOlView(CreateView):
    model = User
    template_name = 'kayit_ol.html'
    fields = ['username', 'password', 'email']

    success_url = reverse_lazy('yeni-kullanici')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

data = {
    "blogs": [
        {
           "id": 1,
           "title": "Eğitim Notları",
           "image": "Ceren1.jpg",
           "is_active": True,
           "is_home": True,
           "description": "Son Turnuva Güncel Konular",
        },
        {
           "id": 2,
           "title": "Münazırlar İçin Yemek Programı",
           "image": "Ceren2.jpg",
           "is_active": True,
           "is_home": True,
           "description": "Turunuva sırasındaki yemek listesi ",
        },
        {
           "id": 3,
           "title": "Münazara Dövüş Teknikleri",
           "image": "Ceren3.jpg",
           "is_active": True,
           "is_home": True,
           "description": "Kendinizi geliştirebilmeniz için yarışma sitilleri",
        }
    ]
}

# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True),
        "categories": Category.objects.all()}
    return render(request, "DM/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.all(),
        "blogs": Blog.objects.filter(is_home=False),
        "categories": Category.objects.all()
    }
    return render(request, "DM/blogs.html", context)

def Admin(request):
    return render(request, "DM/Admin.html")

def Kayıt(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Üyeliğiniz başarıyla oluşturuldu. Şimdi giriş yapabilirsiniz.')
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, "DM/Kayıt.html", {'form': form})

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "DM/blog_details.html", {
        "blog": blog})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Admin')  # Kullanıcı kayıt olduktan sonra giriş sayfasına yönlendirin
    else:
        form = CustomUserCreationForm()
    return render(request, 'DM/Kayıt.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Kullanıcı kayıt olduktan sonra giriş sayfasına yönlendirin
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('anasayfa')  # Başarılı giriş yapan kullanıcıyı ana sayfaya yönlendirir
        else:
            error_message = "Kullanıcı adı veya şifre hatalı."
            return render(request, 'DM/login.html', {'error_message': error_message})
    else:
        return render(request, 'DM/login.html')
    
def blogs_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(is_active=True, categories__slug=slug)
    context = {
        "category": category,
        "blogs": blogs,
    }
    return render(request, "DM/blogs.html", context)