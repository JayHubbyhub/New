from django.forms import ModelForm, DateInput
from django.forms.widgets import SelectDateWidget
from .models import Tree
from django import forms

class TreeRecordForm(ModelForm):
    harvestDate = forms.DateField(widget=SelectDateWidget)
    harvestTime = forms.TimeField(widget=DateInput(attrs={'type': 'time'}))
        
    def __init__(self, *args, **kwargs):
        treeID = kwargs.pop('treeID', None)
        super().__init__(*args, **kwargs)
        self.fields['treeID'].initial = treeID

    tree_id = forms.ModelChoiceField(
        queryset=Tree.objects.order_by('treeID').values_list('treeID', flat=True).distinct(),
        initial=None,
        required=True,
        empty_label=None,
        label='Select a Tree'
    )
    class Meta:
        model = Tree
        fields = ["treeID", "section", "age", "variety", "soil_moisture", "temperature",
                  "humidity", "light_exposure", "nutrient_levels", "pest_disease_outbreaks",
                  "harvestTime", "harvestDate", "tree_image"]
