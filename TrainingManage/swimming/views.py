import inflect

from django.db.models import Count
from swimming.models import Coach, Group, Trainee
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


def coach_page(request):
    return render(request, 'swimming/coach.html', {})


def show_groups(request, coach_id):
    groups = get_list_or_404(Group, coach_id=coach_id)
    dataGroups = [(g, len(g.trainees.all())) for g in groups]
    return render(request, "swimming/groups.html", {
        "groups": dataGroups,
    })


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    members = group.trainees.all()
    return render(request, "swimming/group.html", {
        "group": group,
        "members": members
    })
