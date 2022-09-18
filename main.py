import random
def chackno(romno):
	farnum = []
	zawnum = []
	nomsat = 0
	for i in romno:
		if (nomsat%2 == 0):
			zawnum.append(int(i))
		else :
			farnum.append(int(i))
		nomsat += 1
	mojmo3far = 0
	for i in farnum :
		mojmo3far = mojmo3far + i
	mojmo3zaw = 0
	for i in zawnum:
		i = i*2
		if i>10 :
			i = i - 9
		mojmo3zaw = mojmo3zaw + i
	majmo3lkoli = mojmo3far + mojmo3zaw
	if majmo3lkoli%10==0:
		return True
	else :
		return False
cards = int(input("how card you want : "))
crd = 0
cardsl = []
print("start ...")
while crd<cards :
	lis = ['0','1','2','3','4','5','6','7','8','9']
	nm = ''
	t = 1
	while t <= 16:
		nm = nm + random.choice(lis)
		t +=1

	if len(nm) == 16 :
		if chackno(nm):
			if nm in cardsl :
				pass
			else :
				cardsl.append(nm)
				print("This is a valid card : "  ,nm)
				crd += 1
		else:
			pass
	else :
		print("Error card num mast be 16 number \ntry agen.")
