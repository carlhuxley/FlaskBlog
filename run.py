# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:42:46 2019

@author: JMN
"""
from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
