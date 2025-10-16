#!/bin/bash

iptables -F
iptables -P INPUT DROP
iptables -A INPUT -i lo -j ACCEPT


iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

iptables -L -n --line-numbers
