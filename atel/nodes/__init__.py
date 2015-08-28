from enum import Enum

class NodeType(Enum):
  POSITIVE = 'positive'
  NEGATIVE = 'negative'

from atel_node import AtelNode
from positive_node import PositiveNode
from negative_node import NegativeNode
