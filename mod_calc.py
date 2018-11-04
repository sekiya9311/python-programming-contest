
class mod_calc:
  def __init__(self, N, MOD):
    self._N = N
    self._MOD = MOD
    self._fact = [-1 for _ in range(self._N)]
    self._inv_fact = [-1 for _ in range(self._N)]
    self._fact[0] = 1
    self._inv_fact[0] = 1
  
  @property
  def N(self): return self._N

  @property
  def MOD(self): return self._MOD

  def add(self, a, b): return (a + b) % self.MOD

  def mul(self, a, b): return (a * b) % self.MOD

  def pow_mod(self, a, p):
    if p == 0:
      return 1
    elif p % 2 == 1:
      return a * self.pow_mod(a, p - 1) % self.MOD
    else:
      t = self.pow_mod(a, p // 2) % self.MOD
      return t * t % self.MOD

  def inv(self, v):
    return self.pow_mod(v, self.MOD - 2)

  def fact(self, v):
    if self._fact[v] == -1:
      self._fact[v] = v * self.fact(v - 1) % self.MOD
    return self._fact[v]

  def inv_fact(self, v):
    if self._inv_fact[v] == -1:
      self._inv_fact[v] = self.inv(self.fact(v))
    return self._inv_fact[v]

  def perm(self, n, r):
    return self.fact(n) * self.inv_fact(n - r) % self.MOD

  def comb(self, n, r):
    return ((self.fact(n) * self.inv_fact(r)) % self.MOD * self.inv_fact(n - r)) % self.MOD
