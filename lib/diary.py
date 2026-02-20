class Diary():
    def __init__(self):
        self._entries_list = []

    def add(self, entry):
        self._entries_list.append(entry)

    def all(self):
        return self._entries_list
    
