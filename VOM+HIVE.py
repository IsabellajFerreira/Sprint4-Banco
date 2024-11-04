import tkinter as tk
from tkinter import messagebox
from  pymongo import MongoClient
import json
from datetime import datetime

# Conexao com MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['VOM+HIVE']
collection = db['produto']

# Funções do CRUD
def limpar_campos_produto():
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_publico.delete(0, tk.END)
    entry_diferencial.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_canal.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_estoque.delete(0, tk.END)
    entry_avaliacao.delete(0, tk.END)
    entry_lancamento.delete(0, tk.END)

def criar_produto():
    try:
        produto = {
            "id_produto": int(entry_id.get()),
            "nome": entry_nome.get(),
            "publico_alvo": entry_publico.get(),
            "diferencial": entry_diferencial.get(),
            "preco": float(entry_preco.get()),
            "canal_vendas": entry_canal.get(),
            "categoria": entry_categoria.get(),
            "descricao": entry_descricao.get(),
            "estoque": int(entry_estoque.get()),
            "avaliacao": float(entry_avaliacao.get()),
            "data_lancamento": entry_lancamento.get()  
        }
        collection.insert_one(produto)
        messagebox.showinfo("Sucesso", "Produto criado com sucesso!")
        limpar_campos_produto() 
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criar produto: {e}")

def consultar_produto():
    try:
        identificador = entry_id_consulta.get() or entry_nome_consulta.get()
        query = {"$or": [{"id_produto": int(identificador)}, {"nome_produto": identificador}]}
        produto = collection.find_one(query)
        if produto:
            result = "\n".join(f"{key}: {value}" for key, value in produto.items())
            messagebox.showinfo("Produto Encontrado", result)
        else:
            messagebox.showwarning("Aviso", "Produto não encontrado.")
    except ValueError:
        messagebox.showerror("Erro", "ID deve ser numérico ou nome válido.")

def atualizar_produto():
    try:
        id_produto = int(entry_id_atualizar.get())
        atributo = entry_atributo.get()
        novo_valor = entry_novo_valor.get()

        if atributo in ["id_produto", "estoque"]:
            novo_valor = int(novo_valor)
        elif atributo in ["preco", "avaliacao"]:
            novo_valor = float(novo_valor)

        result = collection.update_one({"id_produto": id_produto}, {"$set": {atributo: novo_valor}})
        if result.modified_count > 0:
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Produto não encontrado ou não houve alterações.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar produto: {e}")

def deletar_produto():
    try:
        id_produto = int(entry_id_deletar.get())
        result = collection.delete_one({"id_produto": id_produto})
        if result.deleted_count > 0:
            messagebox.showinfo("Sucesso", "Produto deletado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Produto não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao deletar produto: {e}")

def exportar_dataset():
    try:
        colecoes = db.list_collection_names()
        dados_export = {}

        for colecao in colecoes:
            collection = db[colecao]
            dados = list(collection.find({}))

            for dado in dados:
                dado["_id"] = str(dado["_id"])
                for key, value in dado.items():
                    if isinstance(value, datetime):
                        dado[key] = value.isoformat()  

            dados_export[colecao] = dados

        with open("dados_exportados.json", "w") as file:
            json.dump(dados_export, file, indent=4)

        messagebox.showinfo("Exportação", "Dados exportados para 'dados_exportados.json'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar dados: {e}")

# Interface Tkinter
app = tk.Tk()
app.title("CRUD de Produtos")
app.geometry("500x600")


tk.Label(app, text="Criar Produto").grid(row=0, column=0, columnspan=2)
entry_id = tk.Entry(app)
entry_nome = tk.Entry(app)
entry_publico = tk.Entry(app)
entry_diferencial = tk.Entry(app)
entry_preco = tk.Entry(app)
entry_canal = tk.Entry(app)
entry_categoria = tk.Entry(app)
entry_descricao = tk.Entry(app)
entry_estoque = tk.Entry(app)
entry_avaliacao = tk.Entry(app)
entry_lancamento = tk.Entry(app)

labels = ["ID (numérico)", "Nome do Produto", "Público Alvo", "Diferencial", "Preço", "Canal de Vendas", "Categoria", "Descrição", "Estoque", "Avaliação", "Data de Lançamento (YYYY-MM-DD)"]
entries = [entry_id, entry_nome, entry_publico, entry_diferencial, entry_preco, entry_canal, entry_categoria, entry_descricao, entry_estoque, entry_avaliacao, entry_lancamento]

for i, (label, entry) in enumerate(zip(labels, entries)):
    tk.Label(app, text=label).grid(row=i+1, column=0)
    entry.grid(row=i+1, column=1)

tk.Button(app, text="Criar Produto", command=criar_produto).grid(row=12, column=0, columnspan=2)

# Consultar Produto
tk.Label(app, text="Consultar Produto").grid(row=13, column=0, columnspan=2)
entry_id_consulta = tk.Entry(app)
entry_nome_consulta = tk.Entry(app)
entry_id_consulta.grid(row=14, column=1)
entry_nome_consulta.grid(row=15, column=1)
tk.Label(app, text="ID").grid(row=14, column=0)
tk.Label(app, text="Nome do Produto").grid(row=15, column=0)
tk.Button(app, text="Consultar Produto", command=consultar_produto).grid(row=16, column=0, columnspan=2)

# Atualizar Produto
tk.Label(app, text="Atualizar Produto").grid(row=17, column=0, columnspan=2)
entry_id_atualizar = tk.Entry(app)
entry_atributo = tk.Entry(app)
entry_novo_valor = tk.Entry(app)
entry_id_atualizar.grid(row=18, column=1)
entry_atributo.grid(row=19, column=1)
entry_novo_valor.grid(row=20, column=1)
tk.Label(app, text="ID").grid(row=18, column=0)
tk.Label(app, text="Atributo").grid(row=19, column=0)
tk.Label(app, text="Novo Valor").grid(row=20, column=0)
tk.Button(app, text="Atualizar Produto", command=atualizar_produto).grid(row=21, column=0, columnspan=2)

# Deletar Produto
tk.Label(app, text="Deletar Produto").grid(row=22, column=0, columnspan=2)
entry_id_deletar = tk.Entry(app)
entry_id_deletar.grid(row=23, column=1)
tk.Label(app, text="ID").grid(row=23, column=0)
tk.Button(app, text="Deletar Produto", command=deletar_produto).grid(row=24, column=0, columnspan=2)

# Exportar Dataset
tk.Button(app, text="Exportar Dataset", command=exportar_dataset).grid(row=25, column=0, columnspan=2)

app.mainloop()
