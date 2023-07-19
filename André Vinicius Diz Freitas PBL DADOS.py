#/*******************************************************************************
#Autor: André Vinícius Diz Freitas
#Componente Curricular: Algoritmos e progamação I
#Concluido em: 04/04/2023
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/#
#Variaveis em lista e acumuladora do total
total_diario = [0] * 7
total_semanal = 0

# variáveis acumuladoras para armazenar os valores totais diários e semanais de cada aplicativo
chrome_diario = [0] * 7
facebook_diario = [0] * 7
instagram_diario = [0] * 7
whatsapp_diario = [0] * 7
outros_diario = [0] * 7

chrome_semanal = 0
facebook_semanal = 0
instagram_semanal = 0
whatsapp_semanal = 0
outros_semanal = 0

#Cores para uma melhor vizualização de erros e do relátorio
reseta_cor = "\033[0m" #Voltar para o branco
vermelho = "\033[1;31;40m"
verde = "\033[1;32;40m"
amarelo = "\033[1;33;40m"
azul = "\033[1;34;40m"
ciano = "\033[1;36;40m"
roxo = "\033[1;49;95m"

#Agora o Menu
menu = ('''
        MENU:
APLICATIVOS = Chrome (1), Facebook(2), Instagram(3)
              Whatsapp(4) e Outros aplicativos (5) 

DIAS DA SEMANA: Segunda(1), Terça(2), Quarta(3), Quinta(4)
                     Sexta(5), Sábado(6), Domingo(7)

DADOS: Quantos dados você usou em cada aplicativo?
        ''')
print(ciano + menu + reseta_cor)

continuar = True
while continuar:
    # entrada de dados do usuário: código do aplicativo, dia da semana e dados usados em bytes
    while True:
        #try e except para o tratamento de erro no uso de letras no codigo
        try:
            codigo = int(input("Digite o código do aplicativo: "))
            if 1 <= codigo <= 5:
                break
            else:
                print(vermelho + 'Código inválido, favor digite de 1 a 5' + reseta_cor)
        except ValueError:
            print(vermelho + 'Entrada inválida, favor digitar um número inteiro de 1 a 5' + reseta_cor)

    while True:
        try:
            dia = int(input("Digite o dia da semana: "))
            if 1 <= dia <= 7:
                break
            else:
                print(vermelho + 'Dia inválido, favor digite um número de 1 a 7' + reseta_cor)
        except ValueError:
            print(vermelho + 'Entrada inválida, favor digite um número de 1 a 7' + reseta_cor)
    while True:
        try:
            dados = int(input("Digite a quantidade de dados usados em bytes: "))
            if dados >= 0:
                break
            else:
                print(vermelho + 'Dados inválidos, favor digitar os dados corretos' + reseta_cor)
                continue
        except ValueError:
            print(vermelho + 'Entrada inválida, favor digitar os dados corretos' + reseta_cor)

    # atualização das variáveis acumuladoras correspondentes ao aplicativo e dia da semana
    if codigo == 1:
        chrome_diario[dia-1] += dados
        chrome_semanal += dados
    elif codigo == 2:
        facebook_diario[dia-1] += dados
        facebook_semanal += dados
    elif codigo == 3:
        instagram_diario[dia-1] += dados
        instagram_semanal += dados
    elif codigo == 4:
        whatsapp_diario[dia-1] += dados
        whatsapp_semanal += dados
    elif codigo == 5:
        outros_diario[dia-1] += dados
        outros_semanal += dados

    total_diario[dia-1] += dados
    total_semanal += dados

    #Caso seja dia 7, o progama irá avisar que o relátorio está pronto e é o ultimo dia
    while dia == 7:
        dia7 = input('O seu relátorio da semana está pronto, deseja colocar mais algum dado? (S/N): ')
        if dia7.lower() == 'n' or dia7.lower() == 'nao' or dia7.lower() == 'não':
            continuar = False
            break
        elif dia7.lower() == 'sim' or dia7.lower() == 's':
            print(ciano + menu + reseta_cor)
            break
        else:
            print(vermelho + 'Opção invalida, favor digitar Sim ou Não' + reseta_cor)

    # verificação se o usuário deseja parar ou continuar o programa
    while dia != 7:
        opcao = input('Deseja continuar registrando os dados? (S/N)')
        if opcao.lower() == 'n' or opcao.lower() == 'nao' or opcao.lower() == 'não':
            continuar = False
            break
        elif opcao.lower() == 'sim' or opcao.lower() == 's':
            print(ciano + menu + reseta_cor)
            break
        else:
            print(vermelho + 'Opção inválida, favor digitar Sim ou Não' + reseta_cor)
    
#Dia
print('--------------------------------------------------------------')
print(ciano + "Total de dados usados por cada aplicativo por dia:")
print(vermelho + 'Chrome:', chrome_diario)
print(azul + 'Facebook:', facebook_diario)
print(roxo + 'Instagram: ', instagram_diario)
print(verde + 'Whatsapp: ', whatsapp_diario)
print(amarelo + 'Outras Aplicações: ', outros_diario )
print(reseta_cor + '--------------------------------------------------------------')
#Semana
print(ciano + "Total de dados usados por cada aplicativo na semana:")
print(vermelho + "Chrome:",chrome_semanal)
print(azul + "Facebook:",facebook_semanal)
print(roxo + "Instagram:",instagram_semanal)
print(verde + "Whatsapp:",whatsapp_semanal)
print(amarelo + "Outros:",outros_semanal)
print(reseta_cor + '--------------------------------------------------------------')
#Dados totais em cada dia
print(ciano + 'Dados totais de cada dia:')
print(total_diario)
print(reseta_cor + '--------------------------------------------------------------')
#Dados totais da semana
print(ciano + 'Dados totais da semana:')
print(total_semanal)
print(reseta_cor + '--------------------------------------------------------------')
#Média diária de consumo total dos dados
print(ciano + 'Média diária de consumo total dos dados:')
print(round((chrome_diario[0] + instagram_diario[0] + outros_diario[0] + facebook_diario[0] + whatsapp_diario[0])/7, 2))
print(reseta_cor + '--------------------------------------------------------------')
#Média diária do consumo dos dados de cada aplicativo
print(ciano + 'Média diária do consumo dos dados de cada aplicativo:')
print(vermelho + 'Chrome:',chrome_semanal/total_semanal)
print(azul + 'Facebook:',facebook_semanal/total_semanal)
print(roxo + 'Instagram:',instagram_semanal/total_semanal)
print(verde + 'Whatsapp:',whatsapp_semanal/total_semanal)
print(amarelo + 'Outras Aplicações:',outros_semanal/total_semanal)
print(reseta_cor + '--------------------------------------------------------------')



