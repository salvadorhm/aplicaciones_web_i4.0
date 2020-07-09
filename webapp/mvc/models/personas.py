import mysql.connector

class Personas():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='user_agenda', 
                password='Agenda.2020',
                host='127.0.0.1',
                port=3309,
                database='agenda_db'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    def select(self):
        try:
            self.connect()
            query = ("SELECT * from personas;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id_persona':row[0],
                    'nombre':row[1],
                    'email':row[2]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result
    
    def view(self,id_persona):
        try:
            self.connect()
            query = ("SELECT * from personas where id_persona = %s;")
            values = (id_persona,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                r = {
                    'id_persona':row[0],
                    'nombre':row[1],
                    'email':row[2]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result


objeto = Personas()
objeto.connect()

for row in objeto.view(1):
    print(row)
