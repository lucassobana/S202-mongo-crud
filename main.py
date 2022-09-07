from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db", "Pessoa")

db.create("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 31.0)
db.create("Harry Potter 2", "J.K. Rowling", 2000, 33.0)
db.create("Harry Potter 3", "J.K. Rowling", 2004, 35.0)

Pessoa = db.read()

writeAJson(Pessoa, "colecao")


