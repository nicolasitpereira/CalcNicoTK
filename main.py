import tkinter as tk

janela = tk.Tk()

janela.title("NicoCalc")
janela.geometry("320x450")
janela.configure(bg="#1e1e1e")
janela.resizable(False,False)

# Variável que controla o texto do visor
texto_visor = tk.StringVar(value="0")

# Visor da calculadora
visor = tk.Label(
    janela,
    textvariable=texto_visor,
    bg="#292929",
    fg="#ffffff",
    font=("Arial", 28),
    anchor="e",
    padx=15
)

visor.pack(
    fill="x",
    padx=15,
    pady=15
)

# Variáveis para guardar o primeiro num digitado e operador escolhido
primeiro_numero = None
operador = None
entrada_atual = "0"
novo_numero = False



# Função que verifica o que está no visor
def clicar_numero(numero):
    global entrada_atual, novo_numero

    if novo_numero:
        entrada_atual = numero
        novo_numero = False
    elif entrada_atual == "0":
        entrada_atual = numero
    else:
        entrada_atual += numero

    if operador is not None:
        texto_visor.set(
            f"{primeiro_numero:g} {operador} {entrada_atual}"
        )
    else:
        texto_visor.set(entrada_atual)


def clicar_decimal():
    global entrada_atual, novo_numero

    if novo_numero:
        entrada_atual = "0."
        novo_numero = False
    elif "." not in entrada_atual:
        entrada_atual += "."

    if operador is not None:
        texto_visor.set(
            f"{primeiro_numero:g} {operador} {entrada_atual}"
        )
    else:
        texto_visor.set(entrada_atual)



def escolher_operador(op):
    global primeiro_numero, operador, novo_numero

    primeiro_numero = float(entrada_atual)
    operador = op
    novo_numero = True

    texto_visor.set(f"{primeiro_numero:g} {operador}")



def calcular():
    global primeiro_numero, operador, entrada_atual, novo_numero

    if primeiro_numero is None or operador is None:
        return

    segundo_numero = float(entrada_atual)

    if operador == "+":
        resultado = primeiro_numero + segundo_numero
    elif operador == "-":
        resultado = primeiro_numero - segundo_numero
    elif operador == "x":
        resultado = primeiro_numero * segundo_numero
    elif operador == "÷":
        if segundo_numero == 0:
            texto_visor.set("Erro")
            primeiro_numero = None
            operador = None
            entrada_atual = "0"
            novo_numero = True
            return
        resultado = primeiro_numero / segundo_numero

    texto_visor.set(f"{resultado:g}")

    entrada_atual = f"{resultado:g}"
    primeiro_numero = None
    operador = None
    novo_numero = True



def limpar_visor():
    global primeiro_numero, operador, entrada_atual, novo_numero

    primeiro_numero = None
    operador = None
    entrada_atual = "0"
    novo_numero = False

    texto_visor.set("0")



# Área onde ficarão os botões
area_botoes = tk.Frame(janela, bg="#1e1e1e")
area_botoes.pack()

# Texto de cda botão, organizado por linha

botoes = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["=", "", "", ""]
]

for linha in range(len(botoes)):
    for coluna in range(len(botoes[linha])):
        texto = botoes[linha][coluna]

        if texto == "":
            continue

        botao = tk.Button(
            area_botoes,
            command=lambda n=texto: (
                limpar_visor() if n == "C"
                else calcular() if n == "="
                else clicar_decimal() if n == "."
                else escolher_operador(n) if n in ["+", "-", "x", "÷"]
                else clicar_numero(n)
            ),
            text=texto,
            width=5,
            height=2,
            font=("Arial", 14),
            bg="#333333",
            fg="#ffffff"
        )

        botao.grid(
            row=linha,
            column=coluna,
            padx=4,
            pady=4
        )

janela.mainloop()
