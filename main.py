"""Main module for the application."""
import api as api
import ui as ui

number = ui.request_number()
department = ui.request_deparment()
client = api.create_client()
data = api.get_data(number, department, client)
data_convert = api.convert_dataframe(data)
data_clean = api.clean_data(data_convert)
formatted_data = api.format_df(data_clean)
ui.show_data(formatted_data)
ui.graph_data(data_clean)
#end line