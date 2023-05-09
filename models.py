"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    # Columns
    user_name = Column("user_name", TEXT, nullable=False, primary_key=True)
    password = Column("password", TEXT, nullable=False)

    searches = relationship("Search", back_populates="user")

    # Constructor
    def __init__(self, user_name, password):
        # id auto-increments
        self.user_name = user_name
        self.password = password
    
    # def __repr__(self):
    #     return self.last_name + ", " + self.first_name + " #" + self.phone_number


class Search(Base):
    __tablename__ = "searches"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    word_id = Column("word_id", ForeignKey("words.id"))
    user_id = Column("user_id", ForeignKey("users.user_name"))

    user = relationship("User", back_populates="searches")
    words = relationship("Word", back_populates="searches")

    # Constructor
    def __init__(self, word_id, user_id):
        # id auto-increments
        self.word_id = word_id
        self.user_id = user_id

class Word(Base):
    __tablename__ = "words"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    word = Column("word", TEXT, nullable=False)
    definition = Column("definition", TEXT, nullable=False)

    searches = relationship("Search", back_populates="words")

    # Constructor
    def __init__(self, word, definition):
        # id auto-increments
        self.word = word
        self.definition = definition

    def __repr__(self):
        return self. word +": " + self.definition