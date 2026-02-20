from pytest import fixture, mark
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Fixtures
"""
@fixture
def test_diary_entry_one():
    return DiaryEntry('Title 1', 'Contents 1')

@fixture
def test_diary_entry_two():
    return DiaryEntry('Title 2', 'Contents 2')

@fixture
def test_diary_entry_three():
    return DiaryEntry('Title 3', 'Contents 3')

"""
class Diary()
- Keeps a list of diary entries
- Adds a DiaryEntry()
- Finds best entry for reading time
"""

class TestInit():

    @mark.it('Diary class initialises with an empty entry_list')
    def test_Diary_class_inits_with_empty_entry_list(self):

        diary = Diary()
        assert diary._entries_list == []
    

class TestAdd():
    @mark.it('Test that multiple diary entries are added to the entries_list')
    def test_multiple_diary_entries_are_added_to_the_entries_list(self):
        diary = Diary()
        diary.add(test_diary_entry_one)
        diary.add(test_diary_entry_two)
        diary.add(test_diary_entry_three)
        assert diary.all() == [test_diary_entry_one, test_diary_entry_two, test_diary_entry_three]

