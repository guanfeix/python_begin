import json
import requests
import random
def main():
    nodes_list =[
                '172.30.229.68', '192.168.2.131', '192.168.0.116', '172.30.195.229', '192.168.0.114', '172.30.193.239',
                '172.30.220.151', '172.30.221.94', '192.168.5.110', '192.168.1.230', '172.30.219.128', '172.30.197.39',
                '172.30.180.248', '172.30.194.8', '172.30.221.61', '172.30.228.29', '172.30.224.178', '172.30.196.56',
                '172.30.233.21', '172.30.211.194', '172.30.198.86', '192.168.0.46', '192.168.1.207', '192.168.1.174',
                '192.168.1.242', '192.168.0.107']
    locked_list={}
    for ip in nodes_list:
        locked = 'locked'
        locked_list[ip] ={locked: True}
        if locked_list.get(ip).get(locked):
            response = requests.get(ip)
            locked_list[ip].setdefault(locked, False)


if __name__=='__main__':
    main()