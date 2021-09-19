from django import forms
from .models import Thumbnail_Configurable

class ConfigurableThumbForm(forms.ModelForm):
    class Meta:
        model = Thumbnail_Configurable
        fields = ('owner', 'thumb_configurable', 'thumb_width', 'thumb_height')

        widgets = {
            'owner': forms.TextInput(attrs={'class':'form-control', 'id':'owner', 'type':'hidden'}),
            'thumb_configurable': forms.FileInput(attrs={'class':'form-control'}),
            'thumb_width': forms.NumberInput(attrs={'class':'form-control', 'min':0.00}),
            'thumb_height': forms.NumberInput(attrs={'class':'form-control', 'min':0.00}),
        } 