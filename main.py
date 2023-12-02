import tkinter as tk
from tkinter import messagebox
import requests

def obter_endereco(cep):
    try:
        # Consulta a API Via CEP
        url = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(url)
        dados = resposta.json()

        # Verifica se a requisição foi bem-sucedida
        if 'erro' not in dados:
            endereco_completo = (
                f"CEP: {dados['cep']}\n"
                f"Logradouro: {dados['logradouro']}\n"
                f"Complemento: {dados['complemento']}\n"
                f"Bairro: {dados['bairro']}\n"
                f"Cidade: {dados['localidade']}\n"
                f"Estado: {dados['uf']}"
            )
            return endereco_completo
        else:
            return "CEP não encontrado"

    except requests.ConnectionError:
        return "Erro de conexão. Verifique sua conexão com a internet."

def buscar_cep():
    cep_digitado = entrada_cep.get()
    endereco = obter_endereco(cep_digitado)
    resultado_label.config(text=endereco)

    # Habilitar o botão e configurar a ação de cópia
    if "CEP não encontrado" not in endereco:
        botao_copiar.config(state=tk.NORMAL, command=copiar_texto, text="Copiar")

def copiar_texto():
    texto = resultado_label.cget("text")
    janela.clipboard_clear()
    janela.clipboard_append(texto)
    janela.update()
    botao_copiar.config(state=tk.DISABLED, command=None, text="Copiado!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Consulta de CEP")

# Configurando o tamanho e centralizando a janela
largura = 400
altura = 300

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela/2) - (largura/2)
y = (altura_tela/2) - (altura/2)

janela.geometry(f'{largura}x{altura}+{int(x)}+{int(y)}')

# Criando widgets
rotulo = tk.Label(janela, text="Digite o CEP:")
rotulo.pack(pady=10)

entrada_cep = tk.Entry(janela)
entrada_cep.pack(pady=10)

botao_buscar = tk.Button(janela, text="Buscar", command=buscar_cep)
botao_buscar.pack(pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(janela, text="", wraplength=300, justify='left', cursor='arrow')
resultado_label.pack(pady=10)

# Botão para copiar
botao_copiar = tk.Button(janela, text="Copiar", state=tk.DISABLED)
botao_copiar.pack(pady=10)

# Iniciando o loop da interface gráfica
janela.mainloop()
