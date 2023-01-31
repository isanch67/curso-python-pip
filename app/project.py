import csv

def read_population (path):
  with open(path, 'r') as population:
    reader = csv.reader(population, delimiter = ",")
    list_population = [] 
    dic_arg_population = {} 
    header = next(reader)
    terminar = 'n'
    for row in reader:
      iterable = zip(header, row)
      dic_population = {key: values for key, values in iterable}
      list_population.append(dic_population)

      #dic_arg_population = {key: values for key, values in dic_population.items() if values == 'ARG'}
      
    dic_arg_population = dic_population
    list_population_arg = []
    list_temp = []
    ciclo = len(list_population)
    # List_population_arg = list(lambda item: item['CCA3'] == 'ARG')
    list_population_arg = [item for item in list_population if item['CCA3'] == 'ARG']
    print(list_population_arg)
    pass
    # list_depurada = [x: y for x, y in list_population_arg if key_dic.startswith('19') == True or key_dic.startswith('20') == True:]
    #try:
    for item_list in list_population_arg:
      item_temp = dict(item_list)
      print(item_temp, type(item_temp)) 
      
      for key_dic in item_temp:
           
        if key_dic.startswith('19') == False and key_dic.startswith('20') == False:
          print(key_dic)
          apuntador = "'" + key_dic + "'"
          del item_temp[key_dic]
    
    #except RuntimeError as error:
      #pass
                
   #print(list_population, 3 * '\n', dic_arg_population, 3 * '\n') 
    print('List_population_arg => ', list_temp)
    
      

  return 0

if __name__  == '__main__':
  resultado = read_population('app/data.csv')
