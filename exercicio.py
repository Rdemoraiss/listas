produtos = [
    [101, "Notebook", 3500.00],
    [102, "Smartphone", 1800.00],
    [103, "Fone de Ouvido", 250.00],
    [104, "Mouse Gamer", 150.00]
]

print("--- 1. LISTA INICIAL DE PRODUTOS ---")
for p in produtos:
    print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f}")

id_busca = 102
print(f"\n--- 2. LOCALIZANDO PRODUTO COM ID {id_busca} ---")

produto_encontrado = None
for p in produtos:
    if p[0] == id_busca:
        produto_encontrado = p
        break  
if produto_encontrado:
    print(f"Produto Encontrado -> Nome: {produto_encontrado[1]} | Preço: R$ {produto_encontrado[2]:.2f}")
else:
    print("Produto não encontrado.")

id_remover = 103
print(f"\n--- 3. REMOVENDO PRODUTO COM ID {id_remover} ---")

for p in produtos:
    if p[0] == id_remover:
        produtos.remove(p)
        print(f"Sucesso: Produto '{p[1]}' removido.")
        break

print("\n--- 4. LISTA ATUALIZADA DE PRODUTOS ---")
for p in produtos:
    print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f}")
