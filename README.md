<p align="center">
    <br>
    <img src="https://github.com/yli169/synapse/blob/main/synapse.png" width="100"/> 
    <img src="https://github.com/yli169/synapse/blob/main/nmnlu.png" width="300"/>
    <br>
<p>

A project that provides neural models with easy-to-use APIs to perform NLU tasks and paper reviews. The models are backed up by [Tensorflow](https://www.tensorflow.org) and all code follow [Google Coding Style](https://google.github.io/styleguide/pyguide.html).

## Model architectures

1. [Transformer](https://github.com/yli169/synapse/blob/main/notebooks/transformer.ipynb) (from Google) released with paper [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf) `NeurIPS 2017`, by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin.

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
