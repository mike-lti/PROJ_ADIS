#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_pool.py
Grupo: 29
Números de aluno:
Gonçalo Miguel Nº54944
Miguel Duarte Nº54941

"""

import time
class resource_lock:
    def __init__(self, resource_id):
        """
        Define e inicializa as características de um LOCK num recurso.
        """
        self._resource_id = resource_id

        self._client_id = -1

        self._lock = "UNLOCKED"

        self._time_lock = 0

        self._num_locks = 0

        self._end_of_lock = 0


    def resource_id_getter(self):
        """
        Devolve o atributo self._resource_id
        """
        return self._resource_id


    def client_id_getter(self):
        """
        Devolve o atributo self._client_id 
        """
        return self._client_id


    def lock_getter(self):
        """
        Devolve o atributo self._lock
        """
        return self._lock


    def lock_number_getter(self):
        """
        Devolve o atributo self._num_locks
        """

        return self._num_locks 


    def time_lock_getter(self):
        """
        Devolve o atributo self._time_lock
        """

        return self._time_lock


    def end_of_lock_getter(self):
        """
        Devolve o atributo self._end_of_lock
        """

        return self._end_of_lock



    def resource_id_setter(self, id):
        """
        Altera o atributo self._resource_id   
        """
        self._resource_id = id

    def client_id_setter(self, clientId):
        """
        Altera o atributo self._client_id   
        """
        self._client_id = clientId

    def locksetter(self, lockState):
        """
        Altera o atributo self._lock   
        """
        self._lock = lockState

    def num_locks_setter(self, num):
        """
        Altera o atributo self._num_locks   
        """
        self._num_locks = num

    def time_lock_setter(self, time):
        """
        Altera o atributo self._time_lock   
        """
        self._time_lock = time

    def end_of_lock_setter(self, endLock):
        """
        Altera o atributo self._end_of_lock   
        """

        self._end_of_lock = endLock


    def lock(self, client_id, time_limit, lock_checker):
        """
        Tenta bloquear o recurso pelo cliente client_id, durante time_limit 
        segundos. Retorna OK ou NOK.
        """

        if self.lock_getter() == "LOCKED" and self.client_id_getter() != client_id:
            return False

        elif self.lock_getter() == "DISABLED":
            return False

        elif self.lock_getter() == "LOCKED" and self.client_id_getter() == client_id:
            newTimeLimit = self.time_lock_getter() + time_limit
            endLock = self.end_of_lock_getter()
            newEndLock = endLock + time_limit
            self.end_of_lock_setter(newEndLock)
            self.time_lock_setter(newTimeLimit)
            lockCounter = self.lock_number_getter()
            self.num_locks_setter(lockCounter + 1)
            return True


        elif not lock_checker:
            return False

        else:
            self.client_id_setter(client_id)
            self.locksetter("LOCKED")
            self.time_lock_setter(time_limit)
            lockCounter = self.lock_number_getter()
            self.num_locks_setter(lockCounter + 1)
            
            startOfLock = time.time()
            timeToAdd = self.time_lock_getter()
            endOfLock = startOfLock + timeToAdd
            self.end_of_lock_setter(endOfLock)

            return True
            


    def release(self):
        """
        Liberta o recurso incondicionalmente, alterando os valores associados
        ao bloqueio.
        """
        self.locksetter("UNLOCKED")
        

    def unlock(self, client_id):
        """
        Liberta o recurso se este está bloqueado pelo cliente client_id.
        Retorna OK ou NOK.
        """
        if self.client_id_getter() == client_id:
            self.client_id_setter(-1)
            self.locksetter("UNLOCKED")
            return True

        else:
            return False

    def status(self, option):
        """
        Obtém o estado do recurso. Se option for R, retorna LOCKED ou UNLOCKED 
        ou DISABLED. Se option for K, retorna <número de bloqueios feitos no 
        recurso>.
        """
        if option == "R":
            return self.lock_getter()

        elif option == "K":
            return self.lock_number_getter()
   
    def disable(self):
        """
        Coloca o recurso como desabilitdado incondicionalmente, alterando os 
        valores associados à sua disponibilidade.
        """
        self.locksetter("DISABLED")

    def __repr__(self):
        """
        Representação da classe para a saída standard. A string devolvida por
        esta função é usada, por exemplo, se uma instância da classe for
        passada à função print ou str.
        """
        if self.lock_getter() == "LOCKED":
            output = "R " + str(self.resource_id_getter()) + " LOCKED " + str(self.client_id_getter()) + " " + str(self.time_lock_getter())
        

        if self.lock_getter() == "UNLOCKED": 
            output = "R " + str(self.resource_id_getter()) +  " UNLOCKED"
      

        if self.lock_getter() == "DISABLED": 
            output = "R " + str(self.resource_id_getter()) + " DISABLED"
       
        return output

###############################################################################

class lock_pool:
    def __init__(self, N, K, Y):
        """
        Define um array com um conjunto de locks para N recursos. Os locks podem
        ser manipulados pelos métodos desta classe. Define K, o número máximo 
        de bloqueios permitidos para cada recurso. Ao atingir K, o recurso fica 
        desabilitdado. Define Y, o número máximo permitido de recursos 
        bloqueados num dado momento. Ao atingir Y, não é possível realizar mais 
        bloqueios até que um recurso seja libertado.
        """
        self._N = N
        self._K = K
        self._Y = Y
        self._resource_list = []

        for resourceNumber in range(N):
            resourceObj = resource_lock(resourceNumber)
            self._resource_list.append(resourceObj)



    def resource_list_getter(self):
        """
        Devolve o atributo self._resource_list 
        """
        return self._resource_list

        
    def clear_expired_locks(self, actualTime):
        """
        Verifica se os recursos que estão bloqueados ainda estão dentro do tempo
        de concessão dos bloqueios. Remove os bloqueios para os quais o tempo de
        concessão tenha expirado.
        """
        resourceList = self.resource_list_getter()


        for resource in resourceList:
            if resource.end_of_lock_getter() <= actualTime:
                resource.client_id_setter(-1)
                resource.locksetter("UNLOCKED")
                resource.time_lock_setter(0)
                resource.end_of_lock_setter(0)
        



    def lock_limit(self, max_limits):
        """
        Desabilita um recurso quando o mesmo chega ao numero maximo de bloqueios
        """

        resourceList = self.resource_list_getter()
        for resource in resourceList:
            if resource.lock_number_getter() >= max_limits:
                resource.disable()


    def max_locks_resource(self, max_locks):
        """
        Limita o numero de recusrsos bloqueados em simultaneo
        """

        lockedCounter = 0
        resourceList = self.resource_list_getter()
        for resource in resourceList:
            if resource.lock_getter() == "LOCKED":
                lockedCounter = lockedCounter + 1

        if lockedCounter >= max_locks:
            canLockChecker = False

        else:
            canLockChecker = True

        return canLockChecker


    def lock(self, resource_id, client_id, time_limit, can_lock):
        """
        Tenta bloquear o recurso resource_id pelo cliente client_id, durante
        time_limit segundos. Retorna OK, NOK ou UNKNOWN RESOURCE.
        """
        
        resourceList = self.resource_list_getter()
        for resource in resourceList:
            if resource.resource_id_getter() == resource_id:  
                lockAnswer = resource.lock(client_id, time_limit, can_lock)
                return lockAnswer
                
        return None


    def unlock(self, resource_id, client_id):
        """
        Liberta o bloqueio sobre o recurso resource_id pelo cliente client_id.
        Retorna OK, NOK ou UNKNOWN RESOURCE.
        """
        resourceList = self.resource_list_getter()
        for resource in resourceList:
            if resource.resource_id_getter() == resource_id:  
                unlockAnswer = resource.unlock(client_id)
                return unlockAnswer


        return None

    def status(self, option, resource_id):
        """
        Obtém o estado de um recurso. Se option for R, retorna LOCKED, UNLOCKED,
        DISABLED ou UNKNOWN RESOURCE. Se option for K, retorna <número de 
        bloqueios feitos no recurso> ou UNKNOWN RESOURCE.
        """

        resourceList = self.resource_list_getter()

        if option == "R":
            for resource in resourceList: 
                if resource.resource_id_getter() == resource_id:
                    lockState = resource.lock_getter()
                    return lockState
            return "UNKNOWN RESOURCE"

        elif option == "K":
            for resource in resourceList: 
                if resource.resource_id_getter() == resource_id:
                    numBlocks = resource.lock_number_getter()
                    return numBlocks

            return "UNKNOWN RESOURCE"


    def stats(self, option):
        """
        Obtém o estado do serviço de exclusão mútua. Se option for Y, retorna 
        <número de recursos bloqueados atualmente>. Se option for N, retorna 
        <número de recursos disponiveis atualmente>. Se option for D, retorna 
        <número de recursos desabilitdados>
        """
        if option == 50:
            counterBlockedRec = 0 
            for resource in self.resource_list_getter():
                if resource.lock_getter() == "LOCKED":
                    counterBlockedRec = counterBlockedRec + 1
            return counterBlockedRec

        if option == 60:
            counterAvailableRec = 0
            for resource in self.resource_list_getter():
                if resource.lock_getter() == "UNLOCKED":
                    counterAvailableRec = counterAvailableRec + 1
            return counterAvailableRec

        if option == 70:
            counterDisabledRec = 0
            for resource in self.resource_list_getter():
                if resource.lock_getter() == "DISABLED":
                    counterDisabledRec = counterDisabledRec + 1

            return counterDisabledRec


    def __repr__(self):
        """
        Representação da classe para a saída standard. A string devolvida por
        esta função é usada, por exemplo, se uma instância da classe for
        passada à função print ou str.
        """

        output = ""
        resourceList = self.resource_list_getter()
        for resource in resourceList:
            output = output + str(resource) + '\n'
        
        return output