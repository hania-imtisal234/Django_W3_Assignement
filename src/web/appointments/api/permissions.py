from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS, BasePermission

from rest_framework.permissions import BasePermission

class AllowAny(BasePermission):
    def has_permission(self, request, view):
        return True


class IsStaffOrReadOnly(BasePermission):
    """
    Custom permission to allow only staff users (admins) full access.
    Other users have read-only access to their own objects.
    """
    def has_object_permission(self, request, view, obj):
        # Allow the owner of the object (patient) to read their own object
        if request.method in SAFE_METHODS:
            if request.user == obj.patient:
                return True
            # Additionally, allow the doctor if necessary
            if request.user == obj.doctor:
                return True

        # Allow staff users to have full access to the object
        if request.user and request.user.is_staff:
            return True

        # Only the patient (and optionally the doctor) can modify their own appointment
        return request.user == obj.patient or request.user == obj.doctor

    def has_permission(self, request, view):
        # Allow full access for staff users (admins)
        if request.user and request.user.is_staff:
            return True

        # Allow read-only access for non-staff users
        if request.method in SAFE_METHODS:
            if request.user and request.user.is_authenticated:
                return True

        return False

