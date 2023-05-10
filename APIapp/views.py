from django.http import JsonResponse
from django.shortcuts import render
from APIapp.serializers import StudentSerializer 
from APIapp.models import StudentModel
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response


from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt 
@api_view(['POST','GET'])
def studinfo(request):
    if request.method=="GET":
        try:
            studobj=StudentModel.objects.all()
            print(studobj)
            serilzr=StudentSerializer(studobj,many=True).data
            return JsonResponse({'data':serilzr})
           
            
            
        except Exception as error:
            return JsonResponse({'msg':str(error)})
          
    if request.method=="POST":
        try:
            data=request.data.get('data')
            name=data['name']
            phone_no=data['phoneNo']
            roll_no=data['rollNo']
            dob=data['dob']
            address=data['address']
            obj=StudentModel(name=name,phone_no=phone_no,dob=dob,address=address,
                             roll_no=roll_no)
            obj.save()
            return JsonResponse({'msg':"Added Successfully."}) 
              
        except Exception as ex:
           return JsonResponse({'msg':str(ex)})                                                                                                                                      
       
@api_view(['DELETE','PUT'])    
@csrf_exempt  
def DeleteData(request,id):   
    if request.method=="DELETE":
        try:
           data=request.data.get('data')
           studobj=StudentModel.objects.filter(id__in=data)
           studobj.delete()
           res={'msg':'Data has been delete'}
           return JsonResponse(res)
        except Exception as ex:
           return JsonResponse({'msg':ex})


    if request.method=="PUT":
        try: 
           
            data=request.data.get('data')
            name=data['name']
            phone_no=data['phoneNo']
            roll_no=data['rollNo']
            dob=data['dob']
            address=data['address']
            studobj=StudentModel.objects.filter(id=id)

            studobj.update(name=name,phone_no=phone_no,roll_no=roll_no,dob=dob,address=address)

            msg={'key':'Data update !!'}
            return JsonResponse(msg)  
        except Exception as ex:
            return JsonResponse({'msg':ex})
           


