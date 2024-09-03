"""Main module for the application."""
import api as api
import ui as ui

number = ui.request_number()
department = ui.request_deparment()
client = api.create_client()
data = api.get_data(number, department, client)
data_convert = api.convert_dataframe(data)
formatted_data = api.format_df(data_convert)
ui.show_data(formatted_data)
#end line