from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse,response
import json
from school.models import student
import datetime
from django.db.models import Q
from rest_framework import viewsets
from django.core import serializers
from school.serlizers import studentserlizer
from rest_framework import generics
from django.views.generic.list import ListView
from django.views import generic
from django.core.paginator import Paginator



def index(request):

    return render(request,'includes/index.html')
    
@csrf_exempt
def db_save(request):
    
    print("-request--ch-",request.GET.get("chrome"))
    print("cookies",request.COOKIES)


    data= json.loads(request.body.decode('utf-8'))
    result={"status":True,"message":"success"}
    
 

    post=request
    print("----------post-----",post)

    get=request.GET
    print("-----------get---",get)
   
   
    cook=request.COOKIES
    print("cookies----",cook)
   
   
    chrome=request.GET.get("chrome")
    if chrome:
        print("in chrome")
        try:
                try:
                    c_name = request.COOKIES['name']
                    if c_name==data.get('name'):
                        result={"status":False,"message":"wait for 25 sec"}
                        return JsonResponse(result)
                except Exception as e:
                    print(str(e))
                s,created=student.objects.get_or_create(fullname=data.get('name'),defaults={"email":data.get('email'),"mobile_number":data.get('mobile')},)
                if created:
                    result={"status":True,"message":" Record created"}
                    response = JsonResponse(result)
                    token={"name":data.get('name'),"mobiel":data.get('mobile')}
                    response.set_cookie('name',token,max_age=25)
                    return response
                else:
                    result={"status":False,"message":" sorry record already exists"}
                    return JsonResponse(result)
        except Exception as e:
                print(str(e))
                result={"status":False,"message":str(e)}
                return JsonResponse(result)
    else:
        result={"status":False,"message":"Please use chrome"}
        return JsonResponse(result)



@csrf_exempt
def delet(request):
    result={"status":False}
    data= json.loads(request.body.decode('utf-8'))
    name=data.get('delete',None)
    if name:
        try:
            obj=student.objects.filter(Q(fullname=name) | Q(mobile_number=data.get("delete")))
            count=obj.count()
            if count==0:
                result["message"]="NO such records"
                return JsonResponse(result)
            obj.delete()
            result={"status":True,"Count":count}
        except Exception as e:
            print(str(e))
        return JsonResponse(result)
    else:
        result={"status":False,"msg":"please give some input"}
        return JsonResponse(result)


@csrf_exempt
def search(request):
    result={"status":False}
    data= json.loads(request.body.decode('utf-8'))
    try:
        obj=student.objects.filter(Q(fullname=data.get('data')) | Q(mobile_number=data.get("data")))
        count=obj.count()
        print(count)
        if count==0:
            print("insidde count-----")
            result["message"]="NO such records"
            return JsonResponse(result)
    except:
        result={"status":False}

    qs_json = studentserlizer(obj,many=True).data
    result={"status":True,"message":"success","data":qs_json}
    return JsonResponse(result,content_type='application/json')



# class GeeksList(ListView):

#         model = student

@csrf_exempt

def get_all(request):
        stu=student.objects.all()
        
        if stu:
            try:
                print("-in try--")
                students=studentserlizer(stu,many=True).data
                result={"status":True,"message":"success","data":students}
                return JsonResponse(result,content_type='application/json')
            except Exception as e:
                print(str(e))
        else:
            result={"status":False,"msg":"Nothing to show"}
            return JsonResponse(result)




@csrf_exempt
def all(request):
    print("----aall----")
    r=student.objects.all()
    c=r.count()
    r.delete()
    result={"status":True,"message":"Deleted","count":c}
    return JsonResponse(result)







class apis(viewsets.ViewSet):

    def info(self,request):
        data= json.loads(request.body.decode('utf-8'))
        result={"status":False,"Msg":"no such records"}
        
        obj=student.objects.filter(Q(fullname=data.get('name')) | Q(mobile_number=data.get("mobile_number")))
        if obj:
            qs_json = studentserlizer(obj,many=True).data
            result={"status":True,"message":"success","data":qs_json}
            return JsonResponse(result)
        return JsonResponse(result)




# class studentset(viewsets.ModelViewSet):
#     queyset=student.objects.all()
#     serializer_class = studentserlizer

class all_data(generic.ListView):
    template_name = "school/all_data.html"

    def get_queryset(self):
        s=student.objects.all()
        paginator = Paginator(s,2)
        page = self.request.GET.get('page')
        page_obj = paginator.get_page(page)
        return page_obj


# class detailview(generic.DeleteView):




