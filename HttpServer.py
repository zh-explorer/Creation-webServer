#! /usr/bin/python

import web
from getData import *
urls = (
        '/(.*)','index'
        )

app = web.application(urls,globals())

class index:
    def GET(self,name):
        data = ''
        i = web.input()
        user = i.get('user')
        if user == "explorer":
            latitude = i.get("latitude")
            longitude = i.get("longitude")
            data = getData(latitude, longitude)
        else:
            data = "Name Error"

        if data == None:
            data = "No Data"

        return data

if __name__ == "__main__":
    app.run()
