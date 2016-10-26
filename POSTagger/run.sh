python3 pos_feature.py pos_test.conll > te.input
python3 pos_feature.py pos_train.conll > tr.input
echo "----------------PASIIVE-----------------------"
crfsuite learn -m m_simple.model -a pa  tr.input
crfsuite tag -q -m m_simple.model -t te.input
echo "----------------PERSEPTRON-----------------------"
crfsuite learn -m m_simple.model -a ap  tr.input
crfsuite tag -q -m m_simple.model -t te.input
#echo "-----------------lbfgs---------------------"
#crfsuite learn -m m_simple.model -a lbfgs  tr.input
#crfsuite tag -q -m m_simple.model -t te.input
#echo "-----------------l2sgd---------------------"
#crfsuite learn -m m_simple.model -a l2sgd  tr.input
#crfsuite tag -q -m m_simple.model -t te.input
