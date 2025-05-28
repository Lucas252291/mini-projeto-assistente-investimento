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


IPCA = 5.53
CDI = 14.65
POPANCA = 6.00

def taxa_final_investimento_renda_fixa(porcentagemRendaFixa):
    return CDI * porcentagemRendaFixa



#Missão 1

print("SIMULADOR DE INVESTIMENTOS")
print("Olá, vou te ajudar a simular as possibilidades de investimento")
time.sleep(0.5)

print(f"\nPra começar, quero te dizer que as {cor_azul}taxas anuais{reset} que estou utilizando são: ")
time.sleep(0.5)
print(f"{cor_azul}IPCA{reset}(inflação): {cor_roxo}{IPCA}%{reset}")
time.sleep(0.5)
print(f"{cor_azul}CDI{reset}(juros):.... {cor_roxo}{CDI}%{reset}")
time.sleep(0.5)
print(f"{cor_azul}Poupança{reset}:...... {cor_roxo}{POPANCA}%{reset}")
time.sleep(0.5)

valor = float(input(f"\nAgora me informe o valor em reais que você quer investir: R$ "))
time.sleep(0.5)
print(f"Ok, registrei o valor do seu investimento.")
time.sleep(0.5)
taxa_rendimento_anual_110_porcento = taxa_final_investimento_renda_fixa(1.10)
taxa_rendimento_anual_120_porcento = taxa_final_investimento_renda_fixa(1.20)
taxa_rendimento_anual_95_porcento = taxa_final_investimento_renda_fixa(0.95)
print("\nEssas são as opções de investimento que tenho disponíveis para você: ")
time.sleep(0.5)
print(f"[A]{cor_azul}CDB{reset} valendo 100% do CDI, taxa final de {cor_roxo}{CDI}%{reset}")
time.sleep(0.5)
print(f"[B]{cor_azul}CDB{reset} valendo 110% do CDI, taxa final de {cor_roxo}{taxa_rendimento_anual_110_porcento:.2f}%{reset}")
time.sleep(0.5)
print(f"[C]{cor_azul}CDB{reset} valendo 120% do CDI, taxa final de {cor_roxo}{taxa_rendimento_anual_120_porcento:.2f}%{reset}")
time.sleep(0.5)
print(f"[D]{cor_azul}LCA{reset} valendo 95% do CDI, taxa final de  {cor_roxo}{taxa_rendimento_anual_95_porcento:.2f}%{reset}")
time.sleep(0.5)
print(f"{italico}Obs.: Lembre que o CDB retém IR na fonte, enquanto a LCA não.{reset}")
time.sleep(0.5)

investimento = input("\nEscolha a opção de investimento (A, B, C ou D): ").upper()
time.sleep(0.5)
print("Ok, registrei sua opção de investimento.\n")
time.sleep(0.5)

if investimento in ["A", "B", "C"]:
    print(f"{italico}Como você escolheu um CDB vou te lembrar as taxas regressivas de IR: {reset}") 
    print(f"{italico}Até 6 meses:...... {cor_roxo}22.50%{reset}")
    print(f"{italico}Até 12 meses:..... {cor_roxo}20.00%{reset}")
    print(f"{italico}Até 24 meses:..... {cor_roxo}17.50%{reset}")
    print(f"{italico}Acima de 24 meses: {cor_roxo}15.00%{reset}")
time.sleep(0.5)

#Missão 2

tempo = int(input(f"\nQuanto tempo você gostaria de esperar para resgatar esse investimento? (em meses): "))
print("Ok, registrei o tempo para o resgate.\n") 
time.sleep(0.5)

taxa_anual = 0.0
taxa_rendimento_mensal = 0.0


def taxaIr(tempo):
    if tempo <= 6:
        return 22.5/100
    elif tempo <= 12:
        return 20.0/100
    elif tempo <= 24:
        return 17.5/100
    elif tempo > 24:
        return 15.0/100



if investimento == "A":
    taxa_ir = taxaIr(tempo)
    taxa_anual = CDI
    taxa_rendimento_mensal = ((1 + (taxa_anual/100))**(1/12)-1)
elif investimento == "B":
    taxa_ir = taxaIr(tempo)
    taxa_anual = taxa_rendimento_anual_110_porcento
    taxa_rendimento_mensal = ((1 + (taxa_anual/100))**(1/12)-1)
elif investimento == "C":
    taxa_ir = taxaIr(tempo)
    taxa_anual = taxa_rendimento_anual_120_porcento
    taxa_rendimento_mensal = ((1 + (taxa_anual/100))**(1/12)-1)

elif investimento == "D":
    taxa_ir = 0.0
    taxa_anual = taxa_rendimento_anual_95_porcento
    taxa_rendimento_mensal = ((1 + (taxa_anual/100))**(1/12)-1)


montante = valor * (1 + taxa_rendimento_mensal) ** tempo

lucro_bruto = montante - valor
valor_ir = lucro_bruto * taxa_ir
valor_liquido = montante - valor_ir
lucro_total = valor_liquido - valor


print("\nTAXAS UTILIZADAS")
print(f"- Taxa de IR aplicada: {cor_roxo}{taxa_ir * 100:.2f}%{reset}")
print(f"- Taxa de rendimento anual: {cor_roxo}{taxa_anual:.2f}%{reset}")  
print(f"- Taxa de rendimento mensal: {cor_roxo}{taxa_rendimento_mensal * 100:.2f}%{reset}")
time.sleep(0.5)

print("\nRESULTADO")
print(f"- Valor investido....... {cor_verde}R$ {valor:.2f}{reset}")
print(f"- Rendendo pelo tempo de {cor_azul}{tempo} meses{reset}")
print(f"- Dedução do IR de...... {cor_roxo}{taxa_ir *100:.2f}%{reset}")
print(f"- Valor deduzido é de....... {cor_verde}R$ {valor_ir:.2f}{reset}")
print(f"- O resgate será de....... {cor_verde}R$ {valor_liquido:.2f}{reset}")
print(f"- O lucro total será....... {cor_verde}R$ {lucro_total:.2f}{reset}")









