# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys

try:
    assert sys.version_info >= (3, 4)
except:
        print("Please use Python higher or equal to vertion 3.4")
        sys.exit()    

from modul.getinfo import Gettinginfo


test = ['system', 'interfaces', 'all', 'all_brief', 'wan']

for x in test:
    recibir_todo = x
    a = Gettinginfo(recibir_todo)
    print(a.get())

