from dagster import job, op
import subprocess
import os

# Define an operation (op) to run the dbt command
@op
def run_dbt_seed(context):
    dbt_project_dir = '/mnt/dbt/buy_box_gcp_1'
    profiles_dir = '/mnt/dbt/buy_box_gcp_1'        # Path to your profiles.yml

    # DBT command to run the seed
    command = f"dbt seed --profiles-dir {profiles_dir} --project-dir {dbt_project_dir}"
    
    # Run the command using subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Log the output and error messages
    context.log.info(f"DBT Seed Output: {result.stdout}")
    context.log.error(f"DBT Seed Errors: {result.stderr}")
    
    if result.returncode != 0:
        raise Exception(f"DBT Seed failed with return code {result.returncode}")

# Define the Dagster job that uses the above operation
@job
def dbt_seed_job():
    run_dbt_seed()






# from dagster import Definitions
# from dagster_dbt import dbt_cli_resource, load_assets_from_dbt_project

# DBT_PROJECT_PATH = "/opt/dagster/app/buy_box_gcp_1"

# # Load DBT assets
# dbt_assets = load_assets_from_dbt_project(DBT_PROJECT_PATH)

# # DBT CLI resource definition
# resources = {
#     "dbt": dbt_cli_resource.configured({"project_dir": DBT_PROJECT_PATH})
# }

# defs = Definitions(assets=dbt_assets, resources=resources)



# from dagster import FilesystemIOManager, graph, op, repository
# from dagster_docker import docker_executor

# # New op for the "Welcome to Data Engineering" message
# @op
# def welcome_message():
#     return "Welcome to Data Engineering!"

# # New graph for welcome message job
# @graph
# def welcome_graph():
#     return welcome_message()

# # New job for welcome message
# welcome_job = welcome_graph.to_job(name="welcome_job")


# # Define the repository to include the new job
# @repository
# def deploy_dagster_repository():
#     return [welcome_job]
