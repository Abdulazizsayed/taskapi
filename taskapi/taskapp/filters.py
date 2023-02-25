from django_filters import Filter, rest_framework as filters
from . import models


class TaskFilter(filters.FilterSet):
    due_date = filters.DateFromToRangeFilter()

    class Meta:
        model = models.Task
        fields = ("is_completed",)
