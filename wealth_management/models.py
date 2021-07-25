from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null= True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null= True, blank=True)

    class Meta:
        abstract = True


class FixedDeposit(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    amount_invested = models.FloatField(null=False, blank=False)
    organization_type = models.CharField(max_length=200, null=False, blank=False)
    organization_name = models.CharField(max_length=200, null=False, blank=False)
    date_of_investment = models.DateField(null=False, blank=False)
    annual_roi = models.FloatField(null=False, blank=False)
    maturity_date = models.DateField(null=False, blank=False)
    created_by = UserForeignKey(auto_user_add=True, related_name='fd_created_by', null=False, blank=False)
    last_modified_by = UserForeignKey(auto_user=True, auto_user_add=True, related_name='fd_updated_by', null=False, blank=False)

    def __str__(self):
        return str(self.id) + str(self.created_by.username)
    class Meta:
        verbose_name_plural="Fixed Deposit"


class Bullion(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200, null=False, blank=False)
    weight = models.FloatField(null=False, blank=False)
    amount_invested = models.FloatField(null=False, blank=False)
    date_of_investment = models.DateField(null=False, blank=False)
    created_by = UserForeignKey(auto_user_add=True, related_name='bullion_created_by', null=False, blank=False)
    last_modified_by = UserForeignKey(auto_user=True, auto_user_add=True, related_name='bullion_updated_by', null=False, blank=False)

    def __str__(self):
        return str(self.id) + str(self.created_by.username)
    class Meta:
        verbose_name_plural="Bullion"