import lock_pool
import pickle


class ListSkeleton:
    def __init__(self):
        self.servicoLista = []


    def servicoLista_getter(self):
        return self.servicoLista



    def processMessage(self, msg_bytes, resource_pool, canLock) :
        msgList = pickle.loads(msg_bytes)
        resposta = []
        if msgList == None or len(msgList) == 0 :
            resposta.append('INVALID MESSAGE')
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
                print(int(float(msgList[2])))
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
                toSendClient = resource_pool.stats("Y")
                final_list.append(51)
                final_list.append(toSendClient)
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized
                

            elif msgList[0] == 60:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.stats("N")
                final_list.append(61)
                final_list.append(toSendClient) 
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized

            elif msgList[0] == 70:
                final_list = self.servicoLista_getter()
                toSendClient = resource_pool.stats("D")
                final_list.append(71)
                final_list.append(toSendClient) 
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized

            elif msgList[0] == 80:
                final_list = self.servicoLista_getter()
                toSendClient = str(resource_pool)
                final_list.append(81)
                final_list.append(toSendClient) 
                final_list_serialized = pickle.dumps(final_list, -1)
                return final_list_serialized


            else:
                print("Comando inválido")

            

            
                











            
