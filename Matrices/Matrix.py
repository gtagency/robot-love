basicallyinfinity = 100000000

def dif(a, b, threshold):
	return max(abs(int(a) - int(b)) - threshold, 0) ** 2

#get weight of p1 towards p2
def weight(p1, p2): 
	t = 0
	#0 and 1 aren't used in weights - timestamp + email
	options = {"1st" : 1, "2nd" : 2, "3rd" : 3, "4th" : 4, "5th" : 5, "6+" : 7, "Grad Student" : 12}
	t += dif(options[p1[2]], options[p2[2]], 1)
	#gender and sexual orientation related
	orientations = {"Heterosexual" : {"Male":["Female"], "Female":["Male"], "Other":["Uhhh...?"]}, #TODO: Figure out?
				    "Homosexual":{"Male":["Male"], "Female":["Female"], "Other":["Other"]},
				    "Bisexual":{"Male":["Male", "Female"], "Female":["Male", "Female"], "Other":["Male", "Female", "Other"]},
				    "Pansexual":{"Male":["Male", "Female", "Other"], "Female":["Male", "Female", "Other"], "Other":["Male", "Female", "Other"]}}
	# if the gender of p2 is not in the list of genders p1 is interested in, set it to basically infinity
	if not p2[3] in orientations[p1[4]][p1[3]]:
		t+=basicallyinfinity
	#political affiliation(5, 7, 8) TODO: questions sort of redundant,(should probably only be 2) need to work on
			#        1  2  3   4    5    6    7
	scales = ["NaN", 0, 1, 10, 50, 100, 1000, basicallyinfinity]
	#Ethnicity(6, 33)
	if p1[6] != p2[6]:
		t+=scales[int(p1[32])]
	#Religious affiliation (9 and 10 - feelings about it)
	if p1[9] != p2[9]:
		t+=scales[int(p1[10])]
	#sports
	t+=dif(p1[11],p2[11],1)
	#giving homework answers
	t+=dif(p1[12],p2[12],0)
	#intellectual curiosity
	t+=dif(p1[13],p2[13],0)
	#Money versus peers
	t+=dif(p1[14],p2[14],0)
	#Cigarettes
	t+=dif(p1[15],p2[15],0) * 10
	#Spontaneous
	t+=dif(p1[16],p2[16],0)
	#420
	t+=dif(p1[17],p2[17],0) * 10
	#Child being gay
	t+=dif(p1[18],p2[18],0)
	#Sex
	t+=dif(p1[19],p2[19],0) * 10
	#Difficult conversations
	t+=dif(p1[20],p2[20],0) #TODO: custom filter
	#Music
	t+=dif(p1[21],p2[21],1)
	#Design
	t+=dif(p1[22],p2[22],1)
	#politically incorrect
	t+=dif(p1[23],p2[23],0)
	#emotional vulnerability
	t+=dif(p1[24],p2[24],0)*3
	#do nothing
	t+=dif(p1[25],p2[25],1)
	#thrifty
	t+=dif(p1[26],p2[26],1)
	#outdoorsy
	t+=dif(p1[27],p2[27],1)
	#gender roles
	t+=dif(p1[28],p2[28],0)*10
	#drinks
	t+=dif(p1[29],p2[29],0)*10
	#social activism
	t+=dif(p1[30],p2[30],0)
	#harder drugs
	t+=dif(p1[31],p2[31],0)*10
	#TODO: not all required
	#robomatch in person
	t+=dif(p1[33],p2[33],0)**2
	if p1 == p2:
		t = 1000 * 3**int(p1[33])
	return t
	
input()
people = []
try:
	while True:
		inp = input()
		inp = [i for i in inp.split(",")]
		people.append(inp)
except:
	pass
print(",".join([i[1] for i in people]))
for j in people:
	print(",".join([str(weight(j,i)) for i in people]))
