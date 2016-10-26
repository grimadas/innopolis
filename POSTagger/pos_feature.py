#!/usr/bin/env python3

import sys
import re
from nltk import corpus as corp
# first, we need a feature extraction function
# this should return a dictionary, made of up attribute:value data

def pos_features(word):
    features = {}
    features['word'] = word.lower() # important
    features['suffix'] = word.lower()[-2:] # important
    features['prefix'] = word.lower()[0] # important
    features['first'] = "upper" if word[0].isupper() else "lower"  # important
    features['len'] = str(len(word)) # effects item small and bigger on instance
    features['number'] = "num" if re.match(r"[-+]?\d*\.\d+|\d+", word) else "nonum"  # slight effect to item accuracy
    features['in_dict'] = 't' if word.lower() in word_dict else 'f'

    #features['ht'] = 't' if word[0] == '#' else 'f'
    #features['x2'] = "t" if '\\' in word.lower() else 'f' # increase item
    #features['spe_symb'] = "t" if '' in word else "f"

    #features['prev'] = prev_word.lower()


    # Reduces instance but increasing item
    '''
    if 'word' in f_prev.keys():
        features['prev_word'] = f_prev['word']
    else:
        features['prev_word'] = ''
    '''


    # Attempts to features

    #features['case'] = "upper" if all(map(str.isupper, word)) else "lower"
    #features['x1'] = "t" if '#' in word.lower() else 'f'


    #features['VBP'] = 't' if re.match(r"\'[a-z]+", word.lower()) else 'f'


    # No postive effect
    '''
    if 'word' in f_prev.keys():
        for i in f_prev.keys():
            if 'p' not in i:
                features['p'+i] = f_prev[i]
    '''
    return features

f_prev = {}
words = []
labels = []

l_file = open(sys.argv[1])
ls_r = l_file.readlines()
l_file.close()

for line in ls_r:
    line = line.strip()

    if not len(line):  # skip blank lines
        words.append('')
        labels.append('')
        continue

    label, word = line.split("\t")
    words.append(word)
    labels.append(label)


ind = -1
word_dict = set(corp.brown.words())

for line in ls_r:
    line = line.strip()  # remove newline from the end of the line
    ind += 1
    if not len(line):  # skip blank lines
        print()
        f_prev = {}
        continue

    label, word = line.split("\t")  # get the label and word out
    features = pos_features(word)  # do feature extraction

    #features['prev'] = words[ind-1] if ind > 0 else ''
    features['next'] = words[ind + 1] if ind < len(words) else ''
    if not ('test' in sys.argv[1] or 'te' in sys.argv[1]):
        #features['prev_lab'] = labels[ind - 1] if ind > 0 else ''
        #features['next_lab'] = labels[ind + 1] if ind < len(words) else ''
        pass



    # build a list of name:value strings, for the features
    crfsuite_features = []
    for feature_name in features:
        crfsuite_features.append(feature_name + '_' + features[feature_name])
    # output the label, a tab, and then all the features with tabs between them
    print(label + "\t" + "\t".join(crfsuite_features))
    f_prev = features
