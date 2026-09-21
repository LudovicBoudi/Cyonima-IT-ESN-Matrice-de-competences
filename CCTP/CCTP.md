# GPEC-IT

## Description

Outil en Python avec Django de gestion des compétences pour les managers de SSII/ESN/ICT. L'idée étant de permettre à des managers de voir les compétences auto évaluées par leurs employés.

Les compétences sont organisées par catégories, les catégories, de même que les compétences disponibles dans l'appli doivent être éditables par les administrateurs, qui pourront aussi en ajouter de nouvelles ou en supprimer d'autres. Les utilisateurs puisent leurs compétences de la liste disponible, puis indiquent leur niveau de 0 à 5. Dans l'interface graphique le niveau indiqué sera indiqué par une série d'étoiles.

L'interface sera en mode Dark pas de thème clair pour cette application. De préférence, les menus de l'application seront affichés en sidebar à gauche.

## profils utilisateurs

| ** Profil de compte ** | ** Droits **|
|** Administrateur ** | accède à l'ensemble des données ainsi qu'à l'administration des comptes utilisateurs. Il peut assigner un utilisateur à un manager |
|** Manager ** | accède en lecture et écriture aux profils de compétences de ses utilisateurs |
|** Utilisateur ** | accède uniquement à son propre profil de compétences en lecture et écriture |

## catégories de base :

- Applications
- Base de données
- Virtualisation
- DevOps
- Cloud
- Conteneurisation
- ERP
- CRM
- GED
- Messagerie
- Orchestration
- Réseau
- Système
- Développement
- Datacenter
- Méthodologie
- Sauvegarde & Restauration
- Stockage
- Cyber Sécurité
- Gestion de projet / programme
- Langue

## Compétences par catégories

### Applications

- Alfresco
- Apache
- ARender
- Certificate Management
- HA Proxy
- HTTP
- IBM PowerVM
- Microsoft IIS
- Nfast
- NGINX
- RabbitMQ
- Radius
- Redmine
- SharePoint
- Squid
- Tomcat
- Wallix Bastion
- Websphere
- MinIO
- Rsyslog
- ActiveMQ
- Keycloak
- SharePoint Online
- Jetty
- WildFly
- Apache Kafka
- Varnish
- Caddy

### Base de données

- Cassandra
- DB2
- Informix
- MariaDB
- MongoDB
- Microsoft SQL Server
- MySQL
- Oracle RAC
- Oracle Dataguard
- PostgreSQL
- ADABAS
- Redis
- Elasticsearch
- Couchbase
- Neo4j
- SQLite
- ClickHouse
- InfluxDB
- Memcached
- Oracle Exadata

### DevOps

- Git
- GitLab
- Gogs
- Gitea
- Ansible
- Bitbucket
- Jenkins
- Terraform
- Puppet
- PowerShell DSC
- Saltstack
- Artifactory
- XLDeploy/XLRelease
- GitHub Actions
- GitLab CI
- ArgoCD
- SonarQube
- Nexus
- Vault
- Packer
- Vagrant
- Azure DevOps

### Virtualisation

- Proxmox
- Microsoft Hyper-V/App-V
- KVM/Qemu
- VMware vSphere
- Oracle VirtualBox
- VMware ESXi
- VMware vCenter
- VMware Horizon
- Citrix Hypervisor (XenServer)

### Cloud

- AWS
- GCP
- Azure
- S3NS
- OVH
- CloudFlare
- Nutanix
- OpenStack
- IBM Cloud
- Oracle Cloud Infrastructure
- Scaleway
- Hetzner

### Conteneurisation

- Docker
- Docker Compose
- Docker Swarm
- Podman
- Containerd
- CRI-O
- Buildah
- Kubernetes
- Helm
- OpenShift
- Rancher
- K3s
- LXC/LXD
- Nomad
- Istio

### ERP

- M3
- MS Dynamics
- OAP
- SAP BW
- SAP Hana
- SAP R3 BC
- SAP S/4HANA
- SAP ECC
- Oracle E-Business Suite
- Sage X3
- Odoo
- Microsoft Dynamics 365

### CRM

- Salesforce
- Microsoft Dynamics 365 CRM
- SAP CRM
- Oracle Siebel
- SugarCRM
- Zoho CRM
- HubSpot
- Pipedrive

### GED

- DocuWare
- Maarch
- Nuxeo
- OpenText Documentum
- M-Files
- FileNet
- Laserfiche
- DocuShare

### Messagerie

- Microsoft Exchange
- Lotus Domino
- Lync/Skype
- Messageries Mobiles
- Office 365
- OpenLDAP
- Postfix
- Teams
- Dovecot
- Cisco ESA
- Cisco Secure Email Gateway
- Fortimail
- Puremessage
- Zimbra
- Sendmail
- Exim
- MDaemon
- MailStore
- Sympa
- Google Workspace (Gmail)

### Orchestration

- Control-M
- Dollar Universe
- Opcon
- VTOM
- IBM Workload Scheduler (TWS)
- Automic (UC4)
- Redwood
- Airflow
- Rundeck

### Réseau

- CCNA
- CCNP
- IP Fabric Juniper
- IPv6
- LibreNMS
- Load Balancer F5 (LTM)
- Load Balancing
- NSXT/SDN
- Patch Management Réseau
- Proxy AV McAfee
- Proxy Broadcom (ex BlueCoat)
- Réseaux convergés (SAN, FCoE)
- Routage (OSPF, EIGRP)
- Routage BGP
- Routage statique
- Routeur Cisco
- Routeur Juniper MX
- SD-WAN
- Switch Cisco
- Switch Juniper
- Switch Cisco Nexus
- Switching (VLAN, Spanning Tree, etc.)
- VPN IPsec
- VPN Mistral
- VPN Netscaler
- VPN Pulse Secure
- WAF F5 (module ASM)
- MPLS
- VXLAN
- Cisco DNA Center
- Cisco ISE (NAC)
- Firewall Cisco ASA
- Zscaler
- Cisco Meraki

### Système

- Active Directory
- ADFS
- AFS
- AIX
- AS400
- Bitlocker
- Citrix MetaFrame
- Citrix XenApp
- Citrix XenDesktop
- Cluster Corosync/Pacemaker
- Cluster VCS
- Columbus (impression)
- Datastage
- DFS
- DHCP
- DNS
- ESXi
- Fail2ban
- Grafana
- GLPI
- Graylog
- HP-UX
- Hyper-V
- iSCSI
- Kaspersky
- Kerberos
- Kibana
- KVM
- LDAP
- LDOM (Solaris)
- Linux CentOS
- Linux CentOS Stream
- Linux NixOS
- Linux ZorinOS
- Linux Mint
- Red Hat Linux
- Open SUSE Linux
- SUSE Linux
- Ubuntu Linux
- Debian Linux
- Rocky Linux
- AlmaLinux
- Logstash
- Nagios
- Nexus
- NXLog
- OpenVZ
- Oracle OVM/OLVM
- Patch Management Satellite
- Patch Management WSUS
- Patch Management Omnibus
- PKI
- Prometheus
- RDS
- Shibboleth
- SiteMinder
- SNMP
- SOFS
- Solaris
- Unix
- Vormetric
- vROPS
- Windows NT 4
- Windows Server 2000
- Windows Server 2003
- Windows Server 2008
- Windows Server 2012
- Windows Server 2016
- Windows Server 2019
- Windows Server 2022
- Windows Server 2025
- ZebOS F5
- nftables
- NFS
- Trellix
- Citrix Netscaler
- Lockpass
- FreeRADIUS

### Développement

- Java
- JBoss
- PHP
- Python
- Script Shell
- PowerShell
- Visual Basic
- Django
- JavaScript
- TypeScript
- C#
- C/C++
- Go
- Ruby
- Perl
- .NET
- Node.js
- Angular
- React
- Vue.js
- SQL
- PL/SQL

### Sauvegarde & Restauration

- NetBackup
- Appliance Veritas
- Commvault
- Networker
- Veeam
- TINA
- Dell Avamar
- Dell Data Domain
- TSM (IBM Spectrum Protect)
- Bacula
- Bareos
- Acronis
- Rubrik
- Cohesity

### Stockage

- SAN Hitachi
- SAN Dell
- SAN Pure Storage
- SAN IBM
- SAN/NAS Huawei Dorado
- HCP Hitachi
- Dell VPlex
- Dell VNX
- Dell Unity
- Dell XtremIO
- SAN HP 3PAR
- NAS NetApp MetroCluster
- NAS NetApp 7-mode
- NAS NetApp cDOT
- NetApp ActiveIQ
- NAS Isilon
- Switch SAN Brocade
- Cisco MDS
- SAN Synology
- Dell PowerStore
- Dell PowerMax
- Pure Storage FlashArray
- HPE Alletra
- IBM FlashSystem
- Ceph
- GlusterFS

### Datacenter

- Baies & câblage (cuivre/fibre)
- Brassage fibre optique
- PDU / Alimentation électrique
- Onduleur (UPS)
- Groupe électrogène
- Climatisation / Refroidissement
- Surveillance environnementale
- Contrôle d'accès physique
- Vidéosurveillance
- DCIM
- Norme TIA-942
- Norme Uptime Institute (Tier I-IV)
- PRA / PCA
- Site de secours

### Méthodologie

- ITIL
- Agile
- Scrum
- Kanban
- Lean
- SAFe
- Cycle en V
- PMP
- PRINCE2
- COBIT
- TOGAF
- Six Sigma
- Lean IT

### Cyber Sécurité

- CipherTrust Manager
- HSM
- Wallix
- Midpoint
- Trend Micro
- Gestion consoles AV Trellix (EPO)
- Gestion consoles Kaspersky
- Gestion consoles Sentinel One
- Forescout
- Cyberwatch
- Microsoft Defender
- BitDefender
- Scan vulnérabilité Nessus
- ISO 27005
- EBIOS RM
- ISO 27001
- Ivanti Endpoint Manager
- RKHunter
- Firewall Checkpoint
- Firewall Forcepoint
- Firewall Fortinet
- Firewall Juniper SRX
- Firewall Watchguard
- Firewall Palo Alto
- Firewall StormShield
- Infrastructure WIFI
- Splunk
- IBM QRadar
- Snort
- nTop/nDPI
- ClamAV
- CrowdStrike
- Wazuh
- Sophos
- Qualys
- OpenVAS
- Nmap
- Wireshark
- Metasploit
- Burp Suite
- MISP
- TheHive

### Gestion de projet / programme

- MS Project
- Jira
- Confluence
- Trello
- Monday.com
- Asana
- Planisware
- Sciforma
- Broadcom Clarity
- Gantt
- PMBOK
- PMI

### Langue

- Français
- Anglais
- Allemand
- Espagnol
- Italien
- Portugais
- Néerlandais
- Arabe
- Chinois (Mandarin)
- Russe
