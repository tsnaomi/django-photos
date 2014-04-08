from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
# from django.shortcuts import render, render_to_response
# from .forms import UploadFileForm
from models import Album, Photo

# Create your views here.


def stub_view(request, *args, **kwargs):  # -Cris Ewing
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def front_view():
    # Shows anonymous users something nice to encourage them to sign up
    pass


def home_view(request):
    # Shows logged-in users a list of their albums
    if request.user.is_authenticated():
        albums = Album.objects.get(creator=request.user)
        albums = albums.order_by('-modified_date')
        template = loader.get_template('home.html')
        context = RequestContext(request, {'albums': albums, })
        body = template.render(context)
        return HttpResponse(body, content_type='text/html')
    return HttpResponseRedirect('front')


def album_view():
    # Shows logged-in users a display of photos in a single album
    pass


def photo_detail_view():
    # Shows logged-in users a single photo along with details about it
    pass


# def all_photos_view(User=None):
#     # all photos view
#     pass


def upload_photo_view():
    # Allows users to add a new photo to an existing album
    pass


def edit_photo_view():
    # Allows users to edit an existing photo
    pass


# def delete_photo_view():
#     # Allows users to delete a photo
#     pass


def create_album_view():
    # Allows users to add a new album
    pass


# def delete_album_view():
#     # Allows users to delete an album
#     pass
