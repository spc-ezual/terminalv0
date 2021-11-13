class Pile:
    def __init__(self):
        self._pile= []
    
    def __len__(self):
        return len(self._pile)
    
    def est_vide(self):
        return len(self)==0
    
    def empiler(self,element):
        self._pile.append(element)
    
    def dePiler(self):
        if self._pile:
            return self._pile.pop()
            