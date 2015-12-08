#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015, Michael Ingraham <mingraham@solarcity.com>, and others
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_import_pfx_cert
short_description: Imports pfx certs to windows machine
description:
    - Imports pfx certs to windows machine with proper condition checks and remote cert location variability
options:
    path:
        description:
            - Local pfx cert file location to copy to the remote windows machines
        required: true
    state:
        description:
            - Whether the pfx cert file given should be imported or deported
        choices:
            - present
            - absent
        default: present
    password:
    	description:
	    - Password for password protected pfx certs
        required: false
author: Michael Ingraham
'''

EXAMPLES = '''
# Import a pfx cert
- win_import_pfx_cert:
    path: /etc/ansible/files/certs/my_cert.pfx

# Import a password-protected pfx cert
- win_import_pfx_cert:
    path: /etc/ansible/files/certs/my_cert.pfx
    password: my_pwd

# Deport a pfx cert
- win_import_pfx_cert:
    path: /etc/ansible/files/certs/my_cert.pfx
    state: absent

# Deport a password-protected pfx cert
- win_import_pfx_cert:
    path: /etc/ansible/files/certs/my_cert.pfx
    state: absent
    password: my_pwd
'''

