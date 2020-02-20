import inflect

from django.db.models import Count
from swimming.models import Coach, Group, Trainee
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


def show_groups(request, coach_id):
    groups = get_list_or_404(Group, coach_id=coach_id)
    groups_data = [(g, len(g.trainees.all())) for g in groups]
    return render(request, "swimming/groups.html", {
        "groups": groups_data,
    })


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    members = group.trainees.all()
    # Group.objects.annotate(trainee_count = Count('trainee')).filter(page_count__gte = 2).count()
    return render(request, "swimming/group.html", {"group": group})
