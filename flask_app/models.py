#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Azbil corporation. All Rights Reserved.


import pymysql


class Member(object):
    def __init__(self):
        super().__init__()
        self.db = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "root",
                        db = "testdb",
                        charset = "utf8",
                        cursorclass = pymysql.cursors.DictCursor
                    )

    def __del__(self):
        self.db.close()

    def all_members(self):
        cur = self.db.cursor()
        sql = "select member from members"
        cur.execute(sql)
        members = list()
        for m in cur.fetchall():
            members.append(m["member"])

        cur.close()
        return members

    def close(self):
        self.db.close()
