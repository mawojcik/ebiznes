const express = require('express');
const session = require('express-session');
const cors = require('cors');
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
require('dotenv').config();
const sqlite3 = require('sqlite3').verbose();
const crypto = require('crypto');

const db = new sqlite3.Database('./users.db');
db.run(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    googleId TEXT,
    username TEXT,
    sessionToken TEXT
  )
`);

const app = express();

app.use(cors({
  origin: 'http://localhost:3000',
  credentials: true
}));
app.use(express.json());

app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false
}));

app.use(passport.initialize());
app.use(passport.session());

passport.serializeUser((user, done) => done(null, user.id));
passport.deserializeUser((id, done) => {
  db.get('SELECT * FROM users WHERE id = ?', [id], (err, row) => {
    if (err) return done(err);
    done(null, row);
  });
});

passport.use(new GoogleStrategy({
  clientID: process.env.GOOGLE_CLIENT_ID,
  clientSecret: process.env.GOOGLE_CLIENT_SECRET,
  callbackURL: '/api/auth/google/callback'
}, (accessToken, refreshToken, profile, done) => {
  const googleId = profile.id;
  const username = profile.displayName;

  db.get('SELECT * FROM users WHERE googleId = ?', [googleId], (err, row) => {
    if (err) return done(err);

    if (row) {
      return done(null, row);
    } else {
      const sessionToken = crypto.randomBytes(32).toString('hex');
      db.run('INSERT INTO users (googleId, username, sessionToken) VALUES (?, ?, ?)',
        [googleId, username, sessionToken],
        function (err) {
          if (err) return done(err);
          db.get('SELECT * FROM users WHERE id = ?', [this.lastID], (err, newUser) => {
            if (err) return done(err);
            done(null, newUser);
          });
        });
    }
  });
}));

app.get('/api/auth/google',
  passport.authenticate('google', { scope: ['profile'] })
);

app.get('/api/auth/google/callback',
  passport.authenticate('google', { failureRedirect: 'http://localhost:3000?error=login_failed' }),
  (req, res) => {
    const token = req.user.sessionToken;
    res.redirect(`http://localhost:3000/?token=${token}`);
  }
);

app.get('/api/me', (req, res) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ message: 'Brak tokena' });

  const token = authHeader.split(' ')[1];
  db.get('SELECT username FROM users WHERE sessionToken = ?', [token], (err, row) => {
    if (err || !row) return res.status(401).json({ message: 'Nieprawidłowy token' });
    res.json({ username: row.username });
  });
});

app.listen(5001, () => {
  console.log('✅ Serwer działa na http://localhost:5001');
});
