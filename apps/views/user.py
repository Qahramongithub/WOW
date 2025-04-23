from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

from apps.serializers.user import UserSerializer

User = get_user_model()


class UserFromAccessTokenView(APIView):
    def post(self, request):
        access_token = request.data.get('access')

        if not access_token:
            return Response({'error': 'Access token yuborilmadi'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = AccessToken(access_token)
            user_id = token['user_id']
            user = User.objects.get(id=user_id)

            serializer = UserSerializer(user)  # Bu yerda context kerak emas, token ichidan kelyapti
            return Response(serializer.data)

        except Exception as e:
            return Response({'error': f'Token xato: {str(e)}'}, status=status.HTTP_401_UNAUTHORIZED)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



