from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Q

from apps.loaddata.models import (
    FoodCompostionTable,
    FoodCompostionTableColMap,
    IndianFoodDatabase,
)

import pandas as pd

from apps.algo_apps.load_pandas_df.food_composition_table import nutrional_data_view


@login_required(login_url="/login/")
def index(request):
    context = {"segment": "index"}

    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split("/")[-1]
        print(load_template)
        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)
        if load_template == "food_composition_table.html":

            return HttpResponse(
                html_template.render(*food_composition_table_view(request))
            )
        elif load_template == "indian_food_database.html":
            return HttpResponse(
                html_template.render(*indian_food_database_view(request))
            )

        else:
            return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    except BaseException as error:
        print(error)
        html_template = loader.get_template("home/page-500.html")
        return HttpResponse(html_template.render(context, request))


def food_composition_table_view(request):
    object_list = FoodCompostionTable.objects.all()
    df = pd.DataFrame(list(object_list.values()))
    df = nutrional_data_view(df)
    col_map = (
        pd.DataFrame.from_records(
            FoodCompostionTableColMap.objects.values("code", "name")
        )
        .set_index("code")
        .to_dict()["name"]
    )
    field_names = [
        "name",
        "grup",
        "enerc",
        "water",
        "ash",
        "vit",
        "fatce",
        "cholc",
        "fibtg",
        "choavldf",
        "protcnt",
        "amiac",
        "cartoid",
        "polyph",
        "phystr",
        "tocph",
    ]
    context = {
        "field_names": field_names,
        "alias_name": [col_map[name] for name in field_names],
        "object_list": df.to_records(index=True),
    }
    return context, request


def indian_food_database_view(request):
    object_list = IndianFoodDatabase.objects.all()
    df = pd.DataFrame(list(object_list.values()))
    df.drop("id", axis=1, inplace=True)
    df = df.applymap(lambda x: x.title())
    field_names = df.columns
    context = {
        "field_names": field_names,
        "alias_name": [name.title() for name in field_names],
        "object_list": df.to_records(index=True),
    }
    return context, request
