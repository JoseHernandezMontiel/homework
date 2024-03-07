import csv

def write_list_of_dicts_to_csv(filename, data):
  with open(filename, 'w') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)


def read_csv_to_dict(filename):
  with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    return list(reader)


def main():
  source = read_csv_to_dict('sample_grocery.csv')
  file_to_compare = read_csv_to_dict('grocery_batch_1.csv')
  
  sku_list = []

  for row in source:
    sku_list.append(row['SKU'])

  for row in file_to_compare:

    if row['SKU'] in sku_list:
      sku_index = sku_list.index(row['SKU'])
      source[sku_index]['Quantity'] = int(source[sku_index]['Quantity']) + int(row['Quantity'])
    else:
      source.append(row)
  
  write_list_of_dicts_to_csv("grocery_db.csv", source)
  

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  main()