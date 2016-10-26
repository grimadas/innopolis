# POS tagging using Structural Machine learning

## Dependencies

- crfsuite (<http://www.chokkan.org/software/crfsuite/>)
- Python3

## Basic Usage

Crfsuite requires a special file format. Python file: pos_feature.py - is formating input file into input format for crfsuite.  The features are specified in the python file.

- Run 'sh run.sh' - for training and testing POS tagging on Twitter dataset (pos_train.conll, pos_test.conll)
- Run 'sh rus_run.sh' - for training and testing POS tagging on Russian LifeJournal dataset (pos_train.conll, pos_test.conll)

## Credits

Second assignment of NLP course.

Full description is presented in pdf file
