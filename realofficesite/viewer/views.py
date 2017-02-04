from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse

@csrf_exempt
def index(response):
    return render(response,'viewer/test.html')

def edit_favorites(request):
    if request.is_ajax():
        message = "YES,Ajax!"
    else:
        message = "Not Ajax"
    return HttpResponse(message)

def test(request):
    data = request.body
    print(data)
    return HttpResponse(data)
