from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
from .forms import BlogPostModelForm
# from .forms import BlogPostForm
from .models import BlogPost
from .models import SearchQuery

# def blog_post_detail_page(request, slug):

#     obj 		= get_object_or_404(BlogPost, slug=slug)

#     context     = {"object": obj}

#     template_name = "blog_post_detail.html"

#     return render(request, template_name , context)

def search_view(request):
	query = request.GET.get('q', None)
	user = None
	if request.user.is_authenticated:
		user = request.user
	context = {
		'query': query
	}

	if query is not None:
		SearchQuery.objects.create(users=user, query=query)
		blog_list = BlogPost.objects.search(query=query)
		context = {
			"blog_list" : blog_list,
			"query" : query,
			"title" : "Blog | Search"
		}
	return render(request, "blog_app/search.html", context)


def blog_post_list_view(request):
	qs = BlogPost.objects.all().published()

	# only show posts created by the user to them if they are logged in
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs= (qs | my_qs).distinct()

	template_name	= "blog_app/list.html"
	context			= {"object_list": qs, "title" : "Blog | All"}
	return render(request,template_name,context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
	form = BlogPostModelForm(request.POST or None, request.FILES or None)
	if not request.user.is_authenticated:
		return render(request, not_a_user.html, {})
	if form.is_valid():
		obj = form.save(commit= False)
		obj.user = request.user
		form.save()
		form = BlogPostModelForm()
	template_name	= "blog_app/form.html"
	context			= {'form': form , "title" : "Create"}
	return render(request, template_name ,context)

def blog_post_detail_view(request, slug):
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context     = {"object": obj, "title":"Blog | Detail"}
	template_name = "blog_app/detail.html"
	return render(request, template_name , context)

@staff_member_required
def blog_post_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None ,request.FILES or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect("/blog")
	template_name = 'blog_app/form.html'
	context = {'form': form , 'title' : f"Update {obj.title}"}
	return render(request,template_name,context)

@staff_member_required
def blog_post_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog_app/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/blog")
	context = {"object": obj }
	return render(request, template_name , context)
