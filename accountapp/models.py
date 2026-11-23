
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator, RegexValidator
from datetime import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class Speciality(models.Model):
    
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Speciality" 
        verbose_name_plural = "Specialities"


    def __str__(self):
        return self.name
    
class User(AbstractUser):
    pass
number_validator = RegexValidator(r'^\d{8}$', 'number must be exactly 8 digits.')
class Doctor(User):
    licence_number = models.CharField(max_length=6, unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialities = models.ManyToManyField('Speciality', related_name='doctors') 
    class Meta:
        verbose_name = "Doctor" 
        verbose_name_plural = "Doctors"
def validate_birth_date(value):
    if value >= timezone.localdate():
        raise ValidationError('Birth date cannot be in the future.')    
class Patient(User):    
    national_id = models.CharField(max_length=8, unique=True,validators=[number_validator])
    phone = models.CharField(max_length=8,validators=[number_validator])
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Patient" 
        verbose_name_plural = "Patients"


