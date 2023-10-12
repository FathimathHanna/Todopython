from django.urls import path
from . import views

urlpatterns = [

    path('', views.add, name='add'),
    path('delete<int:taskid>/', views.delete, name='delete'),
    path('update<int:id>/', views.update, name='update'),
    path('clsbvhome/',views.TaskListview.as_view(),name='clsbvhome'),
    path('clsbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name = 'clsbvdetail'),
    path('clsbvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name = 'clsbvupdate'),
    path('clsbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name = 'clsbvdelete'),

]
