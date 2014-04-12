from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import logout_then_login
from django.core.context_processors import csrf
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from forms import PhotoForm, AlbumForm
from models import Album, Photo


@login_required(login_url='login')
def home_view(request):
    ''' Shows logged-in users a list of their albums '''
    albums = Album.objects.all()
    albums = albums.filter(creator=request.user)
    albums = albums.order_by('-modified_date')
    ALBUMS, EMPTY = {}, []
    for album in albums:
        photos = album.photo_set.all()
        if len(photos) > 0:
            ALBUMS[album] = photos[0]
        else:
            EMPTY.append(album)
    context = {'albums': ALBUMS, 'empty': EMPTY, }
    return render(request, 'home.html', context)


def album_view(request, a):
    ''' Display photos from a single album '''
    try:
        album = Album.objects.get(pk=a)
    except Album.DoesNotExist:
        raise Http404
    if album.creator == request.user or album.public_album is True:
        context = {'album': album, }
        return render(request, 'album.html', context)
    raise PermissionDenied


def photo_detail_view(request, a, p):
    ''' Display a single photo along with details about it '''
    try:
        album = Album.objects.get(pk=a)
        photo = Photo.objects.get(pk=p)
    except Album.DoesNotExist:
        raise Http404
    except Photo.DoesNotExist:
        raise Http404
    if photo.creator == request.user or album.public_album is True:
        context = {'photo': photo, 'album': album}
        return render(request, 'photo.html', context)
    return PermissionDenied


@permission_required('photo_manager.add_album', login_url='login')
@permission_required('photo_manager.add_photo', login_url='login')
def create_album_view(request):
    ''' Allows users to create new albums and upload photos '''
    if request.POST:
        album = Album(creator=request.user)
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return HttpResponseRedirect('/edit/%s' % album.pk)
        messages.info(request, 'Incomplete input.')
        return HttpResponseRedirect(reverse('create'))
    album_form, photo_form, c = AlbumForm(), PhotoForm(), {}
    c.update(csrf(request))
    context = {'album_form': album_form, 'photo_form': photo_form, 'c': c, }
    return render(request, 'create.html', context)


@permission_required('photo_manager.change_album', login_url='login')
@permission_required('photo_manager.delete_album', login_url='login')
@permission_required('photo_manager.add_photo', login_url='login')
@permission_required('photo_manager.change_photo', login_url='login')
@permission_required('photo_manager.delete_photo', login_url='login')
def edit_album_view(request, a):
    ''' Allows users to edit albums '''
    try:
        album = Album.objects.get(pk=a)
    except Album.DoesNotExist:
        raise Http404
    if album.creator == request.user:
        if request.POST:
            photo = Photo(creator=request.user)
            photo_form = PhotoForm(request.POST, request.FILES, instance=photo)
            if photo_form.is_valid():
                photo_form.save()
                photo.albums.add(album)
                photo.save()
            return HttpResponseRedirect('/edit/%s' % a)
        c = {}
        c.update(csrf(request))
        context = {'c': c, 'album': album, 'PhotoForm': PhotoForm(), }
        message = 'Click texts to edit.'
        message += ' Click images to delete.' if \
            len(album.photo_set.all()) > 0 else ''
        messages.info(request, message)
        return render(request, 'edit_album.html', context)
    raise PermissionDenied


@permission_required('photo_manager.change_photo', login_url='login')
@permission_required('photo_manager.delete_photo', login_url='login')
def edit_photo_view(request, a, p):
    ''' Allows users to edit individual photos '''
    try:
        album = Album.objects.get(pk=a)
        photo = Photo.objects.get(pk=p)
    except Album.DoesNotExist:
        raise Http404
    except Photo.DoesNotExist:
        raise Http404
    if photo.creator == request.user:
        context = {'photo': photo, 'album': album}
        messages.info(request, 'Click caption to edit. Click image to delete.')
        return render(request, 'edit_photo.html', context)
    return PermissionDenied


@permission_required('photo_manager.delete_album', login_url='login')
def delete_album_view(request, a):
    ''' Deletes an album '''
    try:
        album = Album.objects.get(pk=a)
    except Album.DoesNotExist:
        raise Http404
    if album.creator == request.user:
        for photo in album.photo_set.all():
            photo.delete()
        album.delete()
    return HttpResponseRedirect(reverse('home'))


@permission_required('photo_manager.delete_photo', login_url='login')
def delete_photo_view(request, a, p):
    ''' Deletes a photo '''
    try:
        photo = Photo.objects.get(pk=p)
    except Photo.DoesNotExist:
        raise Http404
    if photo.creator == request.user:
        photo.delete()
    return HttpResponseRedirect('/edit/%s' % a)


def LOGIN(request):
    if request.user.is_authenticated():
        messages.info(request, 'You are already logged in as %s.' %
                      request.user.username)
        return HttpResponseRedirect(reverse('home'))
    if request.POST:
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'You are now logged in as %s.' %
                          request.user.username)
            return HttpResponseRedirect(reverse('home'))
        messages.info(request, 'Invalid username or password.')
        return HttpResponseRedirect(reverse('login'))
    context = {'AuthenticationForm': AuthenticationForm}
    return render(request, 'login.html', context)


def LOGOUT(request):
    messages.info(request, 'You have been logged out.')
    return logout_then_login(request, login_url='login')


def ACTIVATION_COMPLETE(request):
    if request.user.is_anonymous():
        messages.info(request, 'Registration confirmed! Welcome to Photette.')
    return HttpResponseRedirect(reverse('home'))


def photette_403(request):
    return render_to_response('403.html')


def photette_404(request):
    return render_to_response('404.html')
