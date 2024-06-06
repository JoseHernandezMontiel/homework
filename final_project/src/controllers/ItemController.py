from flask import Blueprint, jsonify, request

from models.Item import Item
from services.ItemService import Service

item_controller_blueprint = Blueprint('item_controller_blueprint', __name__)

service = Service()


# CREATE

@item_controller_blueprint.route('/items', methods=['POST'])
def store():
    
   for key in ['sku', 'name', 'description', 'price', 'quantity', 'expiration_date']:
      if key not in request.json:
         return {"error": f"Missing field: {key}"}, 400

   item = Item(
      sku=request.json['sku'], 
      name=request.json['name'], 
      description=request.json['description'], 
      price=request.json['price'], 
      quantity=request.json['quantity'], 
      expiration_date=request.json['expiration_date']
   )

   serviceResponse = service.store(item)

   if "error" in serviceResponse:
      return serviceResponse, 400

   return {
      "id": serviceResponse.id,
      "sku": serviceResponse.sku,
      "name": serviceResponse.name,
      "description": serviceResponse.description,
      "price": serviceResponse.price,
      "quantity": serviceResponse.quantity,
      "expiration_date": serviceResponse.expiration_date
   }, 201



# READ

@item_controller_blueprint.route('/items/<id>')
def show(id):
   
   item = service.show(id)

   if item is False:
      return {"error": "Item not found"}, 404

   return {
      "id": item.id,
      "sku": item.sku,
      "name": item.name,
      "description": item.description,
      "price": item.price,
      "quantity": item.quantity,
      "expiration_date": item.expiration_date
   }

@item_controller_blueprint.route('/items')
def index():
   items = service.index()
   
   return jsonify([
      {
         "id": item.id,
         "sku": item.sku,
         "name": item.name,
         "description": item.description,
         "price": item.price,
         "quantity": item.quantity,
         "expiration_date": item.expiration_date
      } for item in items
   ])



# UPDATE

@item_controller_blueprint.route('/items/<id>', methods=['PUT'])
def update(id):
   for key in ['sku', 'name', 'description', 'price', 'quantity', 'expiration_date']:
      if key not in request.json:
         return {"error": f"Missing field: {key}"}, 400

   item = Item(
      id=id,
      sku=request.json['sku'], 
      name=request.json['name'], 
      description=request.json['description'], 
      price=request.json['price'], 
      quantity=request.json['quantity'], 
      expiration_date=request.json['expiration_date']
   )

   if service.show(id) is False:
      return {"error": "Item not found"}, 404

   serviceResponse = service.update(item)

   return {
      "id": serviceResponse.id,
      "sku": serviceResponse.sku,
      "name": serviceResponse.name,
      "description": serviceResponse.description,
      "price": serviceResponse.price,
      "quantity": serviceResponse.quantity,
      "expiration_date": serviceResponse.expiration_date
   }

# DELETE

@item_controller_blueprint.route('/items/<id>', methods=['DELETE'])
def destroy(id):
   serviceResponse = service.destroy(id)

   if "error" in serviceResponse:
      return serviceResponse, 400

   return serviceResponse