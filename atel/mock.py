from gensim.models import Word2Vec
from atel import Atel


class MockAtel(Atel):
  def __init__(self):
    self.model = Word2Vec()

  @staticmethod
  def most_similar(n, **kwargs):
    return 'queen'
