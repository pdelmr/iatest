import random
import tkinter as tk
from tkinter import messagebox


def generate_addition(max_digits=4):
    max_value = 10 ** max_digits - 1
    a = random.randint(0, max_value)
    b = random.randint(0, max_value)
    return a, b, a + b


def generate_subtraction(max_digits=4):
    max_value = 10 ** max_digits - 1
    a = random.randint(0, max_value)
    b = random.randint(0, a)
    return a, b, a - b


OPERATIONS = {
    '+': generate_addition,
    '-': generate_subtraction,
}


class MathApp:
    def __init__(self, master):
        self.master = master
        master.title("Ejercicios de Matemáticas")

        self.problem_label = tk.Label(master, text="")
        self.problem_label.pack(pady=5)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(master, textvariable=self.answer_var)
        self.answer_entry.pack(pady=5)

        self.check_button = tk.Button(master, text="Comprobar", command=self.check_answer)
        self.check_button.pack(pady=5)

        self.feedback_label = tk.Label(master, text="")
        self.feedback_label.pack(pady=5)

        self.next_button = tk.Button(master, text="Siguiente", command=self.new_problem)
        self.next_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Salir", command=master.destroy)
        self.exit_button.pack(pady=5)

        self.current_result = None
        self.new_problem()

    def new_problem(self):
        op = random.choice(list(OPERATIONS.keys()))
        a, b, self.current_result = OPERATIONS[op]()
        self.problem_label.config(text=f"¿Cuánto es {a} {op} {b}?")
        self.answer_var.set("")
        self.feedback_label.config(text="")

    def check_answer(self):
        try:
            answer = int(self.answer_var.get())
        except ValueError:
            self.feedback_label.config(text="Introduce un número válido.")
            return
        if answer == self.current_result:
            self.feedback_label.config(text="¡Correcto!")
        else:
            self.feedback_label.config(
                text=f"Incorrecto. La respuesta correcta es {self.current_result}.")


def main():
    root = tk.Tk()
    app = MathApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
