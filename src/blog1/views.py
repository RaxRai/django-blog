from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from blog_app.models import BlogPost

def home_page(request):
    my_title = "Blog | Home"
    qs = BlogPost.objects.all()[:5]
    context ={
        'title': my_title,
        'blogs' : qs,
    }

    return render(request, "homepage.html",context)

def about_page(request):
    return render(request, "about.html", {'title': 'About'})

def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)

	context = {"title" : "Blog | Contact" , "form" : form}

	return render(request, "form.html" , context)
