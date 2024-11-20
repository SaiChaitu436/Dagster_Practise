from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import buy_box_gcp_1_dbt_assets
from .project import buy_box_gcp_1_project
from .schedules import schedules

defs = Definitions(
    assets=[buy_box_gcp_1_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=buy_box_gcp_1_project),
    },
)