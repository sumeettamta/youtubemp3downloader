from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
# Create your models here.
from datetime import datetime
from datetime import date
from djutil.models import TimeStampedModel
# from constants import *


class ModelBase(TimeStampedModel):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        # self.modified_at = datetime.now()
        return super(ModelBase, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class User(AbstractBaseUser, ModelBase):
        """
        creates account models
        """
        username = models.CharField(max_length=50, blank=False,  default="")
        first_name = models.CharField(max_length=254, default="")
        last_name = models.CharField(max_length=254, default="")
        # password = models.CharField(max_length=254, blank=False, default="")
        email = models.EmailField(max_length=254, unique=True)
        is_active = models.BooleanField(default=True)
        last_ip = models.CharField(max_length=40, blank=False, default="")
        # last_login = models.DateTimeField()
        # phone = models.CharField(max_length=254, default="")
        # role = models.CharField(max_length=1, choices=ROLE_CHOICES, default="")


        GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            )
        gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")

        USERNAME_FIELD = 'email'

        # @property
        # def is_admin(self):
        #     return self.role == ADMIN

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(x for x in parts if x)