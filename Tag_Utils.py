import pyconll
from functools import reduce
from sklearn.metrics import classification_report, accuracy_score

def load_data(conllu):
    data = pyconll.load_from_file(conllu)
    tokens_by_sentence = []
    tags_by_sentence = []
    for sentence in data:
        tokens = []
        tags = []
        for token in sentence:
            if token.upos != None and token.form != None:
                tokens.append(token.form)
                tags.append(token.upos)
        tokens_by_sentence.append(tokens)
        tags_by_sentence.append(tags)
    return tokens_by_sentence, tags_by_sentence

def predict(model, sentences):
    predicted_tags_by_sent = []
    for sentence in sentences:
        predicted_tags_by_sent.append(model.tag(sentence))
    return predicted_tags_by_sent

def evaluate_by_tag(true_tags, predicted_tags):
    true_tags_flat = reduce(lambda s, t: s + t, true_tags, [])
    predicted_tags_flat = reduce(lambda s, t: s + t, predicted_tags, [])
    return classification_report(true_tags_flat, predicted_tags_flat)

def accuracy(true_tags, predicted_tags):
    true_tags_flat = reduce(lambda s, t: s + t, true_tags, [])
    predicted_tags_flat = reduce(lambda s, t: s + t, predicted_tags, [])
    return accuracy_score(true_tags_flat, predicted_tags_flat)