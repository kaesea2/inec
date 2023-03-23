from django import forms
from .models import Lga,AnnouncedPuResults,PollingUnit,Party

class LgaForm(forms.Form):
    
    lga = forms.ModelChoiceField(queryset=Lga.objects.all(),to_field_name='lga_id')
    
class PU_ResultForm(forms.ModelForm):
    polling_unit = forms.ModelChoiceField(queryset=PollingUnit.objects.all())
    party = forms.ModelChoiceField(queryset=Party.objects.all())
    class Meta:
        model=AnnouncedPuResults   
        fields = ('party_score',)
