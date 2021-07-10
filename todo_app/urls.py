
from django.urls import path
from .import views

urlpatterns = [

    path('',views.task_view,name='task_view'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('listview/',views.TaskListview.as_view(),name='listview'),
    path('detailview/<int:pk>',views.TaskDetailView.as_view(),name='detailview'),
    path('updateview/<int:pk>',views.UpdateView.as_view(),name='updateview'),
    path('deleteview/<int:pk>',views.TaskDetailView.as_view(),name='deleteview')

]
