document.addEventListener('DOMContentLoaded', () => {

    const loginForm = document.getElementById('login-form');
    const logoutBtn = document.getElementById('logout-btn');
    const loginScreen = document.getElementById('login-screen');
    const mainScreen = document.getElementById('main-screen');

    // Lógica para o Login
    loginForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Verificação simples (substitua pela sua lógica de backend)
        if (username === 'admin' && password === '123') {
            loginScreen.classList.remove('active');
            mainScreen.classList.add('active');
            console.log('Login bem-sucedido!');
        } else {
            alert('Usuário ou senha inválidos.');
        }
    });

    // Lógica para o Logout
    logoutBtn.addEventListener('click', () => {
        mainScreen.classList.remove('active');
        loginScreen.classList.add('active');
        console.log('Usuário deslogado.');
    });

});

// Função para exibir a página de conteúdo correta
function showPage(pageId) {
    // Remove a classe 'active' de todas as páginas de conteúdo
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => page.classList.remove('active'));

    // Adiciona a classe 'active' à página clicada
    document.getElementById(pageId).classList.add('active');

    // Remove a classe 'active' de todos os botões do menu
    const menuButtons = document.querySelectorAll('.menu-btn');
    menuButtons.forEach(btn => btn.classList.remove('active'));

    // Adiciona a classe 'active' ao botão clicado
    event.currentTarget.classList.add('active');
}