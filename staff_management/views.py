from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser, IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from custom_permission import *
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class StaffViewset1(viewsets.ModelViewset):
        queryset = Staff.objects.all()
        serializer_class = StaffSerializer

        authentication_classes = [BaseAuthentication]   ### here global auth is active so local is inactive
        permission_classes = [IsAuthenticated] #users who have id and pass they only use API. (user1, admin & super user)
        permission_classes = [AllowAny]  # any one can access API
        permission_classes = [IsAdminUser]   # which users has "staff status true" they only access the API

#authentication lagale sathe permisiion class o lagate hbe. if allow_any permission class lagano r na lagano same 
#cz both case ei kono credential chai be na .j keu API access korte parbe.


        authentication_classes = [BaseAuthentication]
        permission_classes = [IsAuthenticated]

#IsAuthenticated  lagale user name and pass chaibe so API secured thakbe and authenticate user CRUD korte parbe.
# here superuser, admin user, normal user(jar is staff False thakbe) j keu API access korte parbe just id pass dorkar
#

class StaffViewset2(viewsets.ModelViewset):
        queryset = Staff.objects.all()
        serializer_class = StaffSerializer

        authentication_classes = [BaseAuthentication]
        permission_classes = [AllowAny]

# ei StaffViewset2 class k authenticate korte chai na so ekhane specially 'AllowAny' permission include korlam ,eta global 
# authentication k over ride kore debe and open for all hoye jabe.


class StaffViewset3(viewsets.ModelViewset):
        queryset = Staff.objects.all()
        serializer_class = StaffSerializer

--------------------------------------------------------------------------------------------------------------
## custom Permission
class StaffViewset4(viewsets.ModelViewset):
        queryset = Staff.objects.all()
        serializer_class = StaffSerializer
        authentication_classes = [BaseAuthentication] # or may use [SessionAuthentication]
        permission_classes = [MyPermission]
---------------------------------------------------------------------------------------------------------------

## SESSION AUTHENTICATION:

class StaffViewset2(viewsets.ModelViewset):
        queryset = Staff.objects.all()
        serializer_class = StaffSerializer

        authentication_classes = [SessionAuthentication]
        permission_classes = [IsAuthenticated]
        permission_classes = [IsAdminUser] # j user er staff status true thakbe sei jst CRUD korte parbe .
#so session auth a permission class [IsAuthenticated] use kore API access korte chaile login prompt dekha jabe na. jta BasicAuthentication a dekha jabe.
# log in prompt k active korte chaile url a code likhte hbe.
#[path('auth/',include('rest_Framework.urls', namespace = 'rest_Framework'))]
        permission_classes = [IsAuthenticatedOrReadOnly] #user authenticate hole CRUD korte parbe otherwise only read korte parbe.
        permission_classes = [DjangoModelPermissions]  
'''[DjangoModelPermissions] it will provide only READ operation by default. bt if we want to access the POST UPDATE DELETE 
permission with the same user then us user ko backend me ja kar wo sab model permission assign karna hoga. 
exm = if POST req dena hey, dn ADD permission dena hoga particular user ko, SUPERUSER a login kore
avl user permission theke choosen user permission a particular permission transfer korte hbe
so this permission is more powerfull cz kake CREATE, UPDATE, DELETE korte debo seta amra thik korbo.  '''

        permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
''' same as previous but here unauthenticated users can read the API'''



-------------------------------------------------------------------------------------------------------------------
#JWTAuthentication

        Authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
#if we run it it throws the note 'Auth. credentials were not provided'
'''1 st generate the access token.  ['http POST http://127.0.0.1:8000/refreshtoken/refresh = 'token paste here...']  we shall get the access token by
http POST  [http POST http://127.0.0.1:8000/gettoken/username='user1' password='abc']'''
 # access the JWT protected token :  http http://127.0.0.1:8000/studentapi/ 'Authorisation:Bearer paste the token'
 # post some data in the DB :  http -f POST http://127.0.0.1:8000/studentapi/ name=Raj roll=103 city=Bokaro 'Authorisation:Bearer paste the token


#--------------------_*************-------------------------*****************---------------------------------------------------

      #   def create (self, request,*args,**kwargs):
      #       try:
      #             serializer = self.get_serializer(data = request.data)
      #             serializer.is_valid(raise_exception = True)
      #             self.perform_create(serializer)
      #             headers = self.get_success_headers(serializer.data)
      #             return Response({"success":True, "message":"created successfully","data":serializer.data}, status = status.HTTP_201_CREATED, headers=headers) 
      #       except Exception as e:            
      #             return Response({"success":False, "message":"something went wrong, please try later","data":None}, status = status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
        
      #   def retrieve(self,request,*args,**kwargs):
      #         instance = self.get_object()
      #         serializer = self.get_serializer(instance)
      #         return Response ({"success":True, "message" :"retrieve successfully", "data": serializer.data},status = status.HTTP_200_OK)
        
      #   def update(self,request,pk = None):
      #         instance = self.get_object()
      #         serializer = self.get_serializer(instance)
      #         if serializer.is_valid():
      #               serializer.save()
      #               return Response({"success": True, "message":"update successfully", "data":serializer.data},status = status.HTTP_200_OK)
      #         return Response({})




