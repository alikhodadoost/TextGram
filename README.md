# TextGram

#### TextGram allows text data cleaners to explore their text data and get effective insights.


## How-to
**Clone** this repo

**Run:**
```
streamlit run main.py
```

Screenshot:
![Screenshot](https://github.com/alikhodadoost/TextGram/blob/master/imgs/scr.jpg)

## Add your own tokenizer
You need a class to inherit from this project's base **Tokenizer** class.
Let's do this with replacing **MyTokenizer** class with a pretrained Bert tokenizer.
So edit the **main.py** and replace this part of code:
```
class MyTokenizer(Tokenizer):
    def __init__(self):
        super(MyTokenizer).__init__()
    def tokenize(text: str):
        return text.split(' ')

sentences = read_file(filepath)
gramify = Gramify(
    sentences = sentences,
    tokenizer = MyTokenizer
)
```
With this
```
import torch
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

class MyTokenizer(Tokenizer):
    def __init__(self):
        super(MyTokenizer).__init__()
    def tokenize(text: str):
        return tokenizer.tokenize(text)

sentences = read_file(filepath)
gramify = Gramify(
    sentences = sentences,
    tokenizer = MyTokenizer
)
```

Happy Digesting Data!
