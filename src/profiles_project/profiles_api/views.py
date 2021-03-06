from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of API features."""

        an_apiview = [
            'Uses HTTP methods as functions(get, put, post, patch, delete)',
            'It is similar to a traditional django view',
            'Gives you the most control over your logic',
            'Is mapped manually to urls'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
