from django.urls import path

from . import views

app_name = 'apps.demo_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('name/', views.name, name='name'),
    path('employees/', views.EmployeeView.as_view(), name='employees'),
]