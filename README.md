1. Visão Geral do Projeto
Este documento descreve a arquitetura, requisitos, componentes, agentes de IA, banco de dados, APIs e roadmap de desenvolvimento da plataforma analítica em tempo real para mercado financeiro, com emissão automática de recomendações de compra, venda ou manutenção de ativos.

2. Objetivos
Monitorar cotações de ações em tempo real

Coletar e analisar notícias financeiras

Processar dados com agentes de IA especializados

Emitir parecer automático por ativo

Registrar histórico de decisões

Exibir informações em um dashboard web

3. Arquitetura da Solução
A plataforma é composta por cinco camadas:

Ingestão de Dados

Armazenamento

Agentes de IA

API Backend

Dashboard Web

3.1. Diagrama da Arquitetura
(Inserir o diagrama Mermaid convertido em imagem no PDF)

4. Componentes do Sistema
4.1. Backend (FastAPI – Python)
Responsável por:

Expor endpoints REST

Orquestrar agentes de IA

Registrar decisões

Servir dados ao dashboard

4.2. Banco de Dados (PostgreSQL)
Tabelas principais:

prices

news

decisions

4.3. Agentes de IA
Agente de Notícias (NLP)
Entrada: texto da notícia

Saída: sentimento + relevância

Versão inicial: regras simples

Versão futura: modelo de linguagem treinado

Agente de Mercado
Entrada: últimos preços

Saída: sinal técnico (compra/venda/neutro)

Indicadores: SMA, tendência simples

Agente de Decisão
Entrada: sentimento + sinal técnico

Saída: buy/sell/hold + confiança + justificativa

5. Estrutura do Banco de Dados
5.1. Tabela prices
Campo	Tipo	Descrição
id	int	PK
ticker	string	Código do ativo
price	float	Último preço
volume	float	Volume negociado
timestamp	datetime	Horário da captura

5.2. Tabela news
Campo	Tipo	Descrição
id	int	PK
source	string	Fonte
title	string	Título
content	text	Conteúdo
ticker	string	Ativo
sentiment	string	positivo/negativo/neutro
relevance	string	baixa/média/alta
created_at	datetime	Registro

5.3. Tabela decisions
Campo	Tipo	Descrição
id	int	PK
ticker	string	Ativo
action	string	buy/sell/hold
confidence	float	0–100%
reason	text	Justificativa
created_at	datetime	Registro

6. API – Endpoints Principais
6.1. POST /prices
Registra um novo preço.

6.2. POST /news
Registra notícia e executa análise de sentimento.

6.3. GET /decisions/{ticker}
Gera decisão automática combinando:

Últimos preços

Última notícia

Regras do agente de decisão

7. Roadmap de Desenvolvimento
Fase 1 – Backend + Banco
Criar API FastAPI

Criar tabelas

Endpoints básicos

Fase 2 – Agente de Notícias
Implementar NLP simples

Integrar ao endpoint /news

Fase 3 – Agente de Mercado
Implementar indicadores técnicos

Integrar ao endpoint de decisão

Fase 4 – Agente de Decisão
Criar motor de decisão

Registrar decisões

Fase 5 – Ingestão Automática
Coleta contínua de preços

Coleta contínua de notícias

Fase 6 – Dashboard Web
Criar frontend

Exibir dados e decisões
