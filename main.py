from textgram import *
import streamlit as st
import matplotlib.pyplot as plt

st.title('Welcome to TextGram!')
st.header(
    'TextGram allows text data cleaners to explore their data and get effective insights.'
)

filepath = st.text_input('Your input file path', 'sample.txt')
delimiter = st.text_input('Sentence delimiter', '\n')
nofgrams = st.number_input('(n) of grams',2,100,2)

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
all_grams = gramify.gramify(int(nofgrams))

word = st.text_input('Enter your word', 'off')
num_to_plot = st.number_input(f'No of most recurrnt {nofgrams}grams to plot', 5,100,10)
if word in all_grams.keys():
    # st.write(str(all_grams[word]))
    word_cnts = gramify.get_word_cooccur(all_grams, word)
    plt.barh(list(word_cnts.keys())[:num_to_plot], list(word_cnts.values())[:num_to_plot])
    st.pyplot()
else:
    st.write('Word Not Found!')
