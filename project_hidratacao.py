import tkinter as tk
from tkinter import messagebox
from plyer import notification
import threading
import time

class HidratarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Despertador de Hidratação 💧")
        self.root.geometry("300x200")
        self.intervalo = 60 * 60  # 1 hora

        self.tempo_restante = self.intervalo
        self.rodando = False

        self.label = tk.Label(root, text="Tempo até o próximo copo de água:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.tempo_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
        self.tempo_label.pack()

        self.botao_iniciar = tk.Button(root, text="Iniciar", command=self.iniciar_timer)
        self.botao_iniciar.pack(pady=10)

        self.botao_parar = tk.Button(root, text="Parar", command=self.parar_timer)
        self.botao_parar.pack(pady=5)

        self.atualizar_timer()

    def iniciar_timer(self):
        if not self.rodando:
            self.rodando = True
            threading.Thread(target=self.contador).start()

    def parar_timer(self):
        self.rodando = False

    def contador(self):
        while self.rodando and self.tempo_restante > 0:
            time.sleep(1)
            self.tempo_restante -= 1
        if self.rodando:
            self.alertar()

    def alertar(self):
        notification.notify(
            title="🚰 Hora de beber água!",
            message="Mantenha-se hidratado!",
            timeout=10
        )
        messagebox.showinfo("Hora de Hidratar!", "Levante-se e beba um copo de água 💧")
        self.tempo_restante = self.intervalo
        self.contador()

    def atualizar_timer(self):
        minutos = self.tempo_restante // 60
        segundos = self.tempo_restante % 60
        self.tempo_label.config(text=f"{minutos:02d}:{segundos:02d}")
        self.root.after(1000, self.atualizar_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = HidratarApp(root)
    root.mainloop()
