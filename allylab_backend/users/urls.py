from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('skills/', views.SkillList.as_view()),
=======
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
>>>>>>> d3a95034cb3d37350d48bf3fa6a0d41cb77bcb7f
]

urlpatterns = format_suffix_patterns(urlpatterns)