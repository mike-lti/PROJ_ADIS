#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""


import socket as s
import sys
import net_client
import time
import pickle


if(len(sys.argv) == 4):

    idClient = int(sys.argv[1])
    HOST = sys.argv[2]
    PORT = int(sys.argv[3])
    
    client = net_client.server(HOST, PORT)
    
    while True:
        sock = client.connect()
        
        try:
            
            comando = input("Insira um comando: ")

        except EOFError:
            break

        if comando == "EXIT":
            print("EXIT")
            break        


        elif comando.split()[0] == "SLEEP":
            time.sleep(int(comando.split()[1]))

        elif comando.split()[0] == "CLOSE":
            client.send_receive(sock, comando)
            break
        

        elif comando.split()[0] == "LOCK" and len(comando.split()) == 3:
            lock_list = [10]           
            commandToSendLock = comando + " " + str(idClient)
            element_list = commandToSendLock.split()
            del element_list[0]
            for element in element_list:
                lock_list.append(element)
            msg = pickle.dumps(lock_list, -1)
            
            client.send_receive(sock, msg)

        elif comando.split()[0] == "UNLOCK" and len(comando.split()) == 2:
            
            commandToSendUnlock = comando + " " + str(idClient)
            unlock_list = [20]           
            element_list = commandToSendLock.split()
            for element in element_list:
                unlock_list.append(element)

            msg = pickle.dumps(unlock_list, -1)

            client.send_receive(sock, msg)
            
        elif comando.split()[0] == "STATUS" and len(comando.split()) == 3:
            if comando.split()[1] == "R":
                status_list = [30]
            elif comando.split()[1] == "K":
                status_list = [40]
            else:
                print("Comando inválido")
            
            status_list.append(comando.split()[2])
            msg = pickle.dumps(status_list, -1)

            
            client.send_receive(sock, msg)

        elif comando.split()[0] == "STATS" and len(comando.split()) == 2:
            if comando.split()[1] == "Y":
                stats_list = [50]
            elif comando.split()[1] == "N":
                stats_list = [60]
            elif comando.split()[1] == "D":
                stats_list = [70]
            else:
                print ("comando invalido")
            msg = pickle.dumps(stats_list, -1)

            client.send_receive(sock, msg)    

        elif comando.split()[0] == "PRINT" and len(comando.split()) == 1:
            print_list = [80]
            msg = pickle.dumps(print_list, -1)
            client.send_receive(sock, msg)        

        else: 
            print("UNKNOWN COMMAND")

        client.close(sock)
else:
    print("MISSING ARGUMENTS")