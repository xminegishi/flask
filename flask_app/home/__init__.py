#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Azbil corporation. All Rights Reserved.

from flask import Blueprint
# from jinja2 import Environment, FileSystemLoader

home = Blueprint("home", __name__, template_folder="templates", static_folder="static")
# env = Environment(loader=FileSystemLoader("flask_app/home/templates/home", encoding="utf8"))

from . import views
