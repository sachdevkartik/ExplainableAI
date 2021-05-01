from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split
import pandas as pd
from sklearn.tree import export_graphviz
from subprocess import check_call
import subprocess

""" 
This code generates number of decision trees (.dot file) for the trained RandomForestClassifier 
.dot files can be converted to .png by adding bash command through python
.dot files can also be converted by using the following command in shell where .dot files are stored:
    for i in *.dot; do dot -Tpng $i -o "${i%.dot}.png"; done
"""

train_df = pd.read_csv('./Datasets/classification/data_3.csv')
train, test = train_test_split(train_df, test_size = 0.2, random_state=42)

split_train_X = train.drop("X2urvived", axis=1)
split_train_Y = train["X2urvived"]

split_test_X = test.drop("X2urvived", axis=1)
split_test_Y = test["X2urvived"]

clf = RandomForestClassifier(max_depth=5, n_estimators=100, max_leaf_nodes=4, random_state=0)
clf.fit(split_test_X, split_test_Y)
print("No of tress:", len(clf.estimators_))

labels = train_df.columns

cnt =1
for item in clf.estimators_:
    export_graphviz(item, out_file='./dot/' + str(cnt)+'_tree.dot', feature_names = labels[1:], class_names = ['0', '1'],
                    rounded = True, precision = 4, node_ids = True, proportion = True, filled = True)

    cnt += 1
