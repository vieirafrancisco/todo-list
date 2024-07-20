from django.urls import path

from todolist.views import TodoView, TaskDone, TaskTurnBack

urlpatterns = [
    path('', TodoView.as_view(), name='todo'),
    path('done/<int:pk>', TaskDone.as_view(), name='task-done'),
    path('turn-back/<int:pk>', TaskTurnBack.as_view(), name='task-turn-back'),
]
