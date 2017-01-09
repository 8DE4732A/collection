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
        refer = web.ctx.env.get('HTTP_REFERER', '')
        db.insert('COLLECTION', IPADDRESS=ip, ID=datetime.datetime.utcnow(), REFERER=refer)
        return "OK"

class Query:
    def __init__(self):
        pass

    def GET(self):
        stories =  list(db.select("COLLECTION"))
        render = web.template.frender('templates/query.html')
        return render(stories)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
