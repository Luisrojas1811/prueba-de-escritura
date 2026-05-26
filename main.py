import tkinter as tk
import time
import random

FRASES = [
    "El cielo es azul y el mar es profundo",
    "Python es un lenguaje de programación poderoso",
    "La práctica hace al maestro cada día",
    "Aprender a programar requiere paciencia y dedicación",
    "El código limpio es fácil de leer y entender"
]

tiempo_inicio = None

def iniciar_prueba():
    global tiempo_inicio
    frase = random.choice(FRASES)
    etiqueta_frase.config(text=frase)
    entrada.config(state="normal")
    entrada.delete(0, tk.END)
    resultado.config(text="")
    tiempo_inicio = time.time()
    entrada.focus()

def verificar_escritura(event):
    if tiempo_inicio is None:
        return
    texto_escrito = entrada.get()
    frase_actual = etiqueta_frase.cget("text")
    if texto_escrito == frase_actual:
        tiempo_total = round(time.time() - tiempo_inicio, 2)
        resultado.config(text=f"✅ Correcto! Tardaste {tiempo_total} segundos.")
        entrada.config(state="disabled")

ventana = tk.Tk()
ventana.title("Prueba de Escritura Veloz")
ventana.geometry("500x300")

tk.Label(ventana, text="Copiá la siguiente frase:", font=("Arial", 12)).pack(pady=10)
etiqueta_frase = tk.Label(ventana, text="", font=("Arial", 13, "bold"), wraplength=450)
etiqueta_frase.pack(pady=10)

entrada = tk.Entry(ventana, width=55, state="disabled")
entrada.pack(pady=10)
entrada.bind("<KeyRelease>", verificar_escritura)

tk.Button(ventana, text="Nueva frase", command=iniciar_prueba).pack(pady=10)
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack()

ventana.mainloop()