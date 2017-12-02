from django import forms
from .models import Picture
 
 
class PhotoUploadForm(forms.Form):
    file = forms.ImageField(required=True)