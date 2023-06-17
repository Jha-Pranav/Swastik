from django.shortcuts import render

from apps.home.models import AutoLoadData

# Create your views here.

# Auto add models and migrate
from apps.loaddata.management.commands import data2model

data = data2model.food_composition_table()
AutoLoadData.add_columns_from_dataframe(data)
