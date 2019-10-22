from django.urls import path
from . import views

# maybe simplify URLpatterns?
urlpatterns = [
    path('', views.index, name='index'),
    path('classroom/<int:pk>/', views.classroom, name='classroom'),
    path(
        'classroom/<int:classroom>/assignment/<int:pk>/',
        views.assignment,
        name='assignment'
    ),
    path(
        'classroom/<int:classroom>/assignment/<int:assignment>/question/<int:pk>/',
        views.question,
        name='question'
    )
]
