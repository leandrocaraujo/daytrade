import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export default function AssetList({ token, refresh }) {
  const [assets, setAssets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedAsset, setSelectedAsset] = useState(null);
  const [decision, setDecision] = useState(null);
  const [prices, setPrices] = useState([]);

  const fetchAssets = useCallback(async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_URL}/api/assets`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setAssets(response.data.assets || []);
    } catch (error) {
      console.error('Erro ao buscar ativos:', error);
    } finally {
      setLoading(false);
    }
  }, [token]);

  useEffect(() => {
    fetchAssets();
  }, [fetchAssets, refresh]);

  const handleSelectAsset = async (asset) => {
    setSelectedAsset(asset);

    // Buscar decisão
    try {
      const decisionResponse = await axios.get(
        `${API_URL}/api/decision/${asset.ticker}`,
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setDecision(decisionResponse.data);
    } catch (error) {
      console.error('Erro ao buscar decisão:', error);
    }

    // Buscar preços
    try {
      const pricesResponse = await axios.get(
        `${API_URL}/api/prices/${asset.ticker}?limit=20`,
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setPrices(pricesResponse.data.prices || []);
    } catch (error) {
      console.error('Erro ao buscar preços:', error);
    }
  };

  if (loading) return <p>Carregando ativos...</p>;

  return (
    <div style={{ display: 'flex', gap: '20px' }}>
      <div style={{ flex: 1 }}>
        <h3>Ativos Monitorados</h3>
        {assets.length === 0 ? (
          <p>Nenhum ativo cadastrado. Adicione um novo!</p>
        ) : (
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {assets.map((asset) => (
              <li
                key={asset.ticker}
                onClick={() => handleSelectAsset(asset)}
                style={{
                  padding: '10px',
                  margin: '5px 0',
                  border: `2px solid ${selectedAsset?.ticker === asset.ticker ? '#007bff' : '#ddd'}`,
                  borderRadius: '5px',
                  cursor: 'pointer',
                  backgroundColor: selectedAsset?.ticker === asset.ticker ? '#e7f3ff' : '#f9f9f9'
                }}
              >
                <strong>{asset.ticker}</strong> - {asset.name}
                <br />
                <small style={{ color: '#666' }}>Mercado: {asset.market}</small>
              </li>
            ))}
          </ul>
        )}
      </div>

      <div style={{ flex: 1 }}>
        {selectedAsset && (
          <>
            <h3>{selectedAsset.ticker} - Detalhes</h3>

            {decision && (
              <div style={{
                padding: '15px',
                backgroundColor: decision.decision === 'BUY' ? '#d4edda' : decision.decision === 'SELL' ? '#f8d7da' : '#fff3cd',
                border: '1px solid #ccc',
                borderRadius: '5px',
                marginBottom: '20px'
              }}>
                <h4>Recomendação: <span style={{ fontSize: '18px' }}>{decision.decision}</span></h4>
                {decision.reason && <p>Motivo: {decision.reason}</p>}
                {decision.current_price && <p>Preço Atual: R$ {decision.current_price.toFixed(2)}</p>}
                {decision.sma_20 && <p>SMA 20: R$ {decision.sma_20.toFixed(2)}</p>}
              </div>
            )}

            {prices.length > 0 && (
              <div>
                <h4>Últimos Preços</h4>
                <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                  <thead>
                    <tr style={{ backgroundColor: '#f0f0f0' }}>
                      <th style={{ border: '1px solid #ccc', padding: '8px' }}>Data</th>
                      <th style={{ border: '1px solid #ccc', padding: '8px' }}>Preço</th>
                      <th style={{ border: '1px solid #ccc', padding: '8px' }}>Volume</th>
                    </tr>
                  </thead>
                  <tbody>
                    {prices.slice().reverse().map((price, idx) => (
                      <tr key={idx}>
                        <td style={{ border: '1px solid #ccc', padding: '8px' }}>
                          {new Date(price.timestamp).toLocaleString('pt-BR')}
                        </td>
                        <td style={{ border: '1px solid #ccc', padding: '8px' }}>
                          R$ {parseFloat(price.price).toFixed(2)}
                        </td>
                        <td style={{ border: '1px solid #ccc', padding: '8px' }}>
                          {price.volume.toLocaleString()}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
