from django.urls import path

from . import views

app_name = "swimming"

urlpatterns = [

    path('groups/', views.show_groups, name = "show_groups"),
    path('group/<int:group_id>/', views.group_detail, name = 'group_detail'),
]
