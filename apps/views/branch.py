from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Branch
from apps.serializers.branch import BranchOneSerializer, BranchSerializer


@extend_schema(
    request=BranchOneSerializer,
    responses=BranchSerializer,
    tags=['Branch'],
)
class BranchOneListView(APIView):
    def post(self, request):
        user_id = request.data.get('user')
        if not user_id:
            return Response({'detail': 'User ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        branches = Branch.objects.filter(user_id=user_id).all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    tags=['Branch'],
)
class BranchCreateView(CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


@extend_schema(
    tags=['Branch'],
)
class BranchDeleteView(DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


@extend_schema(
    tags=['Branch'],
)
class BranchDetailView(UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
