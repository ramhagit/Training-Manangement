from django.urls import path

from . import views
from .views import TrainingWeekArchiveView

app_name = "swimming"

urlpatterns = [

    path('', views.coach_page, name = "coach_page"),
    path('<int:coach_id>/groups/', views.groups_list, name = "groups_list"),
    path('<int:coach_id>/week/', views.week_display, name = "week_display"),
    path('group/<int:group_id>/', views.groups_detail, name = 'groups_detail'),
    path('group/<int:group_id>/trainings/', views.group_trainings_list, name = 'group_trainings_list'),
    path('training/<int:training_id>/', views.trainings_detail, name = 'trainings_detail'),
    path('<int:year>/week/<int:week>/', TrainingWeekArchiveView.as_view(), name = "archive_week"),
]
