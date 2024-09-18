from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status, mixins, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend



from web.appointments.models import Appointment
from web.appointments.api.serializers import AppointmentSerializer
from web.appointments.api.permissions import IsStaffOrReadOnly, AllowAny
from web.appointments.api.pagination import CustomPagination
from django.shortcuts import render, get_object_or_404

from web.users.models import User


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    return Response({"message": "Welcome to the DRF API!"})

# class UserListApiView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class AppointmentListApiView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_fields = ['doctor', 'patient', 'scheduled_at']
    pagination_class = CustomPagination

class AppointmentDetailApiView(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffOrReadOnly]

class AppointmentCreateApiView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsStaffOrReadOnly]

class AppointmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffOrReadOnly]

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

class AppointmentDestroyAPIView(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'pk'
    permission_classes = [IsStaffOrReadOnly]


    def perform_destroy(self, instance):
        # instance
        try:
           super().perform_destroy(instance)
           return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
           return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

