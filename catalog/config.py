DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///catalog.db'
SECRET_KEY = "k2978sj1928dhy124(*ASud8907ADSA7(*@#&1"
CLIENT_ID = ('781544697558-3gjnobb4utugg6f867i3m3ekpkg3jm50'
             '.apps.googleusercontent.com')
CLIENT_SECRET = 'kE2rGWXSL99467Vekd3QB1aK'
REDIRECT_URI = 'https://localhost:5000/auth/google'
AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
SCOPE = ['profile', 'email']

UPLOAD_FOLDER = 'uploads'
