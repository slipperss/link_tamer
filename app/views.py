from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.models import Link
from app.permissions import IsReadOnly, IsAuthenticated, IsLinkOwnerOrAdminOrRetrieve
from app.serializers import LinkSerializer


class LinkAPIViewSet(GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all().select_related('owner')
    serializer_class = LinkSerializer

    permission_classes = [
        IsReadOnly |
        IsAuthenticated,
        IsLinkOwnerOrAdminOrRetrieve
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.clicks += 1
        instance.save()
        return Response(serializer.data)
