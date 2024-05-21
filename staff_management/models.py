from django.db import models

# Create your models here.
# class Staff(models.Model):
#     sl_no = models.AutoField(null= False, blank= False)
#     desig = models.CharField(max_length=100,null = False, blank= False)
#     name = models.CharField(max_length=100,null = False, blank= False)
#     Qualification = models.CharField(max_length=10,null = False, blank= False)
#     assigned_work = models.CharField(max_length=1000,null = False, blank= False)
#     ofc_entry = models.DateTimeField(auto_now_add=False)
#     ofc_out = models.DateTimeField(auto_now=False)

class Staff(models.Model):
    sl_no = models.AutoField(primary_key=True)
    desig = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    Qualification = models.CharField(max_length=10, null=False, blank=False)
    assigned_work = models.CharField(max_length=1000, null=False, blank=False)
    ofc_entry = models.DateTimeField(auto_now=False, auto_now_add=False)
    ofc_out = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'Staff_tracking'

    def __str__(self) -> str:
        return self.name

