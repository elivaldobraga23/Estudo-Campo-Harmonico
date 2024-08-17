
graus = ['Qual o I Grau?', 'Qual o II Grau?', 'Qual o III Grau?',
         'Qual o IV Grau?', 'Qual o V Grau?', 'Qual o VI Grau?', 'Qual o VII Grau?',]
total = total_acerto = total_erro = 0
print('-='*20)
print(f'{"ESTUDO DO CAMPO HARMÔNICO":^40}')
print('-='*20)
nota = str(input('Qual nota você quer estudar? ')).capitalize().strip()
while nota not in 'CDEFGABC#D#E#F#G#A#B#CbDbEbFbGbAbBb':
    nota = str(input('Qual nota você quer estudar? ')).capitalize().strip()
print('-' * 40)
print(f'Você escolheu a nota {nota}')
print('-' * 40)
print('vamos começar...')
print('-' * 40)
print('ESCREVA [FIM] QUANDO QUISER PARAR!')
print('-' * 40)
while True:
    if nota == 'C':
        pergunta = random.choice(graus)
        resposta = str(input(f'{pergunta} de {nota}: ')).capitalize().strip()
        if pergunta == 'Qual o I Grau?' and resposta == 'C':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o I Grau?' and resposta != 'C':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta == 'Dm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta != 'Dm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta == 'Em':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta != 'Em':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta == 'F':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta != 'F':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta == 'G':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta != 'G':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta == 'Am':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta != 'Am':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta == 'Bdim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta != 'Bdim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
    if nota == 'D':
        pergunta = random.choice(graus)
        resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
        if pergunta == 'Qual o I Grau?' and resposta == 'D':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o I Grau?' and resposta != 'D':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta == 'Em':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta != 'Em':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta == 'F#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta != 'F#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta == 'G':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta != 'G':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta == 'A':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta != 'A':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta == 'Bm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta != 'Bm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta == 'C#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta != 'C#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
    if nota == 'E':
        pergunta = random.choice(graus)
        resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
        if pergunta == 'Qual o I Grau?' and resposta == 'E':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o I Grau?' and resposta != 'E':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta == 'F#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta != 'F#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta == 'G#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta != 'G#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta == 'A':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta != 'A':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta == 'B':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta != 'B':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta == 'C#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta != 'C#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta == 'D#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta != 'D#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
    if nota == 'F':
        pergunta = random.choice(graus)
        resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
        if pergunta == 'Qual o I Grau?' and resposta == 'F':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o I Grau?' and resposta != 'F':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta == 'Gm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta != 'Gm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta == 'Am':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta != 'Am':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta == 'Bb':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta != 'Bb':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta == 'C':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta != 'C':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta == 'Dm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta != 'Dm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta == 'Edim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta != 'Edim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
    if nota == 'G':
        pergunta = random.choice(graus)
        resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
        if pergunta == 'Qual o I Grau?' and resposta == 'G':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o I Grau?' and resposta != 'G':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta == 'Am':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta != 'Am':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta == 'Bm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta != 'Bm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta == 'C':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta != 'C':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta == 'D':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta != 'D':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta == 'Em':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta != 'Em':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta == 'F#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta != 'F#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
    if nota == 'A':
        pergunta = random.choice(graus)
        resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
        if pergunta == 'Qual o I Grau?' and resposta == 'A':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o I Grau?' and resposta != 'A':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta == 'Bm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta != 'Bm':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta == 'C#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta != 'C#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta == 'D':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta != 'D':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta == 'E':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta != 'E':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta == 'F#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta != 'F#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta == 'G#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta != 'G#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
    if nota == 'B':
        pergunta = random.choice(graus)
        resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
        if pergunta == 'Qual o I Grau?' and resposta == 'B':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o I Grau?' and resposta != 'B':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta == 'C#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o II Grau?' and resposta != 'C#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta == 'D#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o III Grau?' and resposta != 'D#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta == 'E':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o IV Grau?' and resposta != 'E':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta == 'F#':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o V Grau?' and resposta != 'F#':
            if pergunta in graus and resposta == 'Fim':
                break
        elif pergunta == 'Qual o VI Grau?' and resposta == 'G#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VI Grau?' and resposta != 'G#m':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta == 'A#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('Parabéns, VOCÊ ACERTOU!')
            total_acerto += 1
            total += 1
        elif pergunta == 'Qual o VII Grau?' and resposta != 'A#dim':
            if pergunta in graus and resposta == 'Fim':
                break
            print('VOCÊ ERROU!')
            total_erro += 1
            total += 1
while True:
    continuar = str(input('Deseja escolher outra nota? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
    nota = str(input('Qual nota você quer estudar? ')).capitalize().strip()
    while nota not in 'CDEFGABC#D#E#F#G#A#B#CbDbEbFbGbAbBb':
        nota = str(input('Qual nota você quer estudar? ')).capitalize().strip()
    print('-' * 40)
    print(f'Você escolheu a nota {nota}')
    print('-' * 40)
    print('vamos começar...')
    print('-' * 40)
    print('ESCREVA [FIM] QUANDO QUISER PARAR!')
    print('-' * 40)
    while True:
        if nota == 'C':
            pergunta = random.choice(graus)
            resposta = str(input(f'{pergunta} de {nota}: ')).capitalize().strip()
            if pergunta == 'Qual o I Grau?' and resposta == 'C':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o I Grau?' and resposta != 'C':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta == 'Dm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta != 'Dm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta == 'Em':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta != 'Em':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta == 'F':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta != 'F':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta == 'G':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta != 'G':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta == 'Am':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta != 'Am':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta == 'Bdim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta != 'Bdim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
        if nota == 'D':
            pergunta = random.choice(graus)
            resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
            if pergunta == 'Qual o I Grau?' and resposta == 'D':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o I Grau?' and resposta != 'D':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta == 'Em':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta != 'Em':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta == 'F#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta != 'F#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta == 'G':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta != 'G':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta == 'A':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta != 'A':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta == 'Bm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta != 'Bm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta == 'C#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta != 'C#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
        if nota == 'E':
            pergunta = random.choice(graus)
            resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
            if pergunta == 'Qual o I Grau?' and resposta == 'E':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o I Grau?' and resposta != 'E':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta == 'F#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta != 'F#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta == 'G#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta != 'G#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta == 'A':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta != 'A':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta == 'B':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta != 'B':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta == 'C#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta != 'C#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta == 'D#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta != 'D#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
        if nota == 'F':
            pergunta = random.choice(graus)
            resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
            if pergunta == 'Qual o I Grau?' and resposta == 'F':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o I Grau?' and resposta != 'F':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta == 'Gm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta != 'Gm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta == 'Am':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta != 'Am':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta == 'Bb':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta != 'Bb':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta == 'C':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta != 'C':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta == 'Dm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta != 'Dm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta == 'Edim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta != 'Edim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
        if nota == 'G':
            pergunta = random.choice(graus)
            resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
            if pergunta == 'Qual o I Grau?' and resposta == 'G':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o I Grau?' and resposta != 'G':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta == 'Am':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta != 'Am':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta == 'Bm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta != 'Bm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta == 'C':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta != 'C':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta == 'D':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta != 'D':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta == 'Em':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta != 'Em':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta == 'F#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta != 'F#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
        if nota == 'A':
            pergunta = random.choice(graus)
            resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
            if pergunta == 'Qual o I Grau?' and resposta == 'A':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o I Grau?' and resposta != 'A':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta == 'Bm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta != 'Bm':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta == 'C#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta != 'C#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta == 'D':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta != 'D':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta == 'E':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta != 'E':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta == 'F#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta != 'F#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta == 'G#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta != 'G#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
        if nota == 'B':
            pergunta = random.choice(graus)
            resposta = str(input(f'{pergunta} de {nota}: ')).capitalize()
            if pergunta == 'Qual o I Grau?' and resposta == 'B':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o I Grau?' and resposta != 'B':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta == 'C#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o II Grau?' and resposta != 'C#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta == 'D#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o III Grau?' and resposta != 'D#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta == 'E':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o IV Grau?' and resposta != 'E':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta == 'F#':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o V Grau?' and resposta != 'F#':
                if pergunta in graus and resposta == 'Fim':
                    break
            elif pergunta == 'Qual o VI Grau?' and resposta == 'G#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VI Grau?' and resposta != 'G#m':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta == 'A#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('Parabéns, VOCÊ ACERTOU!')
                total_acerto += 1
                total += 1
            elif pergunta == 'Qual o VII Grau?' and resposta != 'A#dim':
                if pergunta in graus and resposta == 'Fim':
                    break
                print('VOCÊ ERROU!')
                total_erro += 1
                total += 1
print('-=' * 20)
print(f'{"PROGRAMA FINALIZADO!":^40}')
print('-=' * 20)
print(f'Você respondeu {total} perguntas.')
print('-' * 40)
print(f'Você ACERTOU {total_acerto}.')
print('-' * 40)
print(f'Você ERROU {total_erro}')
print('-' * 40)
if total_acerto == total_erro:
    print('''Seu desempenho foi equilibrado. Há espaço para melhorar!
Tente novamente para aumentar sua taxa de acertos.''')
elif total_acerto > total_erro:
    print('PARABÉNS! Você teve mais acertos do que erros. Ótimo trabalho!')
elif total_acerto < total_erro:
    print('Não desanime! Continue praticando e você verá melhorias!')
print('-' * 40)
