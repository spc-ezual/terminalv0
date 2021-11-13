class File:
    def __init__(self):
        self._file= []
    
    def __len__(self):
        return len(self._file)
    
    def est_vide(self):
        return len(self)==0
    
    def emFiler(self,element):
        self._file.append(element)
    
    def deFiler(self):
        if self._file:
            return self._file.pop(0)