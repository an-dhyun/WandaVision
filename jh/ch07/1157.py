s = input().upper()
unique = list(set(s))
lst = []
for i in unique:
    lst.append(s.count(i))
if lst.count(max(lst)) > 1:
    print("?")
else:
    max_idx = lst.index(max(lst))
    print(unique[max_idx])