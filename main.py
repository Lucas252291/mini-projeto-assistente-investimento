import time

cor_vermelho = "\033[31m"
cor_verde = "\033[32m"
cor_azul = "\033[34m"
cor_amarelo = "\033[33m"
cor_roxo = "\033[35m"
cor_ciano = "\033[36m"
cor_branco = "\033[37m"
italico = "\033[3m"
negativo = "\033[7m"
reset = "\033[0m"

#Missão 1

print("SIMULADOR DE INVESTIMENTOS")
print("Olá, vou te ajudar a simular as possibilidades de investimento")
time.sleep(1.5)

print(f"\nPra começar, quero te dizer que as {cor_azul}taxas anuais{reset} que estou utilizando são: ")
print(f"{cor_azul}IPCA{reset}(inflação): {cor_roxo}5.53%{reset}")
print(f"{cor_azul}CDI{reset}(juros):.... {cor_roxo}14.65%{reset}")
print(f"{cor_azul}Poupança{reset}:...... {cor_roxo}6.00%{reset}")
time.sleep(1.5)

valor = float(input(f"\nAgora me informe o valor em reais que você quer investir: R$ "))
print(f"Ok, registrei o valor do seu investimento.")
time.sleep(2.0)

print("\nEssas são as opções de investimento que tenho disponíveis para você: ")
print(f"[A]{cor_azul}CDB{reset} valendo 100% do CDI, taxa final de {cor_roxo}14.65%{reset}")
print(f"[B]{cor_azul}CDB{reset} valendo 110% do CDI, taxa final de {cor_roxo}16.12%{reset}")
print(f"[C]{cor_azul}CDB{reset} valendo 120% do CDI, taxa final de {cor_roxo}17.58%{reset}")
print(f"[D]{cor_azul}LCA{reset} valendo 95% do CDI, taxa final de  {cor_roxo}13.92%{reset}")
print(f"{italico}Obs.: Lembre que o CDB retém IR na fonte, enquanto a LCA não.{reset}")
time.sleep(1)

investimento = input("\nEscolha a opção de investimento (A, B, C ou D): ").upper()
print("Ok, registrei sua opção de investimento.\n")
time.sleep(0.5)

if investimento in ["A", "B", "C"]:
    print(f"{italico}Como você escolheu um CDB vou te lembrar as taxas regressivas de IR: {reset}") 
    print(f"{italico}Até 6 meses:...... {cor_roxo}22.50%{reset}")
    print(f"{italico}Até 12 meses:..... {cor_roxo}20.00%{reset}")
    print(f"{italico}Até 24 meses:..... {cor_roxo}17.50%{reset}")
    print(f"{italico}Acima de 24 meses: {cor_roxo}15.00%{reset}")
time.sleep(1.5)

#Missão 2

tempo = int(input(f"\nQuanto tempo você gostaria de esperar para resgatar esse investimento? (em meses): "))
print("Ok, registrei o tempo para o resgate.\n") 
time.sleep(0.5)

if investimento in ["A", "B", "C"]:
    if tempo <= 6:
        taxa_ir = 0.225
    elif tempo <= 12:
        taxa_ir = 0.20
    elif tempo <= 24:
        taxa_ir = 0.175
    else:
        taxa_ir = 0.15
else:
    taxa_ir = 0.0  

if investimento == "A":
    taxa_anual = 0.1465
elif investimento == "B":
    taxa_anual = 0.1612
elif investimento == "C":
    taxa_anual = 0.1758
elif investimento == "D":
    taxa_anual = 0.1392
else:
    taxa_anual = 0.0

taxa_mensal = (1 + taxa_anual) ** (1/12) - 1

valor_investido = valor
valor_final = valor_investido * ((1 + taxa_mensal) ** tempo)
rendimento = valor_final - valor_investido
valor_ir = rendimento * taxa_ir
resgate = valor_final - valor_ir
lucro_total = resgate - valor_investido

