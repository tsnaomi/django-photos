import os

from datetime import timedelta
from django.core.exceptions import ValidationError
from django.core.files import File
from django.db import IntegrityError
from django.test import TestCase
from models import Photo, Album, User  # Tag

# Create your tests here.


# class TestModels(TestCase):

#     def setUp(self):
#         HOME = os.path.dirname(os.path.dirname(__file__))
#         self.filename1 = os.path.join(HOME, 'TEST_IMAGES/Hogwarts.jpg')
#         self.filename2 = os.path.join(HOME, 'TEST_IMAGES/Beauxbatons.jpg')
#         self.title = 'Fantastic Beasts and Where to Find Them'
#         self.user = User.objects.create_user(
#             'HermioneGranger',
#             'NEWTSforever@Hogwarts.edu',
#             'shewhomustnotbenamed')

#     def generate_photo(self, filename, user=None):
#     # source: https://gist.github.com/qingfeng/402903
#         photo = Photo.objects.create(creator=user, image=File(open(filename)),
#                                      caption='Mischief Managed')
#         return Photo.objects.get(pk=photo.pk)

#     def test_photo(self):
#         photo = self.generate_photo(self.filename1, self.user)
#         self.assertAlmostEqual(photo.published_date, photo.modified_date,
#                                delta=timedelta(microseconds=20000))
#         self.assertEqual(photo.caption, 'Mischief Managed')
#         self.assertEqual(unicode(photo), u'Mischief Managed')

#     def test_photo_ordering(self):
#     # source: https://github.com/paulcwatts/codefellows-django-testing
#         photo1 = self.generate_photo(self.filename1, self.user)
#         photo2 = self.generate_photo(self.filename2, self.user)
#         QRY = Photo.objects.all().order_by('-published_date')
#         self.assertQuerysetEqual(QRY, [photo2, photo1], transform=lambda x: x)

#     def test_photo_NAY_USER(self):
#         with self.assertRaises(IntegrityError):
#             Photo.objects.create(caption='Mischief Managed')

#     def test_photo_NAY_CAPTION(self):
#         photo = Photo.objects.create(creator=self.user)
#         self.assertEqual(photo.caption, 'Untitled')
#         self.assertEqual(unicode(photo), u'Untitled')

#     def test_album(self):
#         album = Album.objects.create(creator=self.user, title=self.title)
#         photo = self.generate_photo(self.filename1, self.user)
#         photo.albums.add(album)
#         self.assertAlmostEqual(album.published_date, album.modified_date,
#                                delta=timedelta(microseconds=20000))
#         self.assertEqual(album.title, self.title)
#         self.assertEqual(unicode(album), u'%s' % self.title)
#         self.assertIn(album, photo.albums.all())

#     def test_album_NAY_USER(self):
#         with self.assertRaises(IntegrityError):
#             Album.objects.create(title=self.title)

#     def test_album_NAY_TITLE(self):
#         album = Album.objects.create(creator=self.user)
#         self.assertEqual(album.title, 'Untitled')
#         self.assertEqual(unicode(album), u'Untitled')


class TestViews(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_front_view(self):
        pass

    def test_home_view(self):
        pass

    def test_album_view(self):
        pass

    def test_all_photos_view(self):
        pass

    def test_photo_detail_view(self):
        pass

    def test_upoad_photo_view(self):
        pass

    def test_delete_photo_view(self):
        pass

    def test_create_album_view(self):
        pass

    def test_delete_album_view(self):
        pass
