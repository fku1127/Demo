#-*- coding: utf-8 -*-
import os
import sys
import codecs
import argparse
import transcribe
from os.path import basename, splitext

DEFAULT_OUT_DIR = './result'

def speech2text (file):
    return transcribe.main(file)

def replace_ext (name, ext='.txt'):
    return splitext(name)[0] + ext

def main (src_dir, out_dir):
    src_dir = os.path.abspath(src_dir)
    out_dir = os.path.abspath(out_dir)

    print('===============================')
    print('SRC DIR: {}'.format(src_dir))
    print('OUT DIR: {}'.format(out_dir))

    for i_root, subdirs, files in os.walk(src_dir):
        print('--\ndir = ' + i_root)
        o_root = i_root.replace(src_dir, out_dir);

        if not os.path.isdir(o_root): os.makedirs(o_root)

        for filename in files:
            ifile_path = os.path.join(i_root, filename)
            ofile_path = os.path.join(o_root, replace_ext(filename))

            print('\t- {} -> {})'.format(ifile_path, ofile_path))

            text, confidence = speech2text(ifile_path)
            with codecs.open(ofile_path, mode='w', encoding='utf-8') as of:
                s = u'{}, {}'.format(text, confidence)
                print(u'\t- {}'.format(s))
                of.write(s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src_dir', help='folder containing wav files')
    parser.add_argument('--out_dir', help='folder for output text')
    args = parser.parse_args()

    if not args.out_dir: args.out_dir = DEFAULT_OUT_DIR

    main(args.src_dir, args.out_dir)
