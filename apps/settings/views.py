from django.shortcuts import render,redirect
from .models import InfoUser,About,Skiils,Contact,Experience,Blog,Portfolio
# Create your views here.
def index(request):
    infouser = InfoUser.objects.latest("id")
    return render(request,"index.html", locals())

def about(request):
    info_me = About.objects.latest("id")
    skiils = Skiils.objects.all()
    experience = Experience.objects.all()
    experience_2 = Experience.objects.all()
    return render(request, "about.html", locals())

def contacts(request):
    infouser = InfoUser.objects.latest("id")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name= name, email = email, message = message)
        return redirect('index')
    return render(request, "contact.html", locals())


def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", locals())

def portfolio(request):
    portfolio = Portfolio.objects.all()
    return render(request, "portfolio.html", locals())
