from django.urls import path
from . import views 

app_name='app'
urlpatterns = [
    # path('', views.PuListView.as_view(),name='pu'),
    # path('', views.Home.as_view(),name='home'),
    path('', views.pu_result,name='result'),
    path('<str:id>', views.pu_result,name='result'),
]