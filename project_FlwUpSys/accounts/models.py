from django.db import models
from django.contrib.auth.models import User
from .user_types import get_user_type_choices
from datetime import datetime


class CustomUser(User):
    password_reset_required = models.BooleanField(default=True)


class UserLogin(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    password = models.CharField(max_length=128)


class Staff(models.Model):
    USER_TYPE_CHOICES = get_user_type_choices()
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    code = models.CharField(max_length=20, unique=True)
    isActive = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    Designation = models.CharField(max_length=50, blank=True)
    dob = models.DateField()
    mobile = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50, blank=True)
    ForceReset = models.BooleanField(default=True)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    def is_superuser(self):
        return self.user_type == 'superuser'

    def is_manager(self):
        return self.user_type == 'manager'

    def is_general(self):
        return self.user_type == 'general'

    class Meta:
        db_table = 'Staff'
