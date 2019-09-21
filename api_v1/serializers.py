from rest_framework import serializers
from .models import Pmdex

class PmdexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pmdex
        fields = ('pm_id','pm_name_cn','pm_type','pm_abi','pm_hp','pm_atk','pm_def','pm_satk','pm_sdef','pm_spd')