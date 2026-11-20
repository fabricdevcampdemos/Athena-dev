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

# CELL ********************

from fabric_devops import AppLogger, FabricRestApi, PowerBiRestApi, ItemDefinitionFactory

AppLogger.log_step('Running deployment job to connect semantic model to Azure datasource')

AppLogger.log_step('Reading variable values from variable library')

variable_library = notebookutils.variableLibrary.getLibrary('environment_settings')
adls_server = variable_library.getVariable('adls_server')
adls_path = variable_library.getVariable('adls_path')
adls_connection_id = variable_library.getVariable('adls_connection_id')

AppLogger.log_substep(f'adls_server: {adls_server}')
AppLogger.log_substep(f'adls_path: {adls_path}')
AppLogger.log_substep(f'adls_connection_id: {adls_connection_id}')

model_name = 'Product Sales Imported Model'
AppLogger.log_step(f'Setting up semantic model [{model_name}]')
model = FabricRestApi.get_item_by_name(model_name, 'SemanticModel')

AppLogger.log_substep('Updating Azure datasource for semantic model')
FabricRestApi.update_imported_model_with_azure_datasource(model, adls_server, adls_path)

AppLogger.log_substep('Binding semantic model to connection')
PowerBiRestApi.bind_semantic_model_to_connection(model['id'], adls_connection_id)

AppLogger.log_substep('Refreshing semantic model to import data files')
PowerBiRestApi.refresh_semantic_model(model['id'])


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
