from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    returnobject = HttpResponse('<h1>hello world</h1>')
    return returnobject

class HelloWorldView(TemplateView):
    template_name = 'hello.html'
