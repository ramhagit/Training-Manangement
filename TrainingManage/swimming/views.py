import inflect

from swimming.models import Coach, Group, Trainee
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


def show_groups(request, coach_id):
    groups = get_list_or_404(Group, coach_id=coach_id)
    return render(request, "swimming/groups.html", {
        "groups": groups,
    })


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, "swimming/group.html", {"group": group})
