import pandas as pd

dane = {
    'ananas':[3,5,0,2],
    'jabłko':[4,7,2,1],
    'pomarańcza':[2,3,8,9]
}

p = pd.DataFrame(dane)
print(p)

p = pd.DataFrame(dane,index=['Janek','Paula','Karol','Tekla'])
print(p)

print(p.loc['Janek'])

p.to_csv('owoce.csv')
read = pd.read_csv('owoce.csv')
print(read)
