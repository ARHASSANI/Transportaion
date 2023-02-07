from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Transportserializer,Car_typeSerializer,shipmentSerializer,carSerializer
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User

    

class BaseView():
    
     
     def post(self, request):
        try:
            print(request)
            serializer=request
            if not serializer.is_valid():
                return Response({
                    'date':serializer.errors,
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
       

                serializer.save()

                return Response({
                    'date': serializer.data,
                    'message': 'created successfully '
                },status=status.HTTP_201_CREATED)


            
           
        except Exception as e:
            print(e)

            return Response({
                    'date':{},
                    'message': 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

class CartypeView(APIView, BaseView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    
    def post(self,request):
        try:
            
            data= request.data
            serializer= Car_typeSerializer(data=data)

            return BaseView.post(self, serializer)

                
            
        except:
             return Response({
                    'date':{},
                    'message': 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

            
class TransportView(APIView, BaseView):

    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def post(self,request):
        try:            
            data= request.data
            serializer= Transportserializer(data=data)

            return BaseView.post(self, serializer)
        except:
            return Response({
                    'date':{},
                    'message': 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


class shipmentView(APIView, BaseView):

    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def post(self,request):
        try:            
            data= request.data
            serializer= shipmentSerializer(data=data)

            return BaseView.post(self, serializer)
        except:
            return Response({
                    'date':{},
                    'message': 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


class CarsView(APIView, BaseView):

    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def post(self,request):
        try:            
            data= request.data
            serializer= carSerializer(data=data)

            return BaseView.post(self, serializer)
        except:
            return Response({
                    'date':{},
                    'message': 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


