from flask import jsonify, request

from repository.grocery_loader import read_csv_to_dict, write_list_of_dicts_to_csv

def getData():
  return read_csv_to_dict('layer_application/sample_grocery.csv')


# POST

def store():
  data = getData()
  sku = request.form.get('SKU')

  for item in data:
    if item['SKU'] == sku:
      return jsonify([{
        "error": "Item already exists"
      }]), 400

  item = {
    "SKU": sku,
    "Name": request.form.get('Name'),
    "Description": request.form.get('Description'),
    "Price": request.form.get('Price'),
    "Quantity": request.form.get('Quantity'),
    "Expiration Date": request.form.get('Expiration Date')
  }

  data.append(item)

  write_list_of_dicts_to_csv('layer_application/sample_grocery.csv', data)

  return jsonify(item), 201


# GET

def show(id):
  data = getData()

  for item in data:
    if item['SKU'] == id:
      return jsonify([item])
  return jsonify([]), 404


def index():
  data = getData()
  return jsonify(data)



# DELETE

def destroy(id):
  data = getData()

  for item in data:
    if item['SKU'] == id:
      data.remove(item)
      write_list_of_dicts_to_csv('layer_application/sample_grocery.csv', data)
      return jsonify([{"message": "Item deleted"}])
  return jsonify([]), 404