# News Reduce
CSE 30331 Data Structures

Find the trending news articles from various sources by map reducing their headlines.

# Installation

The program runs on python2.7, which can be installed on the [official website]. Required packages may be installed with the [pip installer].

[official website]:https://www.python.org/download/releases/2.7/
[pip installer]:https://pypi.python.org/pypi/pip

For the program to fully compile, the lxml and requests libraries are required, and can be installed with:

    pip install lxml

    pip install requests

If in a virtual environment, then a **sudo** is not required; otherwise, precede any **pip install** commands with **sudo**.

To run the scripts that create graphs, the matplotlib and numpy libraries are required. Install with:

    pip install matplotlib

    pip install numpy


# Usage

All commands are to be run within the base *final-project* folder. To start the program, run the *master.py* function in *src* with the command:

    ./src/master.py

A series of flags can be added to this command in order to customize the output, which can be viewed by running:

    ./src/master.py -h
    Usage: ./master.py [options]...

    Options:
        -o          output data to stdout
        -n NUM      generate NUM keywords
        -d          disable the search for headlines
        -t          print the top words
        -h          help

To make the graph of current top words, the result of which will be stored in the *graphs* folder, run the command:

    make key-words

To test the code, run the command:

    make test

To run the benchmarking code for all implemented sorting algorithms, run the command:

    make bench
