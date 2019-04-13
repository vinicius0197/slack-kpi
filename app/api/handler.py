import os
import json
import re
import yaml
import gspread

from oauth2client.service_account import ServiceAccountCredentials
from unicodedata import normalize
from oauth2client.service_account import ServiceAccountCredentials

# Suposição que cada requisição so irá executar uma operação
# Dito isso, Cada operação irá requisitar a api do sheets
# Retorna objeto com kpis, valores e metas, formatado ou não

def return_sheet(format_value='FORMATTED_VALUE'):
    """
        Use credentials to create a client to interact with the Google Drive API

        @return: Python dict with data from Sheets API
    """
    config = os.getenv("SHEET_URL")
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/spreadsheets.readonly']

    json_values = os.getenv("JSON_VALUES")
    json_path = json.loads(json_values, strict=False)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json_path, scope)

    client = gspread.authorize(creds)

    # Find a workbook by link and open the first sheet
    # Make sure you use the right link here.
    sheet = client.open_by_url(config).get_worksheet(1)

    # Get values formated or not
    kpis = sheet.col_values(
        8, value_render_option='FORMATTED_VALUE')
    values = sheet.col_values(11, value_render_option=format_value)
    goals = sheet.col_values(13, value_render_option=format_value)

    # remove empty spaces
    kpis = list(filter(lambda x: x != "", kpis))
    values = list(filter(lambda x: x != "", values))
    goals = list(filter(lambda x: x != "", goals))
    goals.pop(0)
    # remove cabeçalho
    kpis.pop(0)
    values.pop(0)

    return kpis, values, goals

def normalize_string(txt):
    """
        Helper function to normalize strings
    """
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def format_data(kpis, values, goals):
    """
        Returns all kpi's in a formatted manner.

        Example: [{"id": 0, "Projetos": 12}]

        @kpis: values returned from API call
        @values:
        @goals:

        @return: formatted data
    """
    # translate to dictionary with index
    cell_tuple = zip(kpis, values)
    id = range(len(values))
    ids = [("id", x) for x in id]
    dictionary = [dict(x) for x in zip(cell_tuple, ids)]
    return dictionary

def all_kpi():
    """
        Returns object with all kpi's, without ID

        @return: all KPi data in dict
    """
    data = format_data(*return_sheet())
    return {k: v for x in data for k, v in x.items() if k != "id"}

def match_kpi(name):
    """
        Returns fragment with exact name of KPI.

        @input: KPI name to be match
        @return: all KPIS with with given name OR empty {} if no match is found
    """
    data = format_data(*return_sheet())
    # if data.get(name):
    #    single = {
    #        name: data.get(name)
    #    }
    # else:
    #    single = "Indicador não encontrado!"

    return {k: v for x in data for k, v in x.items() if re.search(normalize_string(name.lower()), normalize_string(k.lower()))}

def reach_gols():
    kpis, values, goals = return_sheet('UNFORMATTED_VALUE')
    return {k: "{:.0%} Concluído".format(v/g) for (k, v, g) in zip(kpis, values, goals)}
