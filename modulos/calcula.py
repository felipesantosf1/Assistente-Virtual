from pyparsing import Word, nums

def Calculadora(frase):
    try:
        frase = frase.replace("x", "*")
        numeros = Word(nums)
        numeros_encontrados = numeros.searchString(frase)
        numbers = [int(token[0]) for token in numeros_encontrados]

        if "somar" in frase or "+" in frase:
            result = numbers[0] + numbers[1]
            return f"{numbers[0]} mais {numbers[1]} é igual a {result}"
        
        if "menos" in frase or "-" in frase:
            result = numbers[0] - numbers[1]
            return f"{numbers[0]} menos {numbers[1]} é igual a {result}"
        
        if "vezes" in frase or "*" in frase:
            result = numbers[0] * numbers[1]
            return f"{numbers[0]} vezes {numbers[1]} é igual a {result}"
        
        if "dividido" in frase or "/" in frase:
            result = numbers[0] / numbers[1]
            return f"{numbers[0]} dividido para {numbers[1]} é igual a {result}"
        
        if "%" in frase:
            result = ((numbers[0] / 100) * numbers[1])
            return f"{numbers[0]} % de {numbers[1]} é igual a {result}"
    
    except:
        return "Não foi possivel fazer esta operação"