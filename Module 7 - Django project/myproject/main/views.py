from django.shortcuts import render

from .models import DjangoProject

# Create your views here.
def homepage(request):
    return render(
        request=request,
        template_name="home.html",
        context={"cursos": DjangoProject.objects.all},
    )
