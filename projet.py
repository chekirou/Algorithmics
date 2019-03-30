import time
from random import randint


#_____________________________________________recherche exhaustive __________________________________
def Recherche_Exhaustive(k, V, S):
	if S<0:
		return 100000
	else:
		if S == 0:
			return 0
		else:
			nbCont = S
			for i in range(0, k):
				x = Recherche_Exhaustive(k, V, S- V[i])
				if ((x+1) < nbCont) :
					nbCont = x+1
			return nbCont
	pass;			

#_____________________________________________programmation Dynamique__________________________________

def algoProgDyn(K, V,S):
	M = [[0 for x in range(K+1)] for y in range(S+1)]
	for i in range(1, S+1):
		M[i][0] = 9999999
		pass;
	for s in range(1, S+1):
		for i in range(1,K+1):
			if s-V[i-1] < 0:
				
				M[s][i] = M[s][i-1]
			else:
				if M[s][i-1] <= M[s-V[i-1]][i]+1:
					M[s][i] = M[s][i-1]
				else:
					
					M[s][i] = M[s-V[i-1]][i]+1
	#dans le cas ou vous voudriez tester l'algo retouer enlever le # du commentaire suivant et ajouter ", t" au return
	#t = algorithme_retour(S,K,V,M)
	
	return M[S][K]

def algorithme_retour(S, K, V, M):
	t = [0 for x in range(K)]
	tot,p,q=S,S,K
	while tot > 0:
		if p-V[q-1] >=0 and M[p][q] == M[p-V[q-1]][q]+1:
			tot -= V[q-1]
			p = p - V[q-1]
			t[q-1] += 1;
		else:
			q = q-1
	return t


#_____________________________________________GLOUTON_____________________________________________________
def AlgoGlouton(K,V,S):
	tot, nb= S,0
	while tot != 0:
		i=0
		while i< K and tot-V[i]>=0:
			i +=1
		while tot -V[i-1] >=0:
			tot -= V[i-1]
			nb += 1
	return nb
	
def CapaciteGenerateur(Pmax, K):
#pmax doit etre superieur ou egale a K
	tab= [1]
	for i in range(1,K):
		d= randint(2, Pmax)
		
		while d in tab:
			
			d= randint(2, Pmax)
		tab.append(d)
	return sorted(tab)
	
def TestGloutonCompatible(k,V):
	if(k >=3):
		for S in range(V[2]+2, V[k-2]+V[k-1]):
			for j in range(0,k):
				if(V[j] < S) and (AlgoGlouton(k, V, S) > 1+ AlgoGlouton(k, V, S-V[j])):
					return False
	return True

	
#_________________________________________________________________________________________________________
#                                                 Partie des tests
#_________________________________________________Ratios_________________________________________

'''V = CapaciteGenerateur(10, 6)

somme= [0.]*99;
moyenne= [0.]*99
s =0.
f=5
for i in range(1, 100):
	s=0.
	print(i)
	for pmax in range(i, f*i):
		V = CapaciteGenerateur(pmax, i)
		s+= 1.
		if(TestGloutonCompatible(i,V)):
			somme[i-1] += 1.
	moyenne[i-1] = somme[i-1]/s

print moyenne
print(" le ratio Gcompatible/tout : " + str(sum(moyenne)/len(moyenne)))
'''
#---------------------------------------------------------------------------------------------------------
file = open("projetd=2.txt", "r")
l = file.readlines()
#on extrait les informations du fichier specifié
S,k,V = (int(l[0]),int(l[1]), list(map(int, l[2].split(" "))))
file.close()
#_______________________________tests des algorithmes_____________________________________________________

print(Recherche_Exhaustive(k, V, S))
print(algoProgDyn(k, V, S))
print(AlgoGlouton(k, V,S))

#----------------------------------tests statistiques------------------------------------------------------



