from models.Item import Item, SqlAlchemyRepository

class Service:
   def __init__(self):
      self.repository = SqlAlchemyRepository()


   def store(self, item: Item):
      item = self.repository.create(item)

      if item.id is not None & self.repository.find(item.id) is not None:
         return {"error": "Item id already exists"}
      
      if item is False:
         return {"error": "Item sku already exists"}
         

      return item
   

   def show(self, id):
      item = self.repository.find(id)
      
      if item is None:
         return False
      
      return item


   def index(self):
      return self.repository.all()
   

   def update(self, item: Item):      
      item = self.repository.update(item)

      if item is False:
         return {"error": "Item sku already exists"}


   def destroy(self, id):
      if self.repository.find(id) is None:
         return {"error": "Item not found"}
      
      self.repository.delete(id)
      
      return {"message": "Item deleted"}