import time


cor_vermelho = "\033[31m"
cor_verde = "\033[32m"
cor_azul = "\033[34m"
cor_amarelo = "\033[33m"
cor_roxo = "\033[35m"
cor_ciano = "\033[36m"
cor_branco = "\033[37m"
italico = "\033[3m"
reset = "\033[0m"

# Taxas anuais 
IPCA = 5.53
CDI = 14.65
POUPANCA = 6.0

def taxa_final_investimento_renda_fixa(porcentagemRendaFixa):
    return CDI * porcentagemRendaFixa

def taxaIr(tempo):
    if tempo <= 6:
        return 0.225
    elif tempo <= 12:
        return 0.20
    elif tempo <= 24:
        return 0.175
    else:
        return 0.15

print("SIMULADOR DE INVESTIMENTOS")
print(f"{italico}Olá, vou te ajudar a simular as possibilidades de investimentos{reset}\n")
time.sleep(0.5)
print(f"Pra começar, quero te dizer que as {cor_azul}taxas anuais{reset} que estou utilizando são:")
time.sleep(0.5)
print(f"IPCA (inflação):.. {cor_roxo}{IPCA:.2f}%{reset}")
time.sleep(0.5)
print(f"CDI (juros):...... {cor_roxo}{CDI:.2f}%{reset}")
time.sleep(0.5)
print(f"Poupança:......... {cor_roxo}{POUPANCA:.2f}%{reset}\n")
time.sleep(0.5)

valor = float(input(f"Agora me informa o valor em reais que você quer investir {cor_verde}R$ {reset}"))
print(f"Ok, registrei o valor de seu investimento.\n")
time.sleep(0.5)

taxa_100 = CDI
taxa_110 = taxa_final_investimento_renda_fixa(1.10)
taxa_120 = taxa_final_investimento_renda_fixa(1.20)
taxa_95 = taxa_final_investimento_renda_fixa(0.95)

print("Essas são as opções de investimento que tenho disponíveis para você:")
print(f"[A] CDB valendo 100% do CDI, taxa final de {cor_roxo}{taxa_100:.2f}%{reset}")
print(f"[B] CDB valendo 110% do CDI, taxa final de {cor_roxo}{taxa_110:.2f}%{reset}")
print(f"[C] CDB valendo 120% do CDI, taxa final de {cor_roxo}{taxa_120:.2f}%{reset}")
print(f"[D] LCA valendo  95% do CDI, taxa final de {cor_roxo}{taxa_95:.2f}%{reset}")
print("Obs.: lembre que o CDB retém IR na fonte, enquanto a LCA não.\n")

investimento = input("Qual o investimento que você quer fazer? (A, B, C ou D) ").upper()
print("Ok, registrei sua opção de investimento.\n")
time.sleep(0.5)

if investimento in ["A", "B", "C"]:
    print("Como você escolheu um CDB vou te lembrar as taxas regressivas de IR:")
    print(f"Até 6 meses:...... {cor_roxo}22.50%{reset}")
    print(f"Até 12 meses:..... {cor_roxo}20.00%{reset}")
    print(f"Até 24 meses:..... {cor_roxo}17.50%{reset}")
    print(f"Acima de 24 meses: {cor_roxo}15.00%{reset}\n")

tempo = int(input("Quanto tempo você gostaria de esperar para resgatar esse investimento? (em meses) "))
print("Ok, registrei o tempo para o resgate.\n")
time.sleep(0.5)

if investimento == "A":
    taxa_ir = taxaIr(tempo)
    taxa_anual = taxa_100
elif investimento == "B":
    taxa_ir = taxaIr(tempo)
    taxa_anual = taxa_110
elif investimento == "C":
    taxa_ir = taxaIr(tempo)
    taxa_anual = taxa_120
elif investimento == "D":
    taxa_ir = 0.0
    taxa_anual = taxa_95
else:
    taxa_ir = 0.15
    taxa_anual = CDI

# Cálculo da taxa mensal 
taxa_mensal = (1 + taxa_anual / 100) ** (1 / 12) - 1

montante = valor * (1 + taxa_mensal) ** tempo
lucro_bruto = montante - valor
valor_ir = lucro_bruto * taxa_ir
valor_liquido = montante - valor_ir
lucro_liquido = valor_liquido - valor

# Inflação

fator_inflacao = 301.46/100
correcao_inflacao = valor * fator_inflacao
desvalorizacao = 33.17/100

# Poupança
taxa_poupanca_mensal = (1 + POUPANCA / 100) ** (1 / 12) - 1
montante_poupanca = valor * (1 + taxa_poupanca_mensal) ** tempo
lucro_poupanca = montante_poupanca - valor
diferenca_lucro = lucro_liquido - lucro_poupanca
proporcional_investimento = (valor_liquido / correcao_inflacao) * valor
poupanca_proporcional = (montante_poupanca / correcao_inflacao) * valor

# SAÍDAS
print("TAXAS UTILIZADAS")
print(f"- Taxa de IR aplicada...... {cor_roxo}{taxa_ir*100:.2f}%{reset}")
print(f"- Taxa de rendimento anual. {cor_roxo}{taxa_anual:.2f}%{reset}")
print(f"- Taxa de rendimento mensal {cor_roxo}{taxa_mensal*100:.2f}%{reset}\n")

print("RESULTADO")
print(f"Valor investido........... {cor_verde}R$ {valor:.2f}{reset}")
print(f"Rendendo pelo tempo de.... {cor_ciano}{tempo} meses{reset}")
print(f"Dedução do IR de.......... {cor_roxo}{taxa_ir*100:.2f}%{reset}")
print(f"O valor deduzido é de..... {cor_verde}R$ {valor_ir:.2f}{reset}")
print(f"O resgate será de......... {cor_verde}R$ {valor_liquido:.2f}{reset}")
print(f"O lucro total será........ {cor_verde}R$ {lucro_liquido:.2f}{reset}\n")

analise = input("Você gostaria de ver algumas análises adicionais (sim/não)? ").lower()

if analise == "sim":
    print("\nANÁLISES POUPANÇA")
    print(f"Se você tivesse investido.. {cor_verde}R$ {valor:.2f}{reset}")
    print(f"Na poupança, ao final dos {cor_azul}{tempo} meses{reset}")
    print(f"O valor resgatado seria... {cor_verde}R$ {montante_poupanca:.2f}{reset}")
    print(f"O lucro total............. {cor_verde}R$ {lucro_poupanca:.2f}{reset}")
    print(f"A diferença de lucro é de. {cor_verde}R$ {diferenca_lucro:.2f}{reset}\n")

    print("ANÁLISES INFLAÇÃO")
    print(f"A inflação acumulada foi de.................... {cor_roxo}{(fator_inflacao) * 100:.2f}%{reset}")
    print(f"Resultado em desvalorização de................. {cor_roxo}{desvalorizacao*100:.2f}%{reset}")
    print(f"Se você comprava algo por...................... {cor_verde}R${valor:.2f}{reset}")
    print(f"Esse item custaria corrigido pela inflação.... {cor_verde}R$ {correcao_inflacao:.2f}{reset}")

    print(f"O resgate proporcional ao valor corrigido é... {cor_verde}R$ {proporcional_investimento:.2f}{reset}")
    print(f"Na poupança seria proporcional a.............. {cor_verde}R$ {poupanca_proporcional:.2f}{reset}\n")

print("RESUMO")
print(f"Valor investido:.......... {cor_verde}R$ {valor:.2f}{reset}")
print(f"Valor resgatado:.......... {cor_verde}R$ {valor_liquido:.2f}{reset}")
print(f"Se fosse na poupança:..... {cor_verde}R$ {montante_poupanca:.2f}{reset}")
print(f"Correção da inflação:..... {cor_verde}R$ {correcao_inflacao:.2f}{reset}\n")

print("Espero ter ajudado!")
input("")