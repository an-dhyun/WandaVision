word = input()
func = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in func:
    word = word.replace(i, "a")
print(len(word))