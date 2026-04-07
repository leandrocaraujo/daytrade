# Plataforma Analítica em Tempo Real para Mercado Financeiro

Plataforma para monitoramento de ativos financeiros em tempo quase real, análise automatizada de notícias e geração de recomendações de **compra**, **venda** ou **manutenção** com apoio de agentes analíticos.

## Visão Geral

Este projeto tem como objetivo integrar dados de mercado e notícias financeiras em uma única plataforma capaz de:

- monitorar preços de ativos em tempo quase real;
- coletar e analisar notícias relacionadas aos ativos;
- calcular sinais técnicos de mercado;
- combinar diferentes análises para gerar decisões automatizadas;
- registrar histórico completo das decisões emitidas;
- exibir todas as informações em um dashboard web.

## Objetivos do Projeto

- Monitorar cotações de ativos em tempo quase real
- Coletar e processar notícias financeiras
- Aplicar agentes analíticos especializados
- Emitir parecer automático por ativo
- Registrar histórico de decisões
- Disponibilizar API para integração
- Exibir dados e recomendações em dashboard web e, futuramente, mobile

---

## Arquitetura da Solução

A solução foi concebida em camadas para garantir escalabilidade, modularidade e facilidade de evolução.

### Camadas principais

1. **Ingestão de Dados**
   - Recebimento de preços
   - Recebimento de notícias
   - Validação e normalização dos dados

2. **Armazenamento**
   - Persistência de preços
   - Persistência de notícias
   - Persistência de decisões
   - Rastreabilidade histórica

3. **Agentes Analíticos**
   - Agente de Notícias
   - Agente de Mercado
   - Agente de Decisão

4. **API Backend**
   - Exposição de endpoints REST
   - Orquestração dos agentes
   - Controle de autenticação e acesso
   - Fornecimento de dados ao frontend

5. **Dashboard Web**
   - Visualização dos ativos
   - Consulta de notícias
   - Histórico de decisões
   - Indicadores e gráficos

---

## Diagrama Conceitual da Arquitetura

```mermaid
flowchart TD
    A[Fontes de Preço] --> B[Camada de Ingestão]
    C[Fontes de Notícias] --> B

    B --> D[Backend / API]
    D --> E[(PostgreSQL)]
    D --> F[Agente de Notícias]
    D --> G[Agente de Mercado]
    F --> H[Agente de Decisão]
    G --> H
    H --> E
    D --> I[Dashboard Web]
    D --> J[Aplicativo Mobile - Futuro]

---

## 📚 Documentação

A documentação completa do projeto está disponível em [GitHub Pages](https://SEU-USUARIO.github.io/daytrade/).

### Seções da Documentação

- [**Visão Geral**](https://audittmega.github.io/daytrade/visao-geral/) - Objetivo e escopo do sistema
- [**Arquitetura**](https://audittmega.github.io/daytrade/arquitetura/) - Componentes e tecnologias
- [**Requisitos**](https://audittmega.github.io/daytrade/requisitos/) - Funcionais e não funcionais
- [**User Stories**](https://audittmega.github.io/daytrade/user-stories/) - Backlog do usuário
- [**Casos de Uso**](https://audittmega.github.io/daytrade/casos-de-uso/) - Interações detalhadas
- [**Diagramas**](https://audittmega.github.io/daytrade/diagramas/) - UML e arquitetura

### Configuração Local da Documentação

Para visualizar a documentação localmente durante o desenvolvimento:

```bash
# Instalar dependências
pip install mkdocs-material mkdocs-mermaid2-plugin

# Executar servidor local
mkdocs serve

# Abrir http://localhost:8000
```

### Deploy Automático

A documentação é automaticamente publicada no GitHub Pages a cada push na branch `main` através do GitHub Actions.

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.11+**
- **FastAPI** - Framework web assíncrono
- **SQLAlchemy** - ORM
- **Pydantic** - Validação de dados

### Frontend
- **React/TypeScript**
- **Material-UI**
- **Chart.js**

### Infraestrutura
- **PostgreSQL** - Banco de dados
- **Redis** - Cache
- **RabbitMQ** - Mensageria
- **Docker** - Containerização

### Documentação
- **MkDocs** - Gerador de sites
- **Material for MkDocs** - Tema
- **Mermaid** - Diagramas
- **PlantUML** - Diagramas UML

---

## 🚀 Como Começar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SEU-USUARIO/daytrade.git
   cd daytrade
   ```

2. **Configure o ambiente**
   ```bash
   # Instalar dependências Python
   pip install -r requirements.txt

   # Configurar banco de dados
   docker-compose up -d db redis rabbitmq
   ```

3. **Execute as migrações**
   ```bash
   alembic upgrade head
   ```

4. **Inicie o servidor**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Acesse a documentação**
   - [GitHub Pages](https://audittmega.github.io/daytrade/)
   - Ou localmente: `mkdocs serve`

---

## 📋 Status do Projeto

- ✅ **Fase 1**: Estrutura base e documentação
- 🔄 **Fase 2**: Implementação do backend
- ⏳ **Fase 3**: Frontend e integrações
- ⏳ **Fase 4**: Testes e deploy

---

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📞 Contato

- **Projeto**: [GitHub Issues](https://github.com/audittmega/daytrade/issues)
- **Documentação**: [GitHub Pages](https://audittmega.github.io/daytrade/)
