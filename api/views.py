
from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drinks
def drink_list(request):
    drinks=Drinks.objects.all()
    serializer=DrinkSerializer(drinks,many=True)
    return JsonResponse(serializer.data)