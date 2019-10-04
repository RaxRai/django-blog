from django.contrib import admin

# Register your models here.
from .models import BlogPost
from .models import SearchQuery

admin.site.register(BlogPost)
admin.site.register(SearchQuery)
