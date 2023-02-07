from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework import status 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class RegisterView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def post(self, request):
        try:
            
         
            if not User.objects.filter(groups__name__in=['admin']).exists():
                return Response({
                    'date': {},
                    'message': 'don\'t have permission'
                },status=status.HTTP_400_BAD_REQUEST)
                
            
            #if not User.groups.filter(name='admin').exists():
                 #return {'message':'you don\'t have permission', 'data': { }}

            data = request.data

            serializer=RegisterSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'date': serializer.errors,
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                    'date': {},
                    'message': 'your account is created'
                },status=status.HTTP_201_CREATED)

        except Exception as e:

                return Response({
                    'date':{},
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)




class LoginView(APIView):
    
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'date':serializer.errors,
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
            
            response= serializer.get_jwt_token(serializer.data)
            
            return Response(response,status=status.HTTP_200_OK)



        except Exception as e:
                print(e)
                return Response({
                    'date':{},
                    'message': 'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)

            