import unittest

from app.sublime_facade import SublimeFacade


class TestSublimeFacade(unittest.TestCase):
    def setUp(self):
        self.sublime_facade = SublimeFacade()
        self.view = ViewSpy()
        self.view.sel_return_value = ['default selected region']

    def test_get_word_at_caret_returns_view_substr(self):
        self.view.substr_return_value = 'a substring of a region'

        self.assertEqual('a substring of a region', self.sublime_facade.get_word_at_caret(self.view))

    def test_substr_accepts_view_word_region_as_parameter(self):
        self.view.word_return_value = 'a value returned by word'

        self.sublime_facade.get_word_at_caret(self.view)

        self.assertEqual('a value returned by word', self.view.substr_input_value)

    def test_word_accepts_first_element_of_list_returned_by_view_sel(self):
        self.view.sel_return_value = ['selected region']

        self.sublime_facade.get_word_at_caret(self.view)

        self.assertEqual('selected region', self.view.word_input_value)


class ViewSpy:
    def __init__(self):
        self.sel_return_value = None
        self.word_return_value = None
        self.word_input_value = None
        self.substr_return_value = None
        self.substr_input_value = None

    def substr(self, region):
        self.substr_input_value = region

        return self.substr_return_value

    def word(self, region):
        self.word_input_value = region

        return self.word_return_value

    def sel(self):
        return self.sel_return_value
