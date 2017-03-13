#!/bin/sh

GOLDEN_DIR="/share/data/users/jiantai.chen/concat_slice/slice"

GOLDEN="./golden"
LOG_GOLDEN="log.golden"

##### 1. Create GOLDEN text #####
echo '[START] SPEECH -> TEXT: GOLDEN'
python main.py ${GOLDEN_DIR} --out_dir=${GOLDEN} >& ${LOG_GOLDEN} 2>&1


##### 2. Run evaluation #####
#NOISY_DIR="/share/data/users/jiantai.chen/concat_slice/"
##NOISY_CASES="1m 2m 3m 4m 5m"
#NOISY_CASES="1m"
#for c in ${NOISY_CASES}
#do
#	in_dir=${NOISY_DIR}${c}
#	echo '[START] SPEECH -> TEXT: '${in_dir}
#	out_dir="out."${c}
#	rm -rf ${out_dir}
#	LOG_OUT=log.${c}
#	python main.py ${in_dir} --out_dir=${out_dir} >& ${LOG_OUT} 2>&1
#	python eval.py --hyp=${LOG_OUT} --ref=${LOG_GOLDEN} >& cer.${c} 2>&1
#done
