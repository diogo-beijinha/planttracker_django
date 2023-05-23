from django.shortcuts import render
import requests
import json
from .models import Plants

# Create your views here.
# def index(request):
#     username = password = ''
#     if request.POST:
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/orders/')
#     return render(request, template_name='index.html')

def home(request):

    # Get list of owned plants
    plant_list = Plants.objects.all()

    # Get information about owned plants
    token = "pTMeYYiAhYiCULE3e-59pSH-FMBj_2njt7pccKcTpcY"

    image_list = []
    common_names_list = []
    i = 0
    for plant in plant_list:
        r = requests.get('https://trefle.io/api/v1/plants?token={0}&filter[scientific_name]={1}'.format(token, plant_list[i].scientific_name))
        resp_dict = r.json()
        pretty = json.dumps(resp_dict, indent=4)
        print(pretty)
        image_list.append(resp_dict['data'][0]['image_url'])
        common_names_list.append(resp_dict['data'][0]['common_name'])
        i += 1

    # Save data in Context
    context = {
        'plant_num': range(len(plant_list)),
        'plants': plant_list,
        'plant_images': image_list,
        'plant_common_names': common_names_list,
    }

    for n in range(len(plant_list)):
        print(n)

    return render(request, template_name='home.html', context=context)