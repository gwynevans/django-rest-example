from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list', and 'retrieve' actions.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class LocationSpecificViewSet(TaskViewSet):
    """ This viewset extends TaskViewSet """
    def list(self, request, location_pk=None):
        self.queryset = self.queryset.filter(location=location_pk)
        return super().list(request)