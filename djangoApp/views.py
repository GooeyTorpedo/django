from django.shortcuts import render
from django.http import HttpResponse
#request handler
# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World!')
    return render(request, 'hello.html')