from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from DM.models import Blog


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
        "blogs": Blog.objects.filter(is_active=True, is_home=True)
    }
    return render(request, "DM/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.all(is_active=True)
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
            return redirect('login')  # Kullanıcı kayıt olduktan sonra giriş sayfasına yönlendirin
    else:
        form = UserCreationForm()
    return render(request, "DM/Kayıt.html", {'form': form})

def blog_details(request, id):
    #blogs = data["blogs"]
    #selectedBlog = None

    # id değerini integer'a dönüştür

    #for blog in blogs:
        #if blog["id"] == id:
            #selectedBlog = blog
            #break  # Eşleşen blog bulunduğunda döngüyü durdur
    

    blog = Blog.objects.get(id=id)
    return render(request, "DM/blog_details.html", {
        "blog": blog


    })



    

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
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
