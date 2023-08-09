import random

letras = ["a", "b", "c", "d", "e"]

premios = [500, 1000, 2000, 3000, 5000, 10000, 15000, 20000, 30000, 50000, 100000, 150000, 300000, 500000, 1000000]

perguntas_faceis = {
  "Quanto é 1+1?": (2, [1, 0, 2, 3]),
  "A afirmativa a seguir está correta: \"O cerrado é o segundo maior bioma da América do Sul.\"": (0, ["Verdadeiro", "Falso"])
  
}

"""perguntas_medias = {
  "Qual o
}"""

def main():
  numero_pergunta = 1

  print("""Bem vindo a Quem Quer Ser Um Cerratense, estas são as regras do jogo:
  1. O jogo consiste de 15 perguntas sobre o cerrado brasileiro, em ordem ascendente de dificuldade.
  2. A cada pergunta, aumenta o seu prêmio.
  3. A cada 5 perguntas, há um checkpoint. Se você errar, ganhará o prêmio do checkpoint anterior.
  4. A cada pergunta, você pode desistir ou continuar, antes de responder. Se desistir, ficará com o prêmio correspondente à pergunta em que está.""")

  while numero_pergunta <= 15:
    if numero_pergunta <= 5:
      pergunta = random.choice(list(perguntas_faceis.items()))
    elif numero_pergunta <= 10:
      pergunta = random.choice(list(perguntas_medias.items()))
    elif numero_pergunta <= 15:
      pergunta = random.choice(list(perguntas_dificeis.items()))
    questao = pergunta[0]
    respostas = pergunta[1][1]
    print(f"""\nPergunta número {numero_pergunta}: 
    {questao}\nAs alternativas são:\n\n""")
    for i, resposta in enumerate(respostas):
      letra = letras[i]
      print(f"\t{letra}. {resposta}\n")
    desistir = input(f"Deseja continuar ou desistir e ganhar R${premios[numero_pergunta - 1]:2f}? (\"c\" para continuar, qualquer outra coisa para desistir)").lower()
    if desistir != "c":
      print(f"Seu prêmio final foi R${premios[numero_pergunta - 1]:2f}. Parabéns!")
      break
    escolha = ""
    while not escolha in letras[:len(respostas)]:
      escolha = input("\n\n Ok, qual alternativa deseja escolher? ").lower()
      print("Alternativa inválida. Tente novamente")
    if not letras.index(escolha) + 1 == pergunta[1][0]:
      if numero_pergunta < 5:
        premio_final = 0
      elif numero_pergunta < 10:
        premio_final = 5000
      else:
        premio_final = 50000
      print(f"Você errou. Seu prêmio final foi R${premio_final:2f}")
      break
    print("Parabéns, você acertou! Vamos à próxima pergunta.")
    numero_pergunta += 1
dnv = input("Deseja jogar novamente? (S/N)").lower()
if dnv == "s":
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  main()
else:
  print("Então sai daqui animal")
  exit()
if __name__ == "__main__":
  main()
