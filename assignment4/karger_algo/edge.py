class Edge:
  def __init__(self, n1, n2):
    self._node1 = n1
    self._node2 = n2

  @property
  def node1(self):
    return self._node1

  @property
  def node2(self):
    return self._node2

  def __eq__(self, other):
    ''' Edges are equal when they have the same endpoints. '''
    if isinstance(other, self.__class__):
      return (
              ((self._node1 == other._node1)
                   and (self._node2 == other._node2))
              or ((self._node1 == other._node2)
                   and (self._node2 == other._node1))
             )
    else:
      return False

  def __hash__(self):
    '''Generate a hash independent of the order of endpoints'''
    return (hash(self._node1) ^ hash(self._node2))
