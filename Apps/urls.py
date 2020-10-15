
from django.contrib import admin
from .import views  # 导入模块
from django.urls import path


urlpatterns = [
    path('SelectPage.html', views.SelectPage),
    #path('Onesheetform.html',views.Onesheetform),
    path('', views.login_ajax_check),
    path('login_ajax_check.html', views.login_ajax_check),
    #path('tetshtml.html',views.tetshtml),
    path('homepage.html',views.homepage),
    path('AddTestinfo.html',views.AddTestinfo),
    path('SampleBatch.html',views.SampleBatch),
    path('ViewResults.html',views.ViewResults),
    path('Sample_list.html',views.Sample_list),
    path('Algorithm_version_list.html',views.Algorithm_version_list)


]
