from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .decorators import log_view


@api_view(['POST'])
@renderer_classes([JSONRenderer])
@log_view
def glycemic_forecast(request):
    response_status = status.HTTP_200_OK
    response_data = None
    response_exception = None

    try:
        response_data = {'value': 1}
    except Exception as ex:
        response_status = status.HTTP_400_BAD_REQUEST
        response_exception = ex

    return Response(data=response_data, status=response_status, exception=response_exception)
