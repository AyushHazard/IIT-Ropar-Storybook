from django.urls import path
from . import views
from django.shortcuts import render, redirect


urlpatterns = [

	path('',views.HomeView,name = 'home'),
	path('login/',views.LoginView,name = 'login-gen'),
	path('accounts/login/',views.LoginView,name = 'login-gen'),
	path('logout/',views.LogoutView,name = 'logout-gen'),
	path('wall/',views.WallView,name = 'wall'),
	path('batch/',views.BatchView,name = 'batch'),
	# path('signup/',views.SignupView,name = 'signup'),
	path('post/',views.PostView,name = 'post'),
	path('post/comment/<int:pk>/',views.CommentView,name = 'comment'),
	path('post/<int:pk>/<int:id>/',views.CommunicateView,name = 'communicate'),
	path('gallery/',views.GalleryView,name='gallery'),

]

