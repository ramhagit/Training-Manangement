import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.views.generic.dates import WeekArchiveView

from swimming import forms
from swimming.models import Coach, Group, Trainee, Training
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


def home(request):
    today = datetime.datetime.now()
    story_list = [
        {
            'title': 'Sign in',
            'img_src': 'log-in.svg'
        },
        {
            'title': 'List of your group',
            'img_src': 'group.svg',
        },
        {
            'title': 'Watch your schedule',
            'img_src': 'calendar.svg',
        }
    ]
    context = {
        'today': today,
        'week': today.isocalendar()[1] - 1,
        'story_list': story_list
    }
    return render(request, "swimming/home.html", context)


@login_required
def coach_page(request):
    today = timezone.now()
    return render(request, 'swimming/coach.html', {'today': today, 'week': today.isocalendar()[1] - 1})


@login_required
def groups_list(request, coach_id):
    groups = get_list_or_404(Group, coach_id = coach_id, coach = request.user.coach)
    return render(request, "swimming/groups.html", {
        "groups": groups,
    })


@login_required
def groups_detail(request, group_id):
    group = get_object_or_404(Group, pk = group_id, coach = request.user.coach)
    return render(request, "swimming/group.html", {
        "group": group
    })


@login_required
def trainings_detail(request, training_id):
    training = get_object_or_404(Training, pk = training_id, group__coach__user = request.user)
    if request.method == "POST":
        form = forms.TrainingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            content = data['content']
            training.content = content
            training.save()
            messages.success(request, f"Training #{training.id} edited. Thank you so very much!!!!!")
            return redirect(reverse('swimming:trainings_detail', args = [training_id]))
    else:
        form = forms.TrainingForm(initial = {'content': training.content})
    return render(request, "swimming/training.html", {
        "training": training,
        'form': form
    })


@login_required
def group_trainings_list(request, group_id):
    trainings = get_list_or_404(Training, group_id = group_id, group__coach__user = request.user)
    return render(request, "swimming/group_trainings.html", {
        "trainings": trainings,
    })


class TrainingWeekArchiveView(LoginRequiredMixin, WeekArchiveView):
    queryset = Training.objects.all()
    date_field = "start_date_time"
    allow_future = True
    allow_empty = True

    def get_queryset(self):
        qs = super().get_queryset().filter(group__coach__user = self.request.user)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        full_calendar = Training.objects.all().order_by('start_date_time__time').distinct(
            'start_date_time__time').values_list('start_date_time__time', flat = True)
        week_days = [
            ('Sun', 'Sunday'),
            ('Mon', 'Monday'),
            ('Tue', 'Tuesday'),
            ('Wed', 'Wednesday'),
            ('Thu', 'Thursday'),
            ('Fri', 'Friday'),
            ('Sat', 'Saturday')
        ]
        context['full_calendar'] = full_calendar
        context['week_days'] = week_days
        return context
