class NoClosingBracket(Exception):
    bool_func: str
    opening_bracket_index: int

    def __init__(self, bool_func: str, opening_bracket_index: int):
        self.bool_func = bool_func
        self.opening_bracket_index = opening_bracket_index

    def __str__(self):
        return "No closing bracket(index: {0}):\n{1}".format(self.opening_bracket_index, self.bool_func)
