from django.http import HttpResponse

    def hello(request):
        return HttpResponse("From heck_world, Hello")
