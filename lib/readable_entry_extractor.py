class ReadableEntryExtractor():

    def __init__(self, _entries_list):
        self._entries_list = _entries_list

    def count_words(self):
        return sum([entry.count_words() for entry in self._entries_list])
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        if len(self._entries_list) == 0:
            raise ValueError('No entries found')
        reading_length = wpm * minutes 
        possible_entries_to_read = [entry for entry in self._entries_list if entry.count_words() <= reading_length]
        return max(possible_entries_to_read, key=lambda x: x.count_words())