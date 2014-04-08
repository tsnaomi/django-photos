from django.conf.urls import patterns, url

urlpatterns = patterns(
    'photo_manager.views',
    url(r'^home/$',
        'home_view',
        name='home_view'),
    url(r'^album/(\d+)/$',
        'stub_view',
        name='album_view'),
    url(r'^photo/(\d+)/$',
        'stub_view',
        name='photo_detail_view'),
    )
