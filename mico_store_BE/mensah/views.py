
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import School

# Create your views here.
def home(request):

    return JsonResponse({'success':'loaded my first route mensah'})

def school(request):
    s = School(name = 'Atomic Hills', address = 'AK-245-8745', country = 'Ghana')
    s.save()
    return JsonResponse({'success':'loaded my school information'})
