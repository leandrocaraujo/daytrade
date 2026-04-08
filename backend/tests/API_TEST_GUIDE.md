"""
Guia de teste dos endpoints da API

Teste os endpoints usando curl ou Postman
"""

# 1. Health check
GET http://localhost:8000/health

# 2. Login para obter token
POST http://localhost:8000/api/auth/login?email=user@example.com&password=password123

# Resposta esperada:
# {
#   "access_token": "eyJhbGc...",
#   "token_type": "bearer"
# }

# 3. Usar o token para acessar rota protegida
GET http://localhost:8000/api/auth/me
Authorization: Bearer {token_aqui}

# 4. Criar ativo
POST http://localhost:8000/api/assets
Content-Type: application/json

{
  "ticker": "PETR4",
  "name": "Petrobras PN",
  "market": "B3"
}

# 5. Listar ativos
GET http://localhost:8000/api/assets

# 6. Ingerir preço
POST http://localhost:8000/api/prices
Content-Type: application/json

{
  "ticker": "PETR4",
  "price": 30.50,
  "volume": 100000,
  "timestamp": "2026-04-08T10:00:00"
}

# 7. Obter decisão
GET http://localhost:8000/api/decision/PETR4

# 8. Obter histórico de preços
GET http://localhost:8000/api/prices/PETR4?limit=50

# ===== Executar testes com pytest =====
# cd backend
# pytest tests/ -v

# ===== Executar teste específico =====
# pytest tests/test_api.py::test_login -v
