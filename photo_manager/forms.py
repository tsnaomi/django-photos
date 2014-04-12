from django.forms import ModelForm
from models import Photo, Album


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'public_album']
