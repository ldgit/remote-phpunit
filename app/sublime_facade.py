class SublimeFacade:
    def get_word_at_caret(self, view):
        return view.substr(view.word(view.sel()[0]))
