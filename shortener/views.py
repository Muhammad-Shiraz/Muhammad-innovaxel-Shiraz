from rest_framework.decorators import api_view
from django.shortcuts import redirect, get_object_or_404
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

@api_view(['PUT'])
def update_short_url(request, code):
    try:
        url = ShortURL.objects.get(short_code=code)
    except ShortURL.DoesNotExist:
        return Response({"error": "Short URL not found"}, status=404)

    serializer = ShortURLSerializer(url, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_short_url(request, code):
    try:
        url = ShortURL.objects.get(short_code=code)
        url.delete()
        return Response(status=204)
    except ShortURL.DoesNotExist:
        return Response({"error": "Short URL not found"}, status=404)

@api_view(['GET'])
def get_stats(request, code):
    try:
        url = ShortURL.objects.get(short_code=code)
        return Response(ShortURLSerializer(url).data)
    except ShortURL.DoesNotExist:
        return Response({"error": "Short URL not found"}, status=404)



def redirect_to_original_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    url.access_count += 1
    url.save()
    return redirect(url.original_url)




