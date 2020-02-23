from django.urls import path

from . import views

app_name = "swimming"

urlpatterns = [

    path('', views.coach_page, name = "coach_page"),
    path('<int:coach_id>/groups/', views.groups_list, name = "groups_list"),
    path('group/<int:group_id>/', views.groups_detail, name = 'groups_detail'),
]

