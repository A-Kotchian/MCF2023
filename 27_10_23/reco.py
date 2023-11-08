
class Hit:
    """
    Questa classe rappresenta eventi con delle coordinate:
    -id Modulo(id_mod)
    -id Sensore(id_sens)
    -Tempo di rilevazione(time)

    """

    def __init__(self,id_mod,id_sens,time):
        self.id_mod = id_mod
        self.id_sens = id_sens
        self.time = time

    def __eq__(self, other):
        return  self.temp == other.temp and self.id_sens == other.id_sens and self.id_mod == other.id_mod
    
    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time
    
    def __sub__(self, other):
        return self.time-other.time
    
    def __add___(self, other):
        return self.time+other.time

    
