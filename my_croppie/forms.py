from django import forms
from .models import Image


# You can have the fields in your form mirror those in the model automatically by having
# your form derive from forms.ModelForm instead of forms.Form
# BEGIN modelform
# class ImageUploadForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['photo', 'description', 'cropped_photo']
# END modelform


# Deriving from forms.Form creates a standalone form not linked to the model
# You have to map fields yourself. This is what is needed with croppie
# BEGIN form
class ImageUploadForm(forms.Form):
    photo = forms.ImageField()
    description = forms.CharField(max_length=255)
    # croppie passed back the cropped image as base64
    cropped_photo = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ImageUploadForm, self).__init__(*args, **kwargs)
# END form
