from socket import *
import customtkinter as tk
from tkinter import simpledialog, messagebox


class MathProblemGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Генератор математических примеров")

        self.start_menu()

    def start_menu(self):
        self.clear_widgets()

        self.start_label = tk.CTkLabel(self.master, text="Добро пожаловать в Генератор математических примеров!", font=("Helvetica", 14))
        self.start_label.pack(pady=20)

        self.start_button = tk.CTkButton(self.master, text="Начать решать примеры", command=self.choose_operations)
        self.start_button.pack()

        self.info_button = tk.CTkButton(self.master, text="Информация о приложении", command=self.show_info)
        self.info_button.pack()

        self.quit_button = tk.CTkButton(self.master, text="Выйти из приложения", command=self.master.quit)
        self.quit_button.pack()

        self.scores = {}

    def clear_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def choose_operations(self):
        self.clear_widgets()

        self.label = tk.CTkLabel(self.master, text="Выберите типы операций, которые вы хотите решать (+, -, *, /, ^), разделяя их запятыми:")
        self.label.pack()

        self.operations_entry = tk.CTkEntry(self.master)
        self.operations_entry.pack()

        self.start_button = tk.CTkButton(self.master, text="Начать", command=self.start_game)
        self.start_button.pack()

        self.back_button = tk.CTkButton(self.master, text="Вернуться в главное меню", command=self.start_menu)
        self.back_button.pack()

    def start_game(self):
        client = socket(AF_INET, SOCK_STREAM)

        client.connect(('ip', port)) # вставьте ip сервера и порт

        operations = self.operations_entry.get().split(',')
        operations = [op.strip() for op in operations]

        self.clear_widgets()

        self.scores = {}

        for operation in operations:
            score = 0
            while True:
                client.send(operation.encode('utf-8'))

                problem, correct_answer = client.recv(1024).decode('utf-8').split('|')

                user_answer = simpledialog.askinteger("Решите пример", problem)

                if user_answer == int(correct_answer):
                    messagebox.showinfo("Результат", "Правильно!")
                    score += 1
                else:
                    messagebox.showerror("Результат", f"Неправильно. Правильный ответ: {correct_answer}")

                play_again = messagebox.askyesno("Продолжить игру", "Хотите продолжить игру?")
                client.send(str(play_again).encode('utf-8'))
                if not play_again:
                    messagebox.showinfo("Игра завершена", f"Ваш счет за операцию '{operation}': {score}")
                    self.scores[operation] = score
                    break

    def show_info(self):
        messagebox.showinfo("Информация о приложении", "Это приложение позволяет генерировать и решать математические примеры различных типов операций.")


def main():
    root = tk.CTk()
    app = MathProblemGeneratorApp(root)
    root.mainloop()


main()
