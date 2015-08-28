import collections


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

  def _simplify(self):
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

  def simplify(self):
    return self.copy_chain()._simplify()

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

  def copy(self, last=None):
    return self.__class__(self.root, last, self.word)

  def copy_chain(self):
    if self.last:
      end_of_chain = self.last.copy_chain()
      return self.copy(last=end_of_chain)
    else:
      return self.copy()

  def __str__(self):
    if self.last:
      return '{last} {current}'.format(last=str(self.last), current=repr(self))
    else:
      return repr(self)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.word == other.word


from positive_node import PositiveNode
from negative_node import NegativeNode