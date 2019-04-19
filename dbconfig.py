import toml

class DBConfig:
    database = None
    user = None
    password = None
    host = "/tmp/"
    port = 5432

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

    def __repr__(self):
        return "database = {}, user = {}, password = {}".format(
            self.database, self.user, "<set>" if self.password != "" else "<un-set>"
        )

def load_config(path="./db.conf"):
    raw_config = toml.load(path)

    config = DBConfig(raw_config)
    print("Loaded config: {}".format(config))
    return config

