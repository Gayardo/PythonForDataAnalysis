from django.db import models

# Create your models here.
class Incident(models.Model):
    reassignment_count = models.FloatField()
    reopen_count       = models.FloatField()
    sys_mod_count      = models.FloatField()
    made_sla           = models.FloatField()
    u_priority_confirmation = models.FloatField()
    knowledge          = models.FloatField()

    # The dependent variable: y
    Duree_openToClose  = models.FloatField(null=True)
    # Just to give a date to the creation of the object instance
    created       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Un incident avec {self.made_sla}'