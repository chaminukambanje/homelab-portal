# Homelab Hub & Services Launchpad

Unified dashboard and launchpad for the ESXi & Docker Homelab infrastructure at **npcsolutions.co.uk**.

## 🌐 Public Access
Accessible securely via Cloudflare Zero Trust Tunnel at [https://portal.npcsolutions.co.uk](https://portal.npcsolutions.co.uk).

## 🚀 Key Features
* **Intelligent Routing Modes**: Auto-detects public domain vs. local LAN access. Instant switching between Local LAN IPs (`192.168.0.x`), DDNS Domain (`docker.npcsolutions.co.uk`), and Public Cloudflare Tunnels (`*.npcsolutions.co.uk`).
* **Interactive HTML5 Remote Desktop**: Integrated Apache Guacamole gateways for Ubuntu Workstation (`:8084`) and UNICAF Windows Server 2025 (`:8086`).
* **35 Tracked Homelab Services**: Enterprise ERP, AI & Slurm HPC clusters, JupyterLab, Wazuh SIEM, Network Telemetry, Prometheus & Grafana monitoring, and virtualization hosts.
* **Auto-Healing Watchdog**: Protected by `homelab-guardian.service` systemd timer for 100% persistent uptime.

## 🐳 Docker Deployment
```bash
docker compose up -d
```
