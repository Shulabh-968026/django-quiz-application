from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pk>',views.questions,name="question"),
]