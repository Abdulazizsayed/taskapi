from rest_framework.viewsets import ModelViewSet
from . import  models, serailizers
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serailizers.TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
