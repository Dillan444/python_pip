import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    # print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
      dict = {header: row for header, row in iterable}
      data.append(dict)
      # print(row)
    return(data)
      
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[1])