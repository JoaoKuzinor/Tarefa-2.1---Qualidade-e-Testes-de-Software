# Tarefa-2.1---Qualidade-e-Testes-de-Software

📌 Sobre o Projeto

Este projeto foi desenvolvido com foco em práticas de Qualidade e Testes de Software, utilizando Python e Flask para construção da aplicação e Pytest para automação de testes.

O objetivo principal é demonstrar a aplicação de conceitos fundamentais de qualidade de software, incluindo:

Desenvolvimento organizado
Padronização de código
Testes automatizados
Boas práticas de manutenção
Estruturação de API com Flask

O projeto também utiliza ferramentas de lint e formatação para garantir maior qualidade e legibilidade do código.

🚀 Tecnologias Utilizadas
Python 3
Flask
Pytest
Flake8
Black
📂 Estrutura do Projeto
📦 projeto
 ┣ 📂 tests
 ┃ ┗ 📜 test_app.py
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
 ┗ 📜 .flake8
⚙️ Instalação

Clone o repositório:

git clone https://github.com/JoaoKuzinor/Tarefa-2.1---Qualidade-e-Testes-de-Software.git

Acesse a pasta do projeto:

cd Tarefa-2.1---Qualidade-e-Testes-de-Software

Crie um ambiente virtual:

Windows
python -m venv venv
venv\Scripts\activate
Linux/Mac
python3 -m venv venv
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt
▶️ Executando a Aplicação

Para iniciar o servidor Flask:

python run.py

A aplicação ficará disponível em:

http://127.0.0.1:5000
🧪 Executando os Testes

Para executar todos os testes automatizados:

pytest

Para visualizar mais detalhes:

pytest -v

Os testes garantem o funcionamento correto das funcionalidades implementadas e auxiliam na prevenção de falhas futuras.

🎨 Padronização de Código
Formatação automática com Black
black .
Verificação de padrões com Flake8
flake8

Essas ferramentas ajudam a manter o código limpo, organizado e seguindo boas práticas de desenvolvimento.

📦 Dependências do Projeto

Principais bibliotecas utilizadas:

Flask
pytest
black
flake8

Todas as dependências estão disponíveis no arquivo:

requirements.txt
📖 Conceitos Aplicados
Testes automatizados
Qualidade de software
Organização de projeto
Boas práticas de programação
Validação de funcionalidades
Padronização de código

A utilização de testes automatizados é considerada uma das práticas mais importantes para garantir confiabilidade e manutenção em projetos modernos.