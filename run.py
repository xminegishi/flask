#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Azbil corporation. All Rights Reserved.


from flask_app import app


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
