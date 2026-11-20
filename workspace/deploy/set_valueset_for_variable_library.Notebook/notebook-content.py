# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "c09c1f7d-f521-49bb-b432-63c1356f34d6",
# META       "default_lakehouse_name": "deployment_logs",
# META       "default_lakehouse_workspace_id": "1351a8a9-42e9-4a5e-b15b-6753641f58f3",
# META       "known_lakehouses": [
# META         {
# META           "id": "c09c1f7d-f521-49bb-b432-63c1356f34d6"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "255eafde-06e0-4be1-909a-8a7e916a73ce",
# META       "workspaceId": "973f7ce3-7526-4d20-bf9c-3125ba51e0e9"
# META     }
# META   }
# META }

# PARAMETERS CELL ********************

target_environment = None

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from fabric_devops import AppLogger, FabricRestApi, PowerBiRestApi

if target_environment in ['dev', 'test', 'prod']:
    variable_library = FabricRestApi.get_item_by_name('environment_settings', "VariableLibrary")
    FabricRestApi.set_active_valueset_for_variable_library(variable_library, target_environment)
else:
    AppLogger.log_step(f'Cannot set active value set to [{target_environment}]')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

AppLogger.end_logging_session()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
