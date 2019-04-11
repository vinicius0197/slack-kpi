import json
import re
import yaml
import gspread

from oauth2client.service_account import ServiceAccountCredentials
from unicodedata import normalize
from oauth2client.service_account import ServiceAccountCredentials

# Suposição que cada requisição so irá executar uma operação
# Dito isso, Cada operação irá requisitar a api do sheets
# Retorna objeto com indicadores, valores e metas, formatado ou não

def return_sheet(format_value='FORMATTED_VALUE'):
    # use creds to create a client to interact with the Google Drive API

    with open('../../config.yml') as f:
        config = yaml.safe_load(f)

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by link and open the first sheet
    # Make sure you use the right link here.
    sheet = client.open_by_url(config["sheet_url"]).get_worksheet(1)

    # Get values formated or not
    indicadores = sheet.col_values(
        8, value_render_option='FORMATTED_VALUE')
    values = sheet.col_values(11, value_render_option=format_value)
    goals = sheet.col_values(13, value_render_option=format_value)

    # remove empty spaces
    indicadores = list(filter(lambda x: x != "", indicadores))
    values = list(filter(lambda x: x != "", values))
    goals = list(filter(lambda x: x != "", goals))
    goals.pop(0)
    # remove cabeçalho
    indicadores.pop(0)
    values.pop(0)

    return indicadores, values, goals


# Função auxiliar remoção de acentos
def normalize_string(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


# Return all kpi's formated
# Example: [{"id": 0, "Projetos": 12}]
# Espera sequencia de argumentos: indicadores, values, id, gols*optional
def format_data(indicadores, values, goals):
    # translate to dictionary with index
    cell_tuple = zip(indicadores, values)
    id = range(len(values))
    ids = [("id", x) for x in id]
    dictionary = [dict(x) for x in zip(cell_tuple, ids)]
    return dictionary


# Espera dados NÃO
# Retorna objeto com todos os indicadores, sem o id
def all_kpi():
    data = format_data(*return_sheet())
    return {k: v for x in data for k, v in x.items() if k != "id"}


# Espera fragmento ou nome exato do nome do indicador
# Retorna todos os indicadores que contem aquele nome ou fragmento
# Retorna {} caso não tenha nenhum match
def match_kpi(name):
    data = format_data(*return_sheet())
    # if data.get(name):
    #    single = {
    #        name: data.get(name)
    #    }
    # else:
    #    single = "Indicador não encontrado!"

    return {k: v for x in data for k, v in x.items() if re.search(normalize_string(name.lower()), normalize_string(k.lower()))}


def reach_gols():
    indicadores, values, goals = return_sheet('UNFORMATTED_VALUE')
    return {k: "{:.0%} Concluído".format(v/g) for (k, v, g) in zip(indicadores, values, goals)}
