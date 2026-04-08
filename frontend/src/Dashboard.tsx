import { useState, useEffect } from 'react';

export default function Dashboard() {
  const [asset, setAsset] = useState(null);
  const [prices, setPrices] = useState([]);
  const [decision, setDecision] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchAssets();
  }, []);

  const fetchAssets = async () => {
    setLoading(true);
    try {
      // Buscar ativos da API
      console.log('Buscando ativos...');
    } catch (error) {
      console.error('Erro ao buscar ativos:', error);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Dashboard - Plataforma Analítica</h1>
      
      <div style={{ marginBottom: '20px' }}>
        <h2>Ativos Monitorados</h2>
        {loading ? <p>Carregando...</p> : <p>Nenhum ativo selecionado</p>}
      </div>

      <div style={{ marginBottom: '20px' }}>
        <h2>Histórico de Preços</h2>
        {prices.length > 0 ? (
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr>
                <th style={{ border: '1px solid #ccc', padding: '8px' }}>Data</th>
                <th style={{ border: '1px solid #ccc', padding: '8px' }}>Preço</th>
                <th style={{ border: '1px solid #ccc', padding: '8px' }}>Volume</th>
              </tr>
            </thead>
            <tbody>
              {prices.map((p, i) => (
                <tr key={i}>
                  <td style={{ border: '1px solid #ccc', padding: '8px' }}>{p.timestamp}</td>
                  <td style={{ border: '1px solid #ccc', padding: '8px' }}>R$ {p.price}</td>
                  <td style={{ border: '1px solid #ccc', padding: '8px' }}>{p.volume}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>Sem dados de preços</p>
        )}
      </div>

      <div>
        <h2>Recomendação</h2>
        {decision ? (
          <div style={{ padding: '10px', backgroundColor: '#f0f0f0', borderRadius: '5px' }}>
            <p><strong>Decisão:</strong> {decision.decision}</p>
            <p><strong>Motivo:</strong> {decision.reason}</p>
          </div>
        ) : (
          <p>Sem recomendação disponível</p>
        )}
      </div>
    </div>
  );
}
