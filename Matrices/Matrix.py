def weight(p1, p2): 
	return 0
input()
people = []
try:
	while True:
		inp = input()
		inp = [i[1:-1] for i in inp.split(",")]
		people.append(inp)
		inp = input()
except:
	pass
print(",".join([i[1] for i in people]))
for j in people:
	print(",".join([str(weight(j,i)) for i in people]))
