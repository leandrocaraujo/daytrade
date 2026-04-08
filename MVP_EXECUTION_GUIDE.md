# MVP - Instruções de Execução

## 1. Setup Inicial

```bash
# 1.1 Clone/acesse o repositório
cd d:\daytrade

# 1.2 Configure variáveis de ambiente
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

## 2. Iniciar com Docker Compose

```bash
# 2.1 Construa e inicie todos os serviços
docker compose up -d --build

# 2.2 Verifique status
docker compose ps

# Esperado:
# - db (PostgreSQL)
# - redis (Cache)
# - rabbitmq (Message Queue)
# - backend (FastAPI)
# - frontend (React)
# - nginx (Reverse Proxy)
```

## 3. Testar API

### 3.1 Health Check
```bash
curl http://localhost/health
```

### 3.2 Login Obter Token
```bash
curl -X POST "http://localhost/api/auth/login?email=user@example.com&password=password123"
```

### 3.3 Adicionar Ativo
```bash
curl -X POST http://localhost/api/assets \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "PETR4",
    "name": "Petrobras PN",
    "market": "B3"
  }'
```

### 3.4 Ingerir Preço
```bash
curl -X POST http://localhost/api/prices \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "PETR4",
    "price": 30.50,
    "volume": 100000,
    "timestamp": "2026-04-08T10:00:00"
  }'
```

### 3.5 Obter Decisão
```bash
curl http://localhost/api/decision/PETR4
```

## 4. Frontend Web

Acesse: **http://localhost**

- Email: `user@example.com`
- Senha: `password123`

## 5. Executar Testes

```bash
# 5.1 Testes do backend (dentro do container)
docker compose exec backend pytest tests/ -v

# 5.2 Testes unitários
docker compose exec backend pytest tests/test_price_service.py -v

# 5.3 Testes da API
docker compose exec backend pytest tests/test_api.py::test_login -v
```

## 6. Parar Serviços

```bash
docker compose down
```

## 7. Limpar Tudo (incluindo volumes)

```bash
docker compose down -v
```

## 8. Acessos

- **Frontend**: http://localhost (ou http://localhost:3000)
- **Backend API**: http://localhost/api
- **Swagger Docs**: http://localhost/api/docs
- **RabbitMQ**: http://localhost:15672 (guest/guest)
- **PostgreSQL**: localhost:5432 (user/password)
- **Redis**: localhost:6379

## 9. Logs

```bash
# Ver logs de um serviço específico
docker compose logs -f backend

# Ver logs de todos os serviços
docker compose logs -f
```

## 10. Estrutura do Projeto

```
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── routes/
│   │       ├── auth.py
│   │       └── assets.py
│   ├── core/
│   │   ├── models.py
│   │   └── security.py
│   ├── database/
│   │   ├── models.py
│   │   └── session.py
│   ├── services/
│   │   └── price_service.py
│   ├── tests/
│   │   ├── test_api.py
│   │   └── test_price_service.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── Login.tsx
│   │   ├── AssetForm.tsx
│   │   └── AssetList.tsx
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── nginx.conf
└── SETUP_MVP.md
```

## 11. Próximas Melhorias (Pós-MVP)

- [ ] Integração com APIs de dados reais (Alpha Vantage, IEX)
- [ ] Processamento de notícias com NLP
- [ ] Mais indicadores técnicos (RSI, MACD, Bollinger Bands)
- [ ] Persistência em PostgreSQL
- [ ] Autenticação mais robusta
- [ ] Frontend com gráficos (Chart.js)
- [ ] Mobile app (React Native)
- [ ] CI/CD automatizado
