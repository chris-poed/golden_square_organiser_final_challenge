import re
from itertools import chain

class PhoneNumberExtractor():

    def __init__(self, _entries_list):
        self._entries_list = _entries_list
        self.phone_number_list = []

    def extract_phone_number_from_all_diary_entries(self):
        regex = re.compile(r"\+?\d[\d\s\-()]{7,}\d")

        for entry in self._entries_list:
            contents = getattr(entry, "contents", "") or ""
            self.phone_number_list.extend(regex.findall(contents))
        
        return self.phone_number_list
        
