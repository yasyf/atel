from . import NodeType
from atel_node import AtelNode


class NegativeNode(AtelNode):
  @property
  def key(self):
    return NodeType.NEGATIVE.value

  @property
  def opposite(self):
    return NodeType.POSITIVE.value

  def __repr__(self):
    return '- ' + self.word
