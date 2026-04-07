# 📊 Elicitação de Requisitos

## Sistema de Plataforma Analítica em Tempo Real para Mercado Financeiro

---

## 1. Requisitos Funcionais

### 1.1 Gestão de Ativos Monitorados

| ID | Descrição |
|---|---|
| **RF01** | O sistema deve permitir o cadastro de ativos financeiros a serem monitorados. |
| **RF02** | O sistema deve permitir ativar, desativar e atualizar ativos monitorados. |
| **RF03** | O sistema deve armazenar, para cada ativo, no mínimo: ticker, nome, mercado, status e data de cadastro. |
| **RF04** | O sistema deve impedir o cadastro duplicado de ticker para o mesmo mercado. |
| **RF05** | O sistema deve permitir a listagem dos ativos monitorados com filtros por status e mercado. |

### 1.2 Ingestão de Preços

| ID | Descrição |
|---|---|
|**RF06** |O sistema deve receber dados de preço por meio de endpoint de API.|
|**RF07**  |O sistema deve permitir ingestão unitária e em lote de preços.|
|**RF08**  |O sistema deve validar os campos obrigatórios do preço antes do armazenamento.|
|**RF09**  |O sistema deve armazenar, para cada preço, no mínimo: ticker, preço, volume, timestamp do evento, timestamp de ingestão e origem do dado.|
|**RF10**  |O sistema deve rejeitar registros de preço com formato inválido, ticker inexistente ou valores inconsistentes.|
|**RF11**  |O sistema deve registrar o histórico cronológico de preços por ativo.|
|**RF12**  |O sistema deve permitir a consulta do histórico de preços por ativo e intervalo de tempo.|
|**RF13**  |O sistema deve identificar preços desatualizados com base em uma janela de validade configurável.|
|**RF14**  |O sistema deve registrar falhas de ingestão de preços para auditoria.|

### 1.3 Ingestão de Notícias

| ID | Descrição |
|---|---|
| **RF15** | O sistema deve receber notícias por meio de endpoint de API. |
| **RF16** | O sistema deve permitir ingestão unitária e em lote de notícias. |
| **RF17** | O sistema deve validar os campos obrigatórios da notícia antes do processamento. |
| **RF18** | O sistema deve armazenar, para cada notícia, no mínimo: fonte, título, conteúdo, URL quando disponível, data de publicação, data de ingestão e ativo(s) relacionado(s). |
| **RF19** | O sistema deve permitir associar uma notícia a um ou mais ativos. |
| **RF20** | O sistema deve identificar notícias duplicadas ou substancialmente equivalentes, conforme regra configurada. |
| **RF21** | O sistema deve registrar o status da notícia como pendente, processada ou com erro. |
| **RF22** | O sistema deve permitir consulta de notícias por ativo, fonte e período. |
| **RF23** | O sistema deve registrar falhas de ingestão e processamento de notícias para auditoria. |

### 1.4 Análise de Notícias

| ID | Descrição |
|---|---|
| **RF24** | O sistema deve processar automaticamente a notícia após sua ingestão válida. |
| **RF25** | O sistema deve classificar o sentimento da notícia em positivo, negativo ou neutro. |
| **RF26** | O sistema deve classificar a relevância da notícia em baixa, média ou alta. |
| **RF27** | O sistema deve armazenar o resultado da análise de sentimento e relevância vinculado à notícia analisada. |
| **RF28** | O sistema deve gerar uma justificativa resumida da classificação da notícia. |
| **RF29** | O sistema deve registrar a versão do modelo, regra ou agente utilizado na análise. |
| **RF30** | O sistema deve permitir o reprocessamento de notícias previamente armazenadas. |
| **RF31** | O sistema deve disponibilizar os resultados da análise de notícias para o motor de decisão. |

### 1.5 Análise Técnica de Mercado

