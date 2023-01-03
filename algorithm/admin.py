from optparse import Option
from django.contrib import admin

from .models import *

admin.site.register(Doll)
admin.site.register(Algorithm)
admin.site.register(Stat)
admin.site.register(RecommendedSet)