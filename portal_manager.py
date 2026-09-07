import json
import os
import re
import subprocess
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORTAL_DIR = "/home/mbanjec/homelab-portal"
PORTAL_PORT = 8000
CLOUDFLARED_BIN = "/home/mbanjec/.local/bin/cloudflared"

# Complete Services Config (All Webpages & Dashboards)
services_config = [
    {
        "id": "ubuntu-pc-rdp",
        "name": "Ubuntu PC Desktop (Web RDP)",
        "category": "Infrastructure & Access",
        "icon": "fa-desktop",
        "color": "emerald",
        "desc": "Interactive client-less browser RDP desktop session for Ubuntu PC Workstation (192.168.0.104)",
        "local_url": "http://192.168.0.218:8084",
        "target_for_tunnel": "http://localhost:8084",
        "user": "mbanjec / admin",
        "pass": "ig2tq:up8# / admin",
        "auth_type": "HTML5 Web RDP Gateway",
        "public_url": "https://purple-camels-find.loca.lt"
    },
    {
        "id": "unicaf-rdp",
        "name": "UNICAF Windows Server (Web RDP)",
        "category": "Infrastructure & Access",
        "icon": "fa-desktop",
        "color": "indigo",
        "desc": "Interactive client-less browser RDP desktop session for UNICAF Windows Server 2025 (192.168.0.109)",
        "local_url": "http://192.168.0.218:8086",
        "target_for_tunnel": "http://localhost:8086",
        "user": "mbanjec / Administrator",
        "pass": "ig2tq:up8#",
        "auth_type": "HTML5 Web RDP Gateway",
        "public_url": "https://comparison-pearl-typical-limitation.trycloudflare.com"
    },
    {
        "id": "jasmin-portal",
        "name": "JASMIN Cluster Portal",
        "category": "AI & Compute",
        "icon": "fa-server",
        "color": "blue",
        "desc": "Scientific computing cluster portal integrated with SLURM compute nodes",
        "local_url": "http://192.168.0.218:8880",
        "target_for_tunnel": "http://localhost:8880",
        "user": "mbanjec",
        "pass": "ig2tq:up8#",
        "auth_type": "Direct Web Access",
        "public_url": "https://ensures-amount-new-shall.trycloudflare.com"
    },
    {
        "id": "jasmin-notebooks",
        "name": "JASMIN JupyterLab Notebooks",
        "category": "AI & Compute",
        "icon": "fa-book-open",
        "color": "orange",
        "desc": "Interactive Python & Data Science environment with cluster volume mounts",
        "local_url": "http://192.168.0.218:8888",
        "target_for_tunnel": "http://localhost:8888",
        "user": "jovyan / mbanjec",
        "pass": "No Token Required",
        "auth_type": "Tokenless Workspace",
        "public_url": "https://fotos-consisting-enormous-hong.trycloudflare.com"
    },
    {
        "id": "jasmin-xfer",
        "name": "JASMIN Data Transfer (Dufs)",
        "category": "AI & Compute",
        "icon": "fa-folder-open",
        "color": "blue",
        "desc": "High-throughput web file manager and data exchange server for GWS & work volumes",
        "local_url": "http://192.168.0.218:8882",
        "target_for_tunnel": "http://localhost:8882",
        "user": "Anonymous",
        "pass": "None (Full CRUD Access)",
        "auth_type": "Anonymous Access",
        "public_url": "https://poll-scanning-lots-radiation.trycloudflare.com"
    },
    {
        "id": "jasmin-api",
        "name": "JASMIN Cluster REST API",
        "category": "AI & Compute",
        "icon": "fa-code",
        "color": "blue",
        "desc": "FastAPI backend managing Slurm batch submissions, node status, and telemetry",
        "local_url": "http://192.168.0.218:8881/docs",
        "target_for_tunnel": "http://localhost:8881",
        "user": "API Client",
        "pass": "None",
        "auth_type": "Swagger / OpenAPI Docs"
    },
    {
        "id": "grafana",
        "name": "Grafana Monitoring Dashboard",
        "category": "Monitoring & Security",
        "icon": "fa-chart-line",
        "color": "amber",
        "desc": "Real-time metrics visualization for ESXi hypervisor, Linux nodes, and power consumption",
        "local_url": "http://192.168.0.218:3002",
        "target_for_tunnel": "http://localhost:3002",
        "user": "admin",
        "pass": "admin",
        "auth_type": "Basic / Session Auth",
        "public_url": "https://distributor-tramadol-modules-dreams.trycloudflare.com"
    },
    {
        "id": "prometheus",
        "name": "Prometheus Metrics TSDB",
        "category": "Monitoring & Security",
        "icon": "fa-database",
        "color": "red",
        "desc": "Time-series database collecting metrics from cAdvisor, Node Exporter, and ESXi",
        "local_url": "http://192.168.0.218:9090",
        "target_for_tunnel": "http://localhost:9090",
        "user": "None",
        "pass": "None",
        "auth_type": "Direct Web UI"
    },
    {
        "id": "cadvisor",
        "name": "cAdvisor Container Analyzer",
        "category": "Monitoring & Security",
        "icon": "fa-cubes",
        "color": "cyan",
        "desc": "Container resource usage, memory profiling, and hardware telemetry dashboard",
        "local_url": "http://192.168.0.218:8085",
        "target_for_tunnel": "http://localhost:8085",
        "user": "None",
        "pass": "None",
        "auth_type": "Direct Web UI"
    },
    {
        "id": "wazuh",
        "name": "Wazuh Security Platform & SIEM",
        "category": "Monitoring & Security",
        "icon": "fa-shield-halved",
        "color": "teal",
        "desc": "Enterprise security monitoring, threat detection, file integrity, and compliance analytics",
        "local_url": "https://192.168.0.218:8443",
        "target_for_tunnel": "https://localhost:8443",
        "user": "admin",
        "pass": "admin",
        "auth_type": "HTTPS Form Login"
    },
    {
        "id": "news-dashboard",
        "name": "News & Trends Dashboard",
        "category": "Dashboards & Media",
        "icon": "fa-newspaper",
        "color": "purple",
        "desc": "Aggregated global, tech, financial, and AI news feeds with auto-refresh",
        "local_url": "http://192.168.0.218:8090",
        "target_for_tunnel": "http://localhost:8090",
        "user": "Public",
        "pass": "None",
        "auth_type": "No Authentication",
        "public_url": "https://bind-advancement-requested-needle.trycloudflare.com"
    },
    {
        "id": "tiktok-browser",
        "name": "TikTok Chromium Web Session",
        "category": "Dashboards & Media",
        "icon": "fa-brands fa-tiktok",
        "color": "pink",
        "desc": "Isolated remote desktop browser environment for TikTok and media sessions",
        "local_url": "http://192.168.0.218:3000",
        "target_for_tunnel": "http://localhost:3000",
        "user": "None",
        "pass": "None",
        "auth_type": "Web Kasm/VNC"
    },
    {
        "id": "booklore",
        "name": "BookLore Digital Library (Dedicated Server)",
        "category": "Dashboards & Media",
        "icon": "fa-book-bookmark",
        "color": "rose",
        "desc": "Digital library, PDF/ePub reader, and collection management system on booklore-server (192.168.0.99)",
        "local_url": "http://192.168.0.99:6060",
        "target_for_tunnel": "http://192.168.0.99:6060",
        "user": "ubadmin_6835",
        "pass": "NyYPcgvAJnB8#cqN",
        "auth_type": "Form Authentication",
        "public_url": "https://booklore.npcsolutions.co.uk"
    },
    {
        "id": "agro-farm-project",
        "name": "50m × 50m Agro-Enterprise Project",
        "category": "Dashboards & Media",
        "icon": "fa-seedling",
        "color": "emerald",
        "desc": "Commercial livestock masterplan for 300 rabbits/wk, 300 chickens/wk, 30m solar well, 10kWp solar & cold room",
        "local_url": "http://192.168.0.218:8087",
        "target_for_tunnel": "http://localhost:8087",
        "user": "Public",
        "pass": "None",
        "auth_type": "No Authentication",
        "public_url": "https://arranged-infinite-sufficiently-lucky.trycloudflare.com"
    },
    {
        "id": "fast-cash-uk", "business-central",
        "name": "Fast Cash UK Web Application",
        "category": "Dashboards & Media",
        "icon": "fa-sterling-sign",
        "color": "green",
        "desc": "Fast Cash UK production loan and financial services web portal",
        "local_url": "http://192.168.0.218:8098",
        "target_for_tunnel": "http://localhost:8098",
        "user": "Public",
        "pass": "None",
        "auth_type": "Web Portal Access"
    },
    {
        "id": "wg-easy",
        "name": "WireGuard Easy VPN Admin",
        "category": "Infrastructure & Access",
        "icon": "fa-network-wired",
        "color": "red",
        "desc": "Fast, modern VPN server management with QR-code client configuration",
        "local_url": "http://192.168.0.218:51821",
        "target_for_tunnel": "http://localhost:51821",
        "user": "admin",
        "pass": "ig2tq:up8#",
        "auth_type": "Web Admin Password"
    },
    {
        "id": "esxi",
        "name": "VMware ESXi Host Client",
        "category": "Infrastructure & Access",
        "icon": "fa-microchip",
        "color": "slate",
        "desc": "Hypervisor management console for virtual machine allocation and datastore controls (ESXi 8.0.3)",
        "local_url": "https://192.168.0.200",
        "target_for_tunnel": "https://192.168.0.200",
        "user": "root",
        "pass": "Munashe1234# / ig2tq:up8#",
        "auth_type": "Hypervisor Root Login"
    },
    {
        "id": "vcenter",
        "name": "VMware vSphere Client (vCenter 8)",
        "category": "Infrastructure & Access",
        "icon": "fa-cloud",
        "color": "sky",
        "desc": "Centralized virtual infrastructure management and enterprise cluster orchestration",
        "local_url": "https://192.168.0.146",
        "target_for_tunnel": "https://192.168.0.146",
        "user": "administrator@vsphere.local",
        "pass": "Munashe1234@ / ig2tq:up8#",
        "auth_type": "SSO Domain Login"
    },
    {
        "id": "business-central",
        "name": "Dynamics 365 Business Central",
        "category": "Infrastructure & Access",
        "icon": "fa-building",
        "color": "blue",
        "desc": "Enterprise ERP Web Client hosted on Windows Server 2025 (BC-server)",
        "local_url": "http://192.168.0.218:8096",
        "target_for_tunnel": "http://localhost:8096",
        "user": "npcsolutions\\administrator",
        "pass": "ig2tq:up8#",
        "auth_type": "Active Directory NTLM"
    },
    {
        "id": "truenas",
        "name": "TrueNAS Storage System",
        "category": "Infrastructure & Access",
        "icon": "fa-hard-drive",
        "color": "cyan",
        "desc": "Enterprise ZFS storage array managing SMB shares, NFS exports, and data pools",
        "local_url": "http://192.168.0.47",
        "target_for_tunnel": "http://192.168.0.47",
        "user": "admin / mbanjec",
        "pass": "Munashe1234@ / ig2tq:up8#",
        "auth_type": "Web GUI Login"
    },
    {
        "id": "cockpit-login",
        "name": "Cockpit Server Console (Login-01)",
        "category": "Infrastructure & Access",
        "icon": "fa-terminal",
        "color": "zinc",
        "desc": "Web-based interactive administration and performance cockpit for Rocky Linux nodes",
        "local_url": "https://192.168.0.131:9090",
        "target_for_tunnel": "https://192.168.0.131:9090",
        "user": "root / mbanjec",
        "pass": "ig2tq:up8#",
        "auth_type": "Linux PAM Auth"
    },
    {
        "id": "webmin-login01",
        "name": "Webmin Console (Login-01)",
        "category": "Infrastructure & Access",
        "icon": "fa-sliders",
        "color": "zinc",
        "desc": "Webmin full-featured Linux system administration console on Slurm Login-01",
        "local_url": "https://192.168.0.131:10000",
        "target_for_tunnel": "https://192.168.0.131:10000",
        "user": "root / mbanjec",
        "pass": "ig2tq:up8#",
        "auth_type": "Linux PAM Auth"
    },
    {
        "id": "webmin-node01",
        "name": "Webmin Console (Node-01)",
        "category": "Infrastructure & Access",
        "icon": "fa-sliders",
        "color": "zinc",
        "desc": "Webmin administration console for Slurm Compute Node-01 (8 CPUs / 15GB RAM)",
        "local_url": "https://192.168.0.170:10000",
        "target_for_tunnel": "https://192.168.0.170:10000",
        "user": "root / mbanjec",
        "pass": "ig2tq:up8#",
        "auth_type": "Linux PAM Auth"
    },
    {
        "id": "webmin-node03",
        "name": "Webmin Console (Node-03)",
        "category": "Infrastructure & Access",
        "icon": "fa-sliders",
        "color": "zinc",
        "desc": "Webmin administration console for Slurm Compute Node-03 (8 CPUs / 15GB RAM)",
        "local_url": "https://192.168.0.124:10000",
        "target_for_tunnel": "https://192.168.0.124:10000",
        "user": "root / mbanjec",
        "pass": "ig2tq:up8#",
        "auth_type": "Linux PAM Auth"
    },
    {
        "id": "sky-router",
        "name": "Sky Broadband Router Gateway",
        "category": "Infrastructure & Access",
        "icon": "fa-wifi",
        "color": "sky",
        "desc": "Primary LAN network gateway, DHCP server, and ISP broadband router",
        "local_url": "http://192.168.0.1",
        "target_for_tunnel": "http://192.168.0.1",
        "user": "admin",
        "pass": "sky",
        "auth_type": "HTTP Basic Auth"
    }
]

