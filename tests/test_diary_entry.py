from pytest import fixture, mark
from lib.diary_entry import DiaryEntry

"""
- Creates/instantiates a diary entry
- Returns a specified diary entry in a nice format
- count_words
- reading_time
"""

"""
Fixtures
"""
@fixture
def long_text_100_words():
    return """one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        """.strip()

@fixture
def long_text_300_words():
    return """one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        one two three four five six seven eight nine ten
        """.strip()

class TestInit():

    @mark.it('DiaryEntry class intitialises with title and contents properties')
    def test_diary_entry_inits_with_title_contents_and_contacts(self):
        diary_entry = DiaryEntry('Title', 'Contents')
        assert diary_entry.title == 'Title'
        assert diary_entry.contents == 'Contents'

class TestFormat():

    @mark.it('Format method returns single string in Title: Contents format')
    def test_format_returns_a_formatted_diary_entry_as_a_string(self):
        diary_entry = DiaryEntry('Title', 'Contents')
        assert diary_entry.format() == 'Title: Contents'

class TestCountWords():
    @mark.it('count_words method returns the correct word count as an int')
    def test_returns_correct_count(self):
        diary_entry = DiaryEntry('My Title', 'These are the contents')
        assert diary_entry.count_words() == 6
        assert type(diary_entry.count_words()) == int


class TestReadingTime():
    @mark.it('reading_time method returns an int rounded up to 1 when given 100 words and 200wpm')
    def test_reading_time_returns_1(self, long_text_100_words):
        diary_entry = DiaryEntry('My Title', long_text_100_words)
        assert diary_entry.reading_time(200) == 1

    @mark.it('reading_time method returns an int rounded up to 2 when given 300 words and 200wpm')
    def test_reading_time_returns_2(self, long_text_300_words):
        diary_entry = DiaryEntry('My Title', long_text_300_words)
        assert diary_entry.reading_time(200) == 2

    