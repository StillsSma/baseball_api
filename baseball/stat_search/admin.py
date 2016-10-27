from django.contrib import admin

# Register your models here.
from stat_search.models import Master, Batting, Pitching, Fielding

admin.site.register(Master)
admin.site.register(Batting)
admin.site.register(Pitching)
admin.site.register(Fielding)
