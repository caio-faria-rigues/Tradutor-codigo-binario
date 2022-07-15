def printf(text):
    print(text, end="")


spc = " "
vocab1 = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
          "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
          "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
          "1": "·----", "2": "··---", "3": "···--", "4": "····-", "5": "·····", "6": "-····", "7": "--···",
          "8": "---··", "9": "----·", "0": "-----", ".": "·-·-·-", ",": "--··--", "?": "··--··", "=": "-···-", " ": "/",
          "á": ".-", "é": ".", "à": ".-", "ã": ".-"}

vocab2 = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i",
          ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",
          "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",
          "·----": "1", "··---": "2", "···--": "3", "····-": "4", "·····": "5", "-····": "6", "--···": "7",
          "---··": "8", "----·": "9", "-----": "0", "·-·-·-": ".", "--··--": ",", "··--··": "?", "-···-": "=", "/": " "
          }

while True:

    oi = input('''   
                 
    Tradutor de código morse
    digite 1 para traduzir morse em português e 2 para traduzir português em morse.

''')

    if oi == "sair":
        break

    if oi == "1":
        codigo = input('''
    
    Tradutor de código morse 
    Utilize '.' e '-' e separe letras com espaço e palavras com / 
    Insira o código abaixo:

''')
        if codigo == "sair":
            break

        morse = codigo.split()
        for n in morse:
            tradut1 = vocab2.get(n)
            printf(tradut1)

    if oi == "2":
        codigo2 = input('''
    Tradutor de código morse
    Não utilize acentos ou pontuações incomuns
    Insira o texto abaixo:
         
''')
        if codigo2 == "sair":
            break

        texto = list(codigo2.lower())
        print(texto)
        for s in texto:
            tradut2 = vocab1.get(s)
            printf(tradut2 + " ")
