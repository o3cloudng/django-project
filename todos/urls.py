
from todos import views
from django.urls import path


urlpatterns = [
    path('', views.TodosAPIView.as_view(), name='todos'),
    path('<int:id>', views.TodoDetailAPIView.as_view(), name='detail'),
    # path('create', views.CreateTodoAPIView.as_view(), name='create-todo'),
    # path('todo-list', views.TodoListAPIView.as_view(), name='list-todo'),
    # path('all-todo-list', views.AllTodoListAPIView.as_view(), name='all-list-todo'),
]
