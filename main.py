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


print("SIMULADOR DE INVESTIMENTOS")
print("Olá, vou te ajudar a simular as possibilidades de investimento")
time.sleep(1.5)

print(f"\nPra começar, quero te dizer que as {cor_azul}taxas anuais{reset} que estou utilizando são: ")
print(f"{cor_azul}IPCA{reset}(inflação): {cor_roxo}5.53%{reset}")
print(f"{cor_azul}CDI{reset}(juros):.... {cor_roxo}14.65%{reset}")
print(f"{cor_azul}Poupança{reset}:...... {cor_roxo}6.00%{reset}")
time.sleep(1.5)

valor = float(input(f"\nAgora me informe o valor em reais que você quer investir: {cor_verde}R${reset} "))
print(f"Ok, registrei o valor do seu investimento.")
time.sleep(2.0)

print("\nEssas são as opções de investimento que tenho disponíveis para você: ")
print(f"[A]{cor_azul}CDB{reset} valendo 100% do CDI, taxa final de {cor_roxo}14.65%{reset}")
print(f"[B]{cor_azul}CDB{reset} valendo 110% do CDI, taxa final de {cor_roxo}16.12%{reset}")
print(f"[C]{cor_azul}CDB{reset} valendo 120% do CDI, taxa final de {cor_roxo}17.58%{reset}")
print(f"[D]{cor_azul}LCA{reset} valendo 95% do CDI, taxa final de {cor_roxo}13.92%{reset}")
print(f"{italico}Obs.: Lembre que o CDB retém IR na fonte, enquanto a LCA não.{reset}")

investimento = input("\nEscolha a opção de investimento (A, B, C ou D): ").upper()
print("Ok, registrei sua opção de investimento.\n")


if investimento in ["A", "B", "C"]:
    print(f"{italico}Como você escolheu um CDB vou te lembrar as taxas regressivas de IR: {reset}") 
    print(f"{italico}Até 6 meses:...... {cor_roxo}22.50%{reset}")
    print(f"{italico}Até 12 meses:..... {cor_roxo}20.00%{reset}")
    print(f"{italico}Até 24 meses:..... {cor_roxo}17.50%{reset}")
    print(f"{italico}Acima de 24 meses: {cor_roxo}15.00%{reset}")