| ID | Descrição |
|---|---|
| **RF32** | O sistema deve calcular indicadores técnicos com base no histórico de preços do ativo. |
| **RF33** | O sistema deve calcular, no mínimo, média móvel simples e tendência simplificada. |
| **RF34** | O sistema deve validar se existe quantidade mínima de dados para cálculo dos indicadores. |
| **RF35** | O sistema deve gerar um sinal técnico classificado como compra, venda ou neutro. |
| **RF36** | O sistema deve armazenar os valores dos indicadores utilizados no cálculo. |
| **RF37** | O sistema deve registrar a versão da estratégia ou regra técnica utilizada. |
| **RF38** | O sistema deve permitir o reprocessamento da análise técnica quando houver mudança de parâmetros. |

### 1.6 Motor de Decisão

| ID | Descrição |
|---|---|
| **RF39** | O sistema deve combinar análise técnica e análise de notícias para emitir uma decisão por ativo. |
| **RF40** | O sistema deve classificar a decisão final como buy, sell ou hold. |
| **RF41** | O sistema deve atribuir um percentual de confiança à decisão. |
| **RF42** | O sistema deve gerar uma justificativa textual da decisão, mencionando os fatores determinantes. |
| **RF43** | O sistema deve registrar, para cada decisão, os insumos efetivamente utilizados no processamento. |
| **RF44** | O sistema deve armazenar a versão do agente, modelo ou regra responsável pela decisão. |
| **RF45** | O sistema deve permitir gerar decisão sob demanda por ticker. |
| **RF46** | O sistema deve permitir geração automática periódica de decisões para ativos monitorados. |
| **RF47** | O sistema deve registrar o histórico completo de decisões emitidas. |
| **RF48** | O sistema deve permitir reprocessar uma decisão sem sobrescrever o histórico anterior. |
| **RF49** | O sistema deve marcar decisões como atuais, históricas ou reprocessadas. |
| **RF50** | O sistema deve impedir a emissão de decisão quando os dados mínimos exigidos não estiverem disponíveis. |

### 1.7 Consulta e Exposição por API

| ID | Descrição |
|---|---|
| **RF51** | O sistema deve expor endpoints REST para ingestão de preços, ingestão de notícias, consulta de ativos, consulta de preços, consulta de notícias e consulta de decisões. |
| **RF52** | O sistema deve retornar os dados em formato JSON. |
| **RF53** | O sistema deve retornar códigos HTTP compatíveis com sucesso, erro de validação, autenticação, autorização, recurso inexistente e erro interno. |
| **RF54** | O sistema deve oferecer filtros por ticker, data, fonte, relevância, sentimento e status de processamento. |
| **RF55** | O sistema deve oferecer paginação nas consultas de listas. |
| **RF56** | O sistema deve permitir ordenação por data, confiança, relevância e preço. |
| **RF57** | O sistema deve disponibilizar endpoint para consulta do histórico de decisões por ativo. |
| **RF58** | O sistema deve disponibilizar endpoint para consulta da última decisão válida por ativo. |
| **RF59** | O sistema deve disponibilizar endpoint de health check da plataforma. |

### 1.8 Dashboard Web

| ID | Descrição |
|---|---|
| **RF60** | O sistema deve exibir no dashboard a lista de ativos monitorados com seus dados mais recentes. |
| **RF61** | O sistema deve exibir preço atual, variação, sinal técnico, sentimento predominante e decisão atual por ativo. |
| **RF62** | O sistema deve exibir o nível de confiança e a justificativa da decisão. |
| **RF63** | O sistema deve exibir o histórico de preços em formato gráfico. |
| **RF64** | O sistema deve exibir a linha do tempo de notícias relacionadas ao ativo. |
| **RF65** | O sistema deve permitir filtro por ticker, mercado, data, ação recomendada e nível de confiança. |
| **RF66** | O sistema deve permitir a visualização detalhada de um ativo. |
| **RF67** | O sistema deve sinalizar visualmente quando houver dados insuficientes ou desatualizados. |
| **RF68** | O sistema deve atualizar os dados exibidos de forma periódica ou em tempo quase real. |
| **RF69** | O sistema deve permitir ao usuário consultar decisões históricas e suas justificativas. |
| **RF70** | O sistema deve permitir exportar consultas ou relatórios em formato estruturado, caso essa funcionalidade seja habilitada no escopo. |

### 1.9 Administração e Governança

| ID | Descrição |
|---|---|
| **RF71** | O sistema deve permitir autenticação de usuários. |
| **RF72** | O sistema deve permitir controle de acesso por perfil. |
| **RF73** | O sistema deve permitir que administradores cadastrem e gerenciem ativos monitorados. |
| **RF74** | O sistema deve permitir que administradores configurem parâmetros de análise, como janela temporal, pesos e limiares. |
| **RF75** | O sistema deve registrar alterações de parâmetros com data, hora, usuário e valor anterior e novo valor. |
| **RF76** | O sistema deve permitir que administradores reprocessarem notícias, análises técnicas e decisões. |
| **RF77** | O sistema deve permitir visualização de logs operacionais e erros de processamento. |
| **RF78** | O sistema deve registrar trilha de auditoria das ações administrativas. |

## 2. Requisitos Não Funcionais

### 2.1 Desempenho

| ID | Descrição |
|---|---|
| **RNF01** | O sistema deve confirmar o recebimento de dados de ingestão em até 1 segundo, em condições normais de operação. |
| **RNF02** | O sistema deve concluir a análise de uma notícia em até 5 segundos após a ingestão válida, em condições normais. |
| **RNF03** | O sistema deve responder à consulta da última decisão de um ativo em até 2 segundos, em condições normais. |
| **RNF04** | O dashboard deve refletir novas informações em até 5 segundos após o processamento, no cenário operacional previsto para a primeira versão. |

### 2.2 Escalabilidade

| ID | Descrição |
|---|---|
| **RNF05** | O sistema deve suportar crescimento do número de ativos monitorados sem necessidade de reestruturação arquitetural completa. |
| **RNF06** | O sistema deve suportar processamento concorrente de preços, notícias e decisões. |
| **RNF07** | O sistema deve permitir desacoplamento entre ingestão, processamento analítico e visualização. |

### 2.3 Disponibilidade

| ID | Descrição |
|---|---|
| **RNF08** | O sistema deve apresentar disponibilidade mínima de 99% no ambiente de produção. |
| **RNF09** | O sistema deve continuar operando parcialmente mesmo diante de falha pontual em um dos módulos não críticos. |
| **RNF10** | O sistema deve possuir mecanismo de recuperação em caso de falha temporária de integração externa. |

### 2.4 Segurança

| ID | Descrição |
|---|---|
| **RNF11** | O sistema deve exigir autenticação para acesso às funcionalidades protegidas. |
| **RNF12** | O sistema deve restringir funcionalidades administrativas a usuários autorizados. |
| **RNF13** | O sistema deve trafegar dados por conexão segura. |
| **RNF14** | O sistema deve proteger a API contra acesso indevido, payload malicioso e tentativas de abuso. |
| **RNF15** | O sistema deve registrar tentativas de autenticação inválida e falhas de autorização. |

### 2.5 Integridade e Confiabilidade

| ID | Descrição |
|---|---|
| **RNF16** | O sistema deve garantir integridade dos dados persistidos. |
| **RNF17** | O sistema deve garantir rastreabilidade entre dado de entrada, processamento e decisão emitida. |
| **RNF18** | O sistema não deve emitir decisão a partir de dados inválidos, corrompidos ou fora da janela de validade configurada. |
| **RNF19** | O sistema deve manter consistência entre versões de regras, notícias processadas, análise técnica e decisão gerada. |

### 2.6 Auditabilidade

| ID | Descrição |
|---|---|
| **RNF20** | Toda decisão deve ser auditável. |
| **RNF21** | O sistema deve manter histórico imutável das decisões emitidas. |
| **RNF22** | O sistema deve armazenar informações suficientes para reconstrução do contexto de uma decisão. |
| **RNF23** | Alterações em parâmetros críticos devem ficar registradas para fins de auditoria. |

### 2.7 Manutenibilidade

| ID | Descrição |
|---|---|
| **RNF24** | O sistema deve ser desenvolvido de forma modular. |
| **RNF25** | O sistema deve permitir evolução dos agentes de IA sem necessidade de reescrever o sistema completo. |
| **RNF26** | O sistema deve permitir inclusão futura de novos indicadores técnicos, novos classificadores e novas fontes de dados. |
| **RNF27** | O sistema deve possuir versionamento de API. |

### 2.8 Usabilidade

| ID | Descrição |
|---|---|
| **RNF28** | O dashboard deve ser responsivo e de fácil compreensão. |
| **RNF29** | O sistema deve apresentar estados visuais claros para sucesso, erro, carregamento e indisponibilidade de dados. |
| **RNF30** | O sistema deve destacar visualmente recomendações críticas e dados desatualizados. |

### 2.9 Observabilidade e Operação

| ID | Descrição |
|---|---|
| **RNF31** | O sistema deve registrar logs estruturados de ingestão, processamento e falhas. |
| **RNF32** | O sistema deve disponibilizar métricas operacionais mínimas de saúde, latência e volume processado. |
| **RNF33** | O sistema deve permitir monitoramento do status dos módulos principais. |
| **RNF34** | O sistema deve possuir rotina de backup do banco de dados e estratégia de restauração. |

## 3. Regras de Negócio

| ID | Descrição |
|---|---|
| **RN01** | Uma decisão somente poderá ser emitida se existir ao menos um preço válido e recente para o ativo. |
| **RN02** | Caso não haja dados históricos mínimos para análise técnica, o sistema deverá emitir hold ou estado equivalente de insuficiência de dados, conforme parametrização adotada. |
| **RN03** | Caso não exista notícia válida dentro da janela de recência configurada, a decisão poderá ser emitida com base apenas na análise técnica. |
| **RN04** | Notícias de alta relevância devem possuir maior peso no motor de decisão do que notícias de média e baixa relevância. |
| **RN05** | Quando análise técnica e análise de notícias forem convergentes, a confiança da decisão deve ser maior. |
| **RN06** | Quando análise técnica e análise de notícias forem conflitantes, a confiança da decisão deve ser reduzida. |
| **RN07** | Notícias classificadas como duplicadas não devem amplificar artificialmente o peso informacional do ativo. |
| **RN08** | Toda decisão deve conter ação, confiança, justificativa, data/hora e referência à versão da regra ou modelo utilizado. |
| **RN09** | Reprocessamentos não devem apagar decisões anteriores; devem gerar novo registro histórico. |
| **RN10** | Decisões exibidas ao usuário devem ser marcadas como inválidas ou desatualizadas quando baseadas em dados fora da janela de validade. |
| **RN11** | O sistema não deve executar ordens de compra ou venda no mercado; sua função é apenas analítica e recomendatória. |
| **RN12** | O sistema deve apresentar aviso de que a recomendação emitida é automatizada e não substitui avaliação humana ou recomendação financeira regulada. |

## 4. Requisitos de Dados

| ID | Descrição |
|---|---|
| **RD01** | O sistema deve persistir os dados de preços com granularidade temporal compatível com a frequência de ingestão. |
| **RD02** | O sistema deve persistir as notícias em formato bruto e também em formato enriquecido pela análise. |
| **RD03** | O sistema deve persistir as decisões juntamente com os identificadores dos insumos usados em sua geração. |
| **RD04** | O sistema deve armazenar timestamps em padrão consistente e preferencialmente em UTC. |
| **RD05** | O sistema deve manter versionamento lógico dos modelos, regras e parâmetros de decisão. |
| **RD06** | O sistema deve possibilitar indexação eficiente para consultas por ticker, data e status. |
| **RD07** | O sistema deve impedir perda de rastreabilidade entre preço, notícia, análise e decisão. |
| **RD08** | O sistema deve permitir retenção histórica compatível com análises futuras e auditorias. |
