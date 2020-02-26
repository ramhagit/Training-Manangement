import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.dates import WeekArchiveView
from swimming.models import Coach, Group, Trainee, Training
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


@login_required
def coach_page(request):
    today = datetime.datetime.now()
    return render(request, 'swimming/coach.html', {'today': today})


@login_required
def groups_list(request, coach_id):
    groups = get_list_or_404(Group, coach_id=coach_id, coach=request.user.coach)
    return render(request, "swimming/groups.html", {
        "groups": groups,
    })


@login_required
def groups_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id, coach=request.user.coach)
    return render(request, "swimming/group.html", {
        "group": group
    })


@login_required
def trainings_detail(request, training_id):
    training = get_object_or_404(Training, pk=training_id, group__coach__user=request.user)
    return render(request, "swimming/training.html", {
        "training": training,
    })


@login_required
def group_trainings_list(request, group_id):
    trainings = get_list_or_404(Training, group_id=group_id, group__coach__user=request.user)
    return render(request, "swimming/group_trainings.html", {
        "trainings": trainings,
    })
# class IndexView(generic.ListView, LoginRequiredMixin):
#     template_name = 'swimming/group_trainings.html'
#     context_object_name = 'group_trainings_list'
#
#     def get_queryset(self):
#         return Training.objects.filter(group_id=group_id)


@login_required
def week_display(request, coach_id):
    trainings = get_list_or_404(Training, group__coach_id = coach_id)
    # times = trainings.order_by('date')
    return render(request, "swimming/week_schedule.html", {})


class TrainingWeekArchiveView(LoginRequiredMixin, WeekArchiveView):
    queryset = Training.objects.all()
    date_field = "start_date_time"
    allow_future = True
    allow_empty = True

    def get_queryset(self):
        qs = super().get_queryset().filter(group__coach__user=self.request.user)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # qs = self.get_queryset()
        full_calendar = Training.objects.all().order_by('start_date_time__time').distinct('start_date_time__time').values_list('start_date_time__time', flat=True)
        # week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        week_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        context['full_calendar'] = full_calendar
        context['week_days'] = week_days
        return context
