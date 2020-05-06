from django.shortcuts import render
import os
from django.core.files.storage import FileSystemStorage

from .forms import FileForm, PhotoForm
# Create your views here.


def upload_img(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST' and 'img' in request.POST:
        context = dict(backend_form=PhotoForm())
        form = PhotoForm(request.POST, request.FILES)
        context['form'] = form.instance
        if form.is_valid():
            form.save()
    else:
        form = FileForm()

    return render(request, 'upload_img.html', context)


def upload_file(request):

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['fileup']
            name, extension = os.path.splitext(uploaded_file.name)
            print(extension)
            print(name)
            form.save()
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})
