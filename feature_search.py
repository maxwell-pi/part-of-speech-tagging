import Tag_Utils
import Featurizers
from CRF_Tagger import CRF_Tagger

training_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-train.conllu'
dev_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-dev.conllu'

train_tokens_by_sent, train_tags_by_sent = Tag_Utils.load_data(training_data_path)
dev_tokens_by_sent, dev_tags_by_sent = Tag_Utils.load_data(dev_data_path)

featurizers = [Featurizers.combo_featurize_auto, Featurizers.baseline_featurize_no_bias, Featurizers.after_featurize]
reports = []
for featurizer in featurizers:
    tagger = CRF_Tagger(featurizer)
    tagger.train(train_tokens_by_sent, train_tags_by_sent)
    predictions = Tag_Utils.predict(tagger, dev_tokens_by_sent)
    reports.append(Tag_Utils.accuracy(dev_tags_by_sent, predictions))

for (featurizer, report) in zip(featurizers, reports):
    print(str(featurizer))
    print(report)
