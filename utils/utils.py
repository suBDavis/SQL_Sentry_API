#SQL Helper Class
import os
import pymssql
import json

class sql:

    def __init__(self):
        #create the connection
        self.config = config()
        self.dbname = self.config.getDB()
        self.server = self.config.getServer()
        conn= pymssql.connect(self.server)
        self.cursor = conn.cursor()

    def setDB(self):
        self.cursor.execute("USE " + self.dbname + ";")

    def runQuery(self, q, fields):
        #print("Running " + q)
        self.cursor.execute(q)
        response = []
        for row in self.cursor:
            rdict = {}
            i = 0
            for f in fields:
                rdict[f] = row[i]
                i += 1
            response.append(rdict)
        return response

    def getDevice(self, oid):
        response = None
        if oid == "all":
            response = self.getObject("device", oid, 0)
            i = 0 
            for r in response["device"]:
                r.update(self.getConnection(str(r["ID"])))
                i +=1
        elif len(oid) < 10:
            response = self.getObject("device", oid, 1)
        else:
            response = self.getObject("device", oid, 0)
        return response

    def getConnection(self, oid):
        response = None
        if oid == "all":
            response = self.getObject("connection", oid, 0)
            # for r in response["counter"]:
            #     r.update(self.getConnection("all"))
        elif len(oid) < 10:
            response = self.getObject("connection", oid, 1)
        else:
            response = self.getObject("connection", oid, 0)
        return response

    def getSite(self, oid):
        response = None
        if oid == "all":
            response = self.getObject("site", oid, 0)
            i = 0
            for r in response["site"]:
                r.update(self.getDevice(str(r["ID"])))
        elif len(oid) < 10:
            response = self.getObject("site", oid, 1)
        else:
            response = self.getObject("site", oid, 0)

    def getObject(self, ctype, oid, m):
        fields = self.config.getFields(ctype)
        self.setDB()
        q = None
        if oid == "all":
            q = self.config.getQuery(ctype, False, "", 0)
        else:
            q = self.config.getQuery(ctype, True, oid, m)
        
        responseDict = { ctype : self.runQuery(q, fields) }
        return responseDict      

class config:

    def __init__(self):
        #eventuially load from file
        self.cnf = {}
        with open("config.json") as f:
          self.cnf = json.load(f)
        #print("Loaded: \n " + str(self.cnf))
        self.server = self.cnf['config']['hostname']
        self.dbname = self.cnf['config']['db']

    def getServer(self):
        return self.server

    def getDB(self):
        return self.dbname

    # T/F for withClause
    def getQuery(self, name, withClause, oid, m):
        if withClause:
            return self.cnf['queries'][name]['query'] + " " + self.cnf['queries'][name]['modifier'][m] + "'" + oid + "'"
        else:
            return self.cnf['queries'][name]['query']

    def getFields(self, name):
        return self.cnf['queries'][name]['param']

connection = sql()

def getConn():
  return connection