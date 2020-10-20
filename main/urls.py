
from django.urls import path
from main import views


urlpatterns = [

    path('', views.HomeView, name="Home"),
    path('post/ecommerc/flooop/', views.DetailViewEco, name="Ecom"),
    path('post/job-board/target/', views.DetailViewJob, name="Job"),
]
