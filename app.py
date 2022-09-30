from openpyxl import Workbook, load_workbook

planilha = load_workbook("./cadastro.xlsx")
tabela = planilha.active

# A1 - nome
# B1 - cpf
# C1 - setor
# D1 - entrada
# E1 - saida
# G1 - salario
# H1 - auxilio
# I1 - vendas
# J1 - producao
# K1 - comissao
# L1 - remuneracao


tabela['A2'] = "maikel"
print(tabela['A2'].value)

planilha.save("./cadastro.xlsx")
