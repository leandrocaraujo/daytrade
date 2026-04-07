# User Stories — Plataforma Analítica em Tempo Real para Mercado Financeiro

## Sumário por Épico

| Épico | Descrição |
|---|---|
| Épico 1 | Gestão de Ativos |
| Épico 2 | Ingestão de Preços |
| Épico 3 | Ingestão de Notícias |
| Épico 4 | Análise de Notícias |
| Épico 5 | Análise Técnica de Mercado |
| Épico 6 | Motor de Decisão |
| Épico 7 | Dashboard Web |
| Épico 8 | API e Integrações |
| Épico 9 | Administração, Segurança e Auditoria |

## Épico 1 — Gestão de Ativos

### US01 — Cadastrar ativo monitorado

**Como** administrador
**Quero** cadastrar um ativo financeiro com ticker, nome e mercado
**Para que** ele possa ser monitorado pela plataforma

#### Critérios de aceitação
- Deve ser possível informar ticker, nome e mercado.
- O sistema deve impedir cadastro duplicado do mesmo ticker no mesmo mercado.
- O ativo cadastrado deve ficar disponível para consulta e monitoramento.

### US02 — Atualizar ativo monitorado

**Como** administrador
**Quero** editar os dados de um ativo monitorado
**Para** manter a base de ativos atualizada

#### Critérios de aceitação
- Deve ser possível alterar nome, status e mercado do ativo.
- O histórico operacional do ativo não deve ser perdido.
- A alteração deve ser registrada em auditoria.

### US03 — Ativar ou desativar ativo

**Como** administrador
**Quero** ativar ou desativar um ativo
**Para** controlar quais ativos participam das análises automáticas

#### Critérios de aceitação
- Ativos desativados não devem entrar em novos processamentos automáticos.
- O histórico do ativo deve permanecer acessível.
- O status deve ser exibido no painel administrativo.

## Épico 2 — Ingestão de Preços

### US04 — Registrar preço de ativo

**Como** sistema externo de mercado
**Quero** enviar o preço de um ativo pela API
**Para** alimentar a base analítica em tempo quase real

#### Critérios de aceitação
- O endpoint deve aceitar ticker, preço, volume e timestamp.
- O sistema deve validar campos obrigatórios.
- O preço deve ser armazenado com sucesso quando válido.

### US05 — Registrar preços em lote

**Como** sistema externo de mercado
**Quero** enviar múltiplos preços em uma única requisição
**Para** reduzir custo operacional de integração

#### Critérios de aceitação
- O sistema deve aceitar payload em lote.
- Registros válidos devem ser persistidos.
- Registros inválidos devem ser reportados com erro claro.

### US06 — Consultar histórico de preços

**Como** usuário analista
**Quero** consultar o histórico de preços de um ativo
**Para** avaliar seu comportamento recente

#### Critérios de aceitação
- A consulta deve permitir filtro por ticker e período.
- Os dados devem ser retornados em ordem cronológica.
- O sistema deve informar quando não houver dados no intervalo solicitado.

### US07 — Identificar preço desatualizado

**Como** usuário analista
**Quero** saber quando o preço de um ativo está desatualizado
**Para** não confiar em análises com base em dados antigos

#### Critérios de aceitação
- O sistema deve marcar preços fora da janela de validade.
- O dashboard deve exibir alerta visual.
- O motor de decisão deve considerar a regra de recência.

## Épico 3 — Ingestão de Notícias

### US08 — Registrar notícia financeira

**Como** sistema externo de notícias
**Quero** enviar uma notícia para a plataforma
**Para** que ela seja analisada e relacionada a um ativo

#### Critérios de aceitação
- O endpoint deve aceitar fonte, título, conteúdo, data e ticker relacionado.
- O sistema deve armazenar a notícia recebida.
- O sistema deve marcar a notícia como pendente de processamento ou processada.

### US09 — Relacionar notícia a um ou mais ativos

**Como** administrador ou sistema integrador
**Quero** associar uma notícia a um ou mais ativos
**Para** refletir corretamente seu impacto no mercado

#### Critérios de aceitação
- O sistema deve permitir vínculo com múltiplos tickers.
- A consulta por ativo deve exibir a notícia vinculada.
- O motor de decisão deve consumir as associações válidas.

### US10 — Consultar notícias por ativo

**Como** usuário analista
**Quero** visualizar as notícias relacionadas a um ativo
**Para** entender o contexto informacional por trás da recomendação

#### Critérios de aceitação
- Deve ser possível filtrar por ticker e período.
- A lista deve exibir fonte, data, título e classificação.
- O sistema deve permitir ordenar por recência.

### US11 — Detectar notícia duplicada

**Como** administrador
**Quero** que o sistema identifique notícias duplicadas ou equivalentes
**Para** evitar distorção no peso da análise informacional

#### Critérios de aceitação
- O sistema deve aplicar regra de duplicidade.
- Notícias duplicadas devem ser sinalizadas.
- Notícias duplicadas não devem amplificar indevidamente a decisão.

## Épico 4 — Análise de Notícias

### US12 — Classificar sentimento da notícia

**Como** plataforma analítica
**Quero** classificar automaticamente o sentimento de uma notícia
**Para** apoiar a recomendação do ativo

#### Critérios de aceitação
- O sentimento deve ser classificado como positivo, negativo ou neutro.
- O resultado deve ser persistido na base.
- A classificação deve ficar disponível para consulta e decisão.

### US13 — Classificar relevância da notícia

**Como** plataforma analítica
**Quero** classificar a relevância da notícia
**Para** ponderar seu impacto no processo decisório

#### Critérios de aceitação
- A relevância deve ser classificada em baixa, média ou alta.
- O resultado deve ser salvo junto à notícia.
- O motor de decisão deve consumir essa classificação.

### US14 — Reprocessar notícia

**Como** administrador
**Quero** reprocessar uma notícia já cadastrada
**Para** atualizar a análise quando houver mudança de regra ou modelo

#### Critérios de aceitação
- O sistema deve permitir reprocessamento manual.
- A nova análise deve registrar versão do modelo/regra.
- O histórico anterior deve permanecer rastreável.

## Épico 5 — Análise Técnica de Mercado

### US15 — Calcular indicadores técnicos

**Como** plataforma analítica
**Quero** calcular indicadores técnicos com base no histórico de preços
**Para** gerar um sinal objetivo de mercado

#### Critérios de aceitação
- O sistema deve calcular ao menos média móvel simples e tendência simplificada.
- O cálculo deve usar apenas dados válidos.
- O resultado deve ser persistido ou disponibilizado para decisão.

### US16 — Gerar sinal técnico

**Como** plataforma analítica
**Quero** gerar um sinal técnico de compra, venda ou neutro
**Para** apoiar o motor de decisão

#### Critérios de aceitação
- O sistema deve classificar o sinal como compra, venda ou neutro.
- O sistema deve indicar quando houver dados insuficientes.
- O sinal deve ser consumido pelo agente de decisão.

### US17 — Reprocessar análise técnica

**Como** administrador
**Quero** reprocessar a análise técnica de um ativo
**Para** refletir novos parâmetros ou correções

#### Critérios de aceitação
- O sistema deve permitir reprocessamento manual.
- A nova execução deve registrar seus parâmetros.
- O histórico analítico anterior não deve ser apagado.

## Épico 6 — Motor de Decisão

### US18 — Gerar recomendação automática

**Como** investidor
**Quero** receber uma recomendação automática de buy, sell ou hold para um ativo
**Para** apoiar minha análise de decisão

#### Critérios de aceitação
- A decisão deve considerar análise técnica e notícias válidas.
- O resultado deve conter ação, confiança e justificativa.
- A decisão deve ser armazenada no histórico.

### US19 — Gerar decisão sob demanda

**Como** usuário analista
**Quero** solicitar manualmente a decisão de um ativo
**Para** obter uma recomendação atualizada quando necessário

#### Critérios de aceitação
- A API deve aceitar consulta por ticker.
- O sistema deve gerar ou retornar a última decisão conforme a regra definida.
- O resultado deve ser apresentado com contexto suficiente.

### US20 — Calcular confiança da decisão

**Como** investidor
**Quero** visualizar o nível de confiança da decisão
**Para** entender o grau de consistência do parecer emitido

#### Critérios de aceitação
- A confiança deve ser expressa em percentual.
- O sistema deve reduzir confiança em cenários de conflito entre sinais.
- O valor deve ser exibido na API e no dashboard.

### US21 — Exibir justificativa da decisão

**Como** investidor
**Quero** ver uma justificativa textual da recomendação
**Para** compreender os fatores que influenciaram o resultado

#### Critérios de aceitação
- A justificativa deve citar os fatores relevantes usados na decisão.
- A justificativa deve ficar registrada no histórico.
- A justificativa deve ser apresentada em linguagem compreensível.

