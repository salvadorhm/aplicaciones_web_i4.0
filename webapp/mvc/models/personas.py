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

    def insert(self, nombre, email):
        try:
            self.connect()
            query = ("INSERT INTO personas (nombre,email) values(%s,%s);")
            values = (nombre, email)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self,id_persona, nombre, email):
        try:
            self.connect()
            query = ("UPDATE personas SET nombre=%s, email=%s WHERE id_persona=%s;")
            values = (nombre, email, id_persona)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, id_persona):
        try:
            self.connect()
            query = ("DELETE FROM personas WHERE id_persona = %s;")
            values = (id_persona,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

'''
objeto = Personas()
objeto.delete(9)
for row in objeto.select():
    print(row)
'''