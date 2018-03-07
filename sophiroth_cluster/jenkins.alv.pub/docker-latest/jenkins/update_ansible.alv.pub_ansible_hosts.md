item Name: update_ansible.alv.pub_ansible_hosts

Max # of builds to keep:5

Repository URL: https://github.com/AlvinWanCN/TechnologyCenter.git

Polling ignores commits in certain paths.Included Regions: sophiroth_cluster/ansible.alv.pub/ansible/conf.d/hosts

Poll SCM: * * * * *

SSH site: alvin@ansible.alv.pub:22
Command: python -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/TechnologyCenter/master/sophiroth_cluster/ansible.alv.pub/scripts/update.ansible.hosts.py)"