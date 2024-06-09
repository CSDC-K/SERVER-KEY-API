# for the license / key systems

#           version 1.1

import socket


class api():

    def client(host,
               port,
               outputs
               
    ):
        apisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        apisock.connect((host,port))

        data = apisock.recv(1024)
        comdata = data.decode()

        if outputs == False:
            pass
        
        elif outputs == True:
            print(comdata)
        

        else:
            print("KEYAPI ERROR : 0X001 --> The 'outputs' must take a value.\n <True or False.>\n usage: \n apkey.api.server/client(host,port,outputs = False / True)")
            exit()

    def server(host,
               port,
               file
    ):
        
        if port is not int:
            print("KEYAPI ERROR : 0X002 --> Port must take only integer values")

        if host is not str:
            print("KEYAPI ERROR : 0X003 --> Host must take only string values")
            

        

        apisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        apisock.bind((host,port))
        apisock.listen()

        conn,addr = apisock.accept()

        file_content = ""

        with open(file, "r") as file:
            file_content = file.read()
        
        
        conn.send(file_content.encode())

