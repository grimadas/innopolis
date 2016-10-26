python3 pos_feature_rus.py rus_corp.txt > rus_tr.input
python3 pos_feature_rus.py rus_test.txt > rus_te.input
echo "----------------PASIIVE-----------------------"
crfsuite learn -m rus.model -a pa  rus_tr.input
crfsuite tag -q -m rus.model -t rus_te.input
echo "----------------PERSEPTRON-----------------------"
crfsuite learn -m rus.model -a ap  rus_tr.input
crfsuite tag -q -m rus.model -t rus_te.input
#echo "-----------------lbfgs---------------------"
#crfsuite learn -m rus.model -a lbfgs  rus_tr.input
#crfsuite tag -q -m rus.model -t rus_te.input
#echo "-----------------l2sgd---------------------"
#crfsuite learn -m rus.model -a l2sgd rus_tr.input
#crfsuite tag -q -m rus.model -t rus_te.input
