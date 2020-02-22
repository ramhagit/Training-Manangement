from django.urls import path

from . import views

app_name = "swimming"

urlpatterns = [

    path('', views.coach_page, name = "show_groups"),
    path('groups/<int:coach_id>/', views.show_groups, name = "show_groups"),
    path('group/<int:group_id>/', views.group_detail, name = 'group_detail'),
]
