"""Utils for the text tokenizer."""

from itertools import islice
from typing import Dict, List

def inverse_vocab(vocab: Dict):
    """inverse the key-value pairs of the vocabulary."""
    return {v: k for k, v in vocab.items()}


def truncate_vocab(vocab: Dict, max_vocab_size: int) -> Dict:
    """Truncate the vocabulary."""
    return dict(islice(vocab.items(), max_vocab_size))


def NormalizeCorpus(corpus: List[str]) -> List[str]:
    """Normalize words in the corpus."""
    corpus = [word.lower() for word in corpus]

    return corpus