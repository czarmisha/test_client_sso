from django.http import HttpResponse
def home(request):
    print(request.session)
    print(request.session.keys())
    return HttpResponse("NOT OK")