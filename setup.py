from database import init_db, db_session
from models import *

# inititalize databae
init_db()

# initializing a debuger user
user1 = User("Patrick", "Password")
db_session.add(user1)
db_session.commit()

# initializing the databse with CSV data
with open('words.txt', 'r') as infile:
    for l in infile.readlines():
        line = l.split(',', 1)
        db_session.add(Word(line[0], line[1]))
        db_session.commit()

