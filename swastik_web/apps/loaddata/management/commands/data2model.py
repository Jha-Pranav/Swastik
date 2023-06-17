from django.core.management.base import BaseCommand
from apps.loaddata.models import (
    FoodCompostionTable,
    FoodCompostionTableColMap,
    IndianFoodDatabase,
)
from django.db import connections
from django.db.migrations.executor import MigrationExecutor
from django.db.models import Q
from django.db import IntegrityError
from apps.algo_apps.load_pandas_df.food_composition_table import (
    read_nutritional_data,
    read_columns_mapping,
    read_indian_food_database,
)
import pandas as pd


import warnings

warnings.filterwarnings("ignore")

# Change 'default' to your database name if needed
connection = connections["default"]
executor = MigrationExecutor(connection)
migration_targets = executor.loader.graph.leaf_nodes()


class Command(BaseCommand):
    help = "Load data from a dataframe"

    def add_arguments(self, parser):
        pass
        # parser.add_argument('csvfile', type=str)

    def handle(self, *args, **options):
        # Read the CSV file into a pandas DataFrame
        data = read_indian_food_database()
        IndianFoodDatabase.add_columns_from_dataframe(data)

        # Apply migrations - This line is currently not working
        executor.migrate(migration_targets)

        # Create instances of the AutoLoadData model from the data
        instances = [IndianFoodDatabase(**item) for item in data.to_dict("records")]

        # Save the instances to the database
        try:
            print("Write to database")
            IndianFoodDatabase.objects.bulk_create(instances)
            print("Done!!")
        except IntegrityError:
            # If there is a unique constraint violation, delete the existing instances and try again
            conflicting_codes = [item["code"] for item in data.to_dict("records")]
            IndianFoodDatabase.objects.filter(Q(code__in=conflicting_codes)).delete()
            IndianFoodDatabase.objects.bulk_create(instances, ignore_conflicts=True)
