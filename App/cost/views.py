from django.shortcuts import render


# Create your views here.
def cost(request):
    return render(request, "form.html")
