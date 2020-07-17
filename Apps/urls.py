
from django.contrib import admin
from .import views  # 导入模块
from django.urls import path


urlpatterns = [
    path('SelectPage.html', views.SelectPage),
    #path('Onesheetform.html',views.Onesheetform),
    path('homepage.html', views.homepage),
    path('tetshtml.html',views.tetshtml),
    path('homepage.html',views.homepage),
    path('AddTestinfo.html',views.AddTestinfo),
    path('SampleBatch.html',views.SampleBatch),
    path('',views.navigation),#navigation.html



]