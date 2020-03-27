from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializerSerializer,Item
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.conf import settings 
from django.views.generic.base import TemplateView
import stripe 

stripe.api_key = settings.STRIPE_SECRET_KEY

class Index(APIView):
    def get(self, request):
        return render(request,'signup.html')
    def post(self, request):
        all_pro = Product.objects.all()
        se = UserSerializerSerializer(data=request.data)
        if se.is_valid(raise_exception=True):
            user_exist = User_log.objects.filter(email=request.data.get('email')).exists()
            if not user_exist:
                try:
                    usr = User_log.objects.create(
                        name=request.data.get('name'),
                        email=request.data.get('email'),
                        password=request.data.get('password'))
                    return HttpResponseRedirect('login')
                except Exception as e:
                    return Response({"Response": str(e)})
            else:
                return HttpResponse("user is exist plz login")

class login(APIView):
    def get(self, request):
        return render(request,'login.html')
    def post(self, request):
        user_exist = User_log.objects.filter(email=request.data.get('email')).exists()
        ps = User_log.objects.filter(
            email=request.data.get('email'),
            password=request.data.get('password'))
        if ps:
            if user_exist :
                all_pro3=Product3.objects.all()
                all_pro2=Product2.objects.all()
                all_pro1=Product1.objects.all()
                all_pro=Product.objects.all()
                us = User_log.objects.get(email=request.data.get('email'))
                b.n = us.name
                return render(request,'home.html',{'all_pro':all_pro,'us':us,'all_pro1':all_pro1,'all_pro2':all_pro2,'all_pro3':all_pro3})
            else:
                return HttpResponse("user is not exist plz signup")    
        else:
            return HttpResponse('nope')
b = login()

#class home(APIView):
 #   def get(self, request):
  #      all_pro3=Product3.objects.all()
   #     all_pro2=Product2.objects.all()
    #    all_pro1=Product1.objects.all()
     #   all_pro=Product.objects.all()
      #  return render(request,'home.html',{'all_pro':all_pro,'us':us,'all_pro1':all_pro1,'all_pro2':all_pro2,'all_pro3':all_pro3})

class Shop(APIView):
    def post(self, request):
        try:
            k = Pur.objects.create(
                        item=request.data.get('idd'),rates=request.data.get('dd'),nam=request.data.get('us'))

            return HttpResponse(b.n)
        except Exception as e:
            return HttpResponse(str(e))

    def get(self, request):
        pur1=Pur.objects.filter(nam=b.n)
        total = 0
        for i in pur1:
            total += (i.rates)
        return render(request,'cart.html',{"pur1":pur1,"total":total})



class Delete(APIView): 
    def post(self, request):
        Pur.objects.filter(nam=b.n).delete()
        return render(request,'clear.html')
        

class HomePageView(TemplateView):
    template_name = 'paygate.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        pay = Pur.objects.filter(nam=b.n)
        total =0
        for i in pay:
            total += int(i.rates)
            tot = {"tot":total}
            tot.update(context) 
        return tot

def charge(request): # new
    pay = Pur.objects.filter(nam=b.n)
    total =0

    for i in pay:
        total += int(i.rates)
        charge = stripe.Charge.create(
                amount = total,
                currency='INR',
                description='A Django charge',
                source=request.POST['stripeToken']
            )
        
    return render(request, 'charge.html')
