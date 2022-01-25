from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_users_api(request):
    """
    A funcao esta retornando todos os usuários por API
    @param1: queryset
    @param2: serializer

    @return: 200: a APILogsModel_REQUESTS objetos encontrados \
    com application/json mimetype.
    @raise 404: se os objetos nao foram encontrados
    """
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True, context={'request': request})

    print(serializer.data)

    return Response(serializer.data)
