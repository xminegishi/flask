#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Azbil corporation. All Rights Reserved.

from flask import Flask
from .home import home

app = Flask(__name__)
app.register_blueprint(home)
