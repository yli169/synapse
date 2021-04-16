"""The text tokenizer class."""

import json

from collections import defaultdict
from typing import List

from codebase.tokenizers import constants
from codebase.tokenizers import tokenizer_utils

class Tokenizer(object):
    """ Text tokenizer class.

    The tokenizer maps the given token to its corresponding integer index in the 
    vocab. The vocab can either be created by fitting the tokenizer on given 
    text corpus or load from local json files.

    Args:
        num_words: the maximum number of words to keep in the vocab, based on 
            the word frequency. by default keep all the words.
        oov: if allow oov.
        special_tokens: special_tokens to be added, separated by whitespace.
        filters: tokens that should be filtered out, separated by whitespace.
        if_normalize: if the token should be normalized. i.e. lower, striped...
    """

    def __init__(self, num_words: int=None, 
                       oov: bool=True,
                       special_tokens: str='',
                       filters: str='', 
                       if_normalize: bool=False):
        self.num_words = num_words
        self.oov = oov
        self.special_tokens = special_tokens.split()
        self.word_counts = defaultdict(int)
        self.vocab = defaultdict(int)
        self.lookup_table = defaultdict(str)
        self.filters = set(filters.split())
        self.if_normalize = if_normalize


    def fit(self, corpus: List[str], save_vocab_path: str='') -> None:
        """Fit tokenizer on the corpus to create vocab."""
        if self.if_normalize:
            corpus = tokenizer_utils.NormalizeCorpus(corpus)
        for doc in corpus:
            for word in doc.split():
                if word not in self.filters:
                    self.word_counts[word] += 1
        self.word_counts = sorted(self.word_counts.items(), 
                                  key=lambda x: x[1], 
                                  reverse=True)
        
        index = 1
        
        if self.oov:
            self.vocab[constants.OOV] = index
            index += 1

        for token in self.special_tokens:
            self.vocab[token] = index
            index += 1
        
        for word, _ in self.word_counts:
            self.vocab[word] = index
            index += 1

        if save_vocab_path:
            with open(save_vocab_path, 'w') as f:
                f.write(json.dumps(self.vocab))

        if len(self.vocab) > self.num_words:
            self.vocab = tokenizer_utils.truncate_vocab(self.vocab, 
                                                        self.num_words)
        self.lookup_table = tokenizer_utils.inverse_vocab(self.vocab)
    

    def load_vocab(self, vocab_file: str=None) -> None:
        """Load fixed vocab from local file."""
        with open(vocab_file) as f:
            self.vocab = json.load(f)
        if self.num_words:
            self.vocab = truncate_vocab(self.vocab, self.num_words)
        self.lookup_table = inverse_vocab(self.vocab)


    def token2id(self, token: str) -> int:
        """Returns the id of a given token."""
        if token not in self.vocab:
            return self.vocab['[OOV]']
        return self.vocab[token]


    def id2token(self, token_id: int) -> str:
        """Returns the token corresponding to a given id."""
        if token_id not in self.lookup_table:
            return '[OOV]'
        return self.lookup_table[token_id]


    def corpus_to_sequences(self, corpus: List[str]) -> List[List[int]]:
        """Tokenize corpus to sequences of indexes."""
        sequences = []
        for doc in corpus:
             sequences.append([self.token2id(word) for word in doc.split()])
        
        return sequences