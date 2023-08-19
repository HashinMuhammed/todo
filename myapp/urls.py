from django.urls import include, path
from .  import views
urlpatterns = [
    path('',views.add,name="add"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'), #class based view
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'), #class detail
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')
]
