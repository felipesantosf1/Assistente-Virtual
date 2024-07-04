import re
import webbrowser as web

PALAVRAS_CHAVE = [
    'procurar sobre',
    'pesquisar sobre',
    'pesquisa sobre',
    'procurar',
    'pesquisar',
    'pesquisa',
    'acerca de',
    'a respeito de'
]

# Função genérica para realizar pesquisas
def realizar_pesquisa(frase):
    text = re.search(r'\b(google|youtube)\b', frase)
    plataforma = text.group(0)
    frase = frase.replace(f"no {plataforma}", " ").strip()
    for palavra_chave in PALAVRAS_CHAVE:
        if palavra_chave in frase:
            pesquisa = re.split(rf"\b{re.escape(palavra_chave)}\b", frase)[-1].strip()
            break

        else:
            pesquisa = frase

    if plataforma == 'google':
        url = f'https://www.google.com.br/search?q={pesquisa}'
    elif plataforma == 'youtube':
        url = f'https://www.youtube.com/results?search_query={pesquisa}'

    web.open(url)
    return f"Pesquisando sobre {pesquisa} no {plataforma}"