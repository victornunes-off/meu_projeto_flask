# Meu Projeto Flask

**Repositório:** [https://github.com/victornunes-off/meu_projeto_flask](https://github.com/victornunes-off/meu_projeto_flask)

---

## Sobre

Sistema web simples em **Flask** com autenticação, login, cadastro e perfil de usuário.  
Design inspirado no **Instituto Federal de Rondônia (IFRO)**.

---

## Tecnologias

- Python + Flask  
- HTML5 / CSS3 / JavaScript  
- Jinja2 (templates)  
- Git/GitHub

---

## Estrutura
meu_projeto_flask/<br>
├── app.py              # Rotas e lógica<br>
├── templates/          # base.html, login.html, etc.<br>
├── static/<br>
│       ├── css/style.css   # Estilos aprimorados<br>
│       └── js/script.js    # Data/hora e validações<br>

---

## Alterações
Commit | Mudança

Criação do app.py | Início do projeto Flask com criação do ambiente;<br>
Criação de rota e direcionamento de porta | Criou-se a primeira rota raiz com uma saudação simples;<br>
Criação da rota2 | Criação de mais uma rota para ver como funcionam as chamadas na url;<br>
Criação da pasta templates e arquivo homepage.html | O intuitio é entender como renderizar uma página html através de uma rota;<br>
Envio dos dados de app.py para usuario.html | Criação de uma página para dados do usuário que receberia dados através da URL;<br>
Página dinâmica com dados pela URL | Página renderiza com informações ajustadas dinamicamente;<br>
Criação do template base e primeiro uso no index.html | Criação da branch "template" para implementação de template base;<br>
Ajuste demais templates | Criação das demais páginas ajustando ao template base.html;<br>
Função de autenticação de login | Criação de verificação de autenticação de usuário.

