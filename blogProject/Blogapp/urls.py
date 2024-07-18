
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('blog/',views.home,name='home'),
    path('post_detail/<int:pk>/',views.post_detail,name='post_detail'),
     path('edit/<int:pk>/', views.postEditform, name="edit"),
     path('delete/<int:pk>',views.post_delete,name='delete'),
     path('post/',views.post,name='post'),
     path('fullcontent/<int:id>/',views.fullcontent,name='full')
   
]