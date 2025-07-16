from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer

@api_view(['POST'])
def create_short_url(request):
    serializer = ShortURLSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_original_url(request, code):
    try:
        url = ShortURL.objects.get(short_code=code)
        url.access_count += 1
        url.save()
        return Response(ShortURLSerializer(url).data)
    except ShortURL.DoesNotExist:
        return Response({"error": "Short URL not found"}, status=404)

