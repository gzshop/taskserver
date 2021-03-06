
import os

common=dict(
    gzip = 'on',
    debug = False,
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    port = 9999,
    ordertime = int(os.environ.get('ORDERTIME', 30)),
    busiserver = os.environ.get("BUSIURL","http://localhost:9018/v2/api"),
    # busiServer = "http://localhost:9888"
)
common['static'] = os.path.join(common['basedir'],"static")
common['images'] = os.path.join(common['static'],"images")

mysql=dict(
	host = os.environ.get('DBHOST', 'localhost'),
	port = int(os.environ.get('DBPORT', 3306)),
	user = os.environ.get('DBUSER', 'root'),
    name = os.environ.get('DBNAME', 'gzshop'),
	password = os.environ.get('DBPASS', '123456'),
    min_connections=2,
    max_connections=20,
    charset='utf8'
)

redis=dict(
    host='localhost',
    port=6379,
    password="123456",
    db = 0,
    minsize = 5,
    maxsize = 20,
    encoding = 'utf8'
)

config_insert=dict(
	common = common,
	mysql = mysql,
	redis = redis
)