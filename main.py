from PyPDF2 import PdfReader
import matplotlib.pyplot as plt
import pandas as pd


class reader():
    def __init__(self): #Criando variaveis essenciais para classe
        self.reader = PdfReader("notas.pdf")
        self.notasAlunos = []
        self.media = 0
        
    def tratarNotas(self, stringNota): #Faz o segundo tratamento no arquivo pdf obtendo a nota do aluno
        stringNota = stringNota.split(' ')
        stringNota = stringNota[len(stringNota)- 1]        
        notaMin, notaMax = stringNota.split('/')[0], stringNota.split('/')[1]
        return notaMin, notaMax
    
    def extractBase(self, numPage): #Faz o primeiro tratamento do pdf chamando a função de cima para auxiliar
        page = self.reader.pages[numPage]
        pagina = page.extract_text()
        pagina = pagina.splitlines()
        notas = pagina[len(pagina) - 1].encode().decode('utf-8')
        notaAluno, notaMax = self.tratarNotas(notas)
        return notaAluno

    def plotarGrafico(self): #transforma as notas em gráficos
        num0, num5, num10, num15,num20,num24, num25 = 0, 0, 0, 0, 0, 0, 0
        for nota in self.notasAlunos:
            nota = float(nota)
            if(nota == 0):
                num0 += 1
            elif(5 > nota > 0):
                num5 += 1
            elif(10> nota >= 5):
                num10 += 1
            elif(15> nota >= 10):
                num15 += 1
            elif(20> nota >= 15):
                num20 += 1
            elif(25> nota >= 20):
                num24 += 1
            elif( nota == 25):
                num25 += 1
        data = {'notas': ['0', 'até 5', 'até 10', 'até 15', 'até 20', 'até 24', '25'], 'numero de alunos':[num0, num5, num10, num15, num20, num24, num25]}
        df = pd.DataFrame(data)
        
        colors = ['red', 'orange', 'yellow', 'grey', 'blue', 'purple', 'green']
        plt.bar(df['notas'], df['numero de alunos'], color=colors)
        plt.title('Notas dos alunos',fontsize=14)
        plt.xlabel('Notas. Media geral da turma = {:.2f}'.format(self.media), fontsize=14)
        plt.ylabel('Numero de alunos', fontsize=14)
        plt.show()

    def calcularMedia(self): #Calcula a médias das notas de todos os alunos
        soma = 0
        for nota in self.notasAlunos:
            soma += float(nota)
        self.media = soma/len(self.notasAlunos)
        
    
    def loopNotas(self): #roda todas as paginas do pdf
        for x in range(self.reader.numPages):
            try:
                self.notasAlunos.append(self.extractBase(x))
                
            except:
                pass
        self.calcularMedia()
        self.plotarGrafico()
        
teste = reader()
teste.loopNotas()
