import csv
def salvar_livros_csv(livros, nome_arquivo):
    campos = ["titulo", "preco", "disponivel", "nota", "upc", "categoria"]

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        writer.writeheader() # Escreve o cabeçalho
        for livro in livros:
            writer.writerow(livro)
