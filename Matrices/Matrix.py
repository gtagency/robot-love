basicallyinfinity = 100000000
questions = ["timestamp","email","year","gender","orientation","politics","ethnicity","notpolitics","religion","notreligion","soulmate","sports","time","answers","money","smoke","spontaneous","420","childgay","sex", "difficultconversations","music","design","politicallyincorrect","emotionalvulnerability","donothing","outdoorsy","genderroles","drinks","drugs","sameethnicity","inperson"]
qs = {}
for i in range(len(questions)):
	if questions[i] in qs:
		print("Warning: duplicate entry", questions[i])
	qs[questions[i]] = i

def dif(a, b, threshold):
	return max(abs(int(a) - int(b)) - threshold, 0) ** 2

#get weight of p1 towards p2
def weight(p1, p2): 
	t = 0
	#0 and 1 aren't used in weights - timestamp + email
	options = {"1st" : 1, "2nd" : 2, "3rd" : 3, "4th" : 4, "5th" : 5, "6+" : 7, "Grad Student" : 12}
	t += dif(options[p1[qs["year"]]], options[p2[qs["year"]]], 1)
	#gender and sexual orientation related
	orientations = {"Heterosexual" : {"Male":["Female"], "Female":["Male"]},
				    "Homosexual":{"Male":["Male"], "Female":["Female"], "Other":["Other"]},
				    "Bisexual":{"Male":["Male", "Female"], "Female":["Male", "Female"], "Other":["Male", "Female", "Other"]},
				    "Pansexual":{"Male":["Male", "Female", "Other"], "Female":["Male", "Female", "Other"], "Other":["Male", "Female", "Other"]}}
	# if the gender of p2 is not in the list of genders p1 is interested in, set it to basically infinity
	gender = "Other"
	if p1[qs["gender"]] in orientations[p1[qs["orientation"]]]:
		gender = p1[qs["gender"]]
	if ((not p2[qs["gender"]] in orientations[p1[qs["orientation"]]][gender]) and (not "Other" in orientations[p1[qs["orientation"]]][gender])):
		t+=basicallyinfinity
			#        1  2  3   4    5    6    7
	scales = ["NaN", 0, 1, 10, 50, 100, 1000, basicallyinfinity]
	#Political affiliation
	if p2[qs["politics"]] in p1[qs["notpolitics"]]:
		t+=basicallyinfinity
	#Ethnicity(6, 33)
	if p1[qs["ethnicity"]] != p2[qs["ethnicity"]]:
		t+=scales[int(p1[qs["sameethnicity"]])]
	#Religious affiliation (9 and 10 - feelings about it)
	if p2[qs["religion"]] in p1[qs["notreligion"]]:
		t+=basicallyinfinity
	#long term/short term
	t+=dif(p1[qs["soulmate"]],p2[qs["soulmate"]],0)
	#sports
	t+=dif(p1[qs["sports"]],p2[qs["sports"]],1)
	#how much time
	t+=dif(p1[qs["time"]],p2[qs["time"]],0)
	#giving homework answers
	t+=dif(p1[qs["answers"]],p2[qs["answers"]],0)
	#Money versus peers
	t+=dif(p1[qs["money"]],p2[qs["money"]],0)
	#Cigarettes
	t+=dif(p1[qs["smoke"]],p2[qs["smoke"]],0) * 10
	#Spontaneous
	t+=dif(p1[qs["spontaneous"]],p2[qs["spontaneous"]],0)
	#420
	t+=dif(p1[qs["420"]],p2[qs["420"]],0) * 10
	#Child being gay
	t+=dif(p1[qs["childgay"]],p2[qs["childgay"]],0)
	#Sex
	t+=dif(p1[qs["sex"]],p2[qs["sex"]],0) * 10
	#Difficult conversations
	t+=dif(max(p1[qs["difficultconversations"]],p2[qs["difficultconversations"]]),7,1)
	#Music
	t+=dif(p1[qs["music"]],p2[qs["music"]],1)
	#Design
	t+=dif(p1[qs["design"]],p2[qs["design"]],1)
	#politically incorrect
	t+=dif(p1[qs["politicallyincorrect"]],p2[qs["politicallyincorrect"]],0)
	#emotional vulnerability
	t+=dif(p1[qs["emotionalvulnerability"]],p2[qs["emotionalvulnerability"]],0)*3
	#do nothing
	t+=dif(p1[qs["donothing"]],p2[qs["donothing"]],1)
	#outdoorsy
	t+=dif(p1[qs["outdoorsy"]],p2[qs["outdoorsy"]],1)
	#gender roles
	t+=dif(p1[qs["genderroles"]],p2[qs["genderroles"]],0)*10
	#drinks
	t+=dif(p1[qs["drinks"]],p2[qs["drinks"]],0)*10
	#harder drugs
	t+=dif(p1[qs["drugs"]],p2[qs["drugs"]],0)*10
	#robomatch in person
	t+=dif(p1[qs["inperson"]],p2[qs["inperson"]],0)**2
	if p1 == p2:
		t = 1000 * 3**int(p1[qs["inperson"]])
	return t
	
input()
people = []
try:
	while True:
		inp = input()
		inp = [i for i in inp[1:-1].split(",")]
		people.append(inp)
except:
	pass
print(",".join([i[1] for i in people]))
for j in people:
	print(",".join([str(weight(j,i)) for i in people]))
