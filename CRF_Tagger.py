import pycrfsuite
from functools import reduce

class CRF_Tagger:
    def __init__(self, featurize):
        self.featurize = featurize

    def train(self, tokens_by_sent, tags_by_sent, algorithm = 'ap', hyperparameters={}):
        token_features = []
        for sentence in tokens_by_sent:
            for i in range(len(sentence)):
                token_features.append(self.featurize(sentence, i))
        tags = reduce(lambda s, t: s + t, tags_by_sent, [])

        trainer = pycrfsuite.Trainer(algorithm=algorithm)
        trainer.append(token_features, tags)
        trainer.set_params(hyperparameters)
        trainer.train('model-image.crfsuite')

    def tag(self, tokens):
        tagger = pycrfsuite.Tagger()
        tagger.open('model-image.crfsuite')
        input_features = []
        for i in range(len(tokens)):
            input_features.append(self.featurize(tokens, i))
        return tagger.tag(input_features)
