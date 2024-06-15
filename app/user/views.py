"""Views for user API View."""
from res_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in a system."""
    serializer_class = UserSerializer
