import base64
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from .forms import ImageUploadForm
from .models import Image


def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # For modelform, uncomment below, and change forms.py
            # BEGIN modelform
            # saved_form = form.save()
            # image_id = saved_form.id
            # END modelform

            # For form, uncomment below, and change forms.py
            # BEGIN form
            photo = form.cleaned_data["photo"]
            description = form.cleaned_data["description"]
            cropped_photo_file = save_cropped_image_to_file(request)
            image_model = Image(photo=photo,description=description,cropped_photo=cropped_photo_file)
            image_model.save()
            image_id = image_model.id
            # END form

            return HttpResponseRedirect('/images/'+str(image_id))
    else:
        form = ImageUploadForm()

    context = {
        'image_form': form,
    }
    return render(request, 'my_croppie/image_upload.html',  context=context)


def detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    context = {
        'image': image,
    }
    return render(request, 'my_croppie/detail.html', context=context)


def index(request):
    image_list = Image.objects.all()
    context = {'image_list': image_list}
    return render(request, 'my_croppie/index.html', context=context)


# The cropped image is returned from croppie as a base64 string
# This is stored in a char field in the form
# Here, we write that string to a file, and return the path of the file
# so that the path can be stored in the model as an ImageField
def save_cropped_image_to_file(request):
    fs = FileSystemStorage()
    if request.POST.get('cropped_photo'):
        data = request.POST['cropped_photo']
        if request.POST.get('cropped_photo'):
            file_name = "images/cropped_" + request.FILES['photo'].name
        format, imgstr = data.split(';base64,')
        ext = format.split('/')[-1]
        file_obj = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        filename = fs.save(file_name, file_obj)
        return filename
