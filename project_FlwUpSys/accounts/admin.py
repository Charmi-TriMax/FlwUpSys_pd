from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','code','isActive', 'user_type','Designation', 'dob','mobile','Phone','ForceReset','Other1','Other2','CrDtTm','CrBy','CrFrom','UpdDtTm','UpdBy','UpdFrom')