from django.contrib import admin

from.models import Medicine
from.models import Doctors

class AdminImages(admin.ModelAdmin):    
    list_display = ['name','img','price'] 
admin.site.register(Medicine,AdminImages)

class AdminImages(admin.ModelAdmin):    
    list_display = ['name','img','desc'] 
admin.site.register(Doctors,AdminImages)
