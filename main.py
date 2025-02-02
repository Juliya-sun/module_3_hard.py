data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
  summa = 0
  for i in args:
    if isinstance(i, (int, float)):
      summa += i
    elif isinstance(i, str):
      summa += len(i)
    elif isinstance(i,(list, tuple, set)):
      summa += calculate_structure_sum(*i)
    elif isinstance(i,dict):
      summa += calculate_structure_sum(*i.items())
    elif i in None:
      pass

  return summa

result = calculate_structure_sum(data_structure)

print(result)

