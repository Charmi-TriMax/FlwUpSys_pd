from django.shortcuts import render

# Create your views here.
def CrDetails(request):
    return render(request, 'utils/create_Details.html')