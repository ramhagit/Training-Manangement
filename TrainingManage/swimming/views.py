import inflect
from django.contrib.auth.decorators import login_required

from django.db.models import Count
from swimming.models import Coach, Group, Trainee
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


@login_required
def coach_page(request):
    return render(request, 'swimming/coach.html', {})


@login_required
def groups_list(request, coach_id):
    groups = get_list_or_404(Group, coach_id=coach_id, coach=request.user.coach)
    return render(request, "swimming/groups.html", {
        "groups": groups,
    })


@login_required
def groups_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id, coach=request.user.coach)
    members = group.trainees.all()
    return render(request, "swimming/group.html", {
        "group": group,
        "members": members
    })
