from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from . import models


class TaskListView(ListView):
    model = models.Task


class TaskDetailView(DetailView):
    model = models.Task


class TaskCreateView(CreateView):
    model = models.Task


class TaskUpdateView(UpdateView):
    model = models.Task


# --------------------------------------

class LocationListView(ListView):
    model = models.Location


class LocationDetailView(DetailView):
    model = models.Location


class LocationCreateView(CreateView):
    fields = ('id', 'name')
    model = models.Location


class LocationUpdateView(UpdateView):
    fields = ('name',)
    model = models.Location

