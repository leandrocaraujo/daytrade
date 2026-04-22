import React, { useState } from 'react';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export default function AssetForm({ token, onAssetCreated }) {
  const [ticker, setTicker] = useState('');
  const [name, setName] = useState('');
  const [market, setMarket] = useState('B3');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await axios.post(
        `${API_URL}/api/assets`,
        { ticker, name, market },
        { headers: { Authorization: `Bearer ${token}` } }
      );

      setTicker('');
      setName('');
      setMarket('B3');
      onAssetCreated(response.data);
    } catch (err) {
      setError('Erro ao criar ativo');
      console.error('Erro:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      padding: '20px',
      border: '1px solid #ddd',
      borderRadius: '5px',
      marginBottom: '20px'
    }}>
      <h3>Adicionar Novo Ativo</h3>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '10px' }}>
          <label>Ticker:</label>
          <input
            type="text"
            value={ticker}
            onChange={(e) => setTicker(e.target.value.toUpperCase())}
            placeholder="Ex: PETR4"
            required
            style={{ width: '100%', padding: '8px' }}
          />
        </div>

        <div style={{ marginBottom: '10px' }}>
          <label>Nome do Ativo:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Ex: Petrobras PN"
            required
            style={{ width: '100%', padding: '8px' }}
          />
        </div>

        <div style={{ marginBottom: '10px' }}>
          <label>Mercado:</label>
          <select
            value={market}
            onChange={(e) => setMarket(e.target.value)}
            style={{ width: '100%', padding: '8px' }}
          >
            <option>B3</option>
            <option>NYSE</option>
            <option>NASDAQ</option>
          </select>
        </div>

        {error && <p style={{ color: 'red' }}>{error}</p>}

        <button
          type="submit"
          disabled={loading}
          style={{
            padding: '10px 20px',
            backgroundColor: '#28a745',
            color: 'white',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer'
          }}
        >
          {loading ? 'Adicionando...' : 'Adicionar Ativo'}
        </button>
      </form>
    </div>
  );
}
