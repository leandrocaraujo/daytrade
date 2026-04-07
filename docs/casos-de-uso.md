# 📋 Casos de Uso

## Visão Geral

Esta seção descreve os principais casos de uso do sistema, detalhando as interações entre atores e funcionalidades.

## Atores do Sistema

### 👤 Investidor/Usuário Analista
Usuário final que consulta recomendações e analisa o mercado.

### 👨‍💼 Administrador
Responsável pela configuração e manutenção do sistema.

### 🤖 Sistema Externo de Mercado
Fonte de dados de preços e volumes.

### 📰 Sistema Externo de Notícias
Fonte de conteúdo jornalístico financeiro.

---

## Casos de Uso Principais

### UC01: Autenticar Usuário

**Ator Principal:** Todos os usuários humanos

**Pré-condições:**
- Usuário possui credenciais válidas

**Fluxo Principal:**
1. Usuário acessa a plataforma
2. Sistema solicita credenciais
3. Usuário informa login/senha
4. Sistema valida credenciais
5. Sistema gera token de acesso
6. Usuário é redirecionado para dashboard

**Fluxos Alternativos:**
- **Credenciais inválidas:** Sistema exibe mensagem de erro
- **Conta bloqueada:** Sistema informa sobre bloqueio temporário

**Pós-condições:**
- Usuário autenticado com token válido

---

### UC02: Cadastrar Ativo Monitorado

**Ator Principal:** Administrador

**Pré-condições:**
- Administrador autenticado
- Ticker não existe no sistema

**Fluxo Principal:**
1. Administrador acessa área administrativa
2. Seleciona "Cadastrar Ativo"
3. Informa ticker, nome e mercado
4. Sistema valida dados
5. Sistema persiste ativo
6. Sistema confirma cadastro

**Fluxos Alternativos:**
- **Ticker duplicado:** Sistema impede cadastro e informa erro
- **Dados inválidos:** Sistema solicita correção

**Pós-condições:**
- Ativo disponível para monitoramento

---

### UC03: Ingestar Preços

**Ator Principal:** Sistema Externo de Mercado

**Pré-condições:**
- Sistema externo autorizado
- Ativo existe e está ativo

**Fluxo Principal:**
1. Sistema externo envia dados de preço
2. API valida formato e obrigatoriedade
3. Sistema armazena preço
4. Sistema dispara processamento analítico
5. Sistema atualiza indicadores técnicos

**Fluxos Alternativos:**
- **Dados inválidos:** Sistema rejeita e registra erro
- **Ativo inativo:** Sistema aceita mas não processa

**Pós-condições:**
- Preço armazenado e indicadores atualizados

---

### UC04: Processar Notícia

**Ator Principal:** Sistema (automatizado)

**Pré-condições:**
- Notícia recebida e validada
- Ativos relacionados identificados

**Fluxo Principal:**
1. Sistema classifica sentimento (positivo/negativo/neutro)
2. Sistema classifica relevância (baixa/média/alta)
3. Sistema associa notícia aos ativos
4. Sistema armazena análise
5. Sistema atualiza sinais informacionais

**Fluxos Alternativos:**
- **Análise falha:** Sistema marca notícia como erro
- **Reprocessamento:** Fluxo similar com versão atualizada

**Pós-condições:**
- Notícia analisada e sinais atualizados

---

### UC05: Gerar Decisão Automática

**Ator Principal:** Sistema (automatizado)

**Pré-condições:**
- Ativo possui dados suficientes
- Sinais técnicos e informacionais disponíveis

**Fluxo Principal:**
1. Sistema combina sinais técnicos e notícias
2. Sistema aplica regras de negócio
3. Sistema calcula nível de confiança
4. Sistema gera recomendação (buy/sell/hold)
5. Sistema cria justificativa textual
6. Sistema persiste decisão

**Fluxos Alternativos:**
- **Dados insuficientes:** Sistema gera decisão com baixa confiança
- **Conflito de sinais:** Sistema reduz confiança geral

**Pós-condições:**
- Decisão disponível para consulta

---

### UC06: Consultar Dashboard

**Ator Principal:** Investidor/Usuário Analista

**Pré-condições:**
- Usuário autenticado

**Fluxo Principal:**
1. Usuário acessa dashboard
2. Sistema carrega lista de ativos monitorados
3. Sistema exibe preços atuais e recomendações
4. Usuário filtra/seleciona ativos
5. Sistema atualiza visualização

**Fluxos Alternativos:**
- **Sem dados:** Sistema exibe mensagem informativa
- **Dados desatualizados:** Sistema destaca visualmente

**Pós-condições:**
- Usuário visualiza estado atual do mercado

---

### UC07: Analisar Ativo Detalhadamente

**Ator Principal:** Investidor/Usuário Analista

**Pré-condições:**
- Usuário autenticado
- Ativo selecionado

**Fluxo Principal:**
1. Usuário seleciona ativo no dashboard
2. Sistema carrega dados detalhados
3. Sistema exibe gráfico de preços
4. Sistema mostra notícias relacionadas
5. Sistema apresenta decisão atual
6. Sistema exibe histórico de decisões

**Fluxos Alternativos:**
- **Dados limitados:** Sistema informa sobre restrições
- **Notícias ausentes:** Sistema explica ausência

**Pós-condições:**
- Usuário compreende situação completa do ativo

---

### UC08: Reprocessar Análises

**Ator Principal:** Administrador

**Pré-condições:**
- Administrador autenticado
- Motivo para reprocessamento identificado

**Fluxo Principal:**
1. Administrador seleciona tipo de reprocessamento
2. Escolhe escopo (ativo específico ou geral)
3. Sistema executa reprocessamento
4. Sistema atualiza decisões afetadas
5. Sistema registra operação em auditoria

**Fluxos Alternativos:**
- **Processamento longo:** Sistema executa em background
- **Falha parcial:** Sistema informa sobre erros

**Pós-condições:**
- Análises atualizadas com nova lógica

---

## Casos de Uso Secundários

### UC09: Configurar Parâmetros do Sistema

**Ator Principal:** Administrador

**Descrição:** Permite ajustar pesos, limiares e regras de negócio.

### UC10: Consultar Logs de Auditoria

**Ator Principal:** Administrador

**Descrição:** Acesso aos registros de operações administrativas.

### UC11: Monitorar Saúde do Sistema

**Ator Principal:** Administrador

**Descrição:** Verificação de status dos componentes principais.

### UC12: Exportar Relatórios

**Ator Principal:** Investidor/Usuário Analista

**Descrição:** Geração de relatórios em formato estruturado.

---

## Regras de Negócio Aplicáveis

### RN01: Decisão Requer Dados Mínimos
Toda decisão deve ter pelo menos um preço válido nos últimos 5 minutos.

### RN02: Notícias Devem Ser Recentes
Apenas notícias dos últimos 7 dias são consideradas para decisão.

### RN03: Confiança Baseada em Consistência
Sinais conflitantes reduzem o nível de confiança da decisão.

### RN04: Reprocessamentos Não Apagam Histórico
Novas decisões são adicionadas, mantendo rastreabilidade.

---

## Interfaces Externas

### API de Mercado
- **Protocolo:** REST/HTTP
- **Autenticação:** API Key
- **Formato:** JSON
- **Frequência:** Até 1Hz por ativo

### API de Notícias
- **Protocolo:** REST/HTTP
- **Autenticação:** OAuth 2.0
- **Formato:** JSON
- **Volume:** Até 1000 notícias/dia

### Dashboard Web
- **Tecnologia:** React/TypeScript
- **Responsivo:** Mobile-first
- **Tempo Real:** WebSocket para atualizações