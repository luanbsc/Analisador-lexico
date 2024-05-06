import os

def estados (estado_atual, caractere, lexema, ultimo_token):
    palavras_reservadas = ["algoritmo", "principal", "variaveis", "constantes",
                           "registro", "funcao", "retorno", "vazio", "se", "senao",
                           "enquanto", "leia", "escreva", "inteiro", "real", "booleano", "char", "cadeia", "verdadeiro", "falso"]
    delimitadores = [';', ',', '.', '(', ')', '[', ']', '{', '}']

    #Estado inicial
    if estado_atual == 0:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
        elif caractere.isspace():
            pass
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
        else:
            lexema += caractere
            estado_atual = 5
    
    #Estado com possibilidade de palavras reservadas ou identificadores
    elif estado_atual == 1:
        if caractere.isalpha() or caractere == '_' and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 1
        elif caractere == '&':
            lexema += caractere
            estado_atual = 22
        elif caractere == '|':
            lexema += caractere
            estado_atual = 25
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            if lexema[:len(lexema)-1] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 7
    
    #Estado dos numeros
    elif estado_atual == 2:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 28
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
        elif caractere == '.':
            lexema += caractere
            estado_atual = 33
        elif caractere == '&':
            lexema += caractere
            estado_atual = 35
        elif caractere == '|':
            lexema += caractere
            estado_atual = 36
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'NRO', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'NRO', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'NRO', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'NRO', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'NRO', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'NRO', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'NRO', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'NRO', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'NRO', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 28

    #Estado com possibilidade de operadores relacionais ou operador lógico
    elif estado_atual == 3:
        if caractere == '=':
            lexema += caractere
            estado_atual = 4
        elif caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'REL' , lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'REL' , lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'REL' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'REL' , lexema, estado_atual
        elif caractere == '<' or caractere == '>':
            lexema += caractere
            estado_atual = 3
            return 'REL' , lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'REL' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'REL' , lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'REL' , lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'REL' , lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'REL' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'REL' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'REL' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'REL' , lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'REL' , lexema, estado_atual
    
    #Estado final dos operadores relacionais ==, <= e >=
    elif estado_atual == 4:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'REL' , lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'REL' , lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'REL' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'REL' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'REL' , lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'REL' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'REL' , lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'REL' , lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'REL' , lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'REL' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'REL' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'REL' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'REL' , lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'REL' , lexema, estado_atual
    
    #Estado final do token mal formado
    elif estado_atual == 5:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'TMF', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'TMF', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 37
        elif caractere == '|':
            lexema += caractere
            estado_atual = 38
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'TMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'TMF' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'TMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'TMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'TMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'TMF' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'TMF' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'TMF' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'TMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
    
    #Estado dos delimitadores
    elif estado_atual == 6:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'DEL', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'DEL', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'DEL' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'DEL' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'DEL', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'DEL' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'DEL', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'DEL', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'DEL', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'DEL' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'DEL' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'DEL' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'DEL', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'DEL', lexema, estado_atual
    
    #Estado de identificador mal formado
    elif estado_atual == 7:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 7
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 7
        elif caractere == '&':
            lexema += caractere
            estado_atual = 31
        elif caractere == '|':
            lexema += caractere
            estado_atual = 32
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'IMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'IMF' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'IMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'IMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'IMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'IMF' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'IMF' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'IMF' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'IMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 7
    
    #Estado para identificar se é um comentario de linha, operador aritmetico ou comentario de bloco
    elif estado_atual == 8:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'ART', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'ART', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'ART' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'ART' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'ART', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'ART' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'ART', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'ART', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 9
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'ART' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'ART' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 26
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'ART', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'ART', lexema, estado_atual
    
    #Estado final de um comentário de linha
    elif estado_atual == 9:
        pass

    #Estado da cadeia de caracteres
    elif estado_atual == 10:
        if caractere == '"':
            lexema += caractere
            estado_atual = 11
        elif ord(caractere) >= 32 and ord(caractere) <= 126:
            lexema += caractere
        else:
            lexema += caractere
            estado_atual = 12
    
    #Estado final da cadeia de caracteres
    elif estado_atual == 11:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'CAC', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'CAC', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'CAC' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'CAC' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'CAC', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'CAC' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'CAC', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'CAC', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'CAC', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'CAC' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'CAC' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'CAC' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'CAC', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'CAC', lexema, estado_atual
    
    #Estado de cadeia de caracteres mal formado
    elif estado_atual == 12:
        if caractere == '"':
            lexema += caractere
            estado_atual = 13
        else:
            lexema += caractere

    #Estado final de cadeia de caracteres mal formado
    elif estado_atual == 13:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'CMF', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'CMF', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'CMF' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'CMF' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'CMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'CMF' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'CMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'CMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'CMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'CMF' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'CMF' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'CMF' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'CMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'CMF', lexema, estado_atual

    #Estado de operador aritmetico + ou ++
    elif estado_atual == 14:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'ART', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'ART', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'ART' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'ART' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'ART', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'ART' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'ART', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'ART', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'ART', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 15
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'ART' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'ART' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'ART', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'ART', lexema, estado_atual
    
    #Estado final de operador aritmetico ++
    elif estado_atual == 15:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'ART', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'ART', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'ART' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'ART' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'ART', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'ART' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'ART', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'ART', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'ART', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'ART', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'ART' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'ART' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'ART', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'ART', lexema, estado_atual
    
    #Estado de operador aritmetico - ou --
    elif estado_atual == 16:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'ART', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            if not (ultimo_token == 'STARTLINE' or ultimo_token == 'ART' or ultimo_token == 'REL' or ultimo_token == 'LOG'):
                return 'ART', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'ART' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'ART' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'ART', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'ART' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'ART', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'ART', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'ART', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'ART', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 17
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'ART' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'ART', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'ART', lexema, estado_atual
    
    #Estado final de operador aritmetico --
    elif estado_atual == 17:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'ART', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'ART', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'ART' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'ART' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'ART', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'ART' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'ART', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'ART', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'ART', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'ART', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'ART', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'ART' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'ART', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'ART', lexema, estado_atual

    #Estado de operador aritmetico *
    elif estado_atual == 18:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'ART', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'ART', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'ART' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'ART' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'ART', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'ART' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'ART', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'ART', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'ART', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'ART', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'ART', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'ART', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'ART', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'ART', lexema, estado_atual
    
    #Estado de operador logico !
    elif estado_atual == 19:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'LOG', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'LOG', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'LOG' , lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'LOG' , lexema, estado_atual
        elif caractere == '<' or caractere == '>':
            lexema += caractere
            estado_atual = 3
            return 'LOG', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'LOG' , lexema, estado_atual
        elif caractere == '=':
            lexema += caractere
            estado_atual = 4
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'LOG', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'LOG', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'LOG', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'LOG', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'LOG', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'LOG', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'LOG', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'LOG', lexema, estado_atual
    
    #Estado de token mal formado para &
    elif estado_atual == 20:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'TMF', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'TMF', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 21
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'TMF' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'TMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'TMF' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'TMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'TMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'TMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'TMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'TMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'TMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'TMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'TMF', lexema, estado_atual
    
    #Estado de operador logico &&
    elif estado_atual == 21:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'LOG', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'LOG', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'LOG', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'LOG' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'LOG', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'LOG' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'LOG', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'LOG', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'LOG', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'LOG', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'LOG', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'LOG', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'LOG', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'LOG', lexema, estado_atual
    
    #Estado de IDE ou PRE seguido de LOG, ou IMF -> para &
    elif estado_atual == 22:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 7
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 7
        elif caractere == '&':
            lexema += caractere
            estado_atual = 21
            if lexema[:len(lexema)-2] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'IMF' , lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'IMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'IMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'IMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'IMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'IMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'IMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'IMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'IMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'IMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'IMF', lexema, estado_atual
    
    #Estado de token mal formado para |
    elif estado_atual == 23:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'TMF', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'TMF', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'TMF', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 24
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'TMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'TMF' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'TMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'TMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'TMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'TMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'TMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'TMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'TMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'TMF', lexema, estado_atual
    
    #Estado de operador logico ||
    elif estado_atual == 24:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'LOG', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'LOG', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'LOG', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 23
            return 'LOG', lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'LOG', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'LOG' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'LOG', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'LOG', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'LOG', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'LOG', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'LOG', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'LOG', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'LOG', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'LOG', lexema, estado_atual
    
    #Estado de IDE ou PRE seguido de LOG, ou IMF -> para &
    elif estado_atual == 25:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 7
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 7
        elif caractere == '&':
            lexema += caractere
            estado_atual = 20
            return 'IMF', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 24
            if lexema[:len(lexema)-2] in palavras_reservadas:
                return 'PRE', lexema, estado_atual
            else:
                return 'IDE', lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'IMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'IMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'IMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'IMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'IMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'IMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'IMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'IMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'IMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
            return 'IMF', lexema, estado_atual
    
    #Estado do comentario em bloco
    elif estado_atual == 26:
        lexema += caractere
        if caractere == '*':
            estado_atual = 27
    
    #Estado final do comentario em bloco
    elif estado_atual == 27:
        lexema += caractere
        if caractere == '/':
            estado_atual = 0
            lexema = ''
        elif caractere == '*':
            estado_atual = 27
        else:
            estado_atual = 26
    
    #Estado de numero mal formado
    elif estado_atual == 28:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 28
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 28
        elif caractere == '&':
            lexema += caractere
            estado_atual = 29
        elif caractere == '|':
            lexema += caractere
            estado_atual = 30
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'NMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'NMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'NMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'NMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'NMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'NMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'NMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'NMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'NMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 28
    
    #Estado de numero mal formado com possibilidade de ser seguido por &&
    elif estado_atual == 29:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 28
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 28
        elif caractere == '&':
            lexema += caractere
            estado_atual = 21
            return 'NMF', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 30
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'NMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'NMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'NMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'NMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'NMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'NMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'NMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'NMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'NMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 28
    
    #Estado de numero mal formado com possibilidade de ser seguido por ||
    elif estado_atual == 30:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 28
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 28
        elif caractere == '&':
            lexema += caractere
            estado_atual = 29
        elif caractere == '|':
            lexema += caractere
            estado_atual = 24
            return 'NMF', lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'NMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'NMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'NMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'NMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'NMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'NMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'NMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'NMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'NMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 28
    
    #Estado de identificador mal formado com possibilidade de ser seguido por &&
    elif estado_atual == 31:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 7
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 7
        elif caractere == '&':
            lexema += caractere
            estado_atual = 21
            return 'IMF', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 32
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'IMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'IMF' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'IMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'IMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'IMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'IMF' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'IMF' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'IMF' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'IMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 7
    
    #Estado de identificador mal formado com possibilidade de ser seguido por ||
    elif estado_atual == 32:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 7
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 7
        elif caractere == '&':
            lexema += caractere
            estado_atual = 31
        elif caractere == '|':
            lexema += caractere
            estado_atual = 24
            return 'IMF', lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'IMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'IMF' , lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'IMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'IMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'IMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'IMF' , lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'IMF' , lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'IMF' , lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'IMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 7
    
    #Estado dos numeros de ponto flutuante
    elif estado_atual == 33:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 28
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 34
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'NMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 28
    
    #Estado final de numero de ponto flutuante
    elif estado_atual == 34:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 28
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 34
        elif caractere == '.':
            lexema += caractere
            estado_atual = 28
        elif caractere == '&':
            lexema += caractere
            estado_atual = 35
        elif caractere == '|':
            lexema += caractere
            estado_atual = 36
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'NRO', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'NRO', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'NRO', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'NRO', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'NRO', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'NRO', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'NRO', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'NRO', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'NRO', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 28
    
    #Estado de numero de ponto flutuante com possibilidade de ser seguido por &&
    elif estado_atual == 35:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 28
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 28
        elif caractere == '&':
            lexema += caractere
            estado_atual = 21
            return 'NRO', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 30
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'NMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'NMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'NMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'NMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'NMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'NMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'NMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'NMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'NMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 28
    
    #Estado de numero de ponto flutuante com possibilidade de ser seguido por ||
    elif estado_atual == 36:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 28
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 28
        elif caractere == '&':
            lexema += caractere
            estado_atual = 29
        elif caractere == '|':
            lexema += caractere
            estado_atual = 24
            return 'NRO', lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'NMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'NMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'NMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'NMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'NMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'NMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'NMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'NMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'NMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 28
    
    #Estado de TMF com possibilidade de ser seguido por &&
    elif estado_atual == 37:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'TMF', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'TMF', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 21
            return 'TMF', lexema, estado_atual
        elif caractere == '|':
            lexema += caractere
            estado_atual = 38
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'TMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'TMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'TMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'TMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'TMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'TMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'TMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'TMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'TMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
    
    #Estado de TMF com possibilidade de ser seguido por ||
    elif estado_atual == 38:
        if caractere.isalpha() and (ord(caractere) >= 32 and ord(caractere) <= 126):
            lexema += caractere
            estado_atual = 1
            return 'TMF', lexema, estado_atual
        elif caractere.isdigit():
            lexema += caractere
            estado_atual = 2
            return 'TMF', lexema, estado_atual
        elif caractere == '&':
            lexema += caractere
            estado_atual = 37
        elif caractere == '|':
            lexema += caractere
            estado_atual = 24
            return 'TMF', lexema, estado_atual
        elif caractere == '<' or caractere == '>' or caractere == '=':
            lexema += caractere
            estado_atual = 3
            return 'TMF', lexema, estado_atual
        elif caractere == '!':
            lexema += caractere
            estado_atual = 19
            return 'TMF', lexema, estado_atual
        elif caractere in delimitadores:
            lexema += caractere
            estado_atual = 6
            return 'TMF', lexema, estado_atual
        elif caractere.isspace():
            lexema += caractere
            estado_atual = 0
            return 'TMF', lexema, estado_atual
        elif caractere == '/':
            lexema += caractere
            estado_atual = 8
            return 'TMF', lexema, estado_atual
        elif caractere == '+':
            lexema += caractere
            estado_atual = 14
            return 'TMF', lexema, estado_atual
        elif caractere == '-':
            lexema += caractere
            estado_atual = 16
            return 'TMF', lexema, estado_atual
        elif caractere == '*':
            lexema += caractere
            estado_atual = 18
            return 'TMF', lexema, estado_atual
        elif caractere == '"':
            lexema += caractere
            estado_atual = 10
            return 'TMF', lexema, estado_atual
        else:
            lexema += caractere
            estado_atual = 5
    return 0, lexema, estado_atual

    



pasta = './files'

#For para deletar os arquivos saídas ja existentes
for diretorio, pastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if "-saida" in arquivo:
            os.remove(diretorio + '\\' + arquivo)

#For para criação dos arquivos saídas
for diretorio, pastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        acertos = []
        erros = []
        nome_arquivo = arquivo.split('.')[0]+"-saida.txt"

        #Leitura do conteúdo do arquivo de entrada
        with open(diretorio + '\\' + arquivo, 'r') as arquivo_entrada:
            texto = arquivo_entrada.readlines()
            
        #Lendo caractere por caractere para gerar o token
        lexema = ''
        estado_atual = 0
        numero_da_linha = 0
        for linha in texto:
            ultimo_token = 'STARTLINE'
            if estado_atual == 9:
                estado_atual = 0
                lexema = ''
            elif estado_atual == 12 or estado_atual == 10:
                erros.append(str(numero_da_linha) + ' CMF ' + lexema[:len(lexema)-1] + '\n')
                estado_atual = 0
                lexema = ''
            numero_da_linha += 1
            for caractere in linha.strip('\n')+' ':
                token, lexema, estado_atual = estados(estado_atual, caractere, lexema, ultimo_token)
                if estado_atual == 26 and lexema == '/*':
                    numero_da_linha_comentario_bloco = numero_da_linha
                if token != 0:
                    ultimo_token = token
                    if token == 'PRE' or token == 'IDE' or token == 'CAC' or token == 'NRO' or token == 'DEL' or token == 'REL' or token == 'LOG' or token == 'ART':
                        if estado_atual == 21 or estado_atual == 24:
                            acertos.append(str(numero_da_linha) + ' ' + token + ' ' + lexema[:len(lexema)-2] + '\n')
                            lexema = lexema[-2:]
                        else:
                            acertos.append(str(numero_da_linha) + ' ' + token + ' ' + lexema[:len(lexema)-1] + '\n')
                            lexema = lexema[-1]
                    else:
                        if estado_atual == 24 or estado_atual == 21:
                            erros.append(str(numero_da_linha) + ' ' + token + ' ' + lexema[:len(lexema)-2] + '\n')
                            lexema = lexema[-2:]
                        else:
                            erros.append(str(numero_da_linha) + ' ' + token + ' ' + lexema[:len(lexema)-1] + '\n')
                            lexema = lexema[-1]
                    if lexema.isspace():
                        lexema = ''
            if estado_atual == 26 or estado_atual == 27:
                lexema = lexema[:-1] + '\n'
        if estado_atual == 12 or estado_atual == 10:
            erros.append(str(numero_da_linha) + ' CMF ' + lexema[:len(lexema)-1] + '\n')
            estado_atual = 0
            lexema = ''
        elif estado_atual == 26 or estado_atual == 27:
            erros.append(str(numero_da_linha_comentario_bloco) + ' CoMF ' + lexema[:len(lexema)-1] + '\n')
            estado_atual = 0
            lexema = ''
      
        #Preenchendo o arquivo de saída com os tokens
        with open(diretorio + '\\' + nome_arquivo, "a") as arquivo_saida:
            if acertos:
                for i in acertos:
                    arquivo_saida.write(i)
            if erros:
                if acertos:
                    arquivo_saida.write("\n")
                for i in erros:
                    arquivo_saida.write(i)
            else:
                arquivo_saida.write("\nSeu codigo nao possui erros lexicos.")