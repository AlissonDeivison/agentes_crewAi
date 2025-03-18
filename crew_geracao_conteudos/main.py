from crews.crewPrincipal import crew

tema = input("Digite o tema que deseja pesquisar: ")
conteudo = input("Digite o formato do conteúdo: ")

resultado = crew.kickoff(inputs={"tema": tema, "conteudo": conteudo})

print(resultado)