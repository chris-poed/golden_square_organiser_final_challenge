import math

class DiaryEntry:

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
    
    def format(self):
        return f'{self.title}: {self.contents}'
    
    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())
    
    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)