from datetime import datetime
from django.db import models
from django_pandas.managers import DataFrameManager


class Base(models.Model):

    objects = DataFrameManager()

    class Meta:
        abstract = True
        # db_table = 'db workspace'

    @classmethod
    def add_columns_from_dataframe(cls, dataframe):
        for column in dataframe.columns:
            field_type, default_value = cls.get_field_type_and_default_value(
                dataframe[column].dtype
            )
            if not hasattr(cls, column):
                if field_type == models.CharField:
                    cls.add_to_class(
                        column, field_type(default=default_value, max_length=2000)
                    )
                else:
                    cls.add_to_class(column, field_type(default=default_value))

    @classmethod
    def get_field_type_and_default_value(cls, dtype):
        field_map = {
            "int64": (models.FloatField, 0.0),
            "float64": (models.FloatField, 0.0),
            "bool": (models.BooleanField, False),
            "datetime64[ns]": (models.DateTimeField, datetime.now),
            "timedelta64[ns]": (models.DurationField, None),
            "object": (models.CharField, ""),
        }
        return field_map.get(str(dtype), (models.CharField, ""))


class FoodCompostionTable(Base):
    code = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "food_compostion_table"
        verbose_name_plural = "FoodCompostionTable"

    def __str__(self):
        return self.code


class FoodCompostionTableColMap(Base):
    code = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "food_compostion_table_col_map"
        verbose_name_plural = "FoodCompostionTableColMap"

    def __str__(self):
        return self.code


class IndianFoodDatabase(Base):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "indian_food_database"
        verbose_name_plural = "IndianFoodDatabase"

    def __str__(self):
        return self.code


from apps.algo_apps.load_pandas_df.food_composition_table import (
    read_nutritional_data,
    read_columns_mapping,
    read_indian_food_database,
)

data = read_nutritional_data()
FoodCompostionTable.add_columns_from_dataframe(data)
data = read_columns_mapping()
FoodCompostionTableColMap.add_columns_from_dataframe(data)
data = read_indian_food_database()
IndianFoodDatabase.add_columns_from_dataframe(data)
