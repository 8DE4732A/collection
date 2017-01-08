import web
import datetime

urls = (
    '/(.*)js', 'Index',
    '/query', 'Query'
)

db = web.database(dbn='sqlite', db='/var/collect.db')

class Index:
    def __init__(self):
        pass

    def GET(self, value):
        ip = web.ctx.ip
        db.insert('COLLECTION', IPADDRESS=ip, ID=datetime.datetime.utcnow())
        return "IP: ", ip

class Query:
    def __init__(self):
        pass

    def GET(self):
        return list(db.select("COLLECTION"))


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
