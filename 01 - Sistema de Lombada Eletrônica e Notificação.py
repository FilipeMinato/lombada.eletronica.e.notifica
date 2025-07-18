"""
Sistema de Lombada Eletrônica com Interface Gráfica
---------------------------------------------------
Este programa simula o funcionamento de um radar de lombada eletrônica.
O usuário insere a velocidade registrada de um veículo e o sistema:
- Verifica se a velocidade está acima do limite permitido (com tolerância de 10%)
- Classifica o tipo de infração: média, grave ou gravíssima
- Gera dados fictícios do veículo para simular uma notificação oficial
- Exibe os detalhes da infração e do veículo

Ideal para simulações, testes educativos ou demonstrações.
"""

# Importa a biblioteca tkinter para criar a interface gráfica
import tkinter as tk
from tkinter import messagebox

# Importa a biblioteca random para gerar dados aleatórios
import random

# Dicionários e listas com dados fictícios para simulação
modelos = {
    'carro': ['Fiat Uno', 'Chevrolet Onix', 'Volkswagen Gol', 'Hyundai HB20'],
    'moto': ['Honda CG 160', 'Yamaha Fazer 250', 'Honda Biz', 'Kawasaki Ninja'],
    'caminhao': ['Volkswagen Constellation', 'Scania R440', 'Mercedes-Benz Atego']
}
cores = ['preto', 'branco', 'prata', 'vermelho', 'azul', 'cinza']
tipos = ['carro', 'moto', 'caminhao']

# Classe principal do sistema
class SistemaLombada:
    def __init__(self, root):
        # Inicializa a janela principal
        self.root = root
        self.root.title("Sistema de Lombada Eletrônica")
        self.root.geometry("500x500")  # Define o tamanho da janela

        # Cria um frame (container) para agrupar os elementos
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Título do sistema
        self.label_intro = tk.Label(self.frame, text="SISTEMA DE LOMBADA ELETRÔNICA", font=("Helvetica", 16, "bold"))
        self.label_intro.pack(pady=10)

        # Instrução para o usuário
        self.label_info = tk.Label(self.frame, text="Insira a velocidade registrada do veículo (em km/h):")
        self.label_info.pack(pady=5)

        # Campo de entrada de velocidade
        self.entry_velocidade = tk.Entry(self.frame, font=("Helvetica", 14))
        self.entry_velocidade.pack(pady=5)

        # Botão que aciona a verificação
        self.btn_verificar = tk.Button(self.frame, text="Verificar", command=self.verificar)
        self.btn_verificar.pack(pady=10)

        # Área de texto para mostrar os resultados
        self.text_resultado = tk.Text(self.frame, width=60, height=20, font=("Courier", 10))
        self.text_resultado.pack()

    # Função que verifica a velocidade inserida
    def verificar(self):
        # Limpa o conteúdo anterior da área de texto
        self.text_resultado.delete('1.0', tk.END)

        try:
            # Converte o valor inserido para número decimal, aceitando "," ou "."
            velocidade = float(self.entry_velocidade.get().replace(",", "."))

            # Gera aleatoriamente os dados do veículo
            tipo_veiculo = random.choice(tipos)
            modelo = random.choice(modelos[tipo_veiculo])
            cor = random.choice(cores)
            ano = random.randint(2015, 2023)
            # Placa no formato AAA-1234
            placa = f"{chr(random.randint(65,90))}{chr(random.randint(65,90))}{chr(random.randint(65,90))}-{random.randint(1000,9999)}"

            # Define o limite da via e a margem de tolerância (10%)
            limite = 80
            margem = limite * 0.10
            tolerancia = limite + margem

            self.text_resultado.insert(tk.END, f"➡️  Limite da via: {limite} km/h (+10% = {tolerancia:.1f} km/h)\n")

            # Verifica se está dentro do limite com tolerância
            if velocidade <= tolerancia:
                self.text_resultado.insert(tk.END, "✅ Dentro da velocidade permitida. Nenhuma infração registrada.\n")
            else:
                # Calcula o excesso de velocidade
                excesso = velocidade - limite
                percentual = (excesso / limite) * 100

                # Define o tipo de infração com base no percentual
                if percentual <= 20:
                    multa = 193.50
                    pontos = 4
                    mensagem = "Infração média: até 20% acima do limite."
                elif percentual <= 50:
                    multa = 478.50
                    pontos = 5
                    mensagem = "Infração grave: entre 20% e 50% acima do limite."
                else:
                    multa = 1461.10
                    pontos = "Suspensão imediata da CNH"
                    mensagem = "Infração gravíssima: mais de 50% acima do limite."

                # Exibe os dados da infração na tela
                self.text_resultado.insert(tk.END, "\n🚨 INFRAÇÃO DETECTADA!\n")
                self.text_resultado.insert(tk.END, f"{mensagem}\n")
                self.text_resultado.insert(tk.END, f"Multa: R${multa:.2f}\n")
                self.text_resultado.insert(tk.END, f"Pontos: {pontos}\n")

                # Simula a notificação que seria enviada ao proprietário
                self.text_resultado.insert(tk.END, "\n=== NOTIFICAÇÃO DE INFRAÇÃO ===\n")
                self.text_resultado.insert(tk.END, f"Veículo: {modelo.upper()} ({tipo_veiculo})\n")
                self.text_resultado.insert(tk.END, f"Cor: {cor.capitalize()} | Ano/Modelo: {ano}/{ano+1}\n")
                self.text_resultado.insert(tk.END, f"Placa: {placa}\n")
                self.text_resultado.insert(tk.END, f"Velocidade registrada: {velocidade:.1f} km/h\n")
                self.text_resultado.insert(tk.END, f"Velocidade permitida (com tolerância): até {tolerancia:.1f} km/h\n")
                self.text_resultado.insert(tk.END, f"Infração: {mensagem}\n")
                self.text_resultado.insert(tk.END, f"Valor da multa: R${multa:.2f}\n")
                self.text_resultado.insert(tk.END, f"Pontos na CNH: {pontos}\n")
                self.text_resultado.insert(tk.END, "Esta notificação será enviada ao proprietário do veículo.\n")

        # Caso o valor inserido não seja válido
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira uma velocidade válida (ex: 85 ou 90.5).")

# Executa o sistema se o arquivo for rodado diretamente
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = SistemaLombada(root)  # Inicializa a aplicação
    root.mainloop()  # Inicia o loop da interface gráfica
