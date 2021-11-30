import sqlite3
from sqlite3 import Error


try:
    con = sqlite3.connect('basededatos.db')
    print("Connection is established: Database is created in memory")
except Error:
    print(Error)

def crud(con):

        while True:

            def crearTabla(con):
                cursorObj.execute("drop table if exists cliente")
                cursorObj.execute("Create table cliente(id integer, nombre text, primerApellido text, segundoApellido text, ciudad text)")
                con.commit()

            print("----------MENU----------")
            print("[1] Listar clientes     ")
            print("[2] Añadir cliente      ")
            print("[3] Modificar cliente   ")
            print("[4] Borrar cliente      ")
            print("[5] Salir               ")
            print("------------------------")

            option = input("> ")

            if option == '1':
                cursorObj = con.cursor()
                cursorObj.execute('SELECT * FROM cliente')

                rows = cursorObj.fetchall()
                for row in rows:
                    print(row)

            if option == '2':
                print("nombre -")
                nombre = input()
                print("Apellido1 -")
                primerApellido= input()
                print("Apellido2 -")
                segundoApellido = input()
                print("Ciudad -")
                ciudad = input()
                datos = (nombre, primerApellido, segundoApellido, ciudad)
                cursorObj = con.cursor()
                cursorObj.execute('INSERT INTO cliente(nombre, primerApellido, segundoApellido, ciudad) VALUES(?, ?, ?, ?)', datos)
                con.commit()

            if option == '3':
                cursorObj = con.cursor()
                print("Que id quieres modificar")
                numero0 = input()
                print("Que quieres modificar")
                print("[1] Nombre")
                print("[2] Apellido1")
                print("[3] Apellido2")
                print("[4] Ciudad")
                numero2=input()
                if numero2 == '1':
                    print("dime el nombre nuevo")
                    nombre_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET nombre =? where id = ?;',(nombre_nuevo, numero0))
                elif numero2 =='2':
                    print("dime el primer apellido nuevo")
                    apellido1_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET primerApellido =? where id = ?;',(apellido1_nuevo, numero0))
                elif numero2 == '3':
                    print("dime el segundo apellido nuevo")
                    apellido2_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET segundoApellido =? where id = ?;',(apellido2_nuevo, numero0))
                elif numero2 == '4':
                    print("dime la ciudad nuevo")
                    ciudad_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET ciudad =? where id = ?;',(ciudad_nuevo, numero0))
                else:
                    print("numero no valido")
                con.commit()

            if option == '4':
                cursorObj = con.cursor()
                print("Que id quieres borrar")
                numero0 = input()
                con.execute("DELETE from cliente where id ="+numero0)
                con.commit()

            if option == '5':
                print("Saliendo...\n")
                return False
                break
            input("\nPresiona ENTER para continuar...")

crud(con)
