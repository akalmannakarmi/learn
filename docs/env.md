# Required Environment variables
## Mode
### Windows
```
set FLASK_CONFIG production
```
### Unix
```
export FLASK_CONFIG=production
```
## SECRET_KEY
### Windows
```
set SECRET_KEY your_secret_key_here
```
### Unix
```
export SECRET_KEY=your_secret_key_here
```
# SQLALCHEMY_DATABASE_URI
### Windows
```
set SQLALCHEMY_DATABASE_URI postgresql://username:password@localhost/db_name
```
### Unix
```
export SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/db_name
```