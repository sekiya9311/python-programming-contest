def get_int(): return int(input())
def get_float(): return float(input())
def get_line(): return input().split()
def get_lines(v): return [get_line() for _ in range(v)]
def get_int_line(): return list(map(int, get_line()))
def get_int_lines(v): return [get_int_line() for _ in range(v)]
def get_float_line(): return list(map(float, get_line()))
def get_float_lines(v): return [get_float_line() for _ in range(v)]
