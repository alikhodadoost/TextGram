from nltk.util import ngrams
from .utils import Tokenizer
from collections import Counter

class Gramify:
    def __init__(self, sentences: list, tokenizer: Tokenizer):
        self.sentences = sentences
        self.tokenizer = tokenizer

    def get_tokens(self, sentence: str):
        '''
        Tokenize using tokenizer
        '''
        return self.tokenizer.tokenize(sentence)

    def get_word_grams(self, tokens: list, n: int) -> list:
        '''
        Returns Ngrams for a list of tokens
        '''
        word2gram = {}
        grams = ngrams(tokens, n)
        
        for gram in grams:
            for g in gram:
                if g in word2gram.keys():
                    word2gram[g].append(gram)
                else:
                    word2gram[g] = []
                    word2gram[g].append(gram)
        return word2gram

    def gramify(self, n: int):
        '''
        Returns all grams for all sentences
        '''
        word2grams = {}
        for sentence in self.sentences:
            w2g = self.get_word_grams(
                self.get_tokens(sentence),
                n
            )
            for k in w2g.keys():
                if k in word2grams.keys():
                    word2grams[k].extend(w2g[k])
                else:
                    word2grams[k] = w2g[k]

        return word2grams
    def count_sorted(self, ngrams: list):
        return {k: v for k, v in sorted(Counter(ngrams).items(), key=lambda item: item[1],reverse= True)}
    def get_word_ngram_counts(self, word2grams: dict, word: str):
        counts_sorted = self.count_sorted(word2grams[word])

        return { ' '.join(k):v for k,v in counts_sorted.items()}
    def get_word_cooccur(self, word2grams: dict, word: str):
        word_occurs = {}
        for grams in word2grams[word]:
            for w in grams:
                if w != word:
                    if w not in word_occurs:
                        word_occurs[w] = 1
                    else:
                        word_occurs[w] += 1
        counts_sorted = self.count_sorted(word_occurs)
        return counts_sorted
