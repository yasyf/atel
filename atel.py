from gensim.models import Word2Vec
from enum import Enum
import collections

class Atel(object):
  def __init__(self, model_location):
    self.model = Word2Vec.load_word2vec_format(model_location, binary=True)

  def word(self, word):
    return PositiveNode(self, None, word)

  def most_similar(self, n, **kwargs):
    results = (self.word(r[0]) for r in self.model.most_similar(topn=n, **kwargs))
    if n == 1:
      return next(results)
    else:
      return results


class AtelNode(object):
  def __init__(self, root, last, word):
    self.root = root
    self.last = last
    self.next = None
    self.word = word

    if last:
      last.next = self

  def plus(self, word):
    return PositiveNode(self.root, self, word)

  def minus(self, word):
    return NegativeNode(self.root, self, word)

  def replace(self, remove, add):
    return self.minus(remove).plus(add)

  def delete(self):
    if self.last and self.next:
      self.last.next = self.next
      self.next.last = self.last
      self.last = None
      self.next = None
    elif self.last:
      self.last.next = None
      self.last = None
    elif self.next:
      self.next.last = None
      self.next = None

  def simplify(self):
    words = collections.defaultdict(set)
    nodes = collections.defaultdict(list)
    end = self
    current_node = self
    while current_node.last:
      next_current_node_ref = current_node.last

      if current_node.word in words[current_node.opposite]:
        opposing = filter(lambda n: n.key == current_node.opposite, nodes[current_node.word])[0]
        current_node.delete()
        if opposing == end:
          end = opposing.last
        opposing.delete()
      else:
        words[current_node.key].add(current_node.word)
        nodes[current_node.word].append(current_node)

      current_node = next_current_node_ref

    return end

  def __add__(self, word):
    return self.plus(word)

  def __sub__(self, word):
    return self.minus(word)

  def kwargs(self):
    if self.last:
      kwargs = self.last.kwargs()
    else:
      kwargs = collections.defaultdict(list)
    kwargs[self.key].append(self.word)
    return kwargs

  def evaluate(self):
    return self.simplify().root.most_similar(1, **self.kwargs())

  def __str__(self):
    if self.last:
      return '{last} {current}'.format(last=str(self.last), current=repr(self))
    else:
      return repr(self)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.word == other.word

class NodeType(Enum):
  POSITIVE = 'positive'
  NEGATIVE = 'negative'

class PositiveNode(AtelNode):
  @property
  def key(self):
    return NodeType.POSITIVE.value

  @property
  def opposite(self):
    return NodeType.NEGATIVE.value

  def __repr__(self):
    if self.last:
      return '+ ' + self.word
    else:
      return self.word

class NegativeNode(AtelNode):
  @property
  def key(self):
    return NodeType.NEGATIVE.value

  @property
  def opposite(self):
    return NodeType.POSITIVE.value

  def __repr__(self):
    return '- ' + self.word

if __name__ == '__main__':
  model_location = "/Users/yasyf/Downloads/GoogleNews-vectors-negative300.bin"
  atel = Atel(model_location)
  demo = atel.word('king').minus('male').plus('female').plus('foo').minus('foo')
  print(str(demo.simplify()))
  print(demo.evaluate())
