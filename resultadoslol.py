import pandas as pd


Readteam = {'Invocador': ['PadeiroZac', 'victodestruidor', 'LucaoTV', 'LuaPlicesinha', 'Is4Vil4r'],
            'Damage': [17.212, 22.971, 28.087, 22.908, 9.275],
            'Gold': [12.100, 13.500, 14.800, 12.100, 11.400]}

Blueteam = {'Invocador': ['CABEÇA QUADRADA', 'IDhipsy19', 'AishaSZ', 'tuffy', 'Zarpellone'],
            'Damage': [11.674, 19.838, 32.774, 20.855, 28.522],
            'Gold': [12.100, 13.500, 14.800, 12.100, 11.400]}

Readteam_df = pd.DataFrame(Readteam)
Blueteam_df = pd.DataFrame(Blueteam)

print('Resumo da partida')
print('Read Team')
print(Readteam_df)
print('Blueteam')
print(Blueteam_df)
print('Invocador do time vermelho com maior dano:')
print(Readteam_df.loc[1, ['Invocador', 'Damage']])
print('Invocador do time azul com maior dano:')
print(Blueteam_df.loc[2, ['Invocador', 'Damage']])
print('Invocador com maior dano da partida')
print(Blueteam_df.loc[2, ['Invocador', 'Damage']])
