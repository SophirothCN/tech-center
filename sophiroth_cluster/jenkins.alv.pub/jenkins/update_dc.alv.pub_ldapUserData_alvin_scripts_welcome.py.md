item Name: update_dc.alv.pub_ldapUserData_alvin_scripts_welcome.py

Max # of builds to keep:5

Repository URL: https://github.com/AlvinWanCN/scripts.git

Polling ignores commits in certain paths.Included Regions: python/sophiroth.welcome.py

Poll SCM: * * * * *

SSH site: alvin@ansible.alv.pub:22
Command: ssh dc 'curl -fsSL https://github.com/AlvinWanCN/scripts/raw/master/python/sophiroth.welcome.py > /ldapUserData/alvin/scripts/welcome.py'