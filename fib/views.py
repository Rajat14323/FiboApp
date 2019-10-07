from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def home(request):
	# return HttpResponse("Hello World")
	return render(request,'home.html')

def add(request):
	time_start = time.time()


	val1 =request.GET['num1']
      
        
	res= Fibo(int(val1)) 

   
	return render(request,'result.html',{"result":res,"time":(time.time()-time_start)})

def Fibo(n): 
    if n==1: 
        return 1
  
   
    elif n==2: 
        return 1
    
    else: 
        return Fibo(n-1)+Fibo(n-2) 
