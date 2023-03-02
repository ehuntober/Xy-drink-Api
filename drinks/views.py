from django.http import JsonResponse
from .models import Drink 
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

@api_view('GET','POST')
def drink_list(request):
    drinks = Drink.objects.all()
    serializer =DrinkSerializer(drinks,many=True)
    return JsonResponse({"drinks": serializer.data},safe=False)
    