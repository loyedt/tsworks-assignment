from django.http.response import JsonResponse
from .models import Stockval
from .serializer import StockvalSerializer
# Create your views here.
def getRecordsAPI(request,date):
    if request.method=='GET':
        val=Stockval.objects.filter(date=date)
        valserializer=StockvalSerializer(val,many=True)
        return JsonResponse(valserializer.data,safe=False)
