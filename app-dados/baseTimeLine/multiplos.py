import pandas as pd

# # Lê todas as abas do arquivo Excel
all_dfs = pd.read_excel("./BaseTimeLine.xlsx", sheet_name=None)

# Itera sobre as abas e salva cada uma como um arquivo CSV
for sheet_name, df in all_dfs.items():
    df.to_csv(f"./{sheet_name}.csv", index=False, header=True)

# 
# 
#import pandas as pd

# Lê o arquivo Excel com várias abas
# Substitua 'Sheet1' pelo nome da aba que você deseja ler
# Se você não especificar o nome da aba, ele lerá a primeira por padrão
#sheet_name = 'Sheet1'
#df = pd.read_excel("./BaseNavio.xlsx", sheet_name=sheet_name)

# Salva como CSV
#df.to_csv("./BaseNavio.csv", index=False, header=True)

#  