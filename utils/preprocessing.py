"""Utils for pre-processing the data."""

import re
import tensorflow as tf 

from typing import List
from typing import Tuple
from tensorflow.keras.preprocessing.text import Tokenizer


def PreprocessSentence(sentence: str) -> str:
    """Sentence pre-processing util function.
    
    Args:
        sentence: Raw input string.
    Returns:
        sentence: Normalized string.
    """
    sentence = sentence.lower().strip()
    # Add whitespace after certain special characters.
    sentence = re.sub(r"([,.?!$%'])", r" \1 ", sentence)
    # Add <start> and <end> token to sentence.
    sentence = "<start> " + sentence + " <end>"
    # Remove the redundant whitespaces.
    sentence = re.sub(r"[' ']+", " ", sentence)

    return sentence


def TokenizeSentence(sentences: List[str]):
    """Sentence tokenization util funcion.
    
    Args:
        sentences: List of raw sentences.
    Returns:
        tensor: Representation of tokenized sentences of shape
            [len(sentences), max_len(sentence)]
        tokenizer: Tokenizer fitted on given sentences.
    """

    tokenizer = Tokenizer(filters="", oov_token="<OOV>")
    tokenizer.fit_on_texts(sentences)
    tensor = tokenizer.texts_to_sequences(sentences)
    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, 
                                                           padding="post")
    
    return tensor, tokenizer


def CreateSeq2SeqData(input_text: List[str],
                      target_text: List[str],
                      buffer_size: int, 
                      batch_size: int):
    input_tensor, input_tokenizer = TokenizeSentence(input_text)
    target_tensor, target_tokenizer = TokenizeSentence(target_text)

    dataset = tf.data.Dataset.from_tensor_slices(
        (input_tensor, target_tensor))
    dataset = dataset.shuffle(buffer_size).batch(batch_size, 
                                                 drop_remainder=True)
    
    return dataset, input_tokenizer, target_tokenizer