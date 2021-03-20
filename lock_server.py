#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_server.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""

import socket as s
import sys
import time
from lock_pool import resource_lock
from lock_pool import lock_pool
import pickle



if(len(sys.argv) == 6):
    HOST = sys.argv[1] 
    PORT = int(sys.argv[2])
    numRec = int(sys.argv[3])
    numBlocade = int(sys.argv[4])
    numRecBlocade = int(sys.argv[5])

    pool = lock_pool(numRec, numBlocade, numRecBlocade)

    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
   

    while True:
        presentTime = time.time()
        pool.clear_expired_locks(presentTime)
        pool.lock_limit(numBlocade)
        canLock = pool.max_locks_resource(numRecBlocade)

        (conn_sock, (addr, port)) = sock.accept()
        print('ligado a %s no porto %s' % (addr,port))
        
        msgPickle = conn_sock.recv(1024)
        msgList = pickle.loads(msgPickle)
        #msgList = msgStr.decode('utf-8')
        print(msgList)
        
        if msgList[0] == 10:
            toSendClient = pool.lock(int(float(msgList[1])), int(float(msgList[3])), int(float(msgList[2])), canLock)
            listClient = [11]
            listClient.append(toSendClient)
            print(toSendClient)
            ClientInfo = toSendClient.encode()
            conn_sock.sendall(ClientInfo)

        elif msgList[0] == 20:
            toSendClient = pool.unlock(int(float(msgList[1])), int(float(msgList[2])))
            ClientInfo = toSendClient.encode()
            conn_sock.sendall(ClientInfo)

        elif msgList[0] == 30 or msgList == 40:
            type_status = 0
            if  msgList[0] == 30:
                type_status = "R"
            else:
                type_status = "K"
            toSendToClient = pool.status(type_status, int(float(msgList[2])))
            ClientInfo = str(toSendToClient).encode()
            conn_sock.sendall(ClientInfo)

        elif msgList[0] == 50 or msgList[0] == 60 or msgList[0] == 70:
            type_stats = 0
            if msgList[0] == 50:
                type_stats = "Y"
            elif msgList[0] == 60:
                type_stats = "N"
            else:
                type_stats = "D"

            toSendToCLient = pool.stats(type_stats)
            clientInfo = str(toSendToCLient).encode()
            conn_sock.sendall(clientInfo)

        elif "CLOSE" in msgList[0]:
            break

        elif msgList[0] == 80:
            toSendToCLient = str(pool)
            clientInfo = toSendToCLient.encode()
            conn_sock.sendall(clientInfo)
        
    sock.close()
else:
    print("MISSING ARGUMENTS”")