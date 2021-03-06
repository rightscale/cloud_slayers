#!/usr/bin/python2
#The MIT License (MIT)
#
#Copyright (c) 2014 RightScale, Inc, All Rights Reserved Worldwide.
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import time
import havana

menu = '''
********************************************************************************
*Welcome to the OpenStack multinode installer. Please select an option below:  *
********************************************************************************

0: Install the Keystone Identity Service
1: Install the Cinder Storage Service
2: Install the Glance Image Service
3: Install the Nova Metadata Service (server)
4: Install the Nova Compute Service (client)
5: Install the Neutron Service
6: Install the RabbitMQ Service
7: Exit

Enter Choice: '''

def Install_Keystone():
    keystone_ip_address = raw_input("Please enter the public ip address of the keystone server: ")
    keystone_ip_address_mgmt = raw_input("Please enter the internal ip address of the keystone server: ")
    nova_ip_address = raw_input("Please enter the public ip address of the nova server: ")
    nova_ip_address_mgmt = raw_input("Please enter the internal ip address of the nova server: ")
    cinder_ip_address = raw_input("Please enter the public ip address of the cinder server: ")
    cinder_ip_address_mgmt = raw_input("Please enter the internal ip address of the cinder server: ")
    glance_ip_address = raw_input("Please enter the public ip address of the glance server: ")
    glance_ip_address_mgmt = raw_input("Please enter the internal ip address of the glance server: ")
    neutron_ip_address = raw_input("Please enter the public ip address of the neutron server: ")
    neutron_ip_address_mgmt = raw_input("Please enter the internal ip address of the neutron server: ")
    mysql_password=raw_input("Please enter the MySQL root password: ")
    mysql_ip=raw_input("Please enter the MySQL host ip: ")
    havana.initialize_system()
    havana.install_and_configure_keystone( keystone_ip_address, keystone_ip_address_mgmt, nova_ip_address, nova_ip_address_mgmt, cinder_ip_address, cinder_ip_address_mgmt, glance_ip_address, glance_ip_address_mgmt, mysql_ip, mysql_password )
    havana.create_keystone_users( keystone_ip_address, keystone_ip_address_mgmt, nova_ip_address, nova_ip_address_mgmt, cinder_ip_address, cinder_ip_address_mgmt, glance_ip_address, glance_ip_address_mgmt, neutron_ip_address, neutron_ip_address_mgmt )

def Install_Cinder():
    keystone_ip_address_mgmt = raw_input("Please enter the internal ip address of the keystone server: ")
    cinder_ip_address_mgmt = raw_input("Please enter the internal ip address of the cinder server: ")
    rabbit_ip_address_mgmt = raw_input("Please enter the internal ip address of the RabbitMQ server: ")
    mysql_password=raw_input("Please enter the MySQL root password: ")
    mysql_ip=raw_input("Please enter the MySQL host ip: ")
    havana.initialize_system()
    havana.install_and_configure_cinder( keystone_ip_address_mgmt, cinder_ip_address_mgmt, rabbit_ip_address_mgmt, mysql_ip, mysql_password )

def Install_Glance():
    keystone_ip_address_mgmt = raw_input("Please enter the internal ip address of the keystone server: ")
    mysql_password=raw_input("Please enter the MySQL root password: ")
    mysql_ip=raw_input("Please enter the MySQL host ip: ")
    havana.initialize_system()
    havana.install_and_configure_glance( keystone_ip_address_mgmt, mysql_ip, mysql_password )

def Install_Nova_Server():
    keystone_ip_address_mgmt = raw_input("Please enter the internal ip address of the keystone server: ")
    nova_ip_address = raw_input("Please enter the public ip address of the nova server: ")
    rabbit_ip_address_mgmt = raw_input("Please enter the internal ip address of the RabbitMQ server: ")
    glance_ip_address_mgmt = raw_input("Please enter the internal ip address of the glance server: ")
    neutron_ip_address_mgmt = raw_input("Please enter the internal ip address of the neutron server: ")
    mysql_ip=raw_input("Please enter the MySQL host ip: ")
    mysql_password=raw_input("Please enter the MySQL root password: ")
    havana.initialize_system()
    havana.install_and_configure_nova( keystone_ip_address_mgmt, nova_ip_address, rabbit_ip_address_mgmt, glance_ip_address_mgmt, neutron_ip_address_mgmt, mysql_ip, mysql_password )

def Install_Neutron_Server():
    keystone_ip_address_mgmt = raw_input("Please enter the internal ip address of the keystone server: ")
    neutron_ip_address = raw_input("Please enter the public ip address of the neutron server: ")
    neutron_ip_address_mgmt = raw_input("Please enter the internal ip address of the neutron server: ")
    rabbit_ip_address_mgmt = raw_input("Please enter the internal ip address of the RabbitMQ server: ")
    mysql_ip=raw_input("Please enter the MySQL host ip: ")
    mysql_password=raw_input("Please enter the MySQL root password: ")
    havana.initialize_system()
    havana.install_and_configure_neutron( neutron_ip_address, neutron_ip_address_mgmt, keystone_ip_address_mgmt, rabbit_ip_address_mgmt, mysql_ip, mysql_password )

def Install_Nova_Compute():
    keystone_ip_address_mgmt = raw_input("Please enter the internal ip address of the keystone server: ")
    nova_ip_address = raw_input("Please enter the public ip address of the nova server: ")
    glance_ip_address_mgmt = raw_input("Please enter the internal ip address of the glance server: ")
    neutron_ip_address = raw_input("Please enter the public ip address of the neutron server: ")
    neutron_ip_address_mgmt = raw_input("Please enter the internal ip address of the neutron server: ")
    rabbit_ip_address_mgmt = raw_input("Please enter the internal ip address of the RabbitMQ server: ")
    mysql_ip=raw_input("Please enter the MySQL host ip: ")
    havana.initialize_system()
    havana.install_and_configure_nova_compute( keystone_ip_address_mgmt, nova_ip_address, rabbit_ip_address_mgmt, glance_ip_address_mgmt, neutron_ip_address, neutron_ip_address_mgmt, my_ip, mysql_ip )
    havana.install_and_configure_ovs( rabbit_ip_address_mgmt, keystone_ip_address_mgmt, neutron_ip_address, mysql_ip )

def Install_RabbitMQ():
    havana.initialize_system()
    havana.install_rabbitmq()

choices = { "0" : Install_Keystone, "1": Install_Cinder, "2": Install_Glance, "3": Install_Nova_Server, "4": Install_Nova_Compute, "5": Install_Neutron_Server, "6": Install_RabbitMQ }

while True:
    try:
        choice=raw_input(menu)
        if choice == "7":
            break
        choices[choice]()
    except:
        print "Please choose an option from the menu above."


