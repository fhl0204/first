#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

filename='/home/qinwt/PycharmProjects/first/reptile/result.csv'
content = pd.read_csv(filename)
print content.head(2)