import abc

from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database import config

Base = declarative_base()



class Item(Base):
   __tablename__ = "items"

   id = Column(Integer, primary_key=True, autoincrement=True)
   sku = Column(String)
   name = Column(String)
   description = Column(String)
   price = Column(Float)
   quantity = Column(Integer)
   expiration_date = Column(Date)

class AbstractRepository(abc.ABC):
   @abc.abstractmethod
   def create(self, item: Item) -> Item:
      raise NotImplementedError

   @abc.abstractmethod
   def find(self, id) -> Item:
      raise NotImplementedError

   @abc.abstractmethod
   def all(self) -> list[Item]:
      raise NotImplementedError
   
   @abc.abstractmethod
   def update(self, item: Item) -> Item:
      raise NotImplementedError
   
   @abc.abstractmethod
   def delete(self, id):
      raise NotImplementedError



class SqlAlchemyRepository(AbstractRepository):
   def __init__(self):
      self.engine = create_engine(config.get_postgres_connection())
      Base.metadata.create_all(bind=self.engine)
      self.Session = sessionmaker(bind=self.engine)
      self.session = self.Session()

   def create(self, item: Item):
      if (self.session.query(Item).filter(Item.sku == item.sku).count() > 0):
         return False

      self.session.add(item)
      self.session.commit()

      return item

   def find(self, id):
      item = self.session.query(Item).get(id)

      if item is None:
         return None
         
      return item
      
   def all(self):
      return self.session.query(Item).order_by(Item.id).all()
      
   def update(self, item: Item):
      if (self.session.query(Item).filter((Item.id != item.id) & (Item.sku == item.sku)).count() > 0):
         return False
      
      currentItem = self.session.query(Item).get(item.id)

      currentItem.sku = item.sku
      currentItem.name = item.name
      currentItem.description = item.description
      currentItem.price = item.price
      currentItem.quantity = item.quantity
      currentItem.expiration_date = item.expiration_date
         
      self.session.commit()

      return currentItem

   def delete(self, id):
      item = self.session.query(Item).get(id)
      
      self.session.delete(item)
      self.session.commit()
        