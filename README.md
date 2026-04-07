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