# Item 1: Infrastructure Nodes & Topology Data
nodes_data = [
    {
        "name": "ESXi Docker Server",
        "hostname": "docker-74",
        "ip": "192.168.0.218",
        "os": "Ubuntu Linux 24.04 (VM)",
        "role": "Docker Container Hub, Telemetry Exporters & Microservices Host",
        "status": "Online",
        "details": "24 Docker Containers, 22 Images, Prometheus, Wazuh, JASMIN",
        "badge": "Docker Engine"
    },
    {
        "name": "BookLore Dedicated Server",
        "hostname": "booklore-server",
        "ip": "192.168.0.99",
        "os": "Ubuntu Linux 24.04 (VM)",
        "role": "BookLore 3.0 Digital Library & Reader Server",
        "status": "Online",
        "details": "BookLore 3.0 Web App, Port 6060",
        "badge": "Digital Library"
    },
    {
        "name": "Ubuntu PC Workstation",
        "hostname": "mbanjec-OptiPlex-3020M",
        "ip": "192.168.0.104",
        "os": "Ubuntu Linux 26.04 Desktop (Bare-Metal)",
        "role": "Primary Physical Client Workstation / Desktop PC",
        "status": "Online",
        "details": "Dell OptiPlex 3020M, OpenSSH (22), XRDP (3389), Chrome, Remmina",
        "badge": "Workstation"
    },
    {
        "name": "VMware ESXi Bare-Metal Host",
        "hostname": "esxi-01.npcsolutions.co.za",
        "ip": "192.168.0.200",
        "os": "VMware ESXi 8.0.3 (Build 24677879)",
        "role": "Primary Enterprise Type-1 Hypervisor Hosting 15 VMs",
        "status": "Online",
        "details": "Host Client UI (443), SSH (22), Datastore VMFS Pools",
        "badge": "Hypervisor"
    },
    {
        "name": "VMware vCenter Server 8",
        "hostname": "vCenter 8 Appliance",
        "ip": "192.168.0.146",
        "os": "VMware Photon OS (VCSA 8)",
        "role": "Centralized Virtual Datacenter Orchestration & Cluster Management",
        "status": "Online",
        "details": "vSphere Client HTML5 (443), SSO administrator@vsphere.local",
        "badge": "VCSA 8"
    },
    {
        "name": "Dynamics 365 BC Server",
        "hostname": "BC-server",
        "ip": "192.168.0.39",
        "os": "Windows Server 2025 (VM)",
        "role": "Microsoft Dynamics 365 Business Central ERP Web Client",
        "status": "Online",
        "details": "IIS Web Server (80, 8080), Active Directory Domain Member",
        "badge": "Windows Server"
    },
    {
        "name": "UNICAF Academic Server",
        "hostname": "00_UNICAF-2025-2026",
        "ip": "192.168.0.109",
        "os": "Windows Server 2025 (VM)",
        "role": "Remote Academic Desktop & Computing Workspace",
        "status": "Online",
        "details": "RDP (3389), Accessible via Guacamole HTML5 Gateway (8086)",
        "badge": "Windows Server"
    },
    {
        "name": "Slurm Controller / Login-01",
        "hostname": "login-01",
        "ip": "192.168.0.131",
        "os": "Rocky Linux 9 (VM)",
        "role": "Slurm Supercluster Head Node (slurmctld, slurmdbd, NFS)",
        "status": "Online",
        "details": "Cockpit (9090), Webmin (10000), Slurm Controller (6817/6819)",
        "badge": "HPC Controller"
    },
    {
        "name": "Slurm Compute Node-01",
        "hostname": "node-01",
        "ip": "192.168.0.170",
        "os": "Rocky Linux 9 (VM)",
        "role": "HPC Compute Worker: Standard & High-Memory Partition",
        "status": "Online",
        "details": "8 CPUs, 15GB RAM, Webmin (10000), slurmd (6818)",
        "badge": "HPC Worker"
    },
    {
        "name": "Slurm Compute Node-02",
        "hostname": "node-02",
        "ip": "192.168.0.53",
        "os": "Rocky Linux 9 (VM)",
        "role": "HPC Compute Worker: Standard & Debug Partition",
        "status": "Online",
        "details": "4 CPUs, 7GB RAM, slurmd (6818)",
        "badge": "HPC Worker"
    },
    {
        "name": "Slurm Compute Node-03",
        "hostname": "node-03",
        "ip": "192.168.0.124",
        "os": "Rocky Linux 9 (VM)",
        "role": "HPC Compute Worker: Standard, High-Mem & Serial Partition",
        "status": "Online",
        "details": "8 CPUs, 15GB RAM, Webmin (10000), slurmd (6818)",
        "badge": "HPC Worker"
    },
    {
        "name": "Slurm Compute Node-04",
        "hostname": "node-04",
        "ip": "192.168.0.227",
        "os": "Rocky Linux 9 (VM)",
        "role": "HPC Compute Worker: Standard, Debug & Serial Partition",
        "status": "Online",
        "details": "2 CPUs, 7GB RAM, slurmd (6818)",
        "badge": "HPC Worker"
    },
    {
        "name": "TrueNAS Storage System",
        "hostname": "truenas",
        "ip": "192.168.0.47",
        "os": "TrueNAS CORE / SCALE (VM)",
        "role": "Enterprise ZFS Storage Pool, SMB Shares & NFS Exports",
        "status": "Online",
        "details": "ZFS Datastores, Shared Volumes, SSH (22)",
        "badge": "ZFS Storage"
    },
    {
        "name": "Sky Router Gateway",
        "hostname": "skysr213.Home",
        "ip": "192.168.0.1",
        "os": "Sky Broadband Gateway",
        "role": "Network Router, DHCP Server, DNS & WAN Uplink",
        "status": "Online",
        "details": "HTTP (80), HTTPS (443), Gigabit LAN Switching",
        "badge": "Network Gateway"
    }
]

# Item 3: Complete Docker Images & Containers Registry Data
docker_registry_data = [
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "grafana/grafana",
        "tag": "latest",
        "image_id": "3fd54ae12146",
        "disk_size": "474 MB",
        "containers": "grafana",
        "ports": "3002->3000/tcp",
        "status": "Up 2 days",
        "category": "Monitoring"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "prom/prometheus",
        "tag": "latest",
        "image_id": "5ce7540c3c00",
        "disk_size": "109 MB",
        "containers": "prometheus",
        "ports": "9090->9090/tcp",
        "status": "Up 42 hours",
        "category": "Monitoring"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "prom/node-exporter",
        "tag": "latest",
        "image_id": "1b4e4438faca",
        "disk_size": "13.4 MB",
        "containers": "node-exporter",
        "ports": "9100->9100/tcp",
        "status": "Up 2 days",
        "category": "Monitoring"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "gcr.io/cadvisor/cadvisor",
        "tag": "latest",
        "image_id": "3de2bd520312",
        "disk_size": "30.8 MB",
        "containers": "cadvisor",
        "ports": "8085->8080/tcp",
        "status": "Up 2 days (healthy)",
        "category": "Monitoring"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "telegraf",
        "tag": "latest",
        "image_id": "ac66e6482c06",
        "disk_size": "184 MB",
        "containers": "telegraf",
        "ports": "9273->9273/tcp",
        "status": "Up 2 days",
        "category": "Monitoring"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "esxi-exporter",
        "tag": "latest",
        "image_id": "5e3798c09279",
        "disk_size": "48 MB",
        "containers": "esxi-exporter",
        "ports": "9272->9272/tcp",
        "status": "Up 2 days",
        "category": "Monitoring"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "network-power-exporter",
        "tag": "latest",
        "image_id": "4977a6b8c086",
        "disk_size": "137 MB",
        "containers": "network-power-exporter",
        "ports": "Host Net (9275)",
        "status": "Up 42 hours (healthy)",
        "category": "Monitoring"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "wazuh/wazuh-dashboard",
        "tag": "4.9.2",
        "image_id": "7622129f46c4",
        "disk_size": "364 MB",
        "containers": "single-node-wazuh.dashboard",
        "ports": "8443->5601/tcp",
        "status": "Up 2 days",
        "category": "Security"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "wazuh/wazuh-manager",
        "tag": "4.9.2",
        "image_id": "b906ebfc77d7",
        "disk_size": "614 MB",
        "containers": "single-node-wazuh.manager",
        "ports": "1514-1515, 55000/tcp, 514/udp",
        "status": "Up 2 days (healthy)",
        "category": "Security"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "wazuh/wazuh-indexer",
        "tag": "4.9.2",
        "image_id": "654bd546b926",
        "disk_size": "1.82 GB",
        "containers": "single-node-wazuh.indexer",
        "ports": "9200->9200/tcp",
        "status": "Up 2 days (healthy)",
        "category": "Security"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "lscr.io/linuxserver/chromium",
        "tag": "latest",
        "image_id": "4c7b9086d2e5",
        "disk_size": "1.2 GB",
        "containers": "tiktok-browser",
        "ports": "3000-3001->3000-3001/tcp",
        "status": "Up 2 days",
        "category": "Desktop / Media"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "ghcr.io/wg-easy/wg-easy",
        "tag": "latest",
        "image_id": "5f26407fd2ed",
        "disk_size": "61.1 MB",
        "containers": "wg-easy",
        "ports": "51821->51821/tcp, 51820/udp",
        "status": "Up 2 days (healthy)",
        "category": "Networking"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "favonia/cloudflare-ddns",
        "tag": "latest",
        "image_id": "61013368c8f9",
        "disk_size": "5.64 MB",
        "containers": "cloudflare-ddns",
        "ports": "Internal Daemon",
        "status": "Up 2 days",
        "category": "Networking"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "oznu/guacamole",
        "tag": "latest",
        "image_id": "6268b3a08d9b",
        "disk_size": "557 MB",
        "containers": "unicaf-rdp-web, ubuntu-rdp-web",
        "ports": "8086->8080/tcp, 8084->8080/tcp",
        "status": "Up Active",
        "category": "Remote Access"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "fast-cash-uk-app-fast-cash-uk",
        "tag": "latest",
        "image_id": "7711f5b4375b",
        "disk_size": "51.5 MB",
        "containers": "fast-cash-uk-app",
        "ports": "8098->8098/tcp",
        "status": "Up 25 hours",
        "category": "Web Applications"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "news-dashboard",
        "tag": "latest",
        "image_id": "77f6f9ea8b46",
        "disk_size": "64 MB",
        "containers": "news-dashboard",
        "ports": "8090->8090/tcp",
        "status": "Up 47 hours (healthy)",
        "category": "Web Applications"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "jasmin-cluster-jasmin-portal",
        "tag": "latest",
        "image_id": "3ae9fdf7149e",
        "disk_size": "26.3 MB",
        "containers": "jasmin-portal",
        "ports": "8880->8880/tcp",
        "status": "Up 2 days",
        "category": "AI / Cluster"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "jasmin-cluster-jasmin-cluster-api",
        "tag": "latest",
        "image_id": "4b5279136b16",
        "disk_size": "245 MB",
        "containers": "jasmin-cluster-api",
        "ports": "8881->8881/tcp",
        "status": "Up 2 days",
        "category": "AI / Cluster"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "jasmin-cluster-jasmin-notebooks",
        "tag": "latest",
        "image_id": "53ad027e6e50",
        "disk_size": "420 MB",
        "containers": "jasmin-notebooks",
        "ports": "8888->8888/tcp",
        "status": "Up 2 days",
        "category": "AI / Cluster"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "sigoden/dufs",
        "tag": "latest",
        "image_id": "8dd3b7500157",
        "disk_size": "2.98 MB",
        "containers": "jasmin-xfer",
        "ports": "8882->5000/tcp",
        "status": "Up 2 days",
        "category": "Data Transfer"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "nginx",
        "tag": "alpine",
        "image_id": "db35bfc6b295",
        "disk_size": "27.2 MB",
        "containers": "bc-nginx-proxy",
        "ports": "8097->8097/tcp",
        "status": "Up 2 hours",
        "category": "Networking / Proxy"
    },
    {
        "host": "ESXi Docker Server (192.168.0.218)",
        "repository": "node",
        "tag": "alpine",
        "image_id": "2d984a15c9b5",
        "disk_size": "63.9 MB",
        "containers": "fastcash-localtunnel, bc-localtunnel",
        "ports": "Tunnel Agents",
        "status": "Up 2 hours",
        "category": "Tunnels / Proxy"
    },
    {
        "host": "BookLore Server (192.168.0.99)",
        "repository": "ghcr.io/booklore-app/booklore",
        "tag": "latest",
        "image_id": "d3d3af34bc2c",
        "disk_size": "173 MB",
        "containers": "booklore",
        "ports": "6060->6060/tcp",
        "status": "Up 3 days",
        "category": "Digital Library"
    },
    {
        "host": "BookLore Server (192.168.0.99)",
        "repository": "lscr.io/linuxserver/mariadb",
        "tag": "11.4.5",
        "image_id": "eef506eab5c5",
        "disk_size": "107 MB",
        "containers": "mariadb",
        "ports": "3306/tcp",
        "status": "Up 3 days (healthy)",
        "category": "Database"
    }
]

def generate_enhanced_html(services_data, nodes_list, docker_list, portal_public_url):
    categories = sorted(list(set(s["category"] for s in services_data)))
    
    html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise Homelab & Services Portal</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }},
                    colors: {{
                        brand: {{
                            50: '#eff6ff',
                            100: '#dbeafe',
                            500: '#3b82f6',
                            600: '#2563eb',
                            700: '#1d4ed8',
                            900: '#1e3a8a',
                        }},
                        darkcard: '#161e2e',
                        darkbg: '#0b0f19'
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            background-color: #0b0f19;
            background-image: 
                radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.12) 0px, transparent 50%),
                radial-gradient(at 50% 100%, rgba(16, 185, 129, 0.08) 0px, transparent 50%);
            background-attachment: fixed;
        }}
        .glass-card {{
            background: rgba(22, 30, 46, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .glass-card:hover {{
            transform: translateY(-3px);
            border-color: rgba(59, 130, 246, 0.4);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(59, 130, 246, 0.2);
        }}
        .tab-btn.active {{
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            color: #ffffff;
            box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.35);
            border-color: transparent;
        }}
        .custom-scrollbar::-webkit-scrollbar {{
            height: 6px;
            width: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: rgba(15, 23, 42, 0.6);
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: rgba(51, 65, 85, 0.8);
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: rgba(100, 116, 139, 1);
        }}
    </style>
</head>
<body class="text-slate-100 min-h-screen flex flex-col font-sans selection:bg-blue-500 selection:text-white">

    <!-- Top Sticky Header -->
    <header class="sticky top-0 z-50 backdrop-blur-md bg-slate-950/80 border-b border-slate-800/80">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 via-indigo-500 to-purple-500 flex items-center justify-center shadow-lg shadow-blue-500/25">
                    <i class="fa-solid fa-server text-white text-lg"></i>
                </div>
                <div>
                    <h1 class="font-bold text-base tracking-tight bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent">
                        Enterprise Homelab & Services Portal
                    </h1>
                    <p class="text-xs text-slate-400 font-mono">ESXi 8.0.3 &bull; Docker Hub &bull; Slurm HPC &bull; Ubuntu PC</p>
                </div>
            </div>

            <!-- Stats & Portal Public Link -->
            <div class="flex items-center gap-2 sm:gap-3">
                <div class="hidden md:flex items-center gap-2 bg-slate-900/80 border border-slate-800 px-3 py-1.5 rounded-lg text-xs">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                    <span class="text-slate-400">Total Services:</span>
                    <span class="font-bold text-blue-400">{len(services_data)}</span>
                </div>
                <div class="hidden lg:flex items-center gap-2 bg-slate-900/80 border border-slate-800 px-3 py-1.5 rounded-lg text-xs">
                    <span class="text-slate-400">Nodes:</span>
                    <span class="font-bold text-indigo-400">{len(nodes_list)}</span>
                </div>
                <div class="hidden lg:flex items-center gap-2 bg-slate-900/80 border border-slate-800 px-3 py-1.5 rounded-lg text-xs">
                    <span class="text-slate-400">Docker Images:</span>
                    <span class="font-bold text-emerald-400">{len(docker_list)}</span>
                </div>
                {f'''<a href="{portal_public_url}" target="_blank" class="flex items-center gap-2 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white text-xs font-semibold px-3.5 py-1.5 rounded-lg shadow-md shadow-blue-600/30 transition">
                    <i class="fa-solid fa-globe text-xs"></i>
                    <span>Public Tunnel</span>
                </a>''' if portal_public_url else ''}
            </div>
        </div>
    </header>

    <!-- Main Navigation Bar / Switcher -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 w-full">
        <div class="bg-slate-900/90 border border-slate-800/90 rounded-2xl p-2 flex flex-wrap gap-2 items-center justify-between shadow-xl">
            <div class="flex flex-wrap gap-2" id="mainTabNav">
                <button onclick="switchView('services')" id="tabBtn-services" class="tab-btn active px-4 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition">
                    <i class="fa-solid fa-layer-group"></i>
                    <span>Services & Dashboards ({len(services_data)})</span>
                </button>
                <button onclick="switchView('nodes')" id="tabBtn-nodes" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-300 hover:bg-slate-800/80 border border-transparent transition flex items-center gap-2">
                    <i class="fa-solid fa-network-wired text-blue-400"></i>
                    <span>Item 1: Nodes & Topology ({len(nodes_list)})</span>
                </button>
                <button onclick="switchView('webpages')" id="tabBtn-webpages" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-300 hover:bg-slate-800/80 border border-transparent transition flex items-center gap-2">
                    <i class="fa-solid fa-table-list text-purple-400"></i>
                    <span>Item 2: Web Directory ({len(services_data)})</span>
                </button>
                <button onclick="switchView('docker')" id="tabBtn-docker" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-300 hover:bg-slate-800/80 border border-transparent transition flex items-center gap-2">
                    <i class="fa-brands fa-docker text-emerald-400 text-sm"></i>
                    <span>Item 3: Docker Registry ({len(docker_list)})</span>
                </button>
            </div>
            
            <!-- Quick Global Search -->
            <div class="relative w-full sm:w-72 mt-2 sm:mt-0">
                <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                <input type="text" id="globalSearchInput" placeholder="Filter services, nodes, images, IPs..." 
                       class="w-full pl-9 pr-4 py-1.5 bg-slate-950/80 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition">
            </div>
        </div>
    </div>

    <!-- Main Content Body -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 flex-1 w-full">

        <!-- ==================== VIEW 1: SERVICES CARDS ==================== -->
        <section id="view-services" class="space-y-6">
            <!-- Category Filter Pills -->
            <div class="flex items-center gap-1.5 overflow-x-auto pb-1 max-w-full custom-scrollbar" id="categoryFilters">
                <button onclick="filterCategory('All')" class="cat-btn active px-3 py-1.5 rounded-lg text-xs font-medium bg-blue-600 text-white transition">All ({len(services_data)})</button>
                {' '.join([f'''<button onclick="filterCategory('{cat}')" class="cat-btn px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 transition">{cat}</button>''' for cat in categories])}
            </div>

            <!-- Grid of Services -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="servicesGrid">
    """
    
    for s in services_data:
        pub_link = s.get("public_url")
        loc_link = s["local_url"]
        
        html += f"""
                <div class="glass-card rounded-2xl p-5 flex flex-col justify-between service-card" data-category="{s['category']}" data-search="{s['name'].lower()} {s['desc'].lower()} {s['category'].lower()} {loc_link.lower()} {str(pub_link).lower()}">
                    <div>
                        <div class="flex items-start justify-between gap-3 mb-3">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 rounded-xl bg-slate-800/90 flex items-center justify-center text-blue-400 text-lg border border-slate-700/50">
                                    <i class="fa-solid {s['icon']}"></i>
                                </div>
                                <div>
                                    <h3 class="font-bold text-white text-sm leading-snug">{s['name']}</h3>
                                    <span class="text-[10px] px-2 py-0.5 rounded-md bg-slate-800 text-slate-400 border border-slate-700/60 font-medium">{s['category']}</span>
                                </div>
                            </div>
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 shadow-md shadow-emerald-400/50 mt-1.5 shrink-0" title="Active"></span>
                        </div>

                        <p class="text-xs text-slate-400 mb-4 line-clamp-2 leading-relaxed">{s['desc']}</p>

                        <!-- Credentials Box -->
                        <div class="bg-slate-950/60 border border-slate-800/80 rounded-xl p-3 mb-4 space-y-1.5 text-xs">
                            <div class="flex items-center justify-between text-slate-400 border-b border-slate-800/50 pb-1">
                                <span class="font-medium text-[10px] text-slate-500 uppercase tracking-wider">Authentication</span>
                                <span class="text-[10px] text-blue-400 font-medium font-mono">{s['auth_type']}</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span class="text-slate-400 text-[11px]">Username:</span>
                                <div class="flex items-center gap-1.5">
                                    <code class="font-mono text-slate-200 bg-slate-900 px-1.5 py-0.5 rounded text-[11px]">{s['user']}</code>
                                    <button onclick="navigator.clipboard.writeText('{s['user']}'); showToast('Copied username!')" class="text-slate-500 hover:text-slate-200 p-1 transition" title="Copy username">
                                        <i class="fa-regular fa-copy text-xs"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="flex items-center justify-between">
                                <span class="text-slate-400 text-[11px]">Password:</span>
                                <div class="flex items-center gap-1.5">
                                    <code class="font-mono text-slate-200 bg-slate-900 px-1.5 py-0.5 rounded text-[11px]">{s['pass']}</code>
                                    <button onclick="navigator.clipboard.writeText('{s['pass']}'); showToast('Copied password!')" class="text-slate-500 hover:text-slate-200 p-1 transition" title="Copy password">
                                        <i class="fa-regular fa-copy text-xs"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Card Bottom Actions -->
                    <div class="space-y-2 pt-2 border-t border-slate-800/60">
                        {f'''<a href="{pub_link}" target="_blank" class="w-full flex items-center justify-between px-3 py-2 rounded-xl bg-gradient-to-r from-blue-600/90 to-indigo-600/90 hover:from-blue-600 hover:to-indigo-600 text-white text-xs font-semibold shadow-md shadow-blue-500/10 transition group">
                            <span class="flex items-center gap-2 truncate">
                                <i class="fa-solid fa-globe text-blue-200"></i>
                                <span class="truncate">{pub_link}</span>
                            </span>
                            <i class="fa-solid fa-arrow-up-right-from-square text-[10px] text-blue-200 group-hover:translate-x-0.5 transition"></i>
                        </a>''' if pub_link else f'''<div class="w-full flex items-center justify-between px-3 py-2 rounded-xl bg-slate-900/60 border border-slate-800 text-slate-500 text-xs">
                            <span class="flex items-center gap-2 truncate">
                                <i class="fa-solid fa-shield-halved"></i>
                                <span class="truncate">Private / Local LAN Only</span>
                            </span>
                            <span class="text-[10px] uppercase font-mono">LAN</span>
                        </div>'''}

                        <a href="{loc_link}" target="_blank" class="w-full flex items-center justify-between px-3 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white text-xs font-medium transition group">
                            <span class="flex items-center gap-2 truncate font-mono text-[11px]">
                                <i class="fa-solid fa-network-wired text-slate-400"></i>
                                <span class="truncate">{loc_link}</span>
                            </span>
                            <i class="fa-solid fa-arrow-right text-[10px] text-slate-500 group-hover:translate-x-0.5 transition"></i>
                        </a>
                    </div>
                </div>
        """

    html += """
            </div>
        </section>

        <!-- ==================== VIEW 2: ITEM 1 - NODES & TOPOLOGY ==================== -->
        <section id="view-nodes" class="hidden space-y-6">
            <div class="glass-card rounded-2xl p-6">
                <div class="flex items-center justify-between mb-6 pb-4 border-b border-slate-800">
                    <div>
                        <h2 class="text-lg font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-network-wired text-blue-400"></i>
                            <span>Item 1: Summary by Node & Machine Infrastructure</span>
                        </h2>
                        <p class="text-xs text-slate-400">Complete physical and virtual infrastructure inventory across VMware ESXi 8, Docker, Slurm HPC, and Ubuntu PC.</p>
                    </div>
                    <span class="px-3 py-1 bg-blue-900/40 border border-blue-700/50 rounded-lg text-xs font-mono text-blue-300 font-semibold">14 Active LAN Hosts</span>
                </div>

                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="border-b border-slate-800 text-slate-400 uppercase font-mono text-[11px] bg-slate-900/50">
                                <th class="py-3 px-4">Node Name</th>
                                <th class="py-3 px-4">Hostname</th>
                                <th class="py-3 px-4">IP Address</th>
                                <th class="py-3 px-4">Operating System / Platform</th>
                                <th class="py-3 px-4">Role & Infrastructure Function</th>
                                <th class="py-3 px-4">Services / Ports</th>
                                <th class="py-3 px-4 text-center">Status</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60" id="nodesTableBody">
    """
    
    for n in nodes_list:
        html += f"""
                            <tr class="hover:bg-slate-800/40 transition node-row" data-search="{n['name'].lower()} {n['hostname'].lower()} {n['ip'].lower()} {n['os'].lower()} {n['role'].lower()} {n['details'].lower()}">
                                <td class="py-3 px-4 font-semibold text-white">
                                    <div class="flex items-center gap-2">
                                        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                                        <span>{n['name']}</span>
                                    </div>
                                </td>
                                <td class="py-3 px-4 font-mono text-slate-300">{n['hostname']}</td>
                                <td class="py-3 px-4 font-mono text-blue-400 font-bold">{n['ip']}</td>
                                <td class="py-3 px-4 text-slate-300">{n['os']}</td>
                                <td class="py-3 px-4 text-slate-400">{n['role']}</td>
                                <td class="py-3 px-4 text-slate-400 font-mono text-[11px]">{n['details']}</td>
                                <td class="py-3 px-4 text-center">
                                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-900/50 border border-emerald-700/60 text-emerald-300">{n['status']}</span>
                                </td>
                            </tr>
        """

    html += """
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- ==================== VIEW 3: ITEM 2 - ALL WEBPAGES & DIRECTORY ==================== -->
        <section id="view-webpages" class="hidden space-y-6">
            <div class="glass-card rounded-2xl p-6">
                <div class="flex items-center justify-between mb-6 pb-4 border-b border-slate-800">
                    <div>
                        <h2 class="text-lg font-bold text-white flex items-center gap-2">
                            <i class="fa-solid fa-table-list text-purple-400"></i>
                            <span>Item 2: Master Webpages & Dashboards Directory</span>
                        </h2>
                        <p class="text-xs text-slate-400">Full catalog of every web GUI, API, monitoring dashboard, and remote desktop interface across your homelab.</p>
                    </div>
                    <span class="px-3 py-1 bg-purple-900/40 border border-purple-700/50 rounded-lg text-xs font-mono text-purple-300 font-semibold">25 Web Interfaces</span>
                </div>

                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="border-b border-slate-800 text-slate-400 uppercase font-mono text-[11px] bg-slate-900/50">
                                <th class="py-3 px-4">Webpage / Service</th>
                                <th class="py-3 px-4">Category</th>
                                <th class="py-3 px-4">Local URL (LAN)</th>
                                <th class="py-3 px-4">Public Tunnel URL</th>
                                <th class="py-3 px-4">Auth Type</th>
                                <th class="py-3 px-4">Credentials</th>
                                <th class="py-3 px-4 text-center">Action</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60" id="webpagesTableBody">
    """

    for s in services_data:
        pub = s.get("public_url")
        html += f"""
                            <tr class="hover:bg-slate-800/40 transition web-row" data-search="{s['name'].lower()} {s['category'].lower()} {s['local_url'].lower()} {str(pub).lower()} {s['user'].lower()} {s['auth_type'].lower()}">
                                <td class="py-3 px-4 font-semibold text-white">
                                    <div class="flex items-center gap-2">
                                        <i class="fa-solid {s['icon']} text-blue-400 text-sm"></i>
                                        <span>{s['name']}</span>
                                    </div>
                                </td>
                                <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700/60 font-medium text-[10px]">{s['category']}</span></td>
                                <td class="py-3 px-4 font-mono text-blue-400 font-semibold">{s['local_url']}</td>
                                <td class="py-3 px-4 font-mono text-[11px]">
                                    {f'<a href="{pub}" target="_blank" class="text-indigo-400 hover:underline flex items-center gap-1"><i class="fa-solid fa-globe text-[10px]"></i>{pub}</a>' if pub else '<span class="text-slate-600 italic">LAN Only</span>'}
                                </td>
                                <td class="py-3 px-4 text-slate-300 font-mono text-[10px]">{s['auth_type']}</td>
                                <td class="py-3 px-4 font-mono text-slate-300 text-[11px]">{s['user']} / {s['pass']}</td>
                                <td class="py-3 px-4 text-center">
                                    <a href="{s['local_url']}" target="_blank" class="px-2.5 py-1 rounded-lg bg-blue-600/80 hover:bg-blue-600 text-white font-semibold text-[11px] inline-flex items-center gap-1 transition">
                                        <span>Open</span>
                                        <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                                    </a>
                                </td>
                            </tr>
        """

    html += """
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- ==================== VIEW 4: ITEM 3 - DOCKER REGISTRY & CONTAINERS ==================== -->
        <section id="view-docker" class="hidden space-y-6">
            <div class="glass-card rounded-2xl p-6">
                <div class="flex items-center justify-between mb-6 pb-4 border-b border-slate-800">
                    <div>
                        <h2 class="text-lg font-bold text-white flex items-center gap-2">
                            <i class="fa-brands fa-docker text-emerald-400 text-xl"></i>
                            <span>Item 3: All Docker Images & Running Containers Registry</span>
                        </h2>
                        <p class="text-xs text-slate-400">Complete registry of all container images, tags, disk sizes, port mappings, and running containers across the ESXi Docker Host and Ubuntu VM.</p>
                    </div>
                    <span class="px-3 py-1 bg-emerald-900/40 border border-emerald-700/50 rounded-lg text-xs font-mono text-emerald-300 font-semibold">24 Total Images</span>
                </div>

                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="border-b border-slate-800 text-slate-400 uppercase font-mono text-[11px] bg-slate-900/50">
                                <th class="py-3 px-4">Host Node</th>
                                <th class="py-3 px-4">Docker Repository / Image</th>
                                <th class="py-3 px-4">Tag</th>
                                <th class="py-3 px-4">Image ID</th>
                                <th class="py-3 px-4">Size</th>
                                <th class="py-3 px-4">Associated Container(s)</th>
                                <th class="py-3 px-4">Port Mappings</th>
                                <th class="py-3 px-4">Category</th>
                                <th class="py-3 px-4 text-center">Status</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60" id="dockerTableBody">
    """

    for d in docker_list:
        html += f"""
                            <tr class="hover:bg-slate-800/40 transition docker-row" data-search="{d['host'].lower()} {d['repository'].lower()} {d['tag'].lower()} {d['image_id'].lower()} {d['containers'].lower()} {d['ports'].lower()} {d['category'].lower()}">
                                <td class="py-3 px-4 font-semibold text-slate-300">
                                    <div class="flex items-center gap-1.5">
                                        <i class="fa-solid fa-server text-slate-500 text-[10px]"></i>
                                        <span>{d['host']}</span>
                                    </div>
                                </td>
                                <td class="py-3 px-4 font-mono font-bold text-white">{d['repository']}</td>
                                <td class="py-3 px-4 font-mono text-emerald-400"><span class="px-1.5 py-0.5 rounded bg-emerald-950/60 border border-emerald-800/60">{d['tag']}</span></td>
                                <td class="py-3 px-4 font-mono text-slate-400 text-[11px]">{d['image_id']}</td>
                                <td class="py-3 px-4 font-mono text-amber-300">{d['disk_size']}</td>
                                <td class="py-3 px-4 font-mono font-semibold text-blue-300">{d['containers']}</td>
                                <td class="py-3 px-4 font-mono text-slate-400 text-[11px]">{d['ports']}</td>
                                <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700/60 text-[10px]">{d['category']}</span></td>
                                <td class="py-3 px-4 text-center">
                                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-900/50 border border-emerald-700/60 text-emerald-300">{d['status']}</span>
                                </td>
                            </tr>
        """

    html += """
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

    </main>

    <!-- Floating Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 bg-slate-900/95 border border-slate-700 text-white px-4 py-2.5 rounded-xl shadow-2xl text-xs font-semibold flex items-center gap-2 transform translate-y-20 opacity-0 transition-all duration-300 z-50">
        <i class="fa-solid fa-circle-check text-emerald-400 text-sm"></i>
        <span id="toastMsg">Notification</span>
    </div>

    <!-- Footer -->
    <footer class="mt-16 border-t border-slate-800/80 text-center text-xs text-slate-500 py-6">
        <p>Enterprise Homelab &bull; VMware ESXi 8.0.3 &bull; Docker Hub &bull; Slurm Supercluster &bull; 2026</p>
    </footer>

    <!-- Interactive Script -->
    <script>
        function showToast(msg) {
            const toast = document.getElementById('toast');
            document.getElementById('toastMsg').innerText = msg;
            toast.classList.remove('translate-y-20', 'opacity-0');
            setTimeout(() => {
                toast.classList.add('translate-y-20', 'opacity-0');
            }, 2500);
        }

        function switchView(viewName) {
            // Hide all views
            document.getElementById('view-services').classList.add('hidden');
            document.getElementById('view-nodes').classList.add('hidden');
            document.getElementById('view-webpages').classList.add('hidden');
            document.getElementById('view-docker').classList.add('hidden');

            // Deactivate all tab buttons
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));

            // Show selected view and activate button
            const targetView = document.getElementById('view-' + viewName);
            const targetBtn = document.getElementById('tabBtn-' + viewName);
            if (targetView) targetView.classList.remove('hidden');
            if (targetBtn) targetBtn.classList.add('active');
        }

        function filterCategory(cat) {
            document.querySelectorAll('.cat-btn').forEach(btn => {
                btn.classList.remove('bg-blue-600', 'text-white');
                btn.classList.add('bg-slate-900/80', 'text-slate-300');
                if (btn.innerText.startsWith(cat)) {
                    btn.classList.add('bg-blue-600', 'text-white');
                    btn.classList.remove('bg-slate-900/80', 'text-slate-300');
                }
            });

            const query = document.getElementById('globalSearchInput').value.toLowerCase();
            document.querySelectorAll('.service-card').forEach(card => {
                const matchesCat = (cat === 'All' || card.getAttribute('data-category') === cat);
                const matchesQuery = card.getAttribute('data-search').includes(query);
                card.style.display = (matchesCat && matchesQuery) ? 'flex' : 'none';
            });
        }

        document.getElementById('globalSearchInput').addEventListener('input', function(e) {
            const query = e.target.value.toLowerCase();
            
            // Filter Service Cards
            const activeCatBtn = document.querySelector('.cat-btn.bg-blue-600');
            const activeCat = activeCatBtn ? activeCatBtn.innerText.split(' (')[0] : 'All';
            document.querySelectorAll('.service-card').forEach(card => {
                const matchesCat = (activeCat === 'All' || card.getAttribute('data-category') === activeCat);
                const matchesQuery = card.getAttribute('data-search').includes(query);
                card.style.display = (matchesCat && matchesQuery) ? 'flex' : 'none';
            });

            // Filter Nodes Table
            document.querySelectorAll('.node-row').forEach(row => {
                row.style.display = row.getAttribute('data-search').includes(query) ? '' : 'none';
            });

            // Filter Web Directory Table
            document.querySelectorAll('.web-row').forEach(row => {
                row.style.display = row.getAttribute('data-search').includes(query) ? '' : 'none';
            });

            // Filter Docker Table
            document.querySelectorAll('.docker-row').forEach(row => {
                row.style.display = row.getAttribute('data-search').includes(query) ? '' : 'none';
            });
        });
    </script>
</body>
</html>
    """
    return html


def spawn_quick_tunnel(target_url, timeout=12):
    try:
        cmd = [CLOUDFLARED_BIN, "tunnel", "--url", target_url]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        start = time.time()
        public_url = None
        
        while time.time() - start < timeout:
            line = p.stderr.readline()
            if not line:
                if p.poll() is not None:
                    break
                time.sleep(0.1)
                continue
            if "Too Many Requests" in line or "error code: 1015" in line:
                print(f" [Rate-Limited by Cloudflare (429)] for {target_url}")
                break
            m = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
            if m:
                public_url = m.group(0)
                break
        return p, public_url
    except Exception as e:
        print(f"Failed to start tunnel for {target_url}: {e}")
        return None, None

def tunnel_supervisor():
    global services_config
    portal_proc = None
    portal_url = None
    tunnels = []
    
    print("Starting Background Tunnel Supervisor...")
    
    while not portal_url:
        print("Attempting to create Public Tunnel for Portal (port 8000)...")
        proc, url = spawn_quick_tunnel(f"http://localhost:{PORTAL_PORT}", timeout=15)
        if url:
            portal_proc = proc
            portal_url = url
            print(f"🌟 HOMELAB PORTAL PUBLIC URL ACQUIRED: {portal_url}")
            
            final_html = generate_enhanced_html(services_config, nodes_data, docker_registry_data, portal_url)
            with open(f"{PORTAL_DIR}/index.html", "w") as f:
                f.write(final_html)
            with open(f"{PORTAL_DIR}/services.json", "w") as f:
                json.dump({
                    "portal_public_url": portal_url,
                    "portal_local_url": f"http://192.168.0.218:{PORTAL_PORT}",
                    "services": services_config,
                    "nodes_summary_item1": nodes_data,
                    "docker_registry_item3": docker_registry_data
                }, f, indent=2)
            break
        else:
            print("Cloudflare rate limited or busy. Waiting 60s for rate-limit window to clear...")
            time.sleep(60)
            
    services_to_tunnel = [
        "unicaf-rdp", "ubuntu-pc-rdp", "grafana", "news-dashboard", "jasmin-portal", "jasmin-notebooks", 
        "jasmin-xfer", "tiktok-browser", "booklore", "agro-farm-project", "fast-cash-uk", "business-central"
    ]
    
    for s in services_config:
        if s["id"] in services_to_tunnel:
            target = s.get("target_for_tunnel")
            if not target:
                continue
            
            for attempt in range(3):
                print(f"Creating public tunnel for {s['name']} -> {target} ...")
                proc, url = spawn_quick_tunnel(target, timeout=12)
                if url:
                    s["public_url"] = url
                    tunnels.append(proc)
                    print(f" -> [LIVE]: {s['name']} => {url}")
                    final_html = generate_enhanced_html(services_config, nodes_data, docker_registry_data, portal_url)
                    with open(f"{PORTAL_DIR}/index.html", "w") as f:
                        f.write(final_html)
                    with open(f"{PORTAL_DIR}/services.json", "w") as f:
                        json.dump({
                            "portal_public_url": portal_url,
                            "portal_local_url": f"http://192.168.0.218:{PORTAL_PORT}",
                            "services": services_config,
                            "nodes_summary_item1": nodes_data,
                            "docker_registry_item3": docker_registry_data
                        }, f, indent=2)
                    time.sleep(3)
                    break
                else:
                    print(f"Rate limited or pending. Waiting 15s before next attempt...")
                    time.sleep(15)

def main():
    print("=== Initializing Homelab Portal & Web Server (with Items 1 to 3) ===")
    os.makedirs(PORTAL_DIR, exist_ok=True)
    os.chdir(PORTAL_DIR)
    
    cached_portal_url = None
    if os.path.exists(f"{PORTAL_DIR}/services.json"):
        try:
            with open(f"{PORTAL_DIR}/services.json", "r") as f:
                saved = json.load(f)
                cached_portal_url = saved.get("portal_public_url")
                saved_map = {s["id"]: s.get("public_url") for s in saved.get("services", [])}
                for s in services_config:
                    if s["id"] in saved_map and saved_map[s["id"]]:
                        s["public_url"] = saved_map[s["id"]]
        except Exception as e:
            print(f"Note: Could not load cached services.json: {e}")
            
    initial_html = generate_enhanced_html(services_config, nodes_data, docker_registry_data, cached_portal_url)
    with open(f"{PORTAL_DIR}/index.html", "w") as f:
        f.write(initial_html)

    httpd = HTTPServer(('0.0.0.0', PORTAL_PORT), SimpleHTTPRequestHandler)
    print(f"✓ Portal Web Server is LIVE on http://0.0.0.0:{PORTAL_PORT} (Local: http://192.168.0.218:{PORTAL_PORT})")

    sup_thread = threading.Thread(target=tunnel_supervisor, daemon=True)
    sup_thread.start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping portal server...")

if __name__ == '__main__':
    main()
