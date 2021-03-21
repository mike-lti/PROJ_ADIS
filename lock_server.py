#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 2 - lock_server.py
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
import struct


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
    
    
    sockets = [sock]
    while True:
        lista_resposta = lock_skel.ListSkeleton()
        pool.lock_limit(numBlocade)
        canLock = pool.max_locks_resource(numRecBlocade)

        socket_list, M, X = sel.select(sockets, [], [])
        for socket in socket_list:
            presentTime = time.time()
            pool.clear_expired_locks(presentTime)
            if socket is sock:
                conn_sock, (addr, port) = sock.accept()
                print('Cliente ligado em %s no porto %s' % (addr,port))
                sockets.append(conn_sock)
            else:
                sizeDataPickled = socket.recv(4)               
                if sizeDataPickled:
                    sizeData = struct.unpack('i', sizeDataPickled)[0]
                    msgPickle = socket.recv(sizeData)
                    lista_resposta_final = lista_resposta.processMessage(msgPickle, pool, canLock)       
                    socket.sendall(lista_resposta_final)
                else:
                    socket.close()
                    sockets.remove(socket)
                    print("Cliente terminou ligação")
        
        
            
else:
    print("MISSING ARGUMENTS”")