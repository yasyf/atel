from gensim.models import Word2Vec
from nodes import PositiveNode


class Atel(object):
  def __init__(self, model_location):
    self.model = Word2Vec.load_word2vec_format(model_location, binary=True)

  def word(self, word):
    return PositiveNode(self, None, word)

  def wrap(self, word):
      return self.word(word)

  def most_similar(self, n, **kwargs):
    results = (self.word(r[0]) for r in self.model.most_similar(topn=n, **kwargs))
    if n == 1:
      return next(results)
    else:
      return results
