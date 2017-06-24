#!/bin/bash

find hasIpcCorr -type f
	| xargs cat
	| tree-tagger-french
	| sed 's/.*SENT.*/SENT/'
	| cut -f 1 | tr '\n' ' '
	| perl -pe 's/ *SENT */\n/g' > pats-sents.txt
