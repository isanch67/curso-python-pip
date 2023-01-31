# Creación y utilización de modulos propios en Python

import utils 
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ').lower().capitalize()
  result = utils.population_by_country(data, country)

  if len(result) < 1:
    print('Archivo Vacío')
  
  if len(result) > 0:
    country_list_dict = result[0]
    labels, values = utils.get_population(country_list_dict)
    charts.generate_bar_chart(country, labels, values)
  
    data = list(filter(lambda item : item['Continent'] == 'South America',data))
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    
  '''
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

if __name__ == '__main__':
  run()
