# PatronRate ⚡

**PatronRate** é uma plataforma web para fãs do universo de Harry Potter. O sistema permite explorar personagens da saga e gerenciar avaliações e comentários personalizados de forma simples e intuitiva.

## 🚀 Funcionalidades

- **Exploração via HP-API:** Listagem dinâmica de personagens diretamente na tela inicial, consumindo dados da [HP-API](https://hp-api.onrender.com/).
- **Sistema de Comentários (CRUD):** - Interface completa para Criar, Ler, Atualizar e Excluir opiniões sobre o "Mundo Mágico".
- **Validação de Dados:** Backend com lógica de `clean_nome` para evitar duplicidade de registros.

## 🛠️ Tecnologias

- **Linguagem:** Python
- **Framework:** Django (Estrutura do projeto: `wsbackend`)
- **Banco de Dados:** SQLite3
- **Containerização:** Docker

---

## 📦 Como Instalar e Rodar o Projeto **wsbackend**

### Via Docker (Recomendado)

1. Certifique-se de que o Docker está instalado.
2. Na raiz do projeto, execute:
   ```bash
   docker build -t wsbackend .
   docker run -p 8000:8000 wsbackend