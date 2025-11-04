import csv

with open(r"C:\Users\jodson.pierre\Documents\meu projeto\dados.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')  # <-- separa por ponto e vírgula
    print("Pessoas com mais de 18 anos:")

    for linha in leitor:
        if not linha or len(linha) < 3:
            continue

        nome = linha[0].strip()
        idade = int(linha[1].strip())
        cidade = linha[2].strip()

        if idade > 18:
            print(f"{nome} ({idade} anos) - {cidade}")

