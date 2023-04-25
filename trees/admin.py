from django.contrib import admin
from .models import Tree

#Register your models here.
class TreeAdmin(admin.ModelAdmin):
    model = Tree
    list_display = ("section", "age", "variety", "soil_moisture", "temperature",
                  "humidity", "light_exposure", "nutrient_levels", "pest_disease_outbreaks",
                  "harvestTime", "tree_image")
admin.site.register(Tree, TreeAdmin)