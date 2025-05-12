import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
#Bibliotécas acima

#Pedindo pro pandas mostrar todas as colunas e linhas do arquivo
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Usando o pandas para ler o arquivo dados.csv
df_original = pd.read_csv("dados.csv", sep= ';', encoding='ISO-8859-1')

#Testes para ver se está tudo certo
print(df_original.shape)
print(df_original.head())
print(df_original.tail())

#Marcando a data mais antiga e a mais nova
inicio = pd.to_datetime(df_original['DATA_AQUISICAO']).dt.date.min()
fim = pd.to_datetime(df_original['DATA_AQUISICAO']).dt.date.max()

#print para mostrar o período dos dados
print('\nPeríodo dos dados - De:', inicio, 'Até', fim,'\n')

#Verificando as informações das colunas e confirmando os tipos de dados
print(df_original.info(),'\n')

#Verificando aonde possuem campos nulos
print(df_original.isnull().sum(),'\n')

#Verificando os pontos nulos
print(df_original[df_original['IDADE_CLIENTE'].isnull()])

#Mostrando a média, mediana e desvio padrão no número de dias ativos
print(df_original['DIAS_ATIVO'].mean())
print(df_original['DIAS_ATIVO'].median())
print(df_original['DIAS_ATIVO'].std())

#Comando para ter uma visão geral dos dados
print(df_original.describe())

#Teste para ver o resultado de valores em específico
print('Valor mínimo: ', df_original['DIAS_ATIVO'].min())
print('Valor máximo: ', df_original['DIAS_ATIVO'].max())
print('Valor da média: ', df_original['DIAS_ATIVO'].mean())
print('Valor da mediana: ', df_original['DIAS_ATIVO'].median())
print('Valor do desvio padrão: ', df_original['DIAS_ATIVO'].std())
print('Valor da moda: ', df_original['DIAS_ATIVO'].mode(),'\n')

#Total de valores únicos
valores_unicos = []
for i in df_original.columns[0:14].tolist():
    print(i, ':', len(df_original[i].astype(str).value_counts()))
    valores_unicos.append(len(df_original[i].astype(str).value_counts()))

#vendo quantos financiamentos de clientes cada produto tem
print('\n', df_original.groupby(['PRODUTO']).size())

#Menor valor financiado
print('\nO menor valor financiado é:', df_original['VALOR_TABELA'].min(),'\n')

#Maior valor financiado
print('O maior valor financiado foi:',df_original['VALOR_TABELA'].max(),'\n')

#Cliente com menor idade
print('O cliente que possui a menor idade possui',df_original['IDADE_CLIENTE'].min(), 'anos\n')

#Cliente com maior idade
print(('O cliente com a maior idade possui'), df_original['IDADE_CLIENTE'].max(), 'anos\n')

#Grafico com BloxPlot
sns.boxplot(data = df_original, y = "DIAS_ATIVO")
plt.show()

#Grafico de histograma
sns.histplot(data = df_original, x = "DIAS_ATIVO")
plt.show()

#Grafico por prazo de financiamento
sns.countplot(data = df_original, x= "PRAZO_FINANCIAMENTO")
plt.show()

#Grafico da quantidade de financiamentos por valor de tabela
sns.countplot(data = df_original, x = "VALOR_TABELA")
plt.show()

#Grafico anterior só que por produto
sns.countplot(data = df_original, x="VALOR_TABELA", hue='PRODUTO')
plt.show()