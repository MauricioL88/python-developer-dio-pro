A = input().lower()
B = input().lower()
C = input().lower()

if A == 'vertebrado' and B == 'ave' and C == 'carnivoro':
  resposta = 'aguia'
elif A == 'vertebrado' and B == 'ave' and C == 'onivoro':
  resposta = 'pomba'
elif A == 'vertebrado' and B == 'mamifero' and C == 'onivoro':
  resposta = 'homem'
elif A == 'vertebrado' and B == 'mamifero' and C == 'herbivoro':
  resposta = 'vaca'
elif A == 'invertebrado' and B == 'inseto' and C == 'hematofago':
  resposta = 'pulga'
elif A == 'invertebrado' and B == 'inseto' and C == 'herbivoro':
  resposta = 'lagarta'
elif A == 'invertebrado' and B == 'anelideo' and C == 'hematofago':
  resposta = 'sanguessuga'
elif A == 'invertebrado' and B == 'anelideo' and C == 'onivoro':
  resposta = 'minhoca'

print(resposta)
