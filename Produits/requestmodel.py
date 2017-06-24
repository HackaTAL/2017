#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, gensim, argparse, codecs, numpy, scipy.spatial.distance, itertools, logging

aparser = argparse.ArgumentParser(description='Build gensim model from pattents')
aparser.add_argument('-g', '--gensimfile', help='Gensim precomputed model', required=True)
aparser.add_argument('-w', '--word', help='Word to be requested', required=True)
args = aparser.parse_args()

model = gensim.models.Word2Vec.load(args.gensimfile)
print args.word
print model.most_similar(positive=[args.word])