print("\nTAXAS UTILIZADAS")
print(f"- Taxa de IR aplicada: {cor_roxo}{taxa_ir * 100:.2f}%{reset}")
print(f"- Taxa de rendimento anual: {cor_roxo}{taxa_anual * 100:.2f}%{reset}")  
print(f"- Taxa de rendimento mensal: {cor_roxo}{taxa_mensal * 100:.2f}%{reset}")
time.sleep(0.5)

print("\nRESULTADO")
print(f"- Valor investido....... {cor_verde}R$ {valor_investido:.2f}{reset}")
print(f"- Rendendo pelo tempo de {cor_azul}{tempo} meses{reset}")
print(f"- Dedução do IR de...... {cor_roxo}{taxa_ir *100:.2f}%{reset}")
print(f"- Valor deduzido é de... R$ {cor_verde}{valor_ir:.2f}{reset}")
print(f"- O resgate será de..... R$ {cor_verde}{resgate:.2f}{reset}")
print(f"- O lucro total será.... R$ {cor_verde}{lucro_total:.2f}{reset}")
time.sleep(1.5)

#Missão 3
analises = (input(f"\n{italico}Você gostaria de ver algumas análises adicionais (sim/não)?  {reset}"))

if analises.lower() == "sim":
    print("\nANÁLISES POUPANÇA")
    print(f"Se você tivesse investido {cor_verde}R$ {valor:.2f}{reset}")
    print(f"na poupança, ao final dos {cor_azul}{tempo:.2f} meses{reset}")
    valor_poupanca = valor * (1 + 0.06) ** (tempo / 12)
    lucro_poupanca = valor_poupanca - valor
    print(f"o valor resgatado seria.. {cor_verde}R$ {valor_poupanca:.2f}{reset}")
    print(f"e o lucro total.......... {cor_verde}R$ {lucro_poupanca:.2f}{reset}")
    print(f"A diferença de lucro é de {cor_verde}R$ {(resgate - valor_poupanca):.2f}{reset}")

    print("\nANÁLISES INFLAÇÃO")
    inflacao_acumulada = (1 + 0.0553) ** (tempo / 12) - 1
    valor_corrigido = valor * (1 + 0.0553) ** (tempo / 12)
    desvalorizacao = 1 - (valor / valor_corrigido) if valor_corrigido != 0 else 0

    if valor_corrigido != 0:
        resgate_corrigido = resgate / valor_corrigido * valor
        poupanca_corrigida = valor_poupanca / valor_corrigido * valor
    else:
        resgate_corrigido = 0
        poupanca_corrigida = 0

    print(f"A inflação acumulada foi de......................... {cor_roxo}{inflacao_acumulada*100:.2f}%{reset}")
    print(f"resultando em uma desvalorização de................. {cor_roxo}{desvalorizacao*100:.2f}%{reset}")
    print(f"Por exemplo, se você comprava algo por.............. {cor_verde}R$ {valor:.2f}{reset}")
    print(f"O mesemo item custaria corrigido pela inflacão será. {cor_verde}R$ {valor_corrigido:.2f}{reset}")
    print(f"O resgate proporcionalmente ao valor corrigido fica  {cor_verde}R$ {resgate_corrigido:.2f}{reset}")
    print(f"Já na poupança o proporcional a essa correção seria  {cor_verde}R$ {poupanca_corrigida:.2f}{reset}")

print("\nRESUMO")
print(f"Valor investido:..... {cor_verde}R$ {valor_investido:.2f}{reset}")
print(f"Valor resgatado:..... {cor_verde}R$ {resgate:.2f}{reset}")
print(f"Se fosse na poupança: {cor_verde}R$ {poupanca_corrigida:.2f}{reset}")
print(f"correção pela inflação: {cor_verde}R$ {valor_corrigido:.2f}{reset}")

print(f"\n{italico}Espero ter ajudado!{reset}")