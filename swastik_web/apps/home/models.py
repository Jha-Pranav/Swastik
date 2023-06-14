from django.db import models
from django_pandas.managers import DataFrameManager

class AutoLoadData(models.Model):
    objects = DataFrameManager()

    class Meta:
        verbose_name_plural = "AutoLoadData"

    def __str__(self):
        return self.name

    @classmethod
    def add_columns_from_dataframe(cls, dataframe):
        for column in dataframe.columns:
            field_type = cls.get_field_type(dataframe[column].dtype)
            cls.add_to_class(column, field_type)

    @classmethod
    def get_field_type(cls, dtype):
        if dtype == 'int64':
            return models.IntegerField()
        elif dtype == 'float64':
            return models.FloatField()
        elif dtype == 'bool':
            return models.BooleanField()
        else:
            return models.CharField(max_length=255)

# from apps.algo_apps.load_pandas_df import food_composition_table

# # if __name__=="__main__":
# data =  food_composition_table.read_nutritional_data()
# AutoLoadData.add_columns_from_dataframe(data)
# AutoLoadData.objects.from_dataframe(data)   