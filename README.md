<p align="center">
    <br>
    <img src="https://github.com/yli169/synapse/blob/main/synapse.png" width="100"/> 
    <img src="https://github.com/yli169/synapse/blob/main/nmnlu.png" width="300"/>
    <br>
<p>

A project that provides neural models with easy-to-use APIs to perform NLU tasks and paper reviews. The models are backed up by [Tensorflow](https://www.tensorflow.org) and all code follow [Google Coding Style](https://google.github.io/styleguide/pyguide.html).

## Model architectures

1. [LSTM](https://github.com/yli169/synapse/blob/main/notebooks/lstm.ipynb) released with paper [Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf) `Neural Computation 1997`, by Sepp Hochreiter, Jürgen Schmidhuber.

2. [Bahdanau attention](https://github.com/yli169/synapse/blob/main/notebooks/bahdanau_attention.ipynb) (from Jacobs University Bremen, Universite de Montreal ) released with paper [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf) `ICLR 2015`, by Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio.

3. [Copy Mechanism](https://github.com/yli169/synapse/blob/main/notebooks/pointer_generator.ipynb) (from Stanford & Google) released with paper [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/pdf/1704.04368.pdf) `ACL 2017`, by Abigail See, Peter J. Liu, Christopher D. Manning.

4. [Transformer](https://github.com/yli169/synapse/blob/main/notebooks/transformer.ipynb) (from Google) released with paper [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf) `NeurIPS 2017`, by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin.

## Dependencies

The project is tested on [Python 3.8+](https://www.python.org/downloads/release/python-382/) and [Tensorflow Core v2.4+](https://www.tensorflow.org/api_docs).

We suggest installing the required libraries in [virtual environment](https://docs.python.org/3/library/venv.html) to avoid dependency conflicts. Check out the [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to learn how to setup an isolated environment for this project.

Then you will need to install TensorFlow. TensorFlow 2.0 promotes Keras for model experimentation and Estimators for scaled serving, and the two APIs are very convenient to use. It also enableds Eager execution by default, while in TensorFlow 1.x. you need to build the computational graph and later creating a session to execute it. Please refer to [installation page](https://www.tensorflow.org/install/pip#tensorflow-2.0-rc-is-available) for detailed instructions.

Following python libraries might also be necessary for runnning the models or notebooks, we suggest installing with [pip](https://pip.pypa.io/en/stable/) or [conda](https://docs.conda.io/en/latest/)

**[Matplotlib](https://matplotlib.org/)** is a comprehensive library for creating static, animated, and interactive visualizations in Python.
```bash
pip install matplotlib
```

**[Ipython](https://ipython.org/)** Provides a rich architecture for interactive computing
```bash
pip install ipython
```

## Plans

Following is a list of models (papers) we have already implemented (reviewed) or are going to implement (review). If there's a specific model/paper you are interested but is not listed, feel free to raise an issue an tell us why it's worth looking at.

:white_check_mark: &nbsp; Done &nbsp;&nbsp;&nbsp; :black_square_button: &nbsp; No plan

Model | Paper | Code | Review
:------------ | :-------------| :-------------:| :-------------:
RNN | | :black_square_button: |  
LSTM | [Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf) `Neural Computation 1997`  Sepp Hochreiter, Jürgen Schmidhuber |  :black_square_button: | :white_check_mark:
GRU | [Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](https://arxiv.org/pdf/1406.1078.pdf) `EMNLP 2014` Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio | :black_square_button: | 
Seq2seq | [Sequence to Sequence Learning with Neural Networks](https://papers.nips.cc/paper/2014/file/a14ac55a4f27472c5d894ec1c3c743d2-Paper.pdf) `NeurIPS 2014` Ilya Sutskever, Oriol Vinyals, Quoc V. Le | |   
Bahdanau Attention | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf) `ICLR 2015` Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio |  |:white_check_mark: 
Luong Attention | [Effective Approaches to Attention-based Neural Machine Translation](https://arxiv.org/pdf/1508.04025.pdf) `EMNLP 2015` Minh-Thang Luong, Hieu Pham, Christopher D. Manning |  | 
Copy Mechanism | [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/pdf/1704.04368.pdf) `ACL 2017`, Abigail See, Peter J. Liu, Christopher D. Manning |  | :white_check_mark: 
Transformer | [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf) `NeurIPS 2017` Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin |  | :white_check_mark: 
TransformerXL | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) `ACL 2019` Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V. Le, Ruslan Salakhutdinov |  | 
Longformer | [Longformer: The Long-Document Transformer](https://arxiv.org/pdf/2004.05150.pdf) `2020` Iz Beltagy, Matthew E. Peters, Arman Cohan |  | 
BERT | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1706.03762.pdf) `NAACL 2019` Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova |  | 
ALBERT | [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/pdf/1909.11942.pdf) `ICLR 2020` Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut |  | 
GPT-1 | [Improving Language Understanding by Generative Pre-Training](https://openai.com/blog/language-unsupervised/) `2018` Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever |  | 
T5 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf) `JMLR 2020` Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu |  | 
 | | [Don't Parse, Generate! A Sequence to Sequence Architecture for Task-Oriented Semantic Parsing](https://arxiv.org/pdf/2001.11458.pdf) `WWW 2020` Subendhu Rongali, Luca Soldaini, Emilio Monti, Wael Hamza |  | 
