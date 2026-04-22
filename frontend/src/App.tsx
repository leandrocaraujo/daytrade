import React, { useState } from 'react';
import Login from './Login.tsx';
import AssetForm from './AssetForm.tsx';
import AssetList from './AssetList.tsx';

export default function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [refresh, setRefresh] = useState(0);

  const handleLoginSuccess = (accessToken) => {
    setToken(accessToken);
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setToken(null);
  };

  const handleAssetCreated = () => {
    setRefresh(refresh + 1);
  };

  if (!token) {
    return <Login onLoginSuccess={handleLoginSuccess} />;
  }

  return (
    <div style={{
      maxWidth: '1200px',
      margin: '0 auto',
      padding: '20px',
      fontFamily: 'Arial, sans-serif'
    }}>
      <header style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '30px',
        borderBottom: '2px solid #333',
        paddingBottom: '15px'
      }}>
        <h1>Plataforma Analítica Financeira</h1>
        <button
          onClick={handleLogout}
          style={{
            padding: '10px 20px',
            backgroundColor: '#dc3545',
            color: 'white',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer'
          }}
        >
          Sair
        </button>
      </header>

      <main>
        <AssetForm token={token} onAssetCreated={handleAssetCreated} />
        <AssetList token={token} refresh={refresh} />
      </main>

      <footer style={{
        marginTop: '50px',
        padding: '20px',
        backgroundColor: '#f0f0f0',
        textAlign: 'center',
        borderRadius: '5px'
      }}>
        <p>Versão 0.1.0 MVP | © 2026 Plataforma Analítica</p>
      </footer>
    </div>
  );
}
