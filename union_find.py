
class union_find:
  def __init__(self, N):
    self._N = N
    self._uni = [-1 for _ in range(self._N)]
    self._group_count = N
  
  @property
  def N(self): return self._N

  @property
  def group_count(self): return self._group_count

  def group(self, a):
    return -self._uni[self.find(a)]

  def find(self, a):
    if self._uni[a] < 0:
      return a
    else:
      self._uni[a] = self.find(self._uni[a])
      return self._uni[a]

  def same(self, a, b):
    return self.find(a) == self.find(b)

  def unite(self, a, b):
    a = self.find(a)
    b = self.find(b)
    if a == b:
      return False
    if self._uni[a] > self._uni[b]:
      tmp = a
      a = b
      b = tmp
    self._uni[a] += self._uni[b]
    self._uni[b] = a
    self._group_count -= 1
    return True