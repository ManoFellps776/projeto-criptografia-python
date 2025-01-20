#Banco sem Funcionalidade...
#senha
import getpass
def senha_entrar():
  print('Usuário \nBanco de informações restritas:\nAqui todas as informações são protegidas por uma criptográfica que apenas quem tem acesso ao banco de dados e a chave irá conseguir ler as informações.\nColoque a senha do admin para poder acessar:')
  senha =getpass.getpass('Digite a senha: ')
  if senha == 'senha123':
    print('Parabéns você acertou! ')
  elif senha!='senha123':
    print('Você errou!Tente novamente.')
    senha_entrar()
  return senha
senha_entrar()
#criptografador
def cripto(frase):
  tradutor = ""
  for letra in frase:
    if letra in "Aa":                tradutor = tradutor + "!"
    elif letra in "Bb":              tradutor = tradutor + "@"
    elif letra in "Cc":              tradutor = tradutor + "#"
    elif letra in "Dd":              tradutor = tradutor + "$"
    elif letra in "Ee":              tradutor = tradutor + "%"
    elif letra in "Ff":              tradutor = tradutor + "¨"
    elif letra in "Gg":              tradutor = tradutor + "^"
    elif letra in "Hh":              tradutor = tradutor + "~"
    elif letra in "Ii":              tradutor = tradutor + "+"
    elif letra in "Jj":              tradutor = tradutor + "="
    elif letra in "Kk":              tradutor = tradutor + "-"
    elif letra in "Ll":              tradutor = tradutor + ")"
    elif letra in "Mm":              tradutor = tradutor + "("
    elif letra in "Nn":              tradutor = tradutor + "*"
    elif letra in "Oo":              tradutor = tradutor + "&"
    elif letra in "Pp":              tradutor = tradutor + "6"
    elif letra in "Qq":              tradutor = tradutor + "7"
    elif letra in "Rr":              tradutor = tradutor + "?"
    elif letra in "Ss":              tradutor = tradutor + ";"
    elif letra in "Tt":              tradutor = tradutor + "]"
    elif letra in "Uu":              tradutor = tradutor + "{"
    elif letra in "Vv":              tradutor = tradutor + "`"
    elif letra in "Ww":              tradutor = tradutor + "´"
    elif letra in "Xx":              tradutor = tradutor + ">"
    elif letra in "Yy":              tradutor = tradutor + "."
    elif letra in "Zz":              tradutor = tradutor + "<"
    else:        tradutor= tradutor + letra
  return tradutor
def salvar_cripto():
  frase = input('Digite o texto pra criptografar: ')
  tradutor = cripto(frase)
  print(tradutor)
  arquivo=open('cript.txt','a')
  arquivo.write(cripto(frase)+'\n')
  arquivo.close()
  arquivo=open('texto.txt','a')
  arquivo.write((frase)+'\n')
  arquivo.close()
#descriptografador
def descripto(frase):
  tradutor = ""
  for letra in frase:
    if letra in "!":                tradutor = tradutor + "a"
    elif letra in "@":              tradutor = tradutor + "b"
    elif letra in "#":              tradutor = tradutor + "c"
    elif letra in "$":              tradutor = tradutor + "d"
    elif letra in "%":              tradutor = tradutor + "e"
    elif letra in "¨":              tradutor = tradutor + "f"
    elif letra in "^":              tradutor = tradutor + "g"
    elif letra in "~":              tradutor = tradutor + "h"
    elif letra in "+":              tradutor = tradutor + "i"
    elif letra in "=":              tradutor = tradutor + "j"
    elif letra in "-":              tradutor = tradutor + "k"
    elif letra in ")":              tradutor = tradutor + "l"
    elif letra in "(":              tradutor = tradutor + "m"
    elif letra in "*":              tradutor = tradutor + "n"
    elif letra in "&":              tradutor = tradutor + "o"
    elif letra in "6":              tradutor = tradutor + "p"
    elif letra in "7":              tradutor = tradutor + "q"
    elif letra in "?":              tradutor = tradutor + "r"
    elif letra in ";":              tradutor = tradutor + "s"
    elif letra in "]":              tradutor = tradutor + "t"
    elif letra in "{":              tradutor = tradutor + "u"
    elif letra in "`":              tradutor = tradutor + "v"
    elif letra in "´":              tradutor = tradutor + "w"
    elif letra in ">":              tradutor = tradutor + "x"
    elif letra in ".":              tradutor = tradutor + "y"
    elif letra in "<":              tradutor = tradutor + "z"
    else:        tradutor= tradutor + letra
  return tradutor
def salvar_descripto():
  frase = input('Digite o texto pra descriptografar: ')
  tradutor = descripto(frase)
  print(tradutor)
  arquivo=open('historico.txt','a')
  arquivo.write(descripto(frase)+'\n')
  arquivo.close()
def menu():#Menu
  print('1 - criptografar\n2 - descriptografar\n3 - Sair')
  opcao = input('Digite o número da opção: ')
  return opcao
opcao = menu()
while opcao != '3':
  if opcao=='1':
    salvar_cripto()
  elif opcao=='2':
    salvar_descripto()
  opcao = menu()