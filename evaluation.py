import Tag_Utils
import Featurizers
from CRF_Tagger import CRF_Tagger

training_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-train.conllu'
dev_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-dev.conllu'
testing_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-test.conllu'

train_tokens_by_sent, train_tags_by_sent = Tag_Utils.load_data(training_data_path)
dev_tokens_by_sent, dev_tags_by_sent = Tag_Utils.load_data(dev_data_path)
test_tokens_by_sent, test_tags_by_sent = Tag_Utils.load_data(testing_data_path)

reports = []
configurations = [('lbfgs', {'c1' : 0.1, 'c2': 0.0}), ('l2sgd', {'c2': 1.0}), ('ap', {})]

for config in configurations:
    tagger = CRF_Tagger(Featurizers.combo_featurize_auto)
    tagger.train(train_tokens_by_sent, train_tags_by_sent, algorithm=config[0], hyperparameters=config[1])
    predictions = Tag_Utils.predict(tagger, test_tokens_by_sent)
    reports.append(Tag_Utils.evaluate_by_tag(test_tags_by_sent, predictions))

for i in range(len(configurations)):
    print(configurations[i])
    print(reports[i])
    print()


