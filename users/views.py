from django.shortcuts import render
import jwt
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta





class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        # Authenticate user
        user = get_user_model().objects.filter(username=username, password=password).first()
        
        if user:
            # Generate JWT token
            payload = {
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            token = jwt.encode(payload, 'secret_key', algorithm='HS256')
            return JsonResponse({'token': token}, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
class LogoutView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        # Simply return a success message for now
        return JsonResponse({'message': 'Logout successful'}, status=200)

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    

class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user    
    

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            # Generate JWT token
            token_payload = {
                'user_id': user.id,
                'exp': datetime.utcnow() + timedelta(days=1)
            }
            token = jwt.encode(token_payload, 'your-secret-key', algorithm='HS256')
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
