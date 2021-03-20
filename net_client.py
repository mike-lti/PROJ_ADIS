# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - net_client.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941
"""

# zona para fazer importação
import socket as s
from sock_utils import create_tcp_client_socket


# definição da classe server 

class server:
    """
    Abstrai uma ligação a um servidor TCP. Implementa métodos para: estabelecer 
    a ligação; envio de um comando e receção da resposta; terminar a ligação.
    """
    def __init__(self, address, port):
        """
        Inicializa a classe com parâmetros para funcionamento futuro.
        """
        self.address = address
        self.port = port       

    def adress_getter(self):

        return self.address


    def port_getter(self):

        return self.port

    def connect(self):
        """
        Estabelece a ligação ao servidor especificado na inicialização.
        """
        
        address = self.adress_getter()
        port = self.port_getter()

        sock = create_tcp_client_socket(address, port)

        return sock

    def send_receive(self, socket, data):
        """
        Envia os dados contidos em data para a socket da ligação, e retorna
        a resposta recebida pela mesma socket.
        """
        socket.sendall(data)
        respostaToData = socket.recv(1024)
        print(respostaToData.decode('utf-8'))
    
    def close(self, socket):
        """
        Termina a ligação ao servidor.
        """
        socket.close()
