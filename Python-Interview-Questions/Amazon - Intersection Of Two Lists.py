def intersection(a, b):
  return list(set(a).intersection(set(b)))


def intersection(a, b):
  intersection_list = []
  for value in a:
    if value in b:
      intersection_list.append(value)
  return intersection_list    


def intersection(a, b):
  set_a = set(a)
  set_b = set(b)
  if len(set_a) < len(set_b):
	  return [x for x in set_a if x in set_b]
  else:
    return [x for x in set_b if x in set_a]
