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
import lock_skel
import select as sel



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
    
    ListenerSocket = sock
    sockets = [ListenerSocket]
    while True:
        lista_resposta = lock_skel.ListSkeleton()
        presentTime = time.time()
        pool.clear_expired_locks(presentTime)
        pool.lock_limit(numBlocade)
        canLock = pool.max_locks_resource(numRecBlocade)

        (conn_sock, (addr, port)) = sock.accept()
        print('ligado a %s no porto %s' % (addr,port))







        
        msgPickle = conn_sock.recv(1024)
        lista_resposta_final = lista_resposta.processMessage(msgPickle, pool, canLock)
       
        
        conn_sock.sendall(lista_resposta_final)
        
        
        
    sock.close()
else:
    print("MISSING ARGUMENTS”")