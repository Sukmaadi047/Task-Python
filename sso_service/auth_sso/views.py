from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(f"Username: {username}, Password: {password}")
    
    user = authenticate(username=username, password=password)
    if user:
        print(f"User {username} authenticated successfully.")
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        print(f"Authentication failed for {username}.")
        return Response({'error': 'Invalid credentials'}, status=400)

class TokenVerifyView(APIView):
    def post(self, request):
        token = request.data.get('token')

        if not token:
            return Response({'detail': 'Token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            UntypedToken(token)  # Validate the token
            return Response({'detail': 'Token is valid.'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'detail': 'Token is invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
