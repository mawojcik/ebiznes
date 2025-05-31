import React, { useEffect, useState } from 'react';

function App() {
  const [mode, setMode] = useState('login'); // 'login' | 'register'
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('sessionToken');
    if (token) {
      fetch('http://localhost:1/api/me', {
        method: 'GET',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.username) {
            setCurrentUser(data.username);
            setMessage(`Zalogowano jako: ${data.username}`);
          }
        })
        .catch((err) => {
          console.error('Błąd pobierania danych użytkownika:', err);
        });
    }
  }, []);

  
  const handleSubmit = async (e) => {
    e.preventDefault();
    const endpoint = mode === 'login' ? 'login' : 'register';

    try {
      const response = await fetch(`http://localhost:5001/api/${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (response.ok) {
        if (data.sessionToken) {
          localStorage.setItem('sessionToken', data.sessionToken);
          setMessage('Zalogowano pomyślnie!');
          setCurrentUser(username);
        } else {
          setMessage(data.message || 'Sukces!');
        }
      } else {
        setMessage(data.message || 'Wystąpił błąd');
      }
    } catch (err) {
      console.error('Błąd połączenia:', err);
      setMessage('Nie udało się połączyć z serwerem');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('sessionToken');
    setCurrentUser(null);
    setMessage('Wylogowano');
  };

  return (
    <div style={{ maxWidth: 400, margin: '2rem auto', textAlign: 'center' }}>
      <h2>{mode === 'login' ? 'Logowanie' : 'Rejestracja'}</h2>

      {currentUser ? (
        <div>
          <p>Jesteś zalogowany jako <strong>{currentUser}</strong></p>
          <button onClick={handleLogout}>Wyloguj się</button>
        </div>
      ) : (
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Nazwa użytkownika"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            style={{ display: 'block', margin: '0.5rem auto', padding: '0.5rem', width: '100%' }}
          />
          <input
            type="password"
            placeholder="Hasło"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ display: 'block', margin: '0.5rem auto', padding: '0.5rem', width: '100%' }}
          />
          <button type="submit" style={{ padding: '0.5rem 1rem', marginTop: '1rem' }}>
            {mode === 'login' ? 'Zaloguj się' : 'Zarejestruj się'}
          </button>
        </form>
      )}

      <div style={{ marginTop: '1rem' }}>
        <button onClick={() => setMode(mode === 'login' ? 'register' : 'login')}>
          Przełącz na {mode === 'login' ? 'Rejestrację' : 'Logowanie'}
        </button>
      </div>

      {message && <p style={{ marginTop: '1rem' }}>{message}</p>}
    </div>
  );
}

export default App;
