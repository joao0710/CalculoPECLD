from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from time import sleep

# Create your views here.


def home(request):
    return HttpResponse("Olá, Django!")


#def home(request):
#    return render(request, 'base/home.html')
#    #return HttpResponse("Olá Django")
#
#
#def stream_response(request):
#    def stream_content():
#        for i in range(1000):
#            sleep(1)
#            yield f'{i}\n'
#    return StreamingHttpResponse(stream_content())