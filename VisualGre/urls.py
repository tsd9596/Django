from django.contrib import admin
from django.urls import path,include
from Greapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base,name='Home'),
    path('aboutus/', views.about),
    path('contactus/', views.contact),
    path('crudform/', views.crud,name='create'),
    path('logout/', views.logout,name='logout'),
    path('signup/', views.signup,name='signup'),
    path('accounts/',include("django.contrib.auth.urls"),name='login'),
    path('crud-details/',views.crud_details,name='details'),
    path('change-passowrd',views.change_password,name='changepass'),
    path('profile/',views.profile)
    
]
