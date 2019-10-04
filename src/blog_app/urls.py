

from django.urls import path
from .views import (blog_post_detail_view,
                            blog_post_list_view,
                            blog_post_delete_view,
                            blog_post_update_view,
                            search_view)




urlpatterns = [


    path('<str:slug>/',blog_post_detail_view),
    path('<str:slug>/edit',blog_post_update_view),
    path('<str:slug>/delete',blog_post_delete_view),
    path('', blog_post_list_view),
    

]
