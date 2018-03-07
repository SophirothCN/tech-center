
- [x] item Name:
 
 updateAndReload_.alv.pub_named

- [x] Max # of builds to keep

5

- [x] Repository URL
 
 https://github.com/AlvinWanCN/TechnologyCenter.git

- [x]  Polling ignores commits in certain paths.Included Regions

sophiroth_cluster/alv.pub/named/alv.pub.zone

- [x] Poll SCM

(* * * * *)

- [x] SSH site: 

alvin@ansible.alv.pub:22

- [x] Command

ssh dhcp 'sudo python -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/TechnologyCenter/master/sophiroth_cluster/dhcp.alv.pub/updateDhcpd.py)"'