from .database import Database
from .dbconfig import DBConfig

def start():
    config = DBConfig("mydb", "ent", "")
    return Database(config).compile(auto_commit = True)

k
if __name__ == '__main__':
    print(start())
