from django.forms import ModelForm, DateInput
from django.forms.widgets import SelectDateWidget
from .models import Tree
from django import forms

class TreeRecordForm(ModelForm):
    harvestDate = forms.DateField(widget=SelectDateWidget)
    harvestTime = forms.TimeField(widget=DateInput(attrs={'type': 'time'}))

    def __init__(self, treeindex, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['treeID'].initial = treeindex

    class Meta:
        model = Tree
        fields = ["treeID", "section", "age", "variety", "soil_moisture", "temperature",
                  "humidity", "light_exposure", "nutrient_levels", "pest_disease_outbreaks",
                  "harvestTime", "harvestDate", "tree_image"]
        widgets = {
            'treeID': forms.HiddenInput(),
        }



