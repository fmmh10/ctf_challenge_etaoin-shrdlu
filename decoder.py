#Welcome!
#Wfldone!

#So CTFbvk/ This is just, 

cypher = "Wfldone!tp DTGcvl/ Uhjs!it kutt!spmf qaedjnh.!Ig zov qaz btueotjoo,!tiit js!vvloesaclf uo!fserufndy!aoamytit.Jf!ypu!cbn!rfae uhjs- teod!tie!:taotb:!enoki!at b qrjvbtf netsbgf ADjohopn!Djsdosd/ Dhfess/"




a='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

i=0
final = ''

while len(cypher) > i:
	if cypher[i] == "!":
		final = final + "!"
	
	elif cypher[i] == ".":
		final = final + "."
		
	elif cypher[i] == ",":
		final = final + ","
	
	elif cypher[i] == ":":
		final = final + ":"
	
	elif cypher[i] == "-":
		final = final + "-"
	
	elif cypher[i] == "/":
		final = final + "/"

	elif cypher[i] == " ":
		final = final + " "


	elif i==0:
		final = final + cypher[i] 
	
	elif i%2 != 0:
		final = final + a[a.find(cypher[i])-1]

	elif i%2 == 0:
		final = final + a[a.find(cypher[i])]


	i+=1

print final