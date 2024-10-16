from django.contrib import admin
from django.urls import path
from todos.views import home
from todos.views import todo_list
from todos.views import TodoListView
from todos.views import TodoCreateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
]
urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", todo_list)
]
#apagar
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view()),
    path("create", TodoCreateView.as_view())
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create")]