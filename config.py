#API ORIENTED DATABASE CONFIGURATION
from flaskcors import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = '34.173.57.88'
app.config['MYSQL_DATABASE_USER'] = 'test'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
app.config['MYSQL_DATABASE_DB'] = 'Z_README_TO_RECOVER'

#app.config['MYSQL_DATABASE_USER'] = 'ScuRX0z6Nb'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'o6CJSRnS75'
#app.config['MYSQL_DATABASE_DB'] = 'ScuRX0z6Nb'
#app.config['MYSQL_DATABASE_HOST'] = 'remotemysql.com'
mysql.init_app(app)