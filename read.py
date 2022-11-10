import os
import pickle
from Teste02 import pessoa

p = []

# modos de abertura
# Ler ("r")
# Anexar ("a")
# Escrever ("w")
# Criar ("x")

#Modo de texto ("t")
#Modo binário ("b")

file_txt =  open("banana.txt", 'w')
file_txt.write('fruta; 001; qualquer\n')
file_txt.close()

file_txt =  open("banana.txt", 'r')
print(file_txt.readlines())
file_txt.close()

file_txt =  open("banana.txt", 'a')
file_txt.write("outra fruta; 002; outro qualquer")
file_txt.close()

file_txt =  open("banana.txt", 'r')
print(file_txt.readlines())
file_txt.close()

os.remove("banana.txt")


p.append(pessoa.Pessoa("321654987", "Marlon"))
p.append(pessoa.Pessoa("165465", "Pedro"))
p.append(pessoa.Pessoa("634989", "Paulo"))


file_bn = open("pessoas.pkl", 'wb')
pickle.dump(p, file_bn)
file_bn.close()

file_bn = open("pessoas.pkl", 'rb')
p = pickle.load(file_bn)

print(p[0].mostraDados())
print(p[1].mostraDados())
print(p[2].mostraDados())

for dados in p:
    print(dados.nome)