#-*- coding: utf-8 -*-
import os
import sys
import codecs
import argparse
import subprocess
from os.path import basename, splitext

sys.stdout=codecs.getwriter('utf-8')(sys.stdout)

def main (hyp_file, ref_file):
	print '#{}, {}, {}, {}'.format("HYP", "REF", "CER", "DESC")

	with codecs.open(hyp_file, mode='r', encoding='utf-8') as f1:
		with codecs.open(ref_file, mode='r', encoding='utf-8') as f2:
			for line1, line2 in zip(f1, f2):
				tokens1 = line1.split(',')
				tokens2 = line2.split(',')

				t1 = tokens1[1].strip()
				t2 = tokens2[1].strip()

				s1 = tokens1[-2].strip()
				s2 = tokens2[-2].strip()

				with codecs.open('hyp', mode='w', encoding='utf-8') as of: of.write(s1)
				with codecs.open('ref', mode='w', encoding='utf-8') as of: of.write(s2)

				cmd = 'python WERpp/wer++.py --cer {} {}'.format('hyp', 'ref')
				ret = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE).communicate()[0]
				cer = ret.split(' ')[1]

				print '{}, {}, {}, {}'.format(t1, t2, cer, ret)
				break

			os.remove('ref')
			os.remove('hyp')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--hyp', required=True, help='file containing hypothesis texts')
	parser.add_argument('--ref', required=True, help='file containing golden texts')
	args = parser.parse_args()

	main(args.hyp, args.ref)
