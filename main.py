import random

letras = ["a", "b", "c", "d", "e"]

premios = [500, 1000, 2000, 3000, 5000, 10000, 15000, 20000, 30000, 50000, 100000, 150000, 300000, 500000, 1000000]

perguntas = {
  "faceis": {
    "A afirmativa a seguir está correta: \"O cerrado é o segundo maior bioma da América do Sul.\"": (1, ["Verdadeiro", "Falso"]),
    "Qual o bioma encontrado ao norte do cerrado?": (4, ["Pantanal", "Pampa", "Mata Atlântica", "Amazônia"]),
    "Qual é a estação do ano mais característica do Cerrado?": (1, ["Verão", "Inverno", "Primavera", "Outono"]),
    "Qual das seguintes opções representa uma grande ameaça ao Cerrado?": (3, ["Tsunamis", "Vulcões", "Desmatamento", "Furacões"]),
    "Qual o principal bioma vizinho do Cerrado?": (3, ["Amazônia", "Pantanal", "Caatinga", "Pampa"]),
    "O cerrado é conhecido por ser uma:": (2, ["Floresta Densa", "Savana arborizada", "Floresta tropical úmida", "Região polar"]),
    "A vegetação do cerrado é mais adaptada a qual clima?": (2, ["Tropical úmido", "Tropical seco", "Subtropical úmido", "Temperado"]),
    "Qual é o processo natural que promove a renovação da vegetação do cerrado?": (4, ["Inundações anuais", "Polinização por abelhas", "Erosão do solo", "Incêndios frequentes"]),
    "Quais são as principais atividades econômicas desenvolvidas na região do cerrado?": (2, ["Pesca e turismo", "Agricultura e pecuária", "Mineração e construção civil", "Comércio e indústria"]), 
    "Qual é o clima predominante do Cerrado?": (3, ["tropical", "semiárido", "tropical semiúmido", "tropical litorânea"]),
    "Em relação a fauna, o cerrado abriga uma diversidade grande de:": (1, ["Répteis", "Mamíferos marinhos", "Anfíbios", "Aves migratórias"]),
    "São características do cerrado típico, exceto:": (1, ["Vegetação densa", "Troncos retorcidos", "Raízes profundas", "Vegetação esparsa"]),
    "A vegetação do Cerrado que ocorre em zonas rochosas, de altitudes mais elevadas": (4, ["Campo sujo","Cerradão", "Mata seca", "Cerrado Rupestre"]),

  },

  "medias": {
    "Qual é a porcentagem equivalente à área do bioma cerrado no Brasil?": (3, ["32%", "17%", "22%", "25%"]),
    "Qual é o tipo de solo encontrado no Cerrado brasileiro?": (3, ["Arenoso", "Calcário", "Argiloso", "Orgânico"]), 
    "A respeito das características do Cerrado, marque a alternativa incorreta.": (4, ["O Cerrado apresenta predominantemente formações de savana", "O Cerrado é o segundo maior bioma da América do Sul", "O Cerrado apresenta clima tropical quente subúmido", "O Cerrado possui quatro estações bem definidas"]),
    "A vegetação de Cerrado ocupa uma grande extensão territorial do Brasil. Qual dos estados não possui vegetação do Cerrado": (4, ["Mato Grosso do Sul", "Minas Gerais", "Goiás", "Rio Grande do Sul"]),
    "O solo do Cerrado é bastante ácido. Desse modo, a prática de atividades agrícolas em larga escala nesse bioma é possível em razão de:": (2, ["Canalização dos rios", "Realização da calagem", "Impermeabilização do solo", "Proibição dos agrotóxicos"]), 
    "Qual a importância do Cerrado para o ciclo da água no Brasil?": (2, ["Funciona como um grande reservatório de água subterrânea", "Regula o ciclo da água evitando enchentes e secas extremas", "Contribui para o desenvolvimento de plantas", "Não possui relevância para o ciclo"]),
    "As veredas são uma fitofisionomia vegetacional encontrada no Cerrado marcada pela": (1, ["Presença de nascentes", "Ocorrências de desertos", "Vegetação de altitude", "Existência de gramíneas"]),
    "Como é chamada a vegetação de grande porte do Cerrado que é encontrada ao longo dos principais cursos de água desse bioma?": (3, ["Mata seca", "Campo limpo", "Mata de galeria", "Campo sujo"]),
    "Uma atividade econômica específica se adaptou às características naturais do Cerrado e foi responsável por esse povoamento no século XX. A atividade econômica em questão é:": (4, ["indústria de bens duráveis", "indústria extrativa", "agricultura de subsistência", "pecuária extensiva de bovinos"]),
    "O clima predominante do Cerrado é o tropical semiúmido. Marque a alternativa que indica corretamente as características principais desse tipo climático:": (4, ["Temperaturas médias superiores a 26 ºC e índices pluviométricos elevados ao longo do ano.", "Quatro estações bem definidas e chuvas regulares e bem distribuídas ao longo do ano.", "Verões amenos e invernos rigorosos com chuvas regulares e bem distribuídas ao longo do ano.", "Temperaturas elevadas ao longo do ano, com duas estações bem marcadas em relação às chuvas, configurando o verão chuvoso e inverno seco."]),
    "O Cerrado brasileiro se destaca como uma das vegetações mais devastadas do país. O desmatamento se tornou evidente e intenso no bioma em função da expansão:": (3, ["industrial", "urbana", "agropecuária", "da mineração"]),

  },

  "dificeis": {
    "Qual é, aproximadamente, a área, em km², do cerrado?": (1, ["200 milhões", "245 milhões", "190 milhões", "130 milhões"]),
    "No Cerrado são encontrados onze tipos de vegetação, entretanto elas são distribuídas principalmente em três tipos de formações que são:": (4, ["Formações Campestres, Formações Arbustivas e Formações Arbóreas", "Formações Savânicas, Formações Campestres e Formações Vulcânicas",  "Formações Florestais, Formações Savânicas e Formações Urbanas", "Formações Florestais, Formações Campestres e Formações Savânicas"]),
    "Cerca de quantas espécies nativas são encontradas no cerrado?": (3, ["10.925", "11.435", "11.627", "12.005"]),
    "Quantas espécies de plantas já foram identificadas no Cerrado?": (3, ["Cerca de 1000", "Cerca de 5000", "Cerca de 10000", "Cerca de 20000"]),
    "Todo cerrado é uma savana.": (2, ["Verdadeiro", "Falso"]),
    "Qual o nome da ave símbolo do cerrado?": (4, ["A. Tucano", "B. Arara-Azul", "C.Uirapuru" , "D.Ceriema"]),
    "(PUC) Uma das mais recentes preocupações acerca dos danos causados pelas mudanças climáticas recaiu sobre o risco do bioma Cerrado se transformar em um imenso deserto. Entretanto, considerando os padrões de circulação atmosférica, o Cerrado distribui-se entre zonas de alta e baixa pressão, o que se conhece como Célula de Hadley, as quais condicionam a ação de diversas massas de ar, em especial a Equatorial Continental, responsável por grande parte das precipitações no território brasileiro. Acerca da área de ocorrência de desertos, bem como dos fatores de formação, assinale a única alternativa correta:": (1, ["As regiões desérticas tendem a ocorrer em zonas de alta pressão, geralmente marcadas pelo movimento descendente do ar entre duas células de circulação atmosférica.", "O Oriente Médio, mesmo estando sob uma zona de alta pressão, tem a ocorrência de áreas desérticas atenuadas graças à existência de diversos mares, como o Mediterrâneo.", "A exemplo do Oriente Médio, a porção norte do México tem a formação de desertos inibida graças à atuação da umidade advinda das águas do Oceano Pacífico.", "Do efeito proporcionado pela umidade dos oceanos, ambientes como o noroeste da Argentina e o oeste da ilha de Madagascar estão imunes à formação de desertos."]),
    "(UFU) O Inhotim é o maior museu de arte contemporânea do mundo inserido em um jardim botânico. Como está localizado no município de Brumadinho, perto de Belo Horizonte (MG), os visitantes podem observar centenas de espécies vegetais nativas do bioma Cerrado, além de muitas plantas exóticas.\nSobre espécies de vegetais nativas e exóticas, é correto afirmar que:": (2, ["São nativas as espécies vegetais que povoam naturalmente um dado bioma. No caso do Cerrado, são exemplos de espécies vegetais nativas o eucalipto e a araucária. São consideradas exóticas as espécies vegetais que, sendo naturais de outros locais, são introduzidas em um dado bioma pela ação humana. No Brasil pode-se citar como exemplo de plantas exóticas, a bananeira e a cana-de-açúcar.", "São nativas as espécies vegetais que povoam naturalmente um dado bioma. No caso do Cerrado, são exemplos de espécies vegetais nativas o pequizeiro e o ipê amarelo. São consideradas exóticas as espécies vegetais que, sendo nativas de outros locais, são introduzidas pela ação humana em um dado bioma. No Brasil, são exemplos de plantas exóticas as palmeiras australianas e as orquídeas africanas.", "São nativas as espécies vegetais que povoam naturalmente um dado bioma, tendo sido plantadas pelo homem. No caso do Cerrado, são exemplos de espécies vegetais nativas o eucalipto e a araucária. No Brasil, são consideradas exóticas as espécies vegetais utilizadas comercialmente, como a rosa e a bromélia.", "São nativas as espécies vegetais que povoam naturalmente um dado bioma ou que foram introduzidas pela ação humana. No caso do Cerrado, são exemplos de espécies vegetais nativas o pequizeiro e o ipê amarelo. No Brasil, são consideradas exóticas as espécies vegetais utilizadas comercialmente, como a rosa e a bromélia, as palmeiras australianas e as orquídeas africanas."]),
    "(FATEC) Quem já viajou pelo Brasil, certamente atravessou extensos chapadões, cobertos por uma vegetação de pequenas árvores retorcidas, dispersas em meio a um tapete de gramíneas. Durante os meses quentes de verão, quando as chuvas se concentram e os dias são mais longos, tudo ali é muito verde. No inverno, ao contrário, o capim amarelece e seca; quase todas as árvores e arbustos, por sua vez, trocam a folhagem senescente por outra totalmente nova. Mas não o fazem todos os indivíduos a um só tempo. Enquanto alguns ainda mantém suas folhas verdes, outros já as apresentam amarelas ou pardacentas, e outros já se despiram totalmente delas.\nSobre esse bioma pode-se afirmar que apresenta ainda: \n\tI. Muitas variedades de árvores com casca grossa lembrando a cortiça, devido ao excesso de nutrientes do solo.\n\tII. Muitas plantas com raízes longas, que permitem a absorção da água em lençóis freáticos muito distantes da superfície.\n\tIII. Plantas com folhas modificadas em espinhos, caules que armazenam água e cutícula altamente permeável.\n\tIV. Muitas trepadeiras e epífitas, ausência de samambaias e avencas, muitas espécies de anfíbios e animais invertebrados.\n\nEstá correto o contido em:\n": (3, ["II, apenas.", "III e IV, apenas.", "IV e V, apenas.", "I, II e IV, apenas.", "I, II, III e V."]),
    "(Universidade de Passo Fundo) É impossível saber ao certo quantas espécies já foram extintas nos 41% do Cerrado que não existe mais. Pesquisadores da Conservação Internacional (CI) estimam que 13% das espécies de vertebrados do bioma já tenham sido exterminados pela ocupação do homem, antes mesmo de serem descobertos. Não há também como saber quantas plantas foram soterradas pelo avanço da monocultura de grão e bois.\nO bioma Cerrado caracteriza-se por apresentar:": (5, ["Uma vegetação com mecanismos de proteção contra a perda de água, como as cactáceas", "Campos limpos com vegetação herbácea, suporte para a criação de gado e sazonalidade climática em quatro estações", "Plantas típicas do brejo, com imensas planícies de inundação e a maior diversidade de mamíferos e peixes de todos os biomas brasileiros", "Árvores que perdem suas flores na época da seca, que é uma estação prolongada, com temperaturas elevadas propícias para a expansão da vitivinicultura", "Plantas com adaptação para enfrentar o fogo, como cascas espessas ou caules subterrâneos e clima quente"]),
    "(UEG) A taxa de desaparecimento de certos tipos de espécies, particularmente aquelas mais vulneráveis à caça, à poluição e à destruição de habitats, tem aumentado significativamente nos diferentes biomas brasileiros. O estado de Goiás possui como bioma o Cerrado, considerado um complexo mosaico vegetacional com altas potencialidades. A perda de espécies no Cerrado está relacionada principalmente à:": (1, ["Sobre-exploração e à introdução de espécies não nativas, especialmente de predadores, competidores e patógenos no bioma.", "Introdução acelerada de uma agricultura mecanizada e favorável às condições locais para validar as políticas do agronegócio como benefício à sustentabilidade.", "Ausência de políticas adequadas ao manejo sustentável das espécies, visto que o Cerrado é considerado legalmente um patrimônio natural brasileiro como a Amazônia.", "Manutenção de áreas de proteção ambiental em propriedades particulares, uma vez que o Cerrado naturalmente favorece a preservação de determinadas espécies."])

  },
}
def main():
  numero_pergunta = 1

  print("""Bem vindo a Quem Quer Ser Um Cerratense, estas são as regras do jogo:
  1. O jogo consiste de 15 perguntas sobre o cerrado brasileiro, em ordem ascendente de dificuldade.
  2. A cada pergunta, aumenta o seu prêmio.
  3. A cada 5 perguntas, há um checkpoint. Se você errar, ganhará o prêmio do checkpoint anterior.
  4. A cada pergunta, você pode desistir ou continuar, antes de responder. Se desistir, ficará com o prêmio correspondente à pergunta em que está.""")

  while numero_pergunta <= 15:
    if numero_pergunta <= 5:
      dificuldade = "faceis"    
    elif numero_pergunta <= 10:
      dificuldade = "medias"
    elif numero_pergunta <= 15:
      dificuldade = "dificeis"
    pergunta = random.choice(list(perguntas[dificuldade].items()))

    
    questao = pergunta[0]
    respostas = pergunta[1][1]
    print(f"""\nPergunta número {numero_pergunta}: 
    {questao}\nAs alternativas são:\n""")
    for i, resposta in enumerate(respostas):
      letra = letras[i]
      print(f"\t{letra}. {resposta}\n")
    desistir = input(f"Deseja continuar ou desistir e ganhar R${premios[numero_pergunta - 1]:2f}? (\"c\" para continuar, qualquer outra coisa para desistir)").lower()
    if desistir != "c":
      print(f"Seu prêmio final foi R${premios[numero_pergunta - 1]:2f}. Parabéns!")
      return
    escolha = ""
    while not escolha in letras[:len(respostas)]:
      escolha = input("\n\nOk, qual alternativa deseja escolher? ").lower()
      print("Alternativa inválida. Tente novamente")
      break
    if not letras.index(escolha) + 1 == pergunta[1][0]:
      certa = pergunta[1][1][pergunta[1][0] - 1]
      letra = letras[pergunta[1][0] - 1]
      if numero_pergunta < 5:
        premio_final = 0
      elif numero_pergunta < 10:
        premio_final = 5000
      else:
        premio_final = 50000
      print(f"Você errou. A resposta certa era: \n\n\t{letra}. {certa}\n\nSeu prêmio final foi R${premio_final:2f}")
      break
    print("Parabéns, você acertou! Vamos à próxima pergunta.")
    perguntas[dificuldade][questao]
    numero_pergunta += 1
main()
dnv = input("Deseja jogar novamente? (S/N)").lower()
if dnv == "s":
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  main()
else:
  print("Então sai daqui animal")
  exit()
