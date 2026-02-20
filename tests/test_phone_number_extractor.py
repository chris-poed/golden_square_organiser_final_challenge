from pytest import fixture
from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.phone_number_extractor import PhoneNumberExtractor

@fixture
def diary_entry_one():
    return DiaryEntry('Title 1', 'This is entry 1 with no phone number')

@fixture
def diary_entry_two():
    return DiaryEntry('Title 2', 'This is entry 2 with 07111111111 ')

@fixture
def diary_entry_three():
    return DiaryEntry('Title 2', 'This is a diary entry with 07222222222 and 07333333333.')

class TestPhoneContactAdded():
    
    def test_multiple_phone_numbers_added_when_in_entries(self, diary_entry_one, diary_entry_two, diary_entry_three):
        diary = Diary()
        diary.add(diary_entry_one)
        diary.add(diary_entry_two)
        diary.add(diary_entry_three)
        phone_number_extractor = PhoneNumberExtractor(diary.all())
        assert phone_number_extractor.extract_phone_number_from_all_diary_entries() == ['07111111111', '07222222222', '07333333333']