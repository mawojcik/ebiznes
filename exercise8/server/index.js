const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const bcrypt = require('bcryptjs');
const sqlite3 = require('sqlite3').verbose();
const { v4: uuidv4 } = require('uuid');

const app = express();
const db = new sqlite3.Database('./users.db');
const PORT = 5001;

app.use(cors());
app.use(bodyParser.json());

// Tworzenie tabeli users
db.run(`CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE,
  password TEXT
)`);

// Tabela sesji
db.run(`CREATE TABLE IF NOT EXISTS sessions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  token TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(user_id) REFERENCES users(id)
)`);

// Rejestracja
app.post('/api/register', async (req, res) => {
  const { username, password } = req.body;
  db.get(`SELECT * FROM users WHERE username = ?`, [username], async (err, row) => {
    if (row) return res.status(400).json({ message: 'Użytkownik już istnieje' });

    const hashed = await bcrypt.hash(password, 10);
    db.run(`INSERT INTO users (username, password) VALUES (?, ?)`, [username, hashed], function (err) {
      if (err) return res.status(500).json({ message: 'Błąd serwera' });
      res.json({ message: 'Zarejestrowano pomyślnie' });
    });
  });
});

// Logowanie
app.post('/api/login', (req, res) => {
  const { username, password } = req.body;
  db.get(`SELECT * FROM users WHERE username = ?`, [username], async (err, user) => {
    if (!user || !(await bcrypt.compare(password, user.password))) {
      return res.status(401).json({ message: 'Nieprawidłowe dane logowania' });
    }

    const token = uuidv4();
    db.run(`INSERT INTO sessions (user_id, token) VALUES (?, ?)`, [user.id, token], (err) => {
      if (err) return res.status(500).json({ message: 'Błąd sesji' });
      res.json({ sessionToken: token });
    });
  });
});

// Sprawdzenie sesji
app.get('/api/me', (req, res) => {
  const auth = req.headers.authorization;
  if (!auth || !auth.startsWith('Bearer ')) {
    return res.status(401).json({ message: 'Brak tokena' });
  }

  const token = auth.split(' ')[1];
  db.get(`
    SELECT users.username FROM sessions
    JOIN users ON users.id = sessions.user_id
    WHERE sessions.token = ?
  `, [token], (err, row) => {
    if (!row) return res.status(401).json({ message: 'Nieprawidłowy token' });
    res.json({ username: row.username });
  });
});

app.listen(PORT, () => {
  console.log(`✅ Serwer działa na http://localhost:${PORT}`);
});

