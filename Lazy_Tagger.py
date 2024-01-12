from collections import defaultdict, Counter

class Lazy_Tagger:

    def __init__(self):
        self.tag_by_type = {}
        self.default_tag = ''

    def train(self, tokens_by_sent, tags_by_sent):
        counts_by_type = defaultdict(Counter)
        total_counts = Counter()
        for i in range(len(tokens_by_sent)):
            for j in range(len(tokens_by_sent[i])):
                counts_by_type[tokens_by_sent[i][j]][tags_by_sent[i][j]] += 1
                total_counts[tags_by_sent[i][j]] += 1
        self.default_tag = max(total_counts.items(), key = lambda p: p[1])[0]
        self.tag_by_type = {tag : max(counts_by_type[tag].items(), key = lambda p: p[1])[0] for tag in counts_by_type}

    def tag(self, tokens):
        tags = []
        for token in tokens:
            if token in self.tag_by_type:
                tags.append(self.tag_by_type[token])
            else:
                tags.append(self.default_tag)
        return tags
