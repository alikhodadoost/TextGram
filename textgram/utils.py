def read_file(filename: str, sentence_delimiter = '\n'):
    with open(filename, 'r') as f:
        return f.read().split(sentence_delimiter)

class Tokenizer:
    '''
    Base tokenizer class
    '''
    def __init__(self):
        pass
    def tokenize(self, text: str) -> list:
        '''
        Gets a string as text, then returns list of its tokens
        '''
        pass