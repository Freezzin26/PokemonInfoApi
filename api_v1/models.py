
# Create your models here.
from django.db import models

class Pmdex(models.Model):
    pm_id = models.TextField(db_column='pm_Id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    pm_name_cn = models.TextField()
    pm_name_en = models.TextField()
    pm_name_jp = models.TextField()
    pm_type = models.TextField(db_column='pm_Type')  # Field name made lowercase.
    pm_abi = models.TextField(db_column='pm_Abi')  # Field name made lowercase.
    pm_hp = models.IntegerField(db_column='pm_HP')  # Field name made lowercase.
    pm_atk = models.IntegerField(db_column='pm_Atk')  # Field name made lowercase.
    pm_def = models.IntegerField(db_column='pm_Def')  # Field name made lowercase.
    pm_satk = models.IntegerField(db_column='pm_SAtk')  # Field name made lowercase.
    pm_sdef = models.IntegerField(db_column='pm_SDef')  # Field name made lowercase.
    pm_spd = models.IntegerField(db_column='pm_Spd')  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'pmdex'

    def __str__(self):
        return self.pm_name_cn


class Pmnatures(models.Model):
    nature = models.TextField()
    nature_jp = models.TextField()
    nature_en = models.TextField()
    hp_rectify = models.FloatField()  # This field type is a guess.
    atk_rectify = models.FloatField()  # This field type is a guess.
    def_rectify = models.FloatField()  # This field type is a guess.
    satk_rectify = models.FloatField()  # This field type is a guess.
    sdef_rectify = models.FloatField()  # This field type is a guess.
    spd_rectify = models.FloatField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pmnatures'

    def __str__(self):
        return self.nature