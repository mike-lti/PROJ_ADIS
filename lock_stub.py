import pickle


class ListStub:
    def __init__(self):
        self._listObj = []

    def list_getter(self):

        return self._listObj

    def list_formating(self, command_code, command_info):

        list_to_formate = self.list_getter()
        list_to_formate.append(command_code)
        for element in command_info:
            
            self.append(element)



    def list_serialization(self, list_to_pickle):
        """[summary]

        Args:
            list ([type]): [description]
        """
        list_to_serialize = self.list_getter()
        serialized_list = pickle.dumps(list_to_serialize, -1)


        return serialized_list


    def append(self, element):
        list_to_append = self.list_getter()
        list_to_append.append(element)
        

    def clear_element(self, element_index):
        list_to_clear = self.list_getter()
        del list_to_clear[element_index]


    def __str__(self):
        
        
        return_list = []
        for i in self._listObj:
            return_list.append(i)
        return str(return_list)