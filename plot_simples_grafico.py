import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]
vendas = [120, 150, 170, 160, 210]

plt.plot(meses, vendas, marker="o")
plt.title("Vendas da Loja Virtual")
plt.xlabel("Mes")
plt.ylabel("Vendas")
plt.savefig("grafico.png")
print("Grafico gerado com sucesso: grafico.png")
