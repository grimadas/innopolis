# Author's age and gender identification 

The task is to identify the gender and the age of the author only using the posted text in author's blog. 
The language of the blogs: English 

## Dependencies

- nltk, keras, gensim, seaborn 
- Python3

## Basic Usage

Run LangID.ipynb 
Crfsuite requires a special file format. Python file: pos_feature.py - is formating input file into input format for crfsuite.  The features are specified in the python file.

- Run 'sh run.sh' - for training and testing POS tagging on Twitter dataset (pos_train.conll, pos_test.conll)
- Run 'sh rus_run.sh' - for training and testing POS tagging on Russian LifeJournal dataset (pos_train.conll, pos_test.conll)

## Credits

Second assignment of NLP course (http://www.derczynski.com/sheffield/teaching.html).

Full description is presented in pdf file
