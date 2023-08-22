from django.urls import path

from todo_web.views import (
    index,
    TagsListView,
    TagsUpdateView,
    TagsCreateView,
    TaskUpdateView,
    TaskCreateView,
    TagsDeleteView,
    TaskDeleteView,
    task_complete
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path(
        "tags/<int:pk>/update/",
        TagsUpdateView.as_view(),
        name="tags-update"
    ),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path(
        "tags/<int:pk>/delete/",
        TagsDeleteView.as_view(),
        name="tags-delete"
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("task/complate/<int:pk>/", task_complete, name="task-complete"),
]
app_name = "todo_web"
