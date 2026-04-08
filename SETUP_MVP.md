# MVP - Plataforma Analítica em Tempo Real

## Setup Local

### 1. Variáveis de Ambiente

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### 2. Iniciar Serviços com Docker

```bash
docker compose up -d --build
```

### 3. Verificar Status

```bash
docker compose ps
```

### 4. Executar Migrações (quando configurado Alembic)

```bash
docker compose exec backend python -m alembic upgrade head
```

## API Endpoints

### Criar Ativo
```bash
curl -X POST http://localhost/api/assets \
     -H "Content-Type: application/json" \
     -d '{"ticker": "PETR4", "name": "Petrobras PN", "market": "B3"}'
```

### Ingerir Preço
```bash
curl -X POST http://localhost/api/prices \
     -H "Content-Type: application/json" \
     -d '{"ticker": "PETR4", "price": 30.50, "volume": 100000, "timestamp": "2026-04-08T10:00:00Z"}'
```

### Consultar Decisão
```bash
curl http://localhost/api/decision/PETR4
```

## Acessos

- **Frontend**: http://localhost
- **Backend API**: http://localhost/api
- **RabbitMQ**: http://localhost:15672 (guest/guest)
- **Documentação API**: http://localhost/api/docs

## Estrutura do Projeto

- `backend/`: Aplicação FastAPI
- `frontend/`: Aplicação React
- `docker-compose.yml`: Orquestração de serviços
- `nginx.conf`: Configuração do reverse proxy
