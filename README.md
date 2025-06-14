# Reciclo Cash Bank

Sistema de gestão de resíduos e créditos de carbono que converte esses créditos em dinheiro físico ou criptomoedas.

## 📋 Sobre o Projeto

O Reciclo Cash Bank é uma plataforma digital de gestão de resíduos que trabalha com créditos de carbono, convertendo-os em dinheiro físico ou criptomoedas conforme a escolha do usuário. O sistema facilita a coleta, registro e valoração de materiais recicláveis, promovendo a economia circular e a sustentabilidade.

## 🚀 Funcionalidades

- Solicitação de coleta de materiais recicláveis
- Calculadora de preços de materiais
- Painel administrativo para gestão de coletas e compras
- Sistema de notificações por email e WhatsApp
- Registro e acompanhamento de créditos de carbono

## 🛠️ Tecnologias

- **Backend**: Flask (Python)
- **Banco de Dados**: Supabase (PostgreSQL)
- **Autenticação**: Supabase Auth
- **Frontend**: HTML/CSS/JavaScript (com possível migração para React/Vue)
- **DevOps**: GitHub Actions para CI/CD
- **Armazenamento**: Supabase Storage

## 🏗️ Estrutura do Projeto

```
reciclo-cash-bank/
├── .github/
│   └── workflows/           # GitHub Actions para CI/CD
├── docs/                    # Documentação do projeto
├── src/
│   ├── api/                 # Endpoints da API
│   ├── auth/                # Lógica de autenticação
│   ├── config/              # Configurações (sem credenciais)
│   ├── models/              # Modelos de dados
│   ├── services/            # Serviços de negócios
│   ├── static/              # Arquivos estáticos
│   ├── templates/           # Templates Flask
│   └── utils/               # Funções utilitárias
├── tests/                   # Testes automatizados
├── .env.example             # Exemplo de variáveis de ambiente
├── .gitignore               # Arquivos a serem ignorados
└── requirements.txt         # Dependências Python
```

## 🚦 Como Começar

### Pré-requisitos

- Python 3.8+
- Conta no Supabase
- Git

### Instalação

1. Clone o repositório
   ```bash
   git clone https://github.com/reciclabank/cashtoken.git
   cd cashtoken
   ```

2. Crie e ative um ambiente virtual
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com suas credenciais
   ```

5. Execute a aplicação
   ```bash
   python src/main.py
   ```

## 📊 Roadmap

- [x] Sistema básico de coleta e cálculo de preços
- [x] Painel administrativo
- [ ] Migração para Supabase
- [ ] Implementação de autenticação robusta
- [ ] Integração com serviços de email e WhatsApp
- [ ] Sistema de créditos de carbono
- [ ] Integração com blockchain

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar pull requests.

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## 📞 Contato

Para mais informações, entre em contato através do email: [contato@reciclocashbank.com](mailto:contato@reciclocashbank.com)
