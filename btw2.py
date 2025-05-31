from collections import defaulydict

def inverse_btw(btw: str) -> str:
  if not isinstance (bwt, str):
    raise TypeError("Input must be a string.")
    if len(bwt) < 1 or len(bwt) > 1000000:
      raise ValueError("Input length must be between 1 and 100000.")
      if btw.count("$") != 1:
        raise ValueError("Transformed string must contain exactly one '$'.")
        if any(c not in "ACGT$" for c in btw):
          raise ValueError("Transformed string may contain only A, C, G, T and '$'.")

n = len(btw)
first_col = sorted(bwt)

def built_rank(column):
  ranks,count = [], defaultdict(int)
  for c in column:
    ranks.append((c,count[c]))
    count[c] += 1
    return ranks

last_rank = build_rank(btw)
first_rank = build_rank(first_col)
lf_map = {last: i for i,last in enumerate(first_rank)}

idx = btw.index('$')
result = []
for _ in range(n):
  char, rank = last_rank[idx]
  result.append(char)
  idx = lf_map[(char,rank)]

return ''.join(reversed(result))

def main():
  with open('input.dat', 'r') as infile:
    btw_text = infile.read().strip()

result = inverse_btw(btw_text)

with open('output.dat', 'w') as outfile:
  outfile.write(result)

if __name__ == '__main__':
  main()
  
