Role Name
=========

win_import_pfx_cert

Getting Started
---------------

mv files/module/* /usr/share/ansible/my_modules/

Description
-----------

Imports pfx certs to windows machine with proper condition checks and remote cert location variability

Requirements
------------

None

Role Variables
--------------

cert_location can be set in vars/main.yml and is the location on your ansible server where the pfx file is living so that ansible can copy it down to your remote server(s)

Dependencies
------------

The module win_import_pfx_cert.ps1 (with win_import_cert.py) in /usr/share/ansible/my_modules/
- Make sure to fill in your remote cert locations inside $remote_cert_locations in win_import_pfx_cert.ps1
  - Default is "My" and "Root"

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - win_import_pfx_cert

License
-------

MIT

Author Information
------------------

Michael Ingraham is a DevOps Engineer at SolarCity HQ in San Mateo, CA.
