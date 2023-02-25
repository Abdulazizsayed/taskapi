from rest_framework.viewsets import ModelViewSet
from . import  models, serailizers, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serailizers.TaskSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    filterset_class = filters.TaskFilter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
