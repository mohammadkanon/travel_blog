from django.contrib import admin
from blog.models import CommonInfo, BestMoments, Tour, Comments

# Register your models here.

admin.site.register(CommonInfo)
admin.site.register(BestMoments)
admin.site.register(Tour)
admin.site.register(Comments)
