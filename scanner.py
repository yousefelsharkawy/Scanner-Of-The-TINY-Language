#define a token class to hold the token type and value
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token({type}, {value})".format(type=self.type, value=self.value)

#dictionary of all tokens in tiny language and their corresponding values
tokens = {
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'TIMES',
    '/': 'DIVIDE',
    '(': 'LPAREN',
    ')': 'RPAREN',
    ';': 'SEMI',
    ':=': 'ASSIGN',
    '<': 'LT',
    '>': 'GT',
    '=': 'EQ',
    '!=': 'NEQ',
    '<=': 'LEQ',
    '>=': 'GEQ',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'end': 'END',
    'repeat': 'REPEAT',
    'until': 'UNTIL',
    'read': 'READ',
    'write': 'WRITE',
}

class lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.string_value_accumulator = ""

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def isspace(self):
        if self.current_char == " " or self.current_char == "\n":
            return True
        else:
            return False
    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char == ":":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(tokens[':='], ':=')
                else:
                    self.error()
            # TODO: implement the rest of the DFAs in here 

            