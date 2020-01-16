## Net-info: Get IP private/public and interfaces.

## Features

* Runs on Linux/BSD (Ubuntu, Fedora, OpenBSD and others), macOS (10.10+), Windows (7/8/10).
* List Network interfaces.
* Show the operating system.
* know your WAN IP address.
* know your LAN IP address of all interfaces.  

## Python version required  

Use Python version higher or equal to 3.4.10

**NOTE:**  

The purpose of this script is to obtain a list of interfaces and their IPs (Private and Wan) in detail or abbreviated. It also provides the type of device operating system installed.  

**Compatibility:**  

Net-Info has been tested and is know to work on Ubuntu 18.04 LTS, Mac OS 10.15 and Windows 10.  
it probably works on other flavours of Linux, OS X and Windows as well.  

## Documentation  

<https://https://github.com/kentron2019/Get-info/wiki>  

## Installation  

<https://https://github.com/kentron2019/Get-info/wiki/Installation>  


**LINUX:**  

Install packages specified on the requirements.txt

pip install requirements.txt

**Windows** 

Install python and packages specified on the requirements.txt

pip install requirements.txt

**macOS** 

For Mac OS X Install:  
1-  brew install iproute2mac 
and:  
2- pip the specified pakages listed in the requirements.txt  


## Usage 
  
	python3 Get-info help
	python3 Get-info.py interfaces
	python3 Get-info.py all
    python3 Get-info.py all_brief
    python3 Get-info.py system


## Examples

* help (`python3 Get-info.py help`):

    `- Get-info.py [system]`  
    `- Get-info.py [interfaces]`  
    `- Get-info.py [all]`  
    `- Get-info.py [all_brief]`  

* system (`python3 Get-info.py system`):

    Example:

    `-  lo`  
    `-  wlan0`  
    `-  zt3jn4u2jc`  
    `-  eth0`  

* interfaces (`python3 Get-info.py interfaces`):

    Example:  

    `-  lo`  
    `-  wlan0`  
    `-  zt3jn4u2jc`  
    `-  eth0`  

* Interfaces (`python3 Get-info.py all`):

    Example:

    `inet 127.0.0.1/8 scope host lo`  
    `inet6 ::1/128 scope host`  

    `inet 192.168.1.108/24 brd 192.168.1.255 scope global noprefixroute wlan0`  
    `inet6 fe80::fa38:e4f3:2264:300c/64 scope link`  
    
    `inet 192.168.196.110/24 brd 192.168.196.255 scope global zt3jn4u2jc`  
    `inet 169.254.214.74/16 brd 169.254.255.255 scope global noprefixroute zt3jn4u2jc`  
    `inet6 fe80::fc09:86d4:57b4:efd8/64 scope link`  
    `inet6 fe80::94f1:23ff:fe0e:86a5/64 scope link`  

* Interfaces (`python3 Get-info.py all_brief`):

    Example:

    `Private ip:`  
    `--------------------------`  
    `Interface:   lo`  
    `IP address:  127.0.0.1`  
    `--------------------------`  
    `Interface:   wlan0`  
    `IP address:  192.168.1.108`  
    `--------------------------`  
    `Interface:   zt3jn4u2jc`  
    `IP address:  192.168.196.110`  
    `--------------------------`  
    `Interface:   zt3jn4u2jc`  
    `IP address:  169.254.214.74`  

* Interfaces (`python3 Get-info.py wan`):

    Example:

    `IP WAN detected: `
    ` xxx.xxx.xxx.xxx`


## Maintainer

- [Karim Zin El Abidine El Alaoui](https://github.com/kentron2019)

