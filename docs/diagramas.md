# Diagramas de Casos de Uso (DCU)

## 1. Diagrama de Caso de Uso Geral

Este diagrama apresenta uma visão geral de todos os atores e casos de uso da plataforma analítica.

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle

actor "Investidor / Usuário Analista" as Usuario
actor "Administrador" as Admin
actor "Sistema Externo de Mercado" as Mercado
actor "Sistema Externo de Notícias" as Noticias

rectangle "Plataforma Analítica em Tempo Real\npara Mercado Financeiro" {
  usecase "Autenticar usuário" as UC01
  usecase "Consultar dashboard" as UC02
  usecase "Consultar ativo" as UC03
  usecase "Consultar histórico de preços" as UC04
  usecase "Consultar notícias por ativo" as UC05
  usecase "Consultar decisão atual" as UC06
  usecase "Consultar histórico de decisões" as UC07

  usecase "Registrar preço" as UC08
  usecase "Registrar notícia" as UC09

  usecase "Analisar notícia" as UC10
  usecase "Calcular indicadores técnicos" as UC11
  usecase "Gerar decisão automática" as UC12

  usecase "Cadastrar ativo monitorado" as UC13
  usecase "Atualizar ativo monitorado" as UC14
  usecase "Ativar/Desativar ativo" as UC15
  usecase "Configurar parâmetros de análise" as UC16
  usecase "Reprocessar notícia" as UC17
  usecase "Reprocessar análise técnica" as UC18
  usecase "Reprocessar decisão" as UC19
  usecase "Monitorar saúde do sistema" as UC20
  usecase "Consultar logs e auditoria" as UC21
}

Usuario --> UC01
Usuario --> UC02
Usuario --> UC03
Usuario --> UC04
Usuario --> UC05
Usuario --> UC06
Usuario --> UC07

Mercado --> UC08
Noticias --> UC09

Admin --> UC01
Admin --> UC13
Admin --> UC14
Admin --> UC15
Admin --> UC16
Admin --> UC17
Admin --> UC18
Admin --> UC19
Admin --> UC20
Admin --> UC21

UC09 .> UC10 : <<include>>
UC08 .> UC11 : <<include>>
UC10 .> UC12 : <<include>>
UC11 .> UC12 : <<include>>
UC06 .> UC12 : <<include>>
UC19 .> UC12 : <<include>>

@enduml
```

## 2. Diagrama de Caso de Uso — Ingestão e Processamento Analítico

Este diagrama foca no núcleo do sistema: entrada de dados e processamento.

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle

actor "Sistema Externo de Mercado" as Mercado
actor "Sistema Externo de Notícias" as Noticias
actor "Administrador" as Admin

rectangle "Módulo de Ingestão e Processamento" {
  usecase "Registrar preço" as UC1
  usecase "Validar dados de preço" as UC2
  usecase "Armazenar preço" as UC3
  usecase "Consultar preços históricos" as UC4

  usecase "Registrar notícia" as UC5
  usecase "Validar dados da notícia" as UC6
  usecase "Armazenar notícia" as UC7
  usecase "Classificar sentimento" as UC8
  usecase "Classificar relevância" as UC9
  usecase "Armazenar análise da notícia" as UC10

  usecase "Calcular indicadores técnicos" as UC11
  usecase "Gerar sinal técnico" as UC12
  usecase "Gerar decisão automática" as UC13
  usecase "Registrar decisão" as UC14

  usecase "Reprocessar notícia" as UC15
  usecase "Reprocessar análise técnica" as UC16
  usecase "Reprocessar decisão" as UC17
}

Mercado --> UC1
Noticias --> UC5
Admin --> UC15
Admin --> UC16
Admin --> UC17

UC1 .> UC2 : <<include>>
UC1 .> UC3 : <<include>>
UC5 .> UC6 : <<include>>
UC5 .> UC7 : <<include>>
UC5 .> UC8 : <<include>>
UC5 .> UC9 : <<include>>
UC5 .> UC10 : <<include>>

UC13 .> UC11 : <<include>>
UC13 .> UC12 : <<include>>
UC13 .> UC14 : <<include>>

UC15 .> UC8 : <<include>>
UC15 .> UC9 : <<include>>
UC16 .> UC11 : <<include>>
UC16 .> UC12 : <<include>>
UC17 .> UC13 : <<include>>

@enduml
```

## 3. Diagrama de Caso de Uso — Consulta e Dashboard

Este diagrama mostra o que o usuário final faz na plataforma.

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle

actor "Investidor / Usuário Analista" as Usuario

rectangle "Módulo de Consulta e Dashboard" {
  usecase "Autenticar usuário" as UC1
  usecase "Visualizar dashboard geral" as UC2
  usecase "Visualizar detalhes do ativo" as UC3
  usecase "Consultar preço atual" as UC4
  usecase "Consultar histórico de preços" as UC5
  usecase "Consultar notícias do ativo" as UC6
  usecase "Consultar decisão atual" as UC7
  usecase "Consultar histórico de decisões" as UC8
  usecase "Filtrar ativos" as UC9
  usecase "Ordenar resultados" as UC10
  usecase "Visualizar justificativa da decisão" as UC11
  usecase "Visualizar nível de confiança" as UC12
  usecase "Visualizar alerta de dados insuficientes" as UC13
}

Usuario --> UC1
Usuario --> UC2
Usuario --> UC3
Usuario --> UC4
Usuario --> UC5
Usuario --> UC6
Usuario --> UC7
Usuario --> UC8
Usuario --> UC9
Usuario --> UC10
Usuario --> UC11
Usuario --> UC12
Usuario --> UC13

UC2 .> UC9 : <<extend>>
UC2 .> UC10 : <<extend>>
UC3 .> UC4 : <<include>>
UC3 .> UC5 : <<include>>
UC3 .> UC6 : <<include>>
UC3 .> UC7 : <<include>>
UC3 .> UC11 : <<include>>
UC3 .> UC12 : <<include>>
UC3 .> UC13 : <<extend>>

@enduml
```

## 4. Diagrama de Caso de Uso — Administração e Governança

Este diagrama representa as responsabilidades administrativas.

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle

actor "Administrador" as Admin

rectangle "Módulo de Administração e Governança" {
  usecase "Autenticar usuário" as UC1
  usecase "Cadastrar ativo monitorado" as UC2
  usecase "Atualizar ativo monitorado" as UC3
  usecase "Ativar/Desativar ativo" as UC4
  usecase "Configurar parâmetros de análise" as UC5
  usecase "Consultar logs operacionais" as UC6
  usecase "Consultar trilha de auditoria" as UC7
  usecase "Monitorar saúde do sistema" as UC8
  usecase "Reprocessar notícia" as UC9
  usecase "Reprocessar análise técnica" as UC10
  usecase "Reprocessar decisão" as UC11
  usecase "Gerenciar perfis de acesso" as UC12
}

Admin --> UC1
Admin --> UC2
Admin --> UC3
Admin --> UC4
Admin --> UC5
Admin --> UC6
Admin --> UC7
Admin --> UC8
Admin --> UC9
Admin --> UC10
Admin --> UC11
Admin --> UC12

@enduml
```