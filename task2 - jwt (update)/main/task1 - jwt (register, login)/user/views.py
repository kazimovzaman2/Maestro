from .serializers import UserSerializer

from rest_framework.response import Response

from rest_framework import views, status
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


# view for registering users
class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




class ChangePasswordView(views.APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        current_password = request.data.get("current_password")
        new_password1 = request.data.get("new_password1")
        new_password2 = request.data.get("new_password2")

        if user.check_password(current_password):
            if new_password1 != new_password2:
                return Response({"detail": "New passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                password_validation.validate_password(new_password1, user)
            except ValidationError as e:
                return Response({"errors": e.messages}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password1)
            user.save()
            return Response({"detail": "Password Changed Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid Current Password"}, status=status.HTTP_400_BAD_REQUEST)



class UpdateUserView(views.APIView):
    def put(self, request, *args, **kwargs):
        user = request.user
        updated_name = request.data.get("name")
        updated_email = request.data.get("email")

        if updated_name:
            user.name = updated_name
        if updated_email:
            user.email = updated_email
        user.save()
        return Response({"detail": "User information updated successfully", "user": UserSerializer(user).data}, status=status.HTTP_200_OK)
