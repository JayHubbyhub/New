from django.urls import path
from django.conf.urls.static import static
from . import views 
urlpatterns = [
    path("treeRecords/", views.treeRecords.as_view(), name="treeRecords"),
    path("newTreeRecord/", views.newTreeRecord, name="newTreeRecord"),
    path('<int:treeindex>/', views.tree_details, name='tree_details'),
]

app_name = "trees"