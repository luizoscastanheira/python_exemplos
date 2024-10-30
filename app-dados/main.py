import pandas as pd

# Lê o arquivo Excel
read_file = pd.read_excel("./BaseNavio.xlsx")

# Salva como CSV
read_file.to_csv("./BaseNavio.csv", index=False, header=True)


#

# 
#