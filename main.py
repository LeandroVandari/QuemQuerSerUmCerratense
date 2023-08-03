import random

perguntas_faceis = {
  "Quanto é 1+1?": (2, [1, 0, 2, 3])
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
    print(f"""\nPergunta número {numero_pergunta}: 
    {questao}\nAs alternativas são:\n""")
    
if __name__ == "__main__":
  main()
