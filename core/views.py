from django.shortcuts import render
from django.http import HttpResponse
import os
from django.core.files.storage import FileSystemStorage
import simplejson as JSON
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .forms import FileForm, PhotoForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def upload_img(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':

        form = PhotoForm(request.POST, request.FILES)
        context['form'] = form.instance
        if form.is_valid():
            form.save()

            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
    else:

        return render(request, 'upload_img.html', context)


@csrf_exempt
def upload_file(request):

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['fileup']
            name, extension = os.path.splitext(uploaded_file.name)
            print(extension)
            print(name)

            form.save()

            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})

    else:
        form = FileForm()

        return render(request, 'upload.html', {'form': form})
