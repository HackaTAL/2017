#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, gensim, argparse, codecs, numpy, scipy.spatial.distance, itertools, logging

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

aparser = argparse.ArgumentParser(description='Build gensim model from pattents')
aparser.add_argument('-t', '--txtfile', help='Documents txt file', required=True)
aparser.add_argument('-g', '--gensimfile', help='Gensim precomputed model', required=True)
args = aparser.parse_args()

# Retrieve tweeets as documents
documents  = []
for line in open(args.txtfile):
	line = line.strip()
	documents.append(line)

patmodel = gensim.models.Word2Vec(documents, size=100, window=10, min_count=10, workers=4)
patmodel.save(args.gensimfile)
