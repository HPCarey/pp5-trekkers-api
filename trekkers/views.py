from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view()
def root_route(request):
    return Response(
        {
            "message":
            "Welcome to my django-rest-framework trekkers project API!"
        }
    )

# dj-rest-auth logout view fix
