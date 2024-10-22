# NoteKeeperAPI

NoteKeeperAPI é uma aplicação web simples desenvolvida em Flask que permite aos usuários criar, visualizar, editar e excluir notas. Este projeto visa fornecer uma interface amigável para o gerenciamento de anotações pessoais.

## Funcionalidades

- **Criar Notas**: Os usuários podem adicionar novas notas com um título e conteúdo.
- **Listar Notas**: Visualize todas as notas criadas em uma lista.
- **Editar Notas**: Atualize o título ou conteúdo de notas existentes.
- **Excluir Notas**: Remova notas que não são mais necessárias.

## Tecnologias Usadas

- **Flask**: Um microframework em Python que permite o desenvolvimento de aplicações web.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interagir com o banco de dados SQLite.
- **Bootstrap**: Framework CSS para criar uma interface responsiva e moderna.

## Instalação

Para instalar e rodar o projeto, siga os passos abaixo:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/NoteKeeperAPI.git
   cd NoteKeeperAPI
   
2. **Crie um ambiente virtual (opcional, mas recomendado)**:
   
  python -m venv venv
  source venv/bin/activate  # Para Windows, use venv\Scripts\activate

3. **Instale as dependências**:
   
   pip install -r requirements.txt

4. **Inicie a aplicação**:
     python app.py
   
5. **Acesse a aplicação: Abra seu navegador e vá para http://127.0.0.1:5000.**

      ### **Estrutura do Projeto**
NoteKeeperAPI/

### Descrição dos Arquivos

| Pasta/Arquivo            | Descrição                                   |
|--------------------------|---------------------------------------------|
| `app.py`                 | Código principal da aplicação.              |
| `models.py`              | Definições dos modelos de dados.            |
| `static/`                | Contém arquivos estáticos, como CSS e JS.  |
| `static/css/`            | Arquivos de estilo CSS.                     |
| `static/js/`             | Scripts JavaScript utilizados na aplicação. |
| `templates/`             | Contém templates HTML.                      |
| `templates/index.html`   | Página principal da aplicação.              |
| `requirements.txt`       | Lista de dependências do projeto.          |

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests. Para contribuir:

Fork este repositório.
Crie uma nova branch (git checkout -b feature/nome-da-sua-feature).
Faça suas alterações e commit (git commit -m 'Adiciona nova funcionalidade').
Faça push para a branch (git push origin feature/nome-da-sua-feature).
Abra um Pull Request.
