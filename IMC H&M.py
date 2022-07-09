continuar=('S')
while continuar==('S'):
    altura=float(input("Digite sua altura em metros (use '.', e não ','):"))
    peso=float(input("Digite seu peso em quilos (use '.' e não ','):"))
    idade=int(input('Digite sua idade:'))
    IMC=peso/altura**2
    if idade<10:
        print('Infelizmente esta tabela só funciona para maiores de 10 anos')
    if 10<=idade<20:
        sexo=input("Digite seu sexo ('M' para Masculino e 'F' para Feminino):")
        print ('Este é seu IMC',IMC)
        if sexo==('M'):                               #Sexo MASCULINO<20#
            if idade==10:
                if IMC<14.42:
                    print('Você está abaixo do peso')
                elif 14.42<=IMC<19.60:
                    print('Você está abaixo do peso')
                elif IMC>=19.60:
                    print('Você está em sobrepeso')
            elif idade==11:
                if IMC<14.83:
                    print('Você está abaixo do peso')
                elif 14.83<=IMC<20.35:
                    print('Você está abaixo do peso')
                elif IMC>=20.35:
                    print('Você está em sobrepeso')
            elif idade==12:
                if IMC<15.24:
                    print('Você está abaixo do peso')
                elif 15.24<=IMC<21.12:
                    print('Você está abaixo do peso')
                elif IMC>=21.12:
                    print('Você está em sobrepeso')
            elif idade==13:
                if IMC<15.73:
                    print('Você está abaixo do peso')
                elif 15.73<=IMC<21.93:
                    print('Você está abaixo do peso')
                elif IMC>=21.93:
                    print('Você está em sobrepeso')
            elif idade==14:
                if IMC<16.18:
                    print('Você está abaixo do peso')
                elif 16.18<=IMC<22.77:
                    print('Você está abaixo do peso')
                elif IMC>=22.77:
                    print('Você está em sobrepeso')
            elif idade==15:
                if IMC<16.59:
                    print('Você está abaixo do peso')
                elif 16.59<=IMC<23.63:
                    print('Você está abaixo do peso')
                elif IMC>=23.63:
                    print('Você está em sobrepeso')
            elif idade==16:
                if IMC<17.01:
                    print('Você está abaixo do peso')
                elif 17.01<=IMC<24.45:
                    print('Você está abaixo do peso')
                elif IMC>=24.45:
                    print('Você está em sobrepeso')
            elif idade==17:
                if IMC<17.31:
                    print('Você está abaixo do peso')
                elif 17.31<=IMC<25.28:
                    print('Você está abaixo do peso')
                elif IMC>=25.28:
                    print('Você está em sobrepeso')
            elif idade==18:
                if IMC<17.54:
                    print('Você está abaixo do peso')
                elif 17.54<=IMC<25.95:
                    print('Você está abaixo do peso')
                elif IMC>=25.95:
                    print('Você está em sobrepeso')
            elif idade==19:
                if IMC<17.80:
                    print('Você está abaixo do peso')
                elif 17.80<=IMC<26.36:
                    print('Você está abaixo do peso')
                elif IMC>=26.36:
                    print('Você está em sobrepeso')
        elif sexo==('F'):                               #Sexo FEMININO<20#
            if idade==10:
                if IMC<14.23:
                    print('Você está abaixo do peso')
                elif 14.23<=IMC<20.19:
                    print('Você está abaixo do peso')
                elif IMC>=20.19:
                    print('Você está em sobrepeso')
            elif idade==11:
                if IMC<14.60:
                    print('Você está abaixo do peso')
                elif 14.60<=IMC<21.18:
                    print('Você está abaixo do peso')
                elif IMC>=21.18:
                    print('Você está em sobrepeso')
            elif idade==12:
                if IMC<14.98:
                    print('Você está abaixo do peso')
                elif 14.98<=IMC<22.17:
                    print('Você está abaixo do peso')
                elif IMC>=22.17:
                    print('Você está em sobrepeso')
            elif idade==13:
                if IMC<15.36:
                    print('Você está abaixo do peso')
                elif 15.36<=IMC<23.08:
                    print('Você está abaixo do peso')
                elif IMC>=23.08:
                    print('Você está em sobrepeso')
            elif idade==14:
                if IMC<15.67:
                    print('Você está abaixo do peso')
                elif 15.67<=IMC<23.88:
                    print('Você está abaixo do peso')
                elif IMC>=23.88:
                    print('Você está em sobrepeso')
            elif idade==15:
                if IMC<16.01:
                    print('Você está abaixo do peso')
                elif 16.01<=IMC<24.29:
                    print('Você está abaixo do peso')
                elif IMC>=24.29:
                    print('Você está em sobrepeso')
            elif idade==16:
                if IMC<16.37:
                    print('Você está abaixo do peso')
                elif 16.37<=IMC<24.74:
                    print('Você está abaixo do peso')
                elif IMC>=24.74:
                    print('Você está em sobrepeso')
            elif idade==17:
                if IMC<16.59:
                    print('Você está abaixo do peso')
                elif 16.59<=IMC<25.23:
                    print('Você está abaixo do peso')
                elif IMC>=25.23:
                    print('Você está em sobrepeso')
            elif idade==18:
                if IMC<16.71:
                    print('Você está abaixo do peso')
                elif 16.71<=IMC<25.56:
                    print('Você está abaixo do peso')
                elif IMC>=25.56:
                    print('Você está em sobrepeso')
            elif idade==19:
                if IMC<16.87:
                    print('Você está abaixo do peso')
                elif 16.87<=IMC<25.85:
                    print('Você está abaixo do peso')
                elif IMC>=25.85:
                    print('Você está em sobrepeso')  
    elif idade>=20:                                     #MAIORES DE 20 ANOS#
        print ('Este é seu IMC',IMC)
        if IMC<=18.5:
            print('Você está Abaixo do Peso')
        elif 18.5<IMC<=25.0:
            print('Você está no Peso Normal')
        elif 25<IMC<=30:
            print('Você está na Pré-obesidade')
        elif 30<IMC<=35:
            print('Você está na Obesidade Grau 1')
        elif 35<IMC<=40:
            print('Você está na Obesidade Grau 2')
        elif IMC>40:
            print('Você está na Obesidade de Grau 3')
    continuar=input("Deseja Continuar? Use 'S' ou 'N':")
print('Fim do programa.')