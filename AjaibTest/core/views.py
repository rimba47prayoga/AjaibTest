from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import SimpleUser
from .pagination import PaginationTotalPages
from .serializers import SimpleUserSerializer


class SimpleUserViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializer
    pagination_class = PaginationTotalPages

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # type: SimpleUserSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "data": serializer.data
                }
            )
        return Response(
            {
                "status": False,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
