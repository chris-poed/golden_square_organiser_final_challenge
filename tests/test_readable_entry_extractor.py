from pytest import fixture, mark

from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.readable_entry_extractor import ReadableEntryExtractor
from tests.test_diary_entry import long_text_100_words, long_text_300_words


@fixture
def diary_entry_one(long_text_100_words):
    return DiaryEntry('Title 1', long_text_100_words)

@fixture
def diary_entry_two(long_text_300_words):
    return DiaryEntry('Title 2', long_text_300_words)

@fixture
def diary_entry_three():
    return DiaryEntry('Title 2', 'This is a diary entry.')

class TestCountWordsForAllEntries():

    @mark.it('Returns the correct word count of all diary entries')
    def test_returns_word_count_of_all_entries(self, diary_entry_one, diary_entry_two):
        diary = Diary()
        diary.add(diary_entry_one)
        diary.add(diary_entry_two)
        readable_entry_extractor = ReadableEntryExtractor(diary.all())
        assert readable_entry_extractor.count_words() == 404 # titles = 4 words

class TestFindBestEntryForReadingTime():

    @mark.it('Returns a DiaryEntry equal to or less than the specified reading time and wpm')
    def test_find_best_entry_for_reading_time(self, diary_entry_one, diary_entry_two):
        diary = Diary()
        diary.add(diary_entry_one)
        diary.add(diary_entry_two)
        readable_entry_extractor = ReadableEntryExtractor(diary.all())
        assert readable_entry_extractor.find_best_entry_for_reading_time(110, 1) == diary_entry_one