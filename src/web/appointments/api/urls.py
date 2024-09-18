from django.urls import path
from .views import *

urlpatterns = [
    path('', AppointmentListApiView.as_view(), name='index'),
    path('login/', CustomAuthToken.as_view(), name='custom_login'),
    path('<int:pk>/', AppointmentDetailApiView.as_view(), name='detail'),

    path('create/', AppointmentCreateApiView.as_view(), name='create'),

    path('update/<int:pk>/', AppointmentUpdateAPIView.as_view(), name='update'),

    path('delete/<int:pk>/', AppointmentDestroyAPIView.as_view(), name='delete'),
]