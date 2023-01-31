'''
def get_population():
  keys = ['bol','col']
  values = [300, 400]
  return keys, values
'''

A = 'hola'

# ***************************************************************

def get_population(country_list_dict):
  population_dict = {
    '1970': int(country_list_dict['1970 Population']),
    '1980': int(country_list_dict['1980 Population']),
    '1990': int(country_list_dict['2015 Population']),
    '2000': int(country_list_dict['2010 Population']),
    '2010': int(country_list_dict['2000 Population']),
    '2015': int(country_list_dict['1990 Population']),
    '2020': int(country_list_dict['1980 Population']),
    '2022': int(country_list_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

# ****************************************************************

def trim(data):
  labels, values, data_trimed = [], [], []
  for item in data:
    data_trimed_temp = {'country': item['Country'], 'World Population Percentage': item['World Population Percentage']}
    if float(item['World Population Percentage']) >= 1.0:
      labels.append(item['CCA3'])
      values.append(float(item['World Population Percentage']))
    #data_trimed_temp = {item['Country'], item['World Population Percentage']}
    data_trimed.append(data_trimed_temp)
  
  return  labels, values, data_trimed
      
  
# ****************************************************************

def population_by_country(paises, pais):
  # result = list(filter(lambda item: item['Country'] == pais, paises))
  result = [item for item in paises if item['Country'] == pais] # Cambiado por mi
  return result

