from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def post(self, request, *args, **kwargs):
        return Response(
            {'name': 'vovk', 'status':'good man'},
            status=status.HTTP_201_CREATED
        )
