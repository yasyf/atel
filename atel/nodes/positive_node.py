from . import NodeType
from atel_node import AtelNode

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