### US22 — Preservar histórico de decisões

**Como** usuário analista
**Quero** consultar decisões anteriores de um ativo
**Para** acompanhar a evolução do comportamento analítico do sistema

#### Critérios de aceitação
- O sistema deve manter decisões antigas.
- Deve ser possível filtrar por ticker e período.
- Reprocessamentos devem gerar novos registros, não sobrescrever os antigos.

## Épico 7 — Dashboard Web

### US23 — Visualizar painel geral de ativos

**Como** investidor
**Quero** visualizar um painel com os principais ativos monitorados
**Para** acompanhar rapidamente o estado geral da plataforma

#### Critérios de aceitação
- O painel deve exibir ticker, preço atual, recomendação e confiança.
- A lista deve permitir ordenação e filtro.
- O painel deve sinalizar ativos com dados desatualizados.

### US24 — Visualizar detalhes de um ativo

**Como** investidor
**Quero** abrir a visão detalhada de um ativo
**Para** analisar preços, notícias e decisões com mais profundidade

#### Critérios de aceitação
- A tela deve exibir gráfico de preços.
- A tela deve exibir notícias relacionadas.
- A tela deve exibir recomendação atual e histórico de decisões.

### US25 — Filtrar ativos no dashboard

**Como** usuário analista
**Quero** filtrar os ativos por ticker, mercado, ação recomendada e confiança
**Para** localizar rapidamente os casos mais relevantes

#### Critérios de aceitação
- O dashboard deve oferecer filtros combináveis.
- O resultado filtrado deve ser atualizado sem recarga completa, quando possível.
- O sistema deve permitir limpar filtros facilmente.

### US26 — Visualizar alertas de insuficiência de dados

**Como** investidor
**Quero** ser informado quando não houver dados suficientes para uma recomendação confiável
**Para** evitar interpretações equivocadas

#### Critérios de aceitação
- O sistema deve exibir aviso de insuficiência de dados.
- O motivo do estado deve ser informado.
- O ativo deve continuar acessível para consulta histórica.

## Épico 8 — API e Integrações

### US27 — Consumir API documentada

**Como** desenvolvedor integrador
**Quero** consultar a documentação dos endpoints
**Para** integrar sistemas externos com menor esforço

#### Critérios de aceitação
- A API deve possuir documentação acessível.
- Os endpoints devem ter payloads e respostas exemplificadas.
- Os erros mais comuns devem estar documentados.

### US28 — Consultar estado da plataforma

**Como** administrador
**Quero** verificar a saúde da API e dos serviços principais
**Para** monitorar a estabilidade operacional

#### Critérios de aceitação
- Deve existir endpoint de health check.
- O endpoint deve indicar estado básico dos módulos principais.
- Falhas críticas devem ser distinguíveis de operação normal.

## Épico 9 — Administração, Segurança e Auditoria

### US29 — Autenticar usuário

**Como** usuário autorizado
**Quero** fazer login na plataforma
**Para** acessar funcionalidades conforme meu perfil

#### Critérios de aceitação
- O sistema deve exigir autenticação para áreas protegidas.
- Credenciais inválidas devem ser rejeitadas.
- Sessões devem respeitar política de segurança definida.

### US30 — Controlar acesso por perfil

**Como** administrador
**Quero** restringir funcionalidades por perfil de usuário
**Para** proteger operações sensíveis da plataforma

#### Critérios de aceitação
- O sistema deve diferenciar perfis ao menos entre usuário comum e administrador.
- Funcionalidades administrativas não devem ficar acessíveis a perfis sem permissão.
- Violações de acesso devem ser registradas.

### US31 — Auditar alterações administrativas

**Como** administrador
**Quero** consultar o histórico de alterações realizadas no sistema
**Para** garantir rastreabilidade e governança

#### Critérios de aceitação
- O sistema deve registrar quem alterou, quando alterou e o que alterou.
- Alterações de parâmetros críticos devem ter destaque.
- Os registros de auditoria devem ser consultáveis.

### US32 — Reprocessar dados operacionais

**Como** administrador
**Quero** reprocessar notícias, análises técnicas e decisões
**Para** corrigir inconsistências ou atualizar resultados

#### Critérios de aceitação
- O sistema deve permitir reprocessamento manual.
- O sistema deve registrar a versão do modelo ou regra usada.
- O histórico anterior deve permanecer rastreável.
