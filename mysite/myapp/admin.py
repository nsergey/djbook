from myapp.models import Person
from myapp.models import Musician
from myapp.models import Album
from myapp.models import Manufacturer
from myapp.models import Car
from myapp.models import Student
from myapp.models import Teacher
from myapp.models import Article
from myapp.models import Publication

from django.contrib import admin


admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)

admin.site.register(Manufacturer)
admin.site.register(Car)

admin.site.register(Student)
admin.site.register(Teacher)

admin.site.register(Article)
admin.site.register(Publication)

