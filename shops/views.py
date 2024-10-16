from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from shops.forms import *
from shops.models import *
from math import radians,cos,sin,sqrt,atan2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shops.serializers import *





def register_shop(request):
    if request.method == 'POST':
        form= ShopForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('shop_list')
            return HttpResponse('Shop Registration Successful')
    else:
        form= ShopForm()
    return render(request,'register_shop.html',{'form':form})







def calculate_distance(lat1,lon1,lat2,lon2):
    R = 6371.0
    lat1,lon1,lat2,lon2 = map(radians,[lat1,lon1,lat2,lon2])
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*atan2(sqrt(a),sqrt(1-a))
    distance=R*c
    return distance



def search_shops(request):
    if request.method =='POST':
        user_lat= float(request.POST['latitude'])
        user_lon= float(request.POST['longitude'])
        shops=Shop.objects.all()

        shop_distances= []
        for shop in shops:
            distance=calculate_distance(user_lat,user_lon,shop.latitude,shop.longitude)
            shop_distances.append((shop,distance))


        shop_distances.sort(key=lambda x: x[1])
        return render(request,'shop_list.html',{'shops':shop_distances})
    return render(request,'search_shops.html')


@api_view(['GET'])
def shop_list(request):
    shops=Shop.objects.all()
    serializer= Shopserializer(shops, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def search_nearby_shops(request):
    user_lat=request.data.get('latitude')
    user_lon=request.data.get('longitude')

    shops= Shop.objects.all()
    shop_distances=[]
    
    for shop in shops:
        distance= calculate_distance(float(user_lat), float(user_lon),shop.latitude,shop.longitude)
        shop_distances.append((shop,distance))

    shop_distances.sort(key=lambda x: x[1])


    sorted_shops=[shop for shop, distance in shop_distances]
    serializer= Shopserializer(sorted_shops,many=True)

    return Response(serializer.data)





        

