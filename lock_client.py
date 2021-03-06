#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_client.py
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
import lock_stub
import struct


if(len(sys.argv) == 4):

    idClient = int(sys.argv[1])
    HOST = sys.argv[2]
    PORT = int(sys.argv[3])
    
    client = net_client.server(HOST, PORT)
    sock = client.connect()
    while True:
        
        list_manager = lock_stub.ListStub()
        try :
            comando = input("Comando: ")

        except EOFError:
            print("Comando inválido")
            
        try:
            if comando == "EXIT":
                print("EXIT")
                break        

            elif comando.split()[0] == "SLEEP":
                time.sleep(int(comando.split()[1]))

            
            elif comando.split()[0] == "LOCK" and len(comando.split()) == 3:
                commandToSendLock = comando + " " + str(idClient)
                
                element_list = commandToSendLock.split()
                list_manager.list_formating(10, element_list)
                list_manager.clear_element(1)
                list_to_send = list_manager.list_serialization(list_manager)
                size_data = struct.pack('i',len(list_to_send))

                client.send_receive(sock, size_data ,list_to_send)

            elif comando.split()[0] == "UNLOCK" and len(comando.split()) == 2:
                
                commandToSendUnlock = comando + " " + str(idClient)

                element_list = commandToSendUnlock.split()
                list_manager.list_formating(20, element_list)
                list_manager.clear_element(1)
                list_to_send = list_manager.list_serialization(list_manager)
                
                size_data = struct.pack('i',len(list_to_send))

                client.send_receive(sock, size_data ,list_to_send)
                
            elif comando.split()[0] == "STATUS" and len(comando.split()) == 3:
                if comando.split()[1] == "R":
                    status = 30
                elif comando.split()[1] == "K":
                    status = 40
                
                try:
                    list_manager.list_formating(status, list(comando.split()[2]))
                    
                    list_to_send = list_manager.list_serialization(list_manager)
                                  
                    size_data = struct.pack('i',len(list_to_send))

                    client.send_receive(sock, size_data ,list_to_send)

                except:
                    print("comando invalido")
                    break

            elif comando.split()[0] == "STATS" and len(comando.split()) == 2:
                if comando.split()[1] == "Y":
                    status = 50
                elif comando.split()[1] == "N":
                    status = 60
                elif comando.split()[1] == "D":
                    status = 70
                else:
                    print ("comando invalido")
                list_manager.list_formating(status, [])
                    
                list_to_send = list_manager.list_serialization(list_manager)

                size_data = struct.pack('i',len(list_to_send))

                client.send_receive(sock, size_data ,list_to_send)  

            elif comando.split()[0] == "PRINT" and len(comando.split()) == 1:
                list_manager.list_formating(80, [])
                    
                list_to_send = list_manager.list_serialization(list_manager)
                size_data = struct.pack('i',len(list_to_send))

                client.send_receive(sock, size_data ,list_to_send)       

            else: 
                print("Comando desconhecido")

        except:
            print("Comando vazio")

    client.close(sock)
else:
    print("Argumentos em falta")