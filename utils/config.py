import json

class config:

    def __init__(self):
        self.cnf = {}
        with open("config.json") as f:
          self.cnf = json.load(f)

    def getServer(self):
        return self.cnf['config']['hostname']

    def getDB(self):
        return self.cnf['config']['db']

    def getChildType(self, otype):
        return self.cnf['queries'][otype]['child']

    def getQuery(self, name):
        return self.cnf['queries'][name]['query']

    def getFields(self, name):
        return self.cnf['queries'][name]['param'] 

    def getModifier(self, name):
        return self.cnf['queries'][name]['modifier']

    def getChildJoin(self, name):
        return self.cnf['queries'][name]['childJoin']

cfg = config()

def getCnf():
    return cfg