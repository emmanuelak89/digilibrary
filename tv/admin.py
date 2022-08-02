from django.contrib import admin
from .models import *

admin.site.register(VideoPack)
admin.site.register(VideoRepo)
admin.site.register(UserVideoList)
admin.site.register(UserVideoLike)