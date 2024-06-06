import abc
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from starwars import config


Base = declarative_base()


class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True)
    Name = Column(String)


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> Movie:
        raise NotImplementedError



class SqlAlchemyRepository(AbstractRepository):
    def __init__(self):
        self.engine = create_engine(config.get_postgres_uri())
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=sel f.engine)

    def add(self, movie: Movie):
        with self.Session() as session:
            session.add(movie)
            session.commit()

    def get(self, id):
        with self.Session() as session:
            movie = session.query(Movie).filter_by(id=id).one()
            return movie