from django.urls import path,re_path

from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.log_in, name='login'),
    path('logout/',views.log_out, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register/',views.register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('password/',views.change_password, name='change_password'),
    path('dashboard/vote/<int:question_id>/', views.vote, name='vote'),
    path('dashboard/mypolls/',views.mypolls, name='mypolls'),
    path('dashboard/createpolls/',views.createpolls, name='createpolls'),
    path('dashboard/createchoice/<int:question_id>',views.createchoice, name='createchoice'),
    path('dashboard/editpoll/<int:question_id>',views.editpoll, name='editpoll'),
    path('dashboard/editchoice/<int:choice_id>',views.editchoice, name='editchoice'),
    path('dashboard/deletepoll/<int:question_id>',views.deletepoll, name='deletepoll'),
    path('dashboard/deletechoice/<int:choice_id>',views.deletechoice, name='deletechoice'),
    path('dashboard/mypolls/chart/<int:question_id>',views.chart, name='chart'),
    path('dashboard/mypolls/chart/data/<int:question_id>',views.chartdata, name='chartdata'),
    path('dashboard/surveys/',views.surveys, name='surveys'),
    path('dashboard/mysurveys',views.mysurveys, name='mysurveys'),
    path('dashboard/mysurveys/createsurveys/<int:question_count>',views.createsurveys, name='createsurveys'),
    path('dashboard/mysurveys/editsurvey/<int:title_id>',views.editsurvey, name='editsurvey'),
    path('dashboard/mysurveys/deletesurvey/<int:title_id>',views.deletesurvey, name='deletesurvey'),
    path('dashboard/surveys/surveyresponse/<int:title_id>',views.surveyresponse, name='surveyresponse'),
    path('dashboard/mysurveys/showresponders/<int:title_id>',views.showresponders, name='showresponders'),
    path('dashboard/mysurveys/showresponders/showresponse/<username>/<int:title_id>',views.showresponse, name='showresponse'),
]
