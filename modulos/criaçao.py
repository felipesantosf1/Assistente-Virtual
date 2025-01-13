import os 

def Create(name):
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    if name == "pasta":
        x = 0
        nome_base = os.path.join(desktop_path, "Nova Pasta")
        nome_pasta = nome_base

        while os.path.exists(nome_pasta):
            x += 1
            nome_pasta = f"{nome_base} ({x})"

        os.makedirs(nome_pasta)
        return "Pasta criada"
    
    elif name == "bloco de notas":
        x = 0
        nome_base = os.path.join(desktop_path, "Novo Documento")
        nome_documento = f"{nome_base}.txt"

        while os.path.exists(nome_documento):
            x += 1
            nome_documento = f"{nome_base} ({x}).txt"

        with open(nome_documento, "x") as arquivo:
            return "arquivo criado"
        