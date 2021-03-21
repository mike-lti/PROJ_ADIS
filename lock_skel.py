"""
Aplicações distribuídas - Projeto 2 - lock_skel.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""

import lock_pool
import pickle


class ListSkeleton:
    def __init__(self):
        """
        Inicia o parametro servicoLista como uma lista vazia
        """
        self.servicoLista = []


    def servicoLista_getter(self):
        """
        Devolve o interior
        """
        return self.servicoLista



    def processMessage(self, msg_bytes, resource_pool, canLock):
        """
        Nesta função a lista enviada pelo cliente e compreeendida e o comando no seu interior e aplicado
        à lock_pool. Formata depois uma lista para enviar de resposta ao comando do cliente
        """
        
        msgList = pickle.loads(msg_bytes)
              
        if msgList == None or len(msgList) == 0 :
            anwser_list = ["Comando nulo"]
            final_list_serialized = pickle.dumps(anwser_list, -1)
            return final_list_serialized

        else :                       
            if msgList[0] == 10:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.lock(int(float(msgList[1])), int(float(msgList[3])), int(float(msgList[2])), canLock)
                final_list.append(11)
                final_list.append(toSendClient)
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized

            elif msgList[0] == 20:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.unlock(int(float(msgList[1])), int(float(msgList[2])))
                final_list.append(21)
                final_list.append(toSendClient)
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized
                
            elif msgList[0] == 30:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.status("R", int(float(msgList[1])))
                final_list.append(31)
                final_list.append(toSendClient)               
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized

            elif msgList[0] == 40:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.status("K", int(float(msgList[1])))
                final_list.append(41)
                final_list.append(toSendClient)               
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized

            elif msgList[0] == 50:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.stats(50)
                final_list.append(51)
                final_list.append(toSendClient)
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized
                
            elif msgList[0] == 60:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.stats(60)
                final_list.append(61)
                final_list.append(toSendClient) 
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized

            elif msgList[0] == 70:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.stats(70)
                final_list.append(71)
                final_list.append(toSendClient) 
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized

            elif msgList[0] == 80:
                final_list = self.servicoLista_getter()
                toSendClient = str(resource_pool)
                toIterate = toSendClient.split('\n')
                final_list.append(81)
                for element in range(len(toIterate)-1):
                    final_list.append(toIterate[element]) 
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized

            else:
                final_list = ["Comando não obedece às normas definidas pelo servidor"]
                final_list_serialized = pickle.dumps(final_list, -1)

                return final_list_serialized

            
                











            
