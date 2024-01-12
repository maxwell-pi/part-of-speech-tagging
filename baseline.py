import Tag_Utils
import Featurizers
from Lazy_Tagger import Lazy_Tagger
from CRF_Tagger import CRF_Tagger

training_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-train.conllu'
dev_data_path = 'ud-treebanks-v2.13/UD_English-EWT/en_ewt-ud-dev.conllu'

train_tokens_by_sent, train_tags_by_sent = Tag_Utils.load_data(training_data_path)
dev_tokens_by_sent, dev_tags_by_sent = Tag_Utils.load_data(dev_data_path)

lazy_tagger = Lazy_Tagger()
lazy_tagger.train(train_tokens_by_sent, train_tags_by_sent)
lazy_predictions = Tag_Utils.predict(lazy_tagger, dev_tokens_by_sent)

ap_tagger = CRF_Tagger(Featurizers.baseline_featurize_no_bias)
ap_tagger.train(train_tokens_by_sent, train_tags_by_sent)
ap_predictions = Tag_Utils.predict(ap_tagger, dev_tokens_by_sent)

print('Lazy Eval:')
print(Tag_Utils.evaluate_by_tag(dev_tags_by_sent, lazy_predictions))

print('AP Eval:')
print(Tag_Utils.evaluate_by_tag(dev_tags_by_sent, ap_predictions))
