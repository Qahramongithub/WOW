from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from WOW import settings


class User(AbstractUser):
    pass


class Branch(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')


class Terminal(models.Model):
    fast_id = models.CharField(max_length=50)
    branch_id = models.ManyToManyField('Branch', related_name='terminals')


class DayOff(models.Model):
    name = models.CharField(max_length=50)


class Sheff(models.Model):
    branch_id = models.ManyToManyField('Branch', related_name='dayoffs')
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Employee(models.Model):
    class Salary(models.TextChoices):
        Minute = 'minute', _('Minute')
        Hour = 'hour', _('Hour')
        Month = 'month', _('Month')

    full_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_birth = models.DateField()
    day_off = models.ManyToManyField('DayOff', related_name='employees', null=True, blank=True)
    sheff_id = models.ManyToManyField('Sheff', related_name='employees', null=True, blank=True)
    photo = models.ImageField(upload_to='images/')
    salary = models.CharField(max_length=50, choices=Salary.choices, default=Salary.Minute, null=True, blank=True)
    terminal_id = models.ManyToManyField('Terminal', related_name='employees')
    employee_id = models.CharField(max_length=100)
    phone_number = PhoneNumberField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    telegram_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Salary(models.Model):
    employee_id = models.ManyToManyField('Employee', related_name='salaries')
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Kpi(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    employee_id = models.ManyToManyField('Employee', related_name='kpi')


class OneDayOff(models.Model):
    day_off = models.DateField()
    employee_id = models.ManyToManyField('Employee', related_name='dayoffs')

    def __str__(self):
        return self.day_off


class Attendance(models.Model):
    employee_id = models.ManyToManyField('Employee', related_name='attendances')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.employee_id
