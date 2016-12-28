from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey, stupid. You made it through the tutorial")