'''fichierEcart = open("fichierEcart.txt" ,"w")
fichiermoyennes = open("fichiermoyenne.txt" ,"w")
pireCas = open("fichierpireCas.txt" ,"w")
V = CapaciteGenerateur(10, 6)

somme= 0;
ecart =[]
s =0.
f=2
pirecas = []
for i in range(1, 100):
	pmax = f*i
	s=0.
	print(i)
	V = CapaciteGenerateur(pmax, i)
	s+= 1.
	if not (TestGloutonCompatible(i,V)):
		pc = 0
		sommeEcart=0
		for x in range(pmax, f*pmax):
			
			diff = AlgoGlouton(i, V, x) - algoProgDyn(i, V, x)
			sommeEcart+= diff
			if pc < diff : 
				pc = diff
		ecart.append(float(sommeEcart)/float((f-1)*pmax))
		pirecas.append(pc)
	else:
		somme += 1.
		
moyenne = float(somme)/s
fichiermoyennes.write("moyenne pour k variant de 1 a 10 f= 2 pmax = 2*k" + str(moyenne))
ecartMoyenMoyen = sum(ecart)/len(ecart)
for i in range(0, len(ecart)):
	fichierEcart.write(str(i) + " " + str(ecart[i])+"\r\n")
for i in range(0, len(pirecas)):
	pireCas.write(str(i) + " " + str(pirecas[i])+"\r\n")
print("ecart " + str(ecart))
print("pire cas : " + str(pc))
'''
#print moyenne




#--------------------------------------------tests pour la complexité--------------------------------------------


#------------------------------------------------------------------------------------------------------
#                                         Recherche Exhaustive
#-----------------------------------------------------------------------------------------------------
#test1 est le fichier destination des valeurs pour generer les graphes
#on le change selon le test
#===========================S variant
'''while (temps < 60):
	s+=1
	print("s" + str(s))
	t1 = time.clock()
	resultat = Recherche_Exhaustive(k, V, s)
	t2= time.clock()
	temps = t2-t1
	print("recherche exhaustive" , resultat, temps)
	test1.write(str(s)+ " "+ str(temps)+ "\r\n")
test1.close();'''
#============================ k variant

'''while (temps < 60 and k< 30):
	V = [d**(i-1) for i in range(1,k+1)]
	#print(V)
	print("k" + str(k))
	t1 = time.clock()
	resultat = Recherche_Exhaustive(k, V, s)
	t2= time.clock()
	temps = t2-t1
	print("recherche exhaustive" , resultat, temps)
	test1.write(str(k)+ " "+ str(temps)+ "\r\n")
	k+=1
test1.close();'''
#print("recherche exhaustive" , Recherche_Exhaustive(2, [1,2], 35), temps)
#--------------------------------------------------------------------------------------------------------
#                                                       prog dynamique
#--------------------------------------------------------------------------------------------------------
# test de algo Prog dyn pour K fixe et S variant le d change selon le ficher
''''while (s < 5000):
	s+=1
	print("s " + str(s))
	t1 = time.clock()
	resultat = algoProgDyn(k, V,s)
	t2= time.clock()
	temps = t2-t1
	print("algo programmation dynamique" , resultat, temps)
	test1.write(str(s)+ " "+ str(temps)+ "\r\n")
test1.close()
print("programmation dynamique " , algoProgDyn(k, V,S))
'''
#=============================================k variant 
'''while (k< 20):
	V = [d**(i-1) for i in range(1,k+1)]
	#print(V)
	print("k" +TestGloutonCompatible
 str(k))
	t1 = time.clock()
	resultat = algoProgDyn(k, V, s)
	t2= time.clock()
	temps = t2-t1
	print("prog dyn" , resultat, temps)
	test1.write(str(k)+ " "+ str(temps)+ "\r\n")
	k+=1
test1.close()'''
#--------------------------------------------------------------------------------------------------------
#                                                     algo Glouton
#--------------------------------------------------------------------------------------------------------
#==================================================k variant

'''while (k< 30):
	V = [d**(i-1) for i in range(1,k+1)]
	#print(V)
	print("k" + str(k))
	t1 = time.clock()
	resultat = AlgoGlouton(k, V, s)
	t2= time.clock()
	temps = t2-t1
	print("glouton" , resultat, temps)
	test1.write(str(k)+ " "+ str(temps)+ "\r\n")
	k+=1
test1.close()'''
#================================================S variant
'''s=0
while (s < 50000):
	s+=1
	print("s " + str(s))
	t1 = time.clock()
	resultat = AlgoGlouton(k, V,s)
	t2= time.clock()
	temps = t2-t1
	print("algo glouton" , resultat, temps)
	test1.write(str(s)+ " "+ str(temps)+ "\r\n")
test1.close()
#print("algo Glouton " + str(AlgoGlouton(k, V,S)))
				'''
