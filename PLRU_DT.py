# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier

# iris = datasets.load_iris()
# x = iris.data
# y = iris.target

# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(x, y)

# fig = plt.figure(figsize=(25,20))
# tree.plot_tree(clf, filled=True, rounded=True, max_depth=3)
# plt.savefig('PLRU_DT.png')

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier with a depth of 3
tree_classifier = DecisionTreeClassifier(max_depth=3)

# Fit the model on the training data
tree_classifier.fit(X_train, y_train)

# Visualize the decision tree using matplotlib
plt.figure(figsize=(12, 8))
plot_tree(tree_classifier, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True)
plt.savefig('PLRU_DT.png')

