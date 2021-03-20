"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""

import socket as s



def create_tcp_server_socket(address, port, queue_size):
    """
    Cria a socket do servidor que estará à escuta de informacao enviada por parte do cliente
    """
    
    listener_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    listener_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1) 
    listener_socket.bind((address, port))
    listener_socket.listen(queue_size)


    return listener_socket




def create_tcp_client_socket(address, port):
    """
    Cria a socket de ligacao do cliente 
    """

    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket.connect((address, port))

    return client_socket




def receive_all(socket, length):
    """
    Metodo de rececao da socket para determinada dimensao de informacao
    """
    receivedInfo = socket.recv(length)

    return receivedInfo