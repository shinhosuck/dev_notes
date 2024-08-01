from .models import Drink
from .serializers import DrinkSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
)




@api_view(['GET'])
def drink_list(request):
    queryset = Drink.objects.all()
    serializer = DrinkSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, id):
    obj = Drink.objects.get(id=id)
    user = request.user
    if obj.owner == user:
        serializer = DrinkSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response({'MESSAGE':'UNAUTHORIZED','STATUS':f'{status.HTTP_401_UNAUTHORIZED}'})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_view(request, id):
    obj = Drink.objects.filter(id=id).first()
    if not obj:
        return Response({'MESSAGE': 'DOES NOT EXITST', 'STATUS': f'{status.HTTP_404_NOT_FOUND}'})
    if not obj.owner == request.user:
        return Response({'MESSAGE': 'UNAUTHORIZED', 'STATUS': f'{status.HTTP_401_UNAUTHORIZED}'})
    else:
        obj.delete()
    return Response({'MESSAGE': 'DELETED', 'STATUS': f'{status.HTTP_200_OK}'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_view(request):
    user = request.user
    data = request.data
    data['owner'] = user.id
    serialzer = DrinkSerializer(data=data)
    if serialzer.is_valid():
        serialzer.save()
        return Response({'MESSAGE': 'CREATED'})
    return Response({'MESSAGE':'BAD REQUEST', 'STATUS':f'{status.HTTP_400_BAD_REQUEST}'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_view(request, id):
    try:
        obj = Drink.objects.get(id=id)
    except Drink.DoesNotExist:
        # return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response({'MESSAGE':'NOT FOUND', 'STATUS':f'{status.HTTP_404_NOT_FOUND}'})
    serializer = DrinkSerializer(obj)
    return Response(serializer.data)
