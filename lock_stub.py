"""
Aplicações distribuídas - Projeto 2 - lock_stub.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""


import pickle


class ListStub:
    def __init__(self):
        """
        Inicia o objeto como uma lista vazia
        """
        self._listObj = []

    def list_getter(self):
        """
        Devolve o conteudo do parametro self._listObj
        """

        return self._listObj

    def list_formating(self, command_code, command_info):
        """
        Coloca o comando de acordo com as normas do servidor e com a formatação correta definida no enunciado
        """

        list_to_formate = self.list_getter()
        list_to_formate.append(command_code)
        for element in command_info:           
            self.append(element)


    def list_serialization(self, list_to_pickle):
        """
        Serializa a lista formatada de forma a ser enviada para o servidor
        """
        
        list_to_serialize = self.list_getter()
        serialized_list = pickle.dumps(list_to_serialize, -1)

        return serialized_list

    def append(self, element):
        """
        Método que permite adicionar elemento ao objeto self._listObj
        """
        list_to_append = self.list_getter()
        list_to_append.append(element)
        
    def clear_element(self, element_index):
        """
        Método que permite apagar um elemento do objeto self._listObj
        """
        list_to_clear = self.list_getter()
        del list_to_clear[element_index]

    def __str__(self):
        """
        Método que define a apresentação do objeto self._listObj quando são usadoes métodos str() ou print() sobre o mesmo)
        """     
        return_list = []
        for i in self._listObj:
            return_list.append(i)
        return str(return_list)