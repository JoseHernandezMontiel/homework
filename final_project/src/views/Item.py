from flask import Blueprint, redirect, render_template, request, url_for

from models.Item import Item
from services.ItemService import Service

item_views_blueprint = Blueprint('item_views_blueprint', __name__)

service = Service()



# CREATE

@item_views_blueprint.route('/add', methods=['POST'])
def add():

   item = Item(
      sku=request.form['sku'],
      name=request.form['name'],
      description=request.form['description'],
      price=request.form['price'],
      quantity=request.form['quantity'],
      expiration_date=request.form['expiration_date']
   )

   serviceResponse = service.store(item)

   if "error" in serviceResponse:
      return render_template('add.html', error=serviceResponse['error'])

   return redirect(url_for('item_views_blueprint.index'))

@item_views_blueprint.route('/add')
def add_view():
   return render_template('add.html')

# HASTA AQUI FINE


















# UPDATE

@item_views_blueprint.route('/edit/<id>', methods=['POST'])
def edit(id):
   for key in ['id', 'name', 'description', 'price', 'quantity', 'expiration_date']:
      if key not in request.form:
         return redirect(url_for('item_views_blueprint.index'))

   if service.show(id) is False:
      return redirect(url_for('item_views_blueprint.index'))

   updatedItem = Item(
      id=request.form['id'],
      name=request.form['name'],
      description=request.form['description'],
      price=request.form['price'],
      quantity=request.form['quantity'],
      expiration_date=request.form['expiration_date']
   )

   service.update(id, updatedItem)

   return redirect(url_for('item_views_blueprint.index'))

@item_views_blueprint.route('/edit/<id>')
def edit_view(id):

   item = service.show(id)

   if item is False:
      return redirect(url_for('item_views_blueprint.index'))

   return render_template('edit.html', data=item)



# READ

@item_views_blueprint.route('/')
def index():
   items = service.index()

   if "error" in items:
      return render_template('index.html', data=[])
   
   data = [
      {
         "id": item.id,
         "name": item.name,
         "description": item.description,
         "price": item.price,
         "quantity": item.quantity,
         "expiration_date": item.expiration_date
      } for item in items
   ]

   return render_template('index.html', data=data)

# DELETE

@item_views_blueprint.route('/delete/<id>')
def destroy(id):
   item = service.destroy(id)
   
   return redirect(url_for('item_views_blueprint.index'))