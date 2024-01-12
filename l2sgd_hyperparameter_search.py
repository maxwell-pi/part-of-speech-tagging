import Tag_Utils
import Featurizers
from CRF_Tagger import CRF_Tagger

training_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-train.conllu'
dev_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-dev.conllu'

train_tokens_by_sent, train_tags_by_sent = Tag_Utils.load_data(training_data_path)
dev_tokens_by_sent, dev_tags_by_sent = Tag_Utils.load_data(dev_data_path)

search_space = {'c2': [1.0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 0.0]}
accuracy_matrix = {val1 : -1 for val1 in search_space['c2']}

for val2 in search_space['c2']:
    hyperparameters = {'c2': val2, 'max_iterations':100}
    tagger = CRF_Tagger(Featurizers.local_featurize_auto)
    tagger.train(train_tokens_by_sent, train_tags_by_sent, algorithm='l2sgd', hyperparameters=hyperparameters)
    predictions = Tag_Utils.predict(tagger, dev_tokens_by_sent)
    accuracy_matrix[val2] = Tag_Utils.accuracy(dev_tags_by_sent, predictions)

print(accuracy_matrix)
