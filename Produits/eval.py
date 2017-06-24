# python3

# Simple evaluation script made for the Hackatal 2017 event : https://github.com/HackaTAL/2017
__author__ = "Gael Guibon <https://github.com/gguibon>"
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Gael Guibon"
__email__ = "gael.guibon@lsis.org"
__status__ = "Development"

import json, os
from os import listdir
from os.path import isfile, join
import argparse

parser = argparse.ArgumentParser(description='HackaTAL2017 simple evaluation script')
parser.add_argument('-dir','--directory', metavar='INPUT', type=str, help='directory path')
args = parser.parse_args()


def get_score_dir(dir_path):
	files = [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f))]
	d_scores_dir = {'emplacement':{'correct':0, 'total':0}, 'qualite-prix':{'correct':0, 'total':0},'communication':{'correct':0, 'total':0},'proprete':{'correct':0, 'total':0},'precision':{'correct':0, 'total':0},'arrivee':{'correct':0, 'total':0},'averageRanking':{'correct':0, 'total':0}}
	for file in files:
		d_scores = get_score_file(file)
		for k in d_scores_dir.keys():
			d_scores_dir[k]['total'] +=1
			if d_scores[k] == 1: 
				d_scores_dir[k]['correct'] += 1
	for k in d_scores_dir.keys():
		d_scores_dir[k] = float( d_scores_dir[k]['correct'] ) / float( d_scores_dir[k]['total'] )
	return d_scores_dir

def get_score_file(json_path):
	data = json.loads(open( json_path ).read() )
	d_scores = {'emplacement':0, 'qualite-prix':0,'communication':0,'proprete':0,'precision':0,'arrivee':0,'averageRanking':0} 
	for k in d_scores.keys():
		if data[k] == data['p_'+k]:
			d_scores[k] = 1
	return d_scores

d_scores = get_score_dir(args.directory)

print( d_scores )
accuracy = float()
for k in d_scores.keys():
	accuracy = accuracy + d_scores[k]
print(accuracy / len(d_scores))
