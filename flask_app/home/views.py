#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Azbil corporation. All Rights Reserved.


from . import home
from ..models import Member
from flask import render_template

# tpl = env.get_template("index.html")


@home.route("/")
def hello():
    m = Member()
    members = m.all_members()
    # return tpl.render({"title": "flask", "members": members})
    return render_template("home/index.html", title="flask", members=members)
