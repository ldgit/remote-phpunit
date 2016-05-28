class SublimeFacade:
    """
    Offers shortcut commands for some often used sublime actions.
    """
    def get_word_at_caret(self, view):
        return view.substr(view.word(view.sel()[0]))

    def get_line_at_caret(self, view):
        return view.substr(view.line(view.sel()[0]))
