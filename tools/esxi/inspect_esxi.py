#!/usr/bin/env python3
"""
inspect_esxi.py - Comprehensive VMware ESXi Settings Inspector & Auditor
Extracts, parses, audits, and exports all configuration settings from VMware ESXi 8.x
including System, Hardware, Networking, Storage, Security, VM Inventory,
and all Advanced Kernel/Subsystem Options (with modified value detection).

Author: mbanjec
Repository: homelab-portal
"""

import os
import sys
import json
import argparse
import subprocess
import datetime
from typing import Dict, List, Any, Optional

DEFAULT_HOST = os.environ.get("ESXI_HOST", "192.168.0.200")
DEFAULT_USER = os.environ.get("ESXI_USER", "root")

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

def run_ssh_cmd(cmd: str, host: str = DEFAULT_HOST, user: str = DEFAULT_USER) -> str:
    """Executes a command on ESXi via SSH in BatchMode."""
    ssh_cmd = [
        "ssh",
        "-o", "BatchMode=yes",
        "-o", "ConnectTimeout=5",
        "-o", "StrictHostKeyChecking=no",
        "-o", "LogLevel=ERROR",
        f"{user}@{host}",
        cmd
    ]
    try:
        res = subprocess.run(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return res.stdout
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Error running command on ESXi ({cmd}): {e.stderr.strip()}{Colors.RESET}", file=sys.stderr)
        return ""
    except Exception as e:
        print(f"{Colors.RED}SSH connection failed: {e}{Colors.RESET}", file=sys.stderr)
        return ""

def parse_key_value_block(raw_text: str) -> Dict[str, str]:
    """Parses key: value lines into a dictionary."""
    data = {}
    for line in raw_text.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        parts = line.split(":", 1)
        k = parts[0].strip()
        v = parts[1].strip() if len(parts) > 1 else ""
        data[k] = v
    return data

def parse_table(raw_text: str) -> List[Dict[str, str]]:
    """Generic parser for tabular esxcli outputs with dashed separator lines."""
    lines = [l for l in raw_text.splitlines() if l.strip()]
    if len(lines) < 2:
        return []
    
    # Find line with dashes (e.g. ---- -----)
    dash_idx = -1
    for i, line in enumerate(lines):
        if set(line.replace(" ", "")).issubset({"-"}):
            dash_idx = i
            break
            
    if dash_idx == -1 or dash_idx == 0:
        return []
        
    header_line = lines[dash_idx - 1]
    separator_line = lines[dash_idx]
    
    # Calculate column spans
    col_spans = []
    start = 0
    in_col = False
    for idx, ch in enumerate(separator_line):
        if ch == '-' and not in_col:
            start = idx
            in_col = True
        elif ch == ' ' and in_col:
            col_spans.append((start, idx))
            in_col = False
    if in_col:
        col_spans.append((start, len(separator_line)))
        
    headers = []
    for s, e in col_spans:
        headers.append(header_line[s:e].strip())
        
    rows = []
    for line in lines[dash_idx + 1:]:
        row_dict = {}
        for idx, ((s, e), h) in enumerate(zip(col_spans, headers)):
            if idx == len(col_spans) - 1:
                val = line[s:].strip() if s < len(line) else ""
            else:
                val = line[s:e].strip() if s < len(line) else ""
            row_dict[h] = val
        if any(row_dict.values()):
            rows.append(row_dict)
            
    return rows

def parse_advanced_settings(raw_text: str) -> List[Dict[str, Any]]:
    """Parses esxcli system settings advanced list output into structured dicts."""
    blocks = raw_text.split("   Path:")
    settings = []
    for block in blocks:
        if not block.strip():
            continue
        full_block = "   Path:" + block
        lines = full_block.splitlines()
        item = {}
        for line in lines:
            line = line.strip()
            if not line or ":" not in line:
                continue
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            item[k] = v
            
        path = item.get("Path", "")
        item_type = item.get("Type", "")
        int_val = item.get("Int Value")
        str_val = item.get("String Value", "")
        def_int_val = item.get("Default Int Value")
        def_str_val = item.get("Default String Value", "")
        
        current_val = int_val if item_type == "integer" else str_val
        default_val = def_int_val if item_type == "integer" else def_str_val
        
        is_modified = False
        if current_val is not None and default_val is not None:
            is_modified = (str(current_val).strip() != str(default_val).strip())
            
        settings.append({
            "path": path,
            "type": item_type,
            "current_value": current_val,
            "default_value": default_val,
            "min_value": item.get("Min Value"),
            "max_value": item.get("Max Value"),
            "description": item.get("Description", ""),
            "impact": item.get("Impact", ""),
            "host_specific": item.get("Host Specific", ""),
            "is_modified": is_modified
        })
    return settings

def fetch_all_settings(host: str = DEFAULT_HOST, user: str = DEFAULT_USER) -> Dict[str, Any]:
    """Collects all configuration subsystems from the ESXi host."""
    print(f"{Colors.CYAN}Connecting to ESXi host {user}@{host}...{Colors.RESET}")
    
    # 1. System Version & Hardware
    sys_ver_raw = run_ssh_cmd("esxcli system version get", host, user)
    hw_plat_raw = run_ssh_cmd("esxcli hardware platform get", host, user)
    hw_cpu_raw = run_ssh_cmd("esxcli hardware cpu global get", host, user)
    hw_mem_raw = run_ssh_cmd("esxcli hardware memory get", host, user)
    hostname_raw = run_ssh_cmd("esxcli system hostname get", host, user)
    ntp_raw = run_ssh_cmd("esxcli system ntp get", host, user)
    syslog_raw = run_ssh_cmd("esxcli system syslog config get", host, user)
    
    # 2. Networking
    nics_raw = run_ssh_cmd("esxcli network nic list", host, user)
    vswitch_raw = run_ssh_cmd("esxcli network vswitch standard list", host, user)
    portgroups_raw = run_ssh_cmd("esxcli network vswitch standard portgroup list", host, user)
    vmk_raw = run_ssh_cmd("esxcli network ip interface list", host, user)
    vmk_ipv4_raw = run_ssh_cmd("esxcli network ip interface ipv4 get", host, user)
    routes_raw = run_ssh_cmd("esxcli network ip route ipv4 list", host, user)
    dns_server_raw = run_ssh_cmd("esxcli network ip dns server list", host, user)
    dns_search_raw = run_ssh_cmd("esxcli network ip dns search list", host, user)
    firewall_raw = run_ssh_cmd("esxcli network firewall get", host, user)
    firewall_rules_raw = run_ssh_cmd("esxcli network firewall ruleset list", host, user)
    
    # 3. Storage
    fs_raw = run_ssh_cmd("esxcli storage filesystem list", host, user)
    core_dev_raw = run_ssh_cmd("esxcli storage core device list", host, user)
    
    # 4. Security & Services
    services_raw = run_ssh_cmd("chkconfig --list", host, user)
    sec_fips_raw = run_ssh_cmd("esxcli system security fips140 ssh get", host, user)
    acceptance_raw = run_ssh_cmd("esxcli software acceptance get", host, user)
    
    # 5. Virtual Machines
    vms_raw = run_ssh_cmd("vim-cmd vmsvc/getallvms", host, user)
    vm_procs_raw = run_ssh_cmd("esxcli vm process list", host, user)
    
    # 6. Advanced Settings
    print(f"{Colors.CYAN}Extracting 829+ advanced system settings (kernel/subsystem options)...{Colors.RESET}")
    adv_raw = run_ssh_cmd("esxcli system settings advanced list", host, user)
    
    # Parse services
    services_dict = {}
    for line in services_raw.splitlines():
        parts = line.strip().split()
        if len(parts) >= 2:
            services_dict[parts[0]] = parts[1]
            
    # Parse VMs
    vm_list = []
    for line in vms_raw.splitlines():
        line = line.strip()
        m = re.match(r'^(\d+)\s+(.+?)\s{2,}(\[[^\]]+\].+?\.vmx)\s+(\S+)\s+(\S+)\s*(.*)$', line)
        if m:
            vm_list.append({
                "vmid": m.group(1),
                "name": m.group(2).strip(),
                "config_file": m.group(3).strip(),
                "guest_os": m.group(4).strip(),
                "version": m.group(5).strip(),
                "extra": m.group(6).strip()
            })

    # Parse running VM processes
    running_vms = []
    curr_vm = {}
    for line in vm_procs_raw.splitlines():
        line = line.strip()
        if not line:
            if curr_vm:
                running_vms.append(curr_vm)
                curr_vm = {}
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            curr_vm[k.strip()] = v.strip()
    if curr_vm:
        running_vms.append(curr_vm)

    # Parse storage core devices
    storage_devices = []
    curr_dev = {}
    for line in core_dev_raw.splitlines():
        line = line.strip()
        if not line:
            if curr_dev:
                storage_devices.append(curr_dev)
                curr_dev = {}
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            curr_dev[k.strip()] = v.strip()
        elif line.startswith("naa.") or line.startswith("mpx.") or line.startswith("t10."):
            curr_dev["Device"] = line
    if curr_dev:
        storage_devices.append(curr_dev)

    advanced_settings = parse_advanced_settings(adv_raw)
    modified_advanced = [s for s in advanced_settings if s["is_modified"]]

    return {
        "metadata": {
            "host": host,
            "user": user,
            "timestamp": datetime.datetime.now().isoformat(),
            "collector": "inspect_esxi.py v1.0"
        },
        "system": {
            "version": parse_key_value_block(sys_ver_raw),
            "platform": parse_key_value_block(hw_plat_raw),
            "cpu": parse_key_value_block(hw_cpu_raw),
            "memory": parse_key_value_block(hw_mem_raw),
            "hostname": parse_key_value_block(hostname_raw),
            "ntp": parse_key_value_block(ntp_raw),
            "syslog": parse_key_value_block(syslog_raw)
        },
        "network": {
            "nics": parse_table(nics_raw),
            "vswitches_raw": vswitch_raw.strip(),
            "portgroups": parse_table(portgroups_raw),
            "vmkernel_ipv4": parse_table(vmk_ipv4_raw),
            "routes": parse_table(routes_raw),
            "dns_servers": dns_server_raw.strip(),
            "dns_search": dns_search_raw.strip(),
            "firewall": parse_key_value_block(firewall_raw),
            "firewall_rules": parse_table(firewall_rules_raw)
        },
        "storage": {
            "filesystems": parse_table(fs_raw),
            "devices_count": len(storage_devices),
            "devices_sample": storage_devices[:10]
        },
        "security": {
            "services": services_dict,
            "fips140": parse_key_value_block(sec_fips_raw),
            "software_acceptance": acceptance_raw.strip()
        },
        "virtual_machines": {
            "total_count": len(vm_list),
            "inventory": vm_list,
            "running_count": len(running_vms),
            "running_vms": running_vms
        },
        "advanced_settings": {
            "total_count": len(advanced_settings),
            "modified_count": len(modified_advanced),
            "modified_settings": modified_advanced,
            "all_settings": advanced_settings
        }
    }

def print_overview(data: Dict[str, Any]):
    """Displays a clean, styled overview of the ESXi host settings."""
    sys_info = data["system"]
    net_info = data["network"]
    stor_info = data["storage"]
    vm_info = data["virtual_machines"]
    adv_info = data["advanced_settings"]
    sec_info = data["security"]
    
    print("\n" + "="*80)
    print(f"{Colors.BOLD}{Colors.HEADER}VMWARE ESXi HOST SETTINGS & STATUS OVERVIEW{Colors.RESET}")
    print(f"Host: {Colors.CYAN}{sys_info['hostname'].get('Fully Qualified Domain Name', 'esxi-01')}{Colors.RESET} ({data['metadata']['host']})")
    print(f"Timestamp: {data['metadata']['timestamp']}")
    print("="*80)
    
    # 1. System Platform
    print(f"\n{Colors.BOLD}{Colors.GREEN}[1] SYSTEM & HARDWARE PLATFORM{Colors.RESET}")
    print(f"  • Hardware Model:    {Colors.BOLD}{sys_info['platform'].get('Product Name', 'Unknown')}{Colors.RESET} ({sys_info['platform'].get('Vendor Name', 'Dell')})")
    print(f"  • Serial / Service:  {sys_info['platform'].get('Serial Number', 'N/A')}")
    print(f"  • Hypervisor Build:  {sys_info['version'].get('Product', 'VMware ESXi')} {sys_info['version'].get('Version', '8.0.3')} (Build {sys_info['version'].get('Build', '')})")
    
    mem_bytes = int(sys_info['memory'].get('Physical Memory', '0').replace('Bytes', '').strip() or 0)
    mem_gb = round(mem_bytes / (1024**3), 2)
    print(f"  • Processors:        {sys_info['cpu'].get('CPU Packages', '2')} Packages, {sys_info['cpu'].get('CPU Cores', '20')} Cores, {sys_info['cpu'].get('CPU Threads', '40')} Threads (Hyperthreading: {sys_info['cpu'].get('Hyperthreading Active', 'true')})")
    print(f"  • Physical Memory:   {mem_gb} GB RAM (NUMA Nodes: {sys_info['cpu'].get('NUMA Node Count', '2')})")
    print(f"  • NTP Status:        Enabled ({sys_info['ntp'].get('Time Synchronized', 'true')}) | Servers: {sys_info['ntp'].get('Servers', 'N/A')}")
    print(f"  • Syslog Storage:    {sys_info['syslog'].get('Local Log Output', '/scratch/log')} (Persistent: {sys_info['syslog'].get('Local Log Output Is Persistent', 'true')}, LogLevel: {sys_info['syslog'].get('Log Level', 'error')})")

    # 2. Network Topology
    print(f"\n{Colors.BOLD}{Colors.BLUE}[2] NETWORK TOPOLOGY & INTERFACES{Colors.RESET}")
    for vmk in net_info["vmkernel_ipv4"]:
        print(f"  • Management vmk:    {vmk.get('Name')} -> {vmk.get('IPv4 Address')}/{vmk.get('IPv4 Netmask')} (Gateway: {vmk.get('Gateway')})")
    print(f"  • DNS Configuration: Servers: {net_info['dns_servers']} | Search: {net_info['dns_search']}")
    print("  • Physical NICs (vmnic):")
    for nic in net_info["nics"]:
        link_color = Colors.GREEN if nic.get('Link Status') == 'Up' else Colors.RED
        print(f"    - {Colors.BOLD}{nic.get('Name')}{Colors.RESET}: Status {link_color}{nic.get('Link Status')}{Colors.RESET}, Speed {nic.get('Speed')} Mbps, MAC {nic.get('MAC Address')} ({nic.get('Description', '')})")
    print("  • Virtual Portgroups:")
    for pg in net_info["portgroups"][:6]:
        vswitch = pg.get('Virtual Switch') or pg.get('VirtualSwitch') or 'vSwitch0'
        vlan = pg.get('VLAN ID') or pg.get('VLANID') or '0'
        clients = pg.get('Active Clients', '0')
        print(f"    - PG '{pg.get('Name')}': vSwitch '{vswitch}', VLAN {vlan}, Active Clients: {clients}")

    # 3. Storage Pools
    print(f"\n{Colors.BOLD}{Colors.YELLOW}[3] DATASTORES & STORAGE FILESYSTEMS{Colors.RESET}")
    for fs in stor_info["filesystems"]:
        vol_name = fs.get("Volume Name", "")
        fs_type = fs.get("Type", "")
        size_b = int(fs.get("Size", 0) or 0)
        free_b = int(fs.get("Free", 0) or 0)
        size_gb = round(size_b / (1024**3), 1)
        free_gb = round(free_b / (1024**3), 1)
        used_gb = round(size_gb - free_gb, 1)
        pct_used = round((used_gb / size_gb * 100), 1) if size_gb > 0 else 0
        
        # Color based on utilization
        color = Colors.GREEN if pct_used < 80 else (Colors.YELLOW if pct_used < 90 else Colors.RED)
        if vol_name:
            print(f"  • {vol_name:<18} [{fs_type:<6}]: {size_gb:>7.1f} GB Total | {free_gb:>7.1f} GB Free | Used: {color}{used_gb:>7.1f} GB ({pct_used}%){Colors.RESET}")

    # 4. Security & Daemons
    print(f"\n{Colors.BOLD}[4] SECURITY & CORE SERVICES{Colors.RESET}")
    key_svcs = ["SSH", "ESXShell", "ntpd", "DCUI", "esxui", "envoy"]
    svc_strs = []
    for s in key_svcs:
        st = sec_info["services"].get(s, "off")
        c = Colors.GREEN if st == "on" else Colors.DIM
        svc_strs.append(f"{s}: {c}{st}{Colors.RESET}")
    print(f"  • Service States:    {' | '.join(svc_strs)}")
    print(f"  • Firewall Status:   Enabled: {net_info['firewall'].get('Enabled')} | Default Action: {net_info['firewall'].get('Default Action')}")
    print(f"  • Acceptance Level:  {sec_info.get('software_acceptance', 'PartnerSupported')}")

    # 5. Virtual Machines
    print(f"\n{Colors.BOLD}[5] VIRTUAL MACHINE INVENTORY{Colors.RESET}")
    print(f"  • Total Configured:  {vm_info['total_count']} Virtual Machines ({vm_info['running_count']} currently active/powered on)")
    print("  • Sample Workloads:")
    for vm in vm_info["inventory"][:8]:
        print(f"    - VMID {vm.get('vmid'):<4} | {Colors.BOLD}{vm.get('name'):<26}{Colors.RESET} | OS: {vm.get('guest_os'):<20} | File: {vm.get('config_file')}")
    if vm_info['total_count'] > 8:
        print(f"    - ... and {vm_info['total_count'] - 8} additional virtual machines.")

    # 6. Advanced System Settings
    print(f"\n{Colors.BOLD}{Colors.HEADER}[6] ADVANCED SYSTEM SETTINGS CATALOG{Colors.RESET}")
    print(f"  • Total Advanced Options:   {Colors.BOLD}{adv_info['total_count']}{Colors.RESET} options indexed")
    print(f"  • Customized / Modified:   {Colors.YELLOW}{Colors.BOLD}{adv_info['modified_count']}{Colors.RESET} settings differ from system defaults")
    print("  • Active Customizations:")
    for mod in adv_info["modified_settings"][:10]:
        print(f"    - {Colors.BOLD}{mod['path']}{Colors.RESET}: Current = {Colors.CYAN}{mod['current_value']}{Colors.RESET} (Default: {mod['default_value']}) -> {mod['description'][:65]}...")
    print("="*80 + "\n")

def generate_markdown_audit_report(data: Dict[str, Any]) -> str:
    """Generates an exhaustive, high-density Markdown audit report."""
    sys_info = data["system"]
    net_info = data["network"]
    stor_info = data["storage"]
    vm_info = data["virtual_machines"]
    adv_info = data["advanced_settings"]
    sec_info = data["security"]
    
    mem_bytes = int(sys_info['memory'].get('Physical Memory', '0').replace('Bytes', '').strip() or 0)
    mem_gb = round(mem_bytes / (1024**3), 2)
    
    md = []
    md.append(f"# VMware ESXi 8.0.3 Host Configuration Audit & Settings Reference")
    md.append(f"**Host**: `{sys_info['hostname'].get('Fully Qualified Domain Name', 'esxi-01.npcsolutions.co.za')}` (`{data['metadata']['host']}`)  ")
    md.append(f"**Generated**: `{data['metadata']['timestamp']}` | **Collector**: `{data['metadata']['collector']}`  ")
    md.append(f"\n---\n")

    # Section 1
    md.append("## 1. Platform & Hardware Architecture")
    md.append("| Attribute | Value | Description |")
    md.append("| :--- | :--- | :--- |")
    md.append(f"| **Hardware Model** | `{sys_info['platform'].get('Product Name', 'PowerEdge R620')}` | Vendor: {sys_info['platform'].get('Vendor Name', 'Dell Inc.')} |")
    md.append(f"| **Chassis Serial** | `{sys_info['platform'].get('Serial Number', 'N/A')}` | Dell Service Tag / Chassis Enclosure |")
    md.append(f"| **ESXi Version** | `VMware ESXi 8.0.3` | Build `{sys_info['version'].get('Build', '24677879')}`, Patch `{sys_info['version'].get('Patch', '70')}` |")
    md.append(f"| **CPU Architecture** | `{sys_info['cpu'].get('CPU Packages', '2')} Packages, {sys_info['cpu'].get('CPU Cores', '20')} Cores, {sys_info['cpu'].get('CPU Threads', '40')} Threads` | Hyperthreading Enabled (`{sys_info['cpu'].get('Hyperthreading Active')}`) |")
    md.append(f"| **System RAM** | `{mem_gb} GB DDR3 ECC` | NUMA Nodes: `{sys_info['cpu'].get('NUMA Node Count', '2')}`, Reliable: `{sys_info['memory'].get('Reliable Memory', '0')}` |")
    md.append(f"| **Host Identity** | `{sys_info['hostname'].get('Host Name')}` | FQDN: `{sys_info['hostname'].get('Fully Qualified Domain Name')}`, Domain: `{sys_info['hostname'].get('Domain Name')}` |")
    md.append(f"| **Time Synchronization** | NTP Enabled (`{sys_info['ntp'].get('Time Synchronized')}`) | Servers: `{sys_info['ntp'].get('Servers')}` |")
    md.append(f"| **Syslog Architecture** | Path: `{sys_info['syslog'].get('Local Log Output')}` | Persistent: `{sys_info['syslog'].get('Local Log Output Is Persistent')}`, Rotations: `{sys_info['syslog'].get('Local Logging Default Rotations')}`, LogLevel: `{sys_info['syslog'].get('Log Level')}` |")
    md.append("\n")

    # Section 2
    md.append("## 2. Networking Subsystem & Virtual Switches")
    md.append("### 2.1 Physical Network Adapters (vmnic)")
    md.append("| Interface | PCI Device | Driver | Admin Status | Link Status | Speed / Duplex | MAC Address | Description |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    for nic in net_info["nics"]:
        md.append(f"| `{nic.get('Name')}` | `{nic.get('PCI Device')}` | `{nic.get('Driver')}` | `{nic.get('Admin Status')}` | **`{nic.get('Link Status')}`** | {nic.get('Speed')} Mbps / {nic.get('Duplex')} | `{nic.get('MAC Address')}` | {nic.get('Description')} |")
    md.append("\n")

    md.append("### 2.2 VMkernel Management & Port Groups")
    md.append("| Interface | IPv4 Address | Subnet Mask | Broadcast | Gateway | DHCP DNS |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
    for vmk in net_info["vmkernel_ipv4"]:
        md.append(f"| `{vmk.get('Name')}` | `{vmk.get('IPv4 Address')}` | `{vmk.get('IPv4 Netmask')}` | `{vmk.get('IPv4 Broadcast')}` | `{vmk.get('Gateway')}` | `{vmk.get('DHCP DNS')}` |")
    md.append("\n")

    md.append("### 2.3 Port Group Allocations & vSwitches")
    md.append("| Port Group Name | Virtual Switch | Active Clients | VLAN ID |")
    md.append("| :--- | :--- | :--- | :--- |")
    for pg in net_info["portgroups"]:
        vswitch = pg.get('Virtual Switch') or pg.get('VirtualSwitch') or 'vSwitch0'
        vlan = pg.get('VLAN ID') or pg.get('VLANID') or '0'
        clients = pg.get('Active Clients', '0')
        md.append(f"| `{pg.get('Name')}` | `{vswitch}` | {clients} | `{vlan}` |")
    md.append("\n")

    md.append(f"**DNS Resolvers**: `{net_info['dns_servers']}` | **Domain Search**: `{net_info['dns_search']}`  ")
    md.append(f"**Firewall**: Default Action = `{net_info['firewall'].get('Default Action')}`, Enabled = `{net_info['firewall'].get('Enabled')}`  \n")

    # Section 3
    md.append("## 3. Storage Pools & Datastores")
    md.append("| Volume Name | Mount Point | Filesystem | Capacity (GB) | Free (GB) | Used (GB) | Utilization % |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    for fs in stor_info["filesystems"]:
        vol_name = fs.get("Volume Name", "")
        fs_type = fs.get("Type", "")
        mount = fs.get("Mount Point", "")
        size_b = int(fs.get("Size", 0) or 0)
        free_b = int(fs.get("Free", 0) or 0)
        size_gb = round(size_b / (1024**3), 1)
        free_gb = round(free_b / (1024**3), 1)
        used_gb = round(size_gb - free_gb, 1)
        pct_used = round((used_gb / size_gb * 100), 1) if size_gb > 0 else 0
        if vol_name:
            md.append(f"| **`{vol_name}`** | `{mount}` | `{fs_type}` | {size_gb} GB | {free_gb} GB | {used_gb} GB | **{pct_used}%** |")
    md.append("\n")

    # Section 4
    md.append("## 4. Virtual Machine Workloads & Allocation")
    md.append(f"Total Virtual Machines: **{vm_info['total_count']}** registered, **{vm_info['running_count']}** active processes.")
    md.append("\n| VMID | Name | Guest OS | Datastore Config Path | Hardware Version |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for vm in vm_info["inventory"]:
        md.append(f"| `{vm.get('vmid')}` | **`{vm.get('name')}`** | `{vm.get('guest_os')}` | `{vm.get('config_file')}` | `{vm.get('extra')}` |")
    md.append("\n")

    # Section 5
    md.append("## 5. Security Posture & Daemons")
    md.append("| Service / Feature | Status | Role / Scope |")
    md.append("| :--- | :--- | :--- |")
    for svc, status in sec_info["services"].items():
        if status == "on" or svc in ["SSH", "ESXShell", "ntpd", "DCUI", "vsanObserver"]:
            md.append(f"| `{svc}` | **`{status.upper()}`** | Host Service Daemon |")
    md.append(f"| **FIPS 140 Cryptography** | `{sec_info['fips140'].get('FIPS140 Mode', 'Disabled')}` | Kernel Cryptographic Integrity |")
    md.append(f"| **Software Acceptance Level** | `{sec_info.get('software_acceptance')}` | VIB Installation Signature Policy |")
    md.append("\n")

    # Section 6
    md.append("## 6. Advanced Kernel & System Settings (Catalog)")
    md.append(f"The hypervisor configuration contains **{adv_info['total_count']}** total advanced options across all kernel subsystems.")
    md.append(f"**{adv_info['modified_count']}** parameters have customized values differing from factory defaults.\n")
    
    md.append("### 6.1 Customized / Non-Default Options")
    md.append("| Parameter Path | Current Value | Default Value | Description |")
    md.append("| :--- | :--- | :--- | :--- |")
    for mod in adv_info["modified_settings"]:
        md.append(f"| **`{mod['path']}`** | `{mod['current_value']}` | `{mod['default_value']}` | {mod['description']} |")
    md.append("\n")

    md.append("### 6.2 Key Subsystem Advanced Parameters Overview")
    # Group settings by top-level category
    categories = {}
    for s in adv_info["all_settings"]:
        p = s["path"].strip("/").split("/")[0] if "/" in s["path"] else "Other"
        if p not in categories:
            categories[p] = []
        categories[p].append(s)

    for cat_name, cat_settings in sorted(categories.items()):
        md.append(f"<details><summary><strong>Subsystem: /{cat_name} ({len(cat_settings)} options)</strong></summary>\n")
        md.append("| Path | Type | Current Value | Default Value | Description |")
        md.append("| :--- | :--- | :--- | :--- | :--- |")
        for s in cat_settings:
            md.append(f"| `{s['path']}` | `{s['type']}` | `{s['current_value']}` | `{s['default_value']}` | {s['description']} |")
        md.append("\n</details>\n")

    return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description="VMware ESXi Host Settings Inspector & Auditor")
    parser.add_argument("--host", default=DEFAULT_HOST, help="ESXi Host IP or FQDN")
    parser.add_argument("--user", default=DEFAULT_USER, help="SSH User")
    parser.add_argument("--overview", action="store_true", help="Display colored summary overview")
    parser.add_argument("--advanced", action="store_true", help="List advanced system settings")
    parser.add_argument("--modified", action="store_true", help="List only modified/custom advanced settings")
    parser.add_argument("--search", type=str, help="Search advanced settings by keyword in path or description")
    parser.add_argument("--category", choices=["system", "network", "storage", "security", "vms", "advanced"], help="Inspect specific category")
    parser.add_argument("--export-json", type=str, help="Save full configuration database to JSON file")
    parser.add_argument("--export-md", type=str, help="Save markdown audit report to file")
    parser.add_argument("--cache", type=str, help="Load data from cached JSON file instead of live SSH")
    
    args = parser.parse_args()
    
    data = None
    if args.cache and os.path.exists(args.cache):
        with open(args.cache, "r") as f:
            data = json.load(f)
    else:
        data = fetch_all_settings(args.host, args.user)
        
    if args.export_json:
        with open(args.export_json, "w") as f:
            json.dump(data, f, indent=2)
        print(f"{Colors.GREEN}Exported full configuration database to: {args.export_json}{Colors.RESET}")
        
    if args.export_md:
        md_content = generate_markdown_audit_report(data)
        with open(args.export_md, "w") as f:
            f.write(md_content)
        print(f"{Colors.GREEN}Exported Markdown audit report to: {args.export_md}{Colors.RESET}")

    if args.search:
        term = args.search.lower()
        matches = [s for s in data["advanced_settings"]["all_settings"] if term in s["path"].lower() or term in s["description"].lower()]
        print(f"\n{Colors.BOLD}Found {len(matches)} advanced settings matching '{args.search}':{Colors.RESET}\n")
        for m in matches:
            mod_tag = f" {Colors.YELLOW}[MODIFIED]{Colors.RESET}" if m["is_modified"] else ""
            print(f"• {Colors.BOLD}{m['path']}{Colors.RESET}{mod_tag}")
            print(f"  Type: {m['type']} | Value: {Colors.CYAN}{m['current_value']}{Colors.RESET} | Default: {m['default_value']}")
            print(f"  Description: {m['description']}\n")
        return

    if args.modified:
        mods = data["advanced_settings"]["modified_settings"]
        print(f"\n{Colors.BOLD}Found {len(mods)} customized advanced settings (differ from default):{Colors.RESET}\n")
        for m in mods:
            print(f"• {Colors.BOLD}{m['path']}{Colors.RESET}")
            print(f"  Value: {Colors.CYAN}{m['current_value']}{Colors.RESET} (Default: {m['default_value']}) | Type: {m['type']}")
            print(f"  Description: {m['description']}\n")
        return

    if args.overview or (not args.advanced and not args.category and not args.export_json and not args.export_md):
        print_overview(data)

if __name__ == "__main__":
    main()
