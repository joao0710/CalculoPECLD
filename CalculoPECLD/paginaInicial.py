import customtkinter


# Configurações da janela
customtkinter.set_appearance_mode("System")  # "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("Página Inicial")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)  # A linha 1 (conteúdo) deve se expandir

        # --- Frame da Barra de Menu ---
        self.menu_bar_frame = customtkinter.CTkFrame(self, height=50)
        self.menu_bar_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        self.menu_bar_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Botões do menu
        self.btn_inicio = customtkinter.CTkButton(self.menu_bar_frame, text="Início",
                                                  command=lambda: self.show_page("Início"))
        self.btn_inicio.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.btn_calculos = customtkinter.CTkButton(self.menu_bar_frame, text="Cálculos",
                                                    command=lambda: self.show_page("Cálculos"))
        self.btn_calculos.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.btn_simulacao = customtkinter.CTkButton(self.menu_bar_frame, text="Simulação",
                                                     command=lambda: self.show_page("Simulação"))
        self.btn_simulacao.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        self.btn_logout = customtkinter.CTkButton(self.menu_bar_frame, text="Logout", command=self.logout)
        self.btn_logout.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        # --- Frame do Conteúdo Principal ---
        self.main_content_frame = customtkinter.CTkFrame(self)
        self.main_content_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.main_content_frame.grid_columnconfigure(0, weight=1)
        self.main_content_frame.grid_rowconfigure(0, weight=1)

        # Dicionário para armazenar as páginas
        self.pages = {}
        self.current_page = None
        self.create_pages()
        self.show_page("Início")

    def create_pages(self):
        # Página "Início"
        inicio_frame = customtkinter.CTkFrame(self.main_content_frame)
        label_inicio = customtkinter.CTkLabel(inicio_frame, text="Bem-vindo à Página Inicial!",
                                              font=customtkinter.CTkFont(size=20, weight="bold"))
        label_inicio.pack(expand=True, padx=20, pady=20)
        self.pages["Início"] = inicio_frame

        # Página "Cálculos"
        calculos_frame = customtkinter.CTkFrame(self.main_content_frame)
        label_calculos = customtkinter.CTkLabel(calculos_frame, text="Conteúdo da Página de Cálculos",
                                                font=customtkinter.CTkFont(size=20))
        label_calculos.pack(expand=True, padx=20, pady=20)
        self.pages["Cálculos"] = calculos_frame

        # Página "Simulação"
        simulacao_frame = customtkinter.CTkFrame(self.main_content_frame)
        label_simulacao = customtkinter.CTkLabel(simulacao_frame, text="Conteúdo da Página de Simulação",
                                                 font=customtkinter.CTkFont(size=20))
        label_simulacao.pack(expand=True, padx=20, pady=20)
        self.pages["Simulação"] = simulacao_frame

    def show_page(self, page_name):
        # Esconde a página atual, se houver
        if self.current_page:
            self.current_page.pack_forget()

        # Exibe a nova página
        self.current_page = self.pages[page_name]
        self.current_page.pack(expand=True, fill="both")

    def logout(self):
        # Lógica de logout
        print("Usuário deslogado.")
        self.destroy()  # Fecha a janela
