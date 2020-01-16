
# -*- coding: utf-8 -*-
#!/usr/bin/env python

#######################################
#									  #
#       -----   Net-info   ----       #
#									  #
#######################################

import os
import sys
import subprocess
import platform
import psutil
import re
from requests import get

def obtener_ip(recibir_todo):

    # help
    if str(recibir_todo) == 'help':
        cmd_dispoinbles = ['Get-info.py [system]', 'Get-info.py [interfaces]', 'Get-info.py [all]', 'Get-info.py [all_brief]', 'Get-info.py [wan]']
        for x in cmd_dispoinbles:
            print("- "+x)
    # list
    elif str(recibir_todo) == 'interfaces':
        print("Interfaces found: ")
        addrs = psutil.net_if_addrs()
        #print(addrs.keys())
        for x in addrs.keys():
            print("- "+ x)
    # system
    elif str(recibir_todo) == 'system':
        print("Operating system detected: "+ platform.system())
    # all
    elif str(recibir_todo) == 'all':
        addrs = psutil.net_if_addrs()
        
        for x in addrs:
            p1 = os.popen('ip addr show '+str(x)+' | grep inet').read()
            print(p1)
    # all_brief
    elif str(recibir_todo) == 'all_brief':
        print("Private ip:")
        addrs = psutil.net_if_addrs()
        list_sav = []
        #leemos los valores para cada interfaz y lo guardamos.
        for x in addrs:
            p1 = os.popen('ip addr show '+str(x)+' | grep inet').read()
            nuevo_p1 = p1.splitlines()
            for x in p1.splitlines():
                list_sav.append(x)
        
        p1 = re.compile(r'(\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b)', re.M)
       
        linea=[]

        for list_interface in addrs.keys(): #para cada interfaz de del host.
            for valor in list_sav: #para cada línea del output ip addr show all_brief
                name = (r'\s')+ re.escape(list_interface)
                p2 = re.compile(name, re.M)
                res1 = re.search(p2, valor)           
            
                if res1:
                    linea.append(valor)

        for x in linea:
            for list_interface2 in addrs.keys():
                name = (r'\s')+ re.escape(list_interface2)
                p22 = re.compile(name, re.M)

                res11 = re.search(p1, x)
                res12 = re.search(p22, x)


                if res11 and res12 is not None:
                    print("--------------------------")
                    print("Interface: "+ res12.group())
                    print("IP address: "+ res11.group())
                    
    elif str(recibir_todo) == 'wan':
        print("IP WAN detected: \n"+ get('https://api.ipify.org').text)
    
    else:
        print("This argument does not exist.\nUse the help to know the arguments")

if __name__ == "__main__":
    try:
        assert sys.version_info >= (3, 4)
    except:
        print("Please use Python higher or equal to vertion 3.4")
  
    recibir_todo = sys.argv[1]
    obtener_ip(str(recibir_todo).lower())

    