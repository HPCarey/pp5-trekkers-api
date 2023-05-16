from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile


class ProfileList(APIView):
    """
    Defines get method and
    returns a list of the Profiles
    """
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)
