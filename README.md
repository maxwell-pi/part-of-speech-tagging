Discriminative Part-of-Speech Tagging with crfsuite

Pipeline to facilitate experimentation with discriminative 
part-of-speech tagging using python crfsuite. Preset to work
with the Universal Dependencies English Web Treebank, but 
simple to adapt to other UD treebanks in .conllu format.

Scripts:
* baseline.py: reports baselines
* feature_search.py: assesses a list of featurizer functions
* hyperparameter_search.py: performs LBFGS hyperparameter search
* l2sgd_hyperparameter_search.py: peforms L2SGD hyperparameter search
* evaluation.py: evaluates configurations on test set

Classes:
* Lazy_Tagger.py: Tagger object for most common tag per type
* CRF_Tagger.py: Tagger object which takes featurizer, algorithm, and hyperparameters to perform tagging
* Featurizers.py: File with featurizer functions
* Tag_Utils.py: Util functions to read data, perform evaluations

Check NLP_Report.pdf for reported metrics.
