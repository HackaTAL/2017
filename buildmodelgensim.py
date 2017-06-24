#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, gensim, argparse, codecs, numpy, scipy.spatial.distance, itertools, logging

aparser = argparse.ArgumentParser(description='Build gensim model from pattents')
aparser.add_argument('-t', '--txtfile', help='Documents txt file', required=True)
aparser.add_argument('-g', '--gensimfile', help='Gensim precomputed model', required=True)
args = aparser.parse_args()

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO
sents = gensim.models.word2vec.LineSentence(args.txtfile)
patmodel = gensim.models.Word2Vec(sents, size=100, window=10, min_count=10, workers=4)
patmodel.save(args.gensimfile)
