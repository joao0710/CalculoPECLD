import customtkinter


# Configurações da janela
customtkinter.set_appearance_mode("Dark")  # "System", "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # "blue", "green", "dark-blue"


class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("Tela de Login")
        self.geometry("400x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Frame principal para agrupar os widgets
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Label do título
        self.label = customtkinter.CTkLabel(master=self.frame, text="Login", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=12, padx=10)

        # Campo de entrada para o nome de usuário
        self.user_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Usuário")
        self.user_entry.pack(pady=12, padx=10)

        # Campo de entrada para a senha
        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Senha", show="*")
        self.password_entry.pack(pady=12, padx=10)

        # Botão de login
        self.button = customtkinter.CTkButton(master=self.frame, text="Entrar", command=self.login_event)
        self.button.pack(pady=12, padx=10)

    def login_event(self):
        # Lógica de verificação de login (pode ser substituída pela sua)
        username = self.user_entry.get()
        password = self.password_entry.get()
        print(f"Usuário: {username}")
        print(f"Senha: {password}")

        if username == "admin" and password == "123":
            print("Login bem-sucedido!")
            # Você pode adicionar a lógica para abrir uma nova janela aqui
        else:
            print("Usuário ou senha inválidos.")
