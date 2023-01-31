import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader) # Aqui se obtiene los nombres de las columnas o claves
    data = []
    for row in reader:
      # print(15 * '*')
      # print(row)      
      iterable = zip(header, row)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)    
    #print(data)
    return  data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  #print(data[0])