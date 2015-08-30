from gensim.models import Word2Vec
from nodes import PositiveNode
from nltk.stem.snowball import SnowballStemmer


class Atel(object):
  def __init__(self, model_location):
    self.model = Word2Vec.load_word2vec_format(model_location, binary=True)
    self.stemmer = SnowballStemmer('english')

  def word(self, word):
    return PositiveNode(self, None, word)

  def wrap(self, word):
      return self.word(word)

  def most_similar_without_words(self, words, **kwargs):
    stemmed_words = set(map(self.stemmer.stem, words))
    for result in self.model.most_similar(topn=10, **kwargs):
      stemmed_result = self.stemmer.stem(result[0])
      if stemmed_result not in stemmed_words:
        return self.word(result[0])

  def most_similar(self, n, **kwargs):
    results = (self.word(r[0]) for r in self.model.most_similar(topn=n, **kwargs))
    if n == 1:
      return next(results)
    else:
      return results
