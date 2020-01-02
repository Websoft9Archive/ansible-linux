#!/usr/bin/python env
# coding: utf-8

import os, sys, platform, shutil

def py2_input():
    a = raw_input("\nAre you sure to start installation?  [y/n]: ").lower()
    while a not in ('y', 'n'):
        print('\nInput error, please input "y" or "n":  ')
        a = raw_input("\nAre you sure to start installation?  [y/n]: ").lower()
    if a in ('no', 'n'):
        sys.exit()

    b = raw_input(
        "\nWhere do you want to install it? [1/2]: \n\t 1. local server \n\t 2. remote server\nPlease input a number: ")
    while b not in ('1', '2'):
        print('\nInput error, please input "1" or "2".')
        b = raw_input(
            "\nWhere do you want to install it? [1/2]: \n\t 1. local server \n\t 2. remote server\nPlease input a number: ")
    if b == "2":
        print('\nYou must input your remote server IP and account for installation\n')
        ip = raw_input("\tPublic or Internet IP: ")
        username = raw_input("\tUsername: ")
        password = raw_input("\tPassword: ")
    return a, b, ip, username, password

def py3_input():
    a = input("\nAre you sure to start installation?  [y/n]: ").lower()
    if a in ('no', 'n'):
        sys.exit()
    while a not in ('y', 'n'):
        print('\nInput error, please input "y" or "n":  ')
        a = input("\nAre you sure to start installation?  [y/n]: ").lower()

    b = input(
        "\nWhere do you want to install it? [1/2]: \n\t 1. local server \n\t 2. remote server\nPlease input a number: ")
    while b not in ('1', '2'):
        print('\nInput error, please input "1" or "2".')
        b = input(
            "\nWhere do you want to install it? [1/2]: \n\t 1. local server \n\t 2. remote server\nPlease input a number: ")
    if b == "2":
        print('\nYou must input your remote server IP and account for installation\n')
        ip = input("\tPublic or Internet IP: ")
        username = input("\tUsername: ")
        password = input("\tPassword: ")
    return a, b, ip, username, password

if sys.version_info.major < 3:
    py2_input()
elif sys.version_info.major >=3:
    py3_input()

print(a, b, ip, username, password)