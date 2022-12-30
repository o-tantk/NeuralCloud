from optparse import Option
from django.contrib import admin

from .models import *

admin.site.register(Doll)
admin.site.register(AlgorithmBase)
admin.site.register(PrimaryStat)
admin.site.register(SecondaryStat)
admin.site.register(Algorithm)
admin.site.register(Combination)