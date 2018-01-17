#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Azbil corporation. All Rights Reserved.


from flask import Flask
from jinja2 import Environment, FileSystemLoader
import pymysql

app = Flask(__name__)
env = Environment(loader=FileSystemLoader("./templates", encoding="utf8"))
tpl = env.get_template("index.html")

@app.route("/")
def main():

    db = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "root",
            db = "testdb",
            charset = "utf8",
            cursorclass = pymysql.cursors.DictCursor
    )

    cur = db.cursor()
    sql = "select member from members"
    cur.execute(sql)
    members = list()
    for m in cur.fetchall():
        members.append(m["member"])

    cur.close()
    db.close()

    return tpl.render({"title": "flask sample", "members": members})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
