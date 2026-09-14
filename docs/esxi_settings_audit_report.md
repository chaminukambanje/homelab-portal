# VMware ESXi 8.0.3 Host Configuration Audit & Settings Reference
**Host**: `esxi-01.npcsolutions.co.za` (`192.168.0.200`)  
**Generated**: `2026-09-14T21:59:05.774914` | **Collector**: `inspect_esxi.py v1.0`  

---

## 1. Platform & Hardware Architecture
| Attribute | Value | Description |
| :--- | :--- | :--- |
| **Hardware Model** | `PowerEdge R620` | Vendor: Dell Inc. |
| **Chassis Serial** | `8Y4K522` | Dell Service Tag / Chassis Enclosure |
| **ESXi Version** | `VMware ESXi 8.0.3` | Build `Releasebuild-24677879`, Patch `70` |
| **CPU Architecture** | `2 Packages, 20 Cores, 40 Threads` | Hyperthreading Enabled (`true`) |
| **System RAM** | `223.96 GB DDR3 ECC` | NUMA Nodes: `2`, Reliable: `0 Bytes` |
| **Host Identity** | `esxi-01` | FQDN: `esxi-01.npcsolutions.co.za`, Domain: `npcsolutions.co.za` |
| **Time Synchronization** | NTP Enabled (`true`) | Servers: `pool.ntp.org, uk.pool.ntp.org, 0.uk.pool.ntp.org, 1.uk.pool.ntp.org, 2.uk.pool.ntp.org, 3.uk.pool.ntp.org` |
| **Syslog Architecture** | Path: `/scratch/log` | Persistent: `true`, Rotations: `8`, LogLevel: `error` |


## 2. Networking Subsystem & Virtual Switches
### 2.1 Physical Network Adapters (vmnic)
| Interface | PCI Device | Driver | Admin Status | Link Status | Speed / Duplex | MAC Address | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `vmnic0` | `0000:01:00.0` | `ntg3` | `Up` | **`Up`** | 1000 Mbps / Full | `90:b1:1c:3c:c5:61` | Broadcom Co |
| `vmnic1` | `0000:01:00.1` | `ntg3` | `Up` | **`Down`** | 0 Mbps / Half | `90:b1:1c:3c:c5:62` | Broadcom Co |
| `vmnic2` | `0000:02:00.0` | `ntg3` | `Up` | **`Up`** | 1000 Mbps / Full | `90:b1:1c:3c:c5:63` | Broadcom Co |
| `vmnic3` | `0000:02:00.1` | `ntg3` | `Up` | **`Down`** | 0 Mbps / Half | `90:b1:1c:3c:c5:64` | Broadcom Co |


### 2.2 VMkernel Management & Port Groups
| Interface | IPv4 Address | Subnet Mask | Broadcast | Gateway | DHCP DNS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `vmk0` | `192.168.0.200` | `255.255.255.0` | `192.168.0.255` | `192.168.0.1` | `false` |


### 2.3 Port Group Allocations & vSwitches
| Port Group Name | Virtual Switch | VLAN ID | Active Uplinks |
| :--- | :--- | :--- | :--- |
| `Management Network` | `None` | `None` | `None` |
| `Mirror-Network` | `None` | `None` | `None` |
| `SPAN-Monitoring-PG` | `None` | `None` | `None` |
| `VM Network` | `None` | `None` | `None` |


**DNS Resolvers**: `DNSServers: 192.168.0.229, 192.168.0.1` | **Domain Search**: `DNSSearch Domains: npcsolutions.co.za`  
**Firewall**: Default Action = `DROP`, Enabled = `true`  

## 3. Storage Pools & Datastores
| Volume Name | Mount Point | Filesystem | Capacity (GB) | Free (GB) | Used (GB) | Utilization % |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`datastore2`** | `/vmfs/volumes/6893488d-c4dfd4bb-20bb-90b11c3cc561` | `VMFS-6` | 2234.2 GB | 716.5 GB | 1517.7 GB | **67.9%** |
| **`datastore3`** | `/vmfs/volumes/6a4fb9d9-3b7d8b33-0da4-90b11c3cc561` | `VMFS-6` | 2234.2 GB | 482.8 GB | 1751.4 GB | **78.4%** |
| **`datastore1`** | `/vmfs/volumes/6824ca0f-0b857519-707b-90b11c3cc561` | `VMFS-6` | 1733.8 GB | 409.9 GB | 1323.9 GB | **76.4%** |
| **`OSDATA-6824ca0f-f9173a53-55ca-90b11c3cc561`** | `/vmfs/volumes/6824ca0f-f9173a53-55ca-90b11c3cc561` | `VMFSOS` | 119.8 GB | 114.5 GB | 5.3 GB | **4.4%** |
| **`BOOTBANK1`** | `/vmfs/volumes/1625b350-a74a0254-b68c-3f9c8a969ecd` | `vfat` | 4.0 GB | 3.8 GB | 0.2 GB | **5.0%** |
| **`BOOTBANK2`** | `/vmfs/volumes/f904d0cb-b0472b50-b19e-0f73a37f49da` | `vfat` | 4.0 GB | 3.7 GB | 0.3 GB | **7.5%** |


## 4. Virtual Machine Workloads & Allocation
Total Virtual Machines: **15** registered, **11** active processes.

| VMID | Name | Guest OS | Datastore Config Path | Hardware Version |
| :--- | :--- | :--- | :--- | :--- |
| `101` | **`VMware`** | `Server` | `vCenter` | `8   [datastore3] VMware vCenter Server 8/VMware vCenter Server 8.vmx   other3xLinux64Guest          vmx-10    VMware vCenter Server Appliance` |
| `103` | **`001_login-01`** | `001_login-01/001_login-01.vmx` | `[datastore3]` | `centos9_64Guest              vmx-18` |
| `106` | **`001_node-01`** | `001_node-01/001_node-01.vmx` | `[datastore3]` | `centos9_64Guest              vmx-18` |
| `107` | **`Docker`** | `Docker/Docker.vmx` | `[datastore3]` | `ubuntu64Guest                vmx-21` |
| `108` | **`006_ai-cortex-01`** | `ubuntu_test/ubuntu_test.vmx` | `[datastore3]` | `ubuntu64Guest                vmx-21` |
| `109` | **`005_DC-01`** | `DC-01/DC-01.vmx` | `[datastore3]` | `windows2022srvNext_64Guest   vmx-21` |
| `110` | **`00_UNICAF-2025-2026`** | `windows-home-use/windows-home-use.vmx` | `[datastore2]` | `windows2022srvNext_64Guest   vmx-20` |
| `6` | **`001_node-03`** | `node-03/node-03.vmx` | `[datastore1]` | `centos9_64Guest              vmx-21` |
| `76` | **`003_truenas`** | `truenas/truenas.vmx` | `[datastore1]` | `debian11_64Guest             vmx-21` |
| `82` | **`003_Booklore`** | `booklore/booklore.vmx` | `[datastore1]` | `centos8_64Guest              vmx-21` |
| `86` | **`001_node-02`** | `00_node-02/00_node-02.vmx` | `[datastore3]` | `rockylinux_64Guest           vmx-21` |
| `87` | **`001_node-04`** | `00_node-04/00_node-04.vmx` | `[datastore3]` | `rockylinux_64Guest           vmx-21` |
| `89` | **`005_BC-server`** | `BC-server/BC-server.vmx` | `[datastore3]` | `windows2022srvNext_64Guest   vmx-21` |
| `90` | **`005_sql`** | `sql/sql.vmx` | `[datastore3]` | `windows2022srvNext_64Guest   vmx-21` |
| `91` | **`005_DC-02`** | `DC-02/DC-02.vmx` | `[datastore3]` | `windows2022srvNext_64Guest   vmx-21` |


## 5. Security Posture & Daemons
| Service / Feature | Status | Role / Scope |
| :--- | :--- | :--- |
| `vsanObserver` | **`OFF`** | Host Service Daemon |
| `ntpd` | **`ON`** | Host Service Daemon |
| `SSH` | **`ON`** | Host Service Daemon |
| `ESXShell` | **`ON`** | Host Service Daemon |
| `DCUI` | **`ON`** | Host Service Daemon |
| `esxui` | **`ON`** | Host Service Daemon |
| `sandboxd` | **`ON`** | Host Service Daemon |
| `esxgdpd` | **`ON`** | Host Service Daemon |
| `envoy` | **`ON`** | Host Service Daemon |
| `vdtc` | **`ON`** | Host Service Daemon |
| `swapobjd` | **`ON`** | Host Service Daemon |
| `kmxa` | **`ON`** | Host Service Daemon |
| `iofilterd-vmwarevmcrypt` | **`ON`** | Host Service Daemon |
| `iofilterd-spm` | **`ON`** | Host Service Daemon |
| `vaai-nasd` | **`ON`** | Host Service Daemon |
| `vvold` | **`ON`** | Host Service Daemon |
| `rhttpproxy` | **`ON`** | Host Service Daemon |
| `hostdCgiServer` | **`ON`** | Host Service Daemon |
| `hostd` | **`ON`** | Host Service Daemon |
| `esxTokenCPS` | **`ON`** | Host Service Daemon |
| `apiForwarder` | **`ON`** | Host Service Daemon |
| `storageRM` | **`ON`** | Host Service Daemon |
| `sensord` | **`ON`** | Host Service Daemon |
| `sdrsInjector` | **`ON`** | Host Service Daemon |
| `nfcd` | **`ON`** | Host Service Daemon |
| `lbtd` | **`ON`** | Host Service Daemon |
| `gstored` | **`ON`** | Host Service Daemon |
| `vmfstraced` | **`ON`** | Host Service Daemon |
| `infravisor` | **`ON`** | Host Service Daemon |
| `clusterAgent` | **`ON`** | Host Service Daemon |
| `pmemGarbageCollection` | **`ON`** | Host Service Daemon |
| `nscd` | **`ON`** | Host Service Daemon |
| `nicmgmtd` | **`ON`** | Host Service Daemon |
| `dcbd` | **`ON`** | Host Service Daemon |
| `cdp` | **`ON`** | Host Service Daemon |
| `smartd` | **`ON`** | Host Service Daemon |
| `lacp` | **`ON`** | Host Service Daemon |
| `settingsd` | **`ON`** | Host Service Daemon |
| `vobd` | **`ON`** | Host Service Daemon |
| `vpxa` | **`ON`** | Host Service Daemon |
| `health` | **`ON`** | Host Service Daemon |
| `lwsmd` | **`ON`** | Host Service Daemon |
| `sfcbd-watchdog` | **`ON`** | Host Service Daemon |
| `wsman` | **`ON`** | Host Service Daemon |
| `snmpd` | **`ON`** | Host Service Daemon |
| `xorg` | **`ON`** | Host Service Daemon |
| `drivervm-init` | **`ON`** | Host Service Daemon |
| `gpuManager` | **`ON`** | Host Service Daemon |
| `vmtoolsd` | **`ON`** | Host Service Daemon |
| `vmsyslogd` | **`ON`** | Host Service Daemon |
| `lsud` | **`ON`** | Host Service Daemon |
| **FIPS 140 Cryptography** | `Disabled` | Kernel Cryptographic Integrity |
| **Software Acceptance Level** | `CommunitySupported` | VIB Installation Signature Policy |


## 6. Advanced Kernel & System Settings (Catalog)
The hypervisor configuration contains **829** total advanced options across all kernel subsystems.
**9** parameters have customized values differing from factory defaults.

### 6.1 Customized / Non-Default Options
| Parameter Path | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- |
| **`/Misc/HostName`** | `esxi-01.npcsolutions.co.za` | `localhost` | Host name |
| **`/Disk/AllowUsbClaimedAsSSD`** | `1` | `0` | Permit claim rules to mark USB disks as SSD |
| **`/Power/PerfBias`** | `16` | `17` | In Custom policy, Performance Energy Bias Hint, where 0-15 directly specifies preference on a scale where 0=MaxPerf and 15=MinPower, while 16-18 chooses an automatically determined value from a preset policy: 16=Low Power, 17=Balanced, 18=High Performance |
| **`/Power/CpuPolicy`** | `Low Power` | `Balanced` | Host power management policy: High Performance, Balanced, Low Power, or Custom |
| **`/UserVars/HostClientCEIPOptIn`** | `2` | `0` | Whether or not to opt-in for CEIP in Host Client, 0 for ask, 1 for yes, 2 for no |
| **`/UserVars/HostClientSessionTimeout`** | `0` | `900` | Default timeout for Host Client sessions in seconds |
| **`/UserVars/HostClientShowOnlyRecentObjects`** | `0` | `1` | Whether or not to show only recent objects in Host Client |
| **`/UserVars/SuppressHyperthreadWarning`** | `1` | `0` | Don't show warning for potential security vulnerability due to hyperthreading |
| **`/UserVars/SuppressShellWarning`** | `1` | `0` | Don't show warning for enabled local and remote shell access |


### 6.2 Key Subsystem Advanced Parameters Overview
<details><summary><strong>Subsystem: /CBRC (1 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/CBRC/DCacheMemReserved` | `integer` | `400` | `400` | Memory consumed by CBRC Data Cache (in MB) |

</details>

<details><summary><strong>Subsystem: /COW (4 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/COW/COWMaxHeapSizeMB` | `integer` | `192` | `192` | Maximum size (in MB) to which the COW heap is allowed to grow |
| `/COW/COWREPageCacheEviction` | `integer` | `1` | `1` | VMFSSparse metadata cache eviction: 0 - disabled, 1 enabled |
| `/COW/COWMaxREPageCacheszMB` | `integer` | `256` | `256` | Maximum size (in MB) of VMFSSparse metadata cache size before cache eviction kicks in |
| `/COW/COWMinREPageCacheszMB` | `integer` | `0` | `0` | Minimum size (in MB) of VMFSSparse metadata cache size. Valid when cache eviction enabled. |

</details>

<details><summary><strong>Subsystem: /Cpu (26 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Cpu/HostRebalancePeriod` | `integer` | `2000` | `2000` | average milliseconds between opportunities for a pcpu to migrate vcpus from within the whole system, 0 to disable |
| `/Cpu/PackageRebalancePeriod` | `integer` | `2000` | `2000` | average milliseconds between opportunities for a pcpu to migrate vcpus from within a package, 0 to disable |
| `/Cpu/L3RebalancePeriod` | `integer` | `20` | `20` | average milliseconds between opportunities for a pcpu to migrate vcpus from within the shared L3 cache, 0 to disable |
| `/Cpu/L2RebalancePeriod` | `integer` | `10` | `10` | average milliseconds between opportunities for a pcpu to migrate vcpus from within the shared L2 cache, 0 to disable |
| `/Cpu/HTRebalancePeriod` | `integer` | `5` | `5` | average milliseconds between opportunities for a pcpu to migrate vcpus from within a core |
| `/Cpu/FairnessRebalancePcpus` | `integer` | `4` | `4` | max number of PCPUs to be considered when doing fairness rebalance, 0 to disable |
| `/Cpu/WakeupMigrateIdlePcpus` | `integer` | `4` | `4` | max number of PCPUs to be considered when doing wakeup idle rebalance, 0 to disable |
| `/Cpu/PcpuMigrateIdlePcpus` | `integer` | `4` | `4` | max number of remote PCPUs to be considered when doing pcpu idle rebalance, 0 to disable |
| `/Cpu/CreditAgePeriod` | `integer` | `3000` | `3000` | period in milliseconds |
| `/Cpu/NonTimerWakeupRate` | `integer` | `500` | `500` | Disable P state if the running vcpu's non-timer wakeup rate is higher than this threshold, 0 to disable |
| `/Cpu/CommRateThreshold` | `integer` | `500` | `500` | threshold for inter-schedcontext rate above which the contexts are considered to be related (in num/sec), 0 to disable |
| `/Cpu/BoundLagQuanta` | `integer` | `8` | `8` | number of global quanta before bound lag |
| `/Cpu/HTWholeCoreThreshold` | `integer` | `800` | `800` | a vcpu with vtime falling behind by this threshold (in ms) is eligible to use the whole core (HT only), 0 to disable (may violate resource settings) |
| `/Cpu/HTStolenAgeThreshold` | `integer` | `8` | `8` | the amount of htStolen time a vcpu can keep without being aged (in seconds) |
| `/Cpu/Quantum` | `integer` | `200` | `200` | quantum in milliseconds |
| `/Cpu/UseMwait` | `integer` | `2` | `2` | use MWAIT vs. HLT in the idle loop; 0: use HLT, 1: use MWAIT if possible, 2: choose by cpu type, 3: spin (not recommended) |
| `/Cpu/CoschedCrossCall` | `integer` | `1` | `1` | 0: disable cosched on crosscall; 1: enable cosched on crosscall |
| `/Cpu/CoschedHandoffLLC` | `integer` | `1` | `1` | 0: handoff by switching pcpu; 1: handoff to LLC if possible |
| `/Cpu/CoschedPollUsec` | `integer` | `1000` | `1000` | interval between coscheduling skew checks, in usec |
| `/Cpu/CoschedCostartThreshold` | `integer` | `2000` | `2000` | costart threshold in usec, costart threshold should be less than costopThreshold |
| `/Cpu/CoschedCostopThreshold` | `integer` | `3000` | `3000` | maximum skew between vcpus in usec, 0 to disable |
| `/Cpu/CoschedHandoffSkip` | `integer` | `10` | `10` | only skip handoff if ready time is smaller than this threshold, in usec, 0 to allow skip always |
| `/Cpu/VMAdmitCheckPerVcpuMin` | `integer` | `1` | `1` | Check per-vcpu cpu reservation does not exceed the speed of a single physical  cpu. [0:disabled, 1: enabled] |
| `/Cpu/MaxSampleRateLg` | `integer` | `7` | `7` | Sampling system services at most (2^MaxSampleRateLg) times a second |
| `/Cpu/AllowWideVsmp` | `integer` | `0` | `0` | Allow VMs with more VCPUs than host PCPUs, 0 to disable |
| `/Cpu/LimitEnforcementThreshold` | `integer` | `200` | `200` | Only allows low-vtime children ro run when a group/VM's vtimeLimit is smaller than the global virtual time by less than this threshold (in ms), 0 to disable |

</details>

<details><summary><strong>Subsystem: /DataMover (3 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/DataMover/HardwareAcceleratedMove` | `integer` | `1` | `1` | Enable hardware accelerated VMFS data movement (requires compliant hardware) |
| `/DataMover/HardwareAcceleratedInit` | `integer` | `1` | `1` | Enable hardware accelerated VMFS data initialization (requires compliant hardware) |
| `/DataMover/MaxHeapSize` | `integer` | `64` | `64` | Maximum size of the heap in MB used for data movement |

</details>

<details><summary><strong>Subsystem: /Digest (3 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Digest/AlgoType` | `integer` | `1` | `1` | Digest Crypto Hash Type (1=SHA-1, 2=SHA-256). |
| `/Digest/BlockSize` | `integer` | `1` | `1` | Blocksize in the original VMDK to compute crypto hash codes. In pages of 4K size. Value needs to be power of 2. |
| `/Digest/CollisionEnabled` | `integer` | `0` | `0` | Enable collision detection (0=disabled, 1=enabled) |

</details>

<details><summary><strong>Subsystem: /DirentryCache (1 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/DirentryCache/MaxDentryPerObj` | `integer` | `15000` | `15000` | Maximum directory entries cached per directory |

</details>

<details><summary><strong>Subsystem: /Disk (66 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Disk/SharesNormal` | `integer` | `1000` | `1000` | shares for normal/default disk priority |
| `/Disk/SharesHigh` | `integer` | `2000` | `2000` | shares for high disk priority |
| `/Disk/SharesLow` | `integer` | `500` | `500` | shares for low disk priority |
| `/Disk/BandwidthCap` | `integer` | `4294967294` | `4294967294` | cap on disk bandwidth (KB/s) usage |
| `/Disk/ThroughputCap` | `integer` | `4294967294` | `4294967294` | cap on disk throughput (IO/s) usage |
| `/Disk/SectorMaxDiff` | `integer` | `2000` | `2000` | Distance in sectors at which disk BW sched affinity stops |
| `/Disk/SchedQuantum` | `integer` | `8` | `8` | Number of consecutive requests from one World |
| `/Disk/IdleCredit` | `integer` | `32` | `32` | Amount of idle credit that a VM can gain for IO requests |
| `/Disk/SchedulerWithReservation` | `integer` | `1` | `1` | Disk IO scheduler (0:default 1:mclock) |
| `/Disk/SchedQPriorityPercentage` | `integer` | `80` | `80` | Percentage of priority commands to serve from priority queue |
| `/Disk/SchedQControlSeqReqs` | `integer` | `128` | `128` | Number of consecutive requests from a VM required to raise the outstanding commands to max |
| `/Disk/SchedQControlVMSwitches` | `integer` | `6` | `6` | Number of switches between commands issued by different VMs required to reduce outstanding commands to SchedNumReqOutstanding |
| `/Disk/MaxLUN` | `integer` | `1024` | `1024` | Maximum LUN id (N+1) that is scanned on a SCSI target |
| `/Disk/SupportSparseLUN` | `integer` | `1` | `1` | Support for sparse LUNs if set to one |
| `/Disk/UseReportLUN` | `integer` | `1` | `1` | Use the REPORT LUN command to speed up scanning for devices |
| `/Disk/UseDeviceReset` | `integer` | `1` | `1` | Use device reset (instead of bus reset) to reset a SCSI device |
| `/Disk/UseLunReset` | `integer` | `1` | `1` | Use LUN reset (instead of device/bus reset) to reset a SCSI device |
| `/Disk/RetryUnitAttention` | `integer` | `1` | `1` | Retry all SCSI commands that return a unit attention error |
| `/Disk/PathEvalTime` | `integer` | `300` | `300` | The number of seconds between storage path evaluations |
| `/Disk/DeviceReclaimTime` | `integer` | `300` | `300` | The number of seconds between device re-claim attempts |
| `/Disk/EnableNaviReg` | `integer` | `1` | `1` | Enable automatic NaviAgent registration with EMC CLARiiON and Invista |
| `/Disk/DelayOnBusy` | `integer` | `400` | `400` | Delay in milliseconds for completion of commands with a BUSY status |
| `/Disk/ResetLatency` | `integer` | `1000` | `1000` | Delay in milliseconds between reset thread wake-ups |
| `/Disk/MaxResetLatency` | `integer` | `2000` | `2000` | Delay in milliseconds before logging warnings and spawning new reset worlds if a reset is overdue or taking too long |
| `/Disk/DeviceEnableIOLatencyMsgs` | `integer` | `0` | `0` | Enable or disable storage latency-related error messages from PSA |
| `/Disk/ResetPeriod` | `integer` | `30` | `30` | Delay in seconds between bus resets retries |
| `/Disk/ResetMaxRetries` | `integer` | `0` | `0` | Max number of bus reset retries (0=infinite) |
| `/Disk/ResetThreadMin` | `integer` | `1` | `1` | Min number of reset handler threads |
| `/Disk/ResetThreadMax` | `integer` | `16` | `16` | Max number of reset handler threads |
| `/Disk/ResetThreadExpires` | `integer` | `1800` | `1800` | Life in seconds of an inactive reset handle thread |
| `/Disk/ResetOverdueLogPeriod` | `integer` | `60` | `60` | Delay in seconds between logs of overdue reset |
| `/Disk/SkipResetNoCIF` | `integer` | `1` | `1` | Do not send Device/Virt RESET if No Cmds in Flight |
| `/Disk/PreventVMFSOverwrite` | `integer` | `1` | `1` | Prevent overwriting VMFS partitions |
| `/Disk/DumpMaxRetries` | `integer` | `10` | `10` | Max number of I/O retries during disk dump |
| `/Disk/DumpPollMaxRetries` | `integer` | `10000` | `10000` | Max number of device poll retries during disk dump |
| `/Disk/DumpPollDelay` | `integer` | `1000` | `1000` | Number of microseconds to wait between polls during a disk dump. |
| `/Disk/DiskMaxIOSize` | `integer` | `32767` | `32767` | Max Disk READ/WRITE I/O size before splitting (in KB) |
| `/Disk/QFullSampleSize` | `integer` | `0` | `0` | Default I/O samples to monitor for detecting non-transient queue full condition. Should be nonzero to enable queue depth throttling. Device specific QFull options will take precedence over this value if set. |
| `/Disk/QFullThreshold` | `integer` | `8` | `8` | Default BUSY or QFULL threshold, upon which LUN queue depth will be throttled. Should be <= QFullSampleSize if throttling is enabled. Device specific QFull options will take precedence over this value if set. |
| `/Disk/DiskRetryPeriod` | `integer` | `2000` | `2000` | Retry period in milliseconds for a command with retry status |
| `/Disk/VSCSIOptimalTransLen` | `integer` | `0` | `0` | optimal transfer length in blocks for VSCSI. |
| `/Disk/VSCSIMaxTransLen` | `integer` | `0` | `0` | Max transfer length in blocks for VSCSI. |
| `/Disk/VSCSIDisableNvmeRetry` | `integer` | `1` | `1` | Disable vNVME Retries in VSCSI. |
| `/Disk/DiskReservationThreshold` | `integer` | `45` | `45` | Time window within which refcounted reservations on a device are permitted (in msec) |
| `/Disk/DiskDelayPDLHelper` | `integer` | `10` | `10` | Delay PDL helper in secs |
| `/Disk/ReqCallThreshold` | `integer` | `8` | `8` | Threshold in number of pending requests before calling into vmkernel to process the requests |
| `/Disk/ReturnCCForNoSpace` | `integer` | `0` | `0` | Return CC 0x7/0x27/0x7 in the event where a backing datastore has run out of space as opposed to posting a monitor event to halt the VM |
| `/Disk/AutoremoveOnPDL` | `integer` | `1` | `1` | Autoremove paths to a disk that is in PDL (Permanent Device Loss) |
| `/Disk/VSCSIPollPeriod` | `integer` | `1000` | `1000` | Period in microseconds to poll the vHBAs' queues |
| `/Disk/VSCSIHaltPollInterval` | `integer` | `5` | `5` | Period in microseconds to poll the vHBAs' queues when vCPU halts (too low waste CPU cycles, but may improve VM IO latency slightly on super fast storage) |
| `/Disk/VSCSICoalesceCount` | `integer` | `1000` | `1000` | Frequeuncy with which coalesce callback is called |
| `/Disk/VSCSIResvCmdRetryInSecs` | `integer` | `1` | `1` | Time (in secs) to retry on transient errors for Reservation commands for MSCS CAB configs. |
| `/Disk/VSCSIWriteSameBurstSize` | `integer` | `4` | `4` | Max number of split IOs per write same request. |
| `/Disk/ApdTokenRetryCount` | `integer` | `25` | `25` | APD Token Retry Count |
| `/Disk/UseIoPool` | `integer` | `0` | `0` | Enable PSA deferred work pools (a bitmask: 0x1 - adapter submission pool, 0x2 - device completion pool, 0x4 - device queueing pool). |
| `/Disk/NmpMaxCmdExtension` | `integer` | `0` | `0` | Increase the maximum number of commands to be processed at once in NMP |
| `/Disk/AllowUsbClaimedAsSSD` | `integer` | `1` | `0` | Permit claim rules to mark USB disks as SSD |
| `/Disk/SchedCostUnit` | `integer` | `32768` | `32768` | IO Scheduler block Size for accounting |
| `/Disk/SchedReservationBurst` | `integer` | `1` | `1` | Permit I/O bursts in mclock scheduler with reservations. |
| `/Disk/FastPathRestoreInterval` | `integer` | `100` | `100` | Time interval (in msec) when IO latency is monitored to evaluate enabling fast path in PSA |
| `/Disk/SchedQCleanupInterval` | `integer` | `300` | `300` | Time interval (in secs) to cleanup per device unused schedQ list (default = 5 minutes). |
| `/Disk/Disable4knSSD` | `integer` | `1` | `1` | Disable use of 4kn SSDs |
| `/Disk/MaxNumIOIntervals` | `integer` | `1024` | `1024` | Maximum number of IO intervals per device that can be stored in order to detect overlapping IOs to 4Kn disks |
| `/Disk/PVSCSIEnablePreemption` | `integer` | `1` | `1` | Enable PVSCSI Preemption. |
| `/Disk/FailDiskRegistration` | `integer` | `1` | `1` | Fail device registration if disk has only standby paths and supports only implicit asymmetric logical unit access. |
| `/Disk/SllThrottleTime` | `integer` | `800` | `800` | Time (in msecs) I/Os to SLLs will be throttled in the event of a TASK_SET_FULL being received. |

</details>

<details><summary><strong>Subsystem: /FSS (1 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/FSS/FSSLightWeightProbe` | `integer` | `1` | `1` | Enable light-weight efficient probe of ESX supported datastores |

</details>

<details><summary><strong>Subsystem: /FT (31 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/FT/BindToVmknic` | `integer` | `0` | `0` | Bind the FT socket to a specific vmknic |
| `/FT/FTCptConcurrentSend` | `integer` | `1` | `1` | Send non-diff pages in parallel with diffing rather than after |
| `/FT/FTCptDiffThreads` | `integer` | `6` | `6` | Number of threads for diffing pages |
| `/FT/FTCptPagePolicy` | `integer` | `65538` | `65538` | Page placement policy for side data.  < 2^16: Use a specific node mask, 0x10000: Put pages anywhere, 0x10001: Match nodes with VM, 0x10002: Avoid matching nodes with VM |
| `/FT/FTCptNumaIndex` | `integer` | `0` | `0` | Index dirty pages by NUMA node.  Workers will use the index to prefer local work. |
| `/FT/FTCptStartTimeout` | `integer` | `90000` | `90000` | Time in milliseconds for the primary to wait for the FT connection from the secondary |
| `/FT/FTCptThreadPolicy` | `integer` | `65536` | `65536` | Policy for placing helper threads.  < 2^16: Use a fixed NUMA node mask, 0x10000: Put threads anywhere, 0x10001: Match threads to a dynamic node index |
| `/FT/FTCptLogTimeout` | `integer` | `8000` | `8000` | Time in milliseconds to wait for FT log entries (read or write) |
| `/FT/FTCptDiskWriteTimeout` | `integer` | `3000` | `3000` | Time in milliseconds for backup site to wait for a disk IO to complete |
| `/FT/FTCptMinInterval` | `integer` | `4` | `4` | Time in milliseconds to wait between two forced checkpoints |
| `/FT/FTCptStatsInterval` | `integer` | `30` | `30` | If nonzero, force a flush of the kernel stats buffer in this many seconds |
| `/FT/FTCptMaxPktsDelay` | `integer` | `0` | `0` | Max number of packets in the delayed queue before forcing a checkpoint |
| `/FT/FTCptVcpuMinUsage` | `integer` | `40` | `40` | VCPU usage in percentage below which the VM will be considered for forced checkpoint |
| `/FT/FTCptPoweroff` | `integer` | `0` | `0` | Poweroff the primary: If set to 1, primary is powered off after the next checkpoint, if set to 2, primary is powered off if/when there are any outstanding IOs in flight |
| `/FT/FTCptSndBufSize` | `integer` | `562140` | `562140` | TCP send buffer size for the primary |
| `/FT/FTCptRcvBufSize` | `integer` | `562140` | `562140` | TCP receive buffer size for the backup |
| `/FT/FTCptDontSendPages` | `integer` | `0` | `0` | Don't send over modified pages - for testing only |
| `/FT/FTCptDontDelayPkts` | `integer` | `0` | `0` | Don't delay network packets - for testing only |
| `/FT/FTCptWaitOnSocket` | `integer` | `1` | `1` | Wait when socket is empty |
| `/FT/FTCptDelayCheckpoint` | `integer` | `2` | `2` | Delay checkpoint if no network packet waiting |
| `/FT/FTCptDiffCap` | `integer` | `100` | `100` | Max percent pages via diffs (EXPERIMENTAL, failover will not work if not 100) |
| `/FT/FTCptDisableFailover` | `integer` | `0` | `0` | Disable failovers (testing only) |
| `/FT/FTCptNumConnections` | `integer` | `2` | `2` | # of data connections to use for page sending |
| `/FT/FTCptNetDelayNoCpt` | `integer` | `0` | `0` | Delay to impose on VM network output in ms |
| `/FT/FTCptEpochSample` | `integer` | `1000` | `1000` | Single epoch sampling time in ms |
| `/FT/FTCptEpochWait` | `integer` | `8000` | `8000` | Wait in ms after epoch sampling |
| `/FT/FTCptIORetryTimes` | `integer` | `15` | `15` | Maximum retries on disk I/O error |
| `/FT/FTCptIORetryInterval` | `integer` | `10` | `10` | Sleep interval (in ms) between retries on disk I/O error |
| `/FT/FTCptIORetryExtraInterval` | `integer` | `200` | `200` | Extra sleep interval (in ms) between retries on disk I/O error |
| `/FT/Vmknic` | `string` | `` | `` | Vmknic for FT vmkernel VNIC |
| `/FT/FTCptEpochList` | `string` | `5,10,20,100` | `5,10,20,100` | List of potential epochs to try in order of increasing value |

</details>

<details><summary><strong>Subsystem: /HBR (72 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/HBR/HbrStaticHeapMinBaseMB` | `integer` | `1` | `1` | A base value in MB for the minimum size of the active heap. |
| `/HBR/HbrStaticHeapMaxBaseMB` | `integer` | `726` | `726` | A base value in MB for the maximum size of the active heap. |
| `/HBR/HbrRuntimeHeapMinBaseMB` | `integer` | `1` | `1` | A base value in MB for the minimum size of the initial heap. |
| `/HBR/HbrRuntimeHeapMaxBaseMB` | `integer` | `1` | `1` | A base value in MB for the maximum size of the initial heap. |
| `/HBR/HbrBitmapAllocTimeoutMS` | `integer` | `3000` | `3000` | A timeout in MS for how long we will wait to allocate a bitmap. |
| `/HBR/HbrBitmapVMMaxStorageGB` | `integer` | `65536` | `65536` | An estimation of the maximum storage allocated per VM in gigabytes. |
| `/HBR/HbrResourceHeapSizeMB` | `integer` | `3` | `3` | A base value in MB for the size of the resource heap. |
| `/HBR/HbrResourceHeapPerVMSizeKB` | `integer` | `128` | `128` | The additional amount of memory in KB per supported VM to add to the resource heap size. |
| `/HBR/HbrResourceHeapUtilization` | `integer` | `95` | `95` | Expected usable percentage of the resource heap (minus overheads, fragmentation). |
| `/HBR/HbrResourceMaxDiskContexts` | `integer` | `64` | `64` | The maximum number of resource contexts allowed in disk phase for all VMs. |
| `/HBR/HbrResourceMaxCompletionContexts` | `integer` | `8192` | `8192` | The maximum number of resource contexts allowed in completion phase for all VMs. |
| `/HBR/HbrDemandLogIOPerVM` | `integer` | `64` | `64` | Number of concurrent demand log copies per VM. |
| `/HBR/OpportunisticBlockListSize` | `integer` | `4000` | `4000` | Number of blocks to keep around in a LRU list for opportunistic replication. |
| `/HBR/TransferFileExtentSize` | `integer` | `8192` | `8192` | Chunk size for config file transfers. |
| `/HBR/CopySnapDiskMaxExtentCount` | `integer` | `16` | `16` | Number of extents for a single snapshot disk that can be copied in parallel. |
| `/HBR/DisconnectedEventDelayMs` | `integer` | `60000` | `60000` | Time to wait (while attempting reconnection) before posting a 'no connection to HBR server' event. |
| `/HBR/ProgressReportIntervalMs` | `integer` | `5000` | `5000` | Interval between per-disk progress updates to hostd. |
| `/HBR/WireChecksum` | `integer` | `1` | `1` | Use wire checksums. |
| `/HBR/UnmapOptimization` | `integer` | `0` | `0` | Use optimizations for SCSI Unmap. |
| `/HBR/HelperQueueMaxRequests` | `integer` | `8192` | `8192` | Maximum number of helper requests the helper queue can support. |
| `/HBR/HelperQueueMaxWorlds` | `integer` | `8` | `8` | Maximum number of world processing helper queue requests. |
| `/HBR/ReconnectFailureDelaySecs` | `integer` | `10` | `10` | Additional delay in seconds added per reconnection failure for a session. |
| `/HBR/ReconnectMaxDelaySecs` | `integer` | `90` | `90` | Maximum delay in seconds between reconnection attempts for a session. |
| `/HBR/RetryMinDelaySecs` | `integer` | `1` | `1` | Minimum server request retry delay in seconds (for non-fatal errors). |
| `/HBR/RetryMaxDelaySecs` | `integer` | `5` | `5` | Maximum server request retry delay in seconds (for non-fatal errors). |
| `/HBR/DemandlogReadRetries` | `integer` | `20` | `20` | Number of times we retry an internal read (for the demand log) before aborting the delta. |
| `/HBR/DemandlogWriteRetries` | `integer` | `20` | `20` | Number of times we retry a demand log write before aborting the delta. |
| `/HBR/DemandlogRetryDelayMs` | `integer` | `10` | `10` | Delay in milliseconds for retrying a demand log write. |
| `/HBR/DemandlogExtentHashBuckets` | `integer` | `16384` | `16384` | Number of hash buckets to use to track extents that haven't been read. |
| `/HBR/ResourceServerHashBuckets` | `integer` | `8` | `8` | Number of hash buckets to use to track remote HBR servers. |
| `/HBR/NetworkerRecvHashBuckets` | `integer` | `64` | `64` | Number of hash buckets to use to track commands waiting to receive a response. |
| `/HBR/DemandlogCompletedHashBuckets` | `integer` | `16384` | `16384` | Number of hash buckets to use to track extents that have been written to the demand log. |
| `/HBR/HbrMaxUnmapsInFlight` | `integer` | `128` | `128` | Maximum expected number of SCSI UNMAP commands in flight on a single disk. |
| `/HBR/HbrMaxUnmapExtents` | `integer` | `10` | `10` | Maximum expected number of extents for SCSI UNMAP commands. |
| `/HBR/MigrateFlushTimerSecs` | `integer` | `3` | `3` | Time between attempt to flush the state to the persistent file during migration. |
| `/HBR/SyncTransferRetrySleepSecs` | `integer` | `5` | `5` | Time in seconds to wait after a failure before retrying a sync operation. |
| `/HBR/XferBitmapCheckIntervalSecs` | `integer` | `1` | `1` | Time in seconds to wait before checking the transfer bitmap for availability of dirty blocks. |
| `/HBR/CopySnapFidHashBuckets` | `integer` | `256` | `256` | Number of hash buckets to use to track the snapshot disks open to copy to demand log. |
| `/HBR/DemandlogIoTimeoutSecs` | `integer` | `120` | `120` | Timeout for IOs for demand log operations. |
| `/HBR/LocalReadIoTimeoutSecs` | `integer` | `120` | `120` | Timeout for IOs for dce local reads. |
| `/HBR/PsfIoTimeoutSecs` | `integer` | `300` | `300` | Timeout for IOs for persistent state file/demand log metadata. |
| `/HBR/ChecksumUseChecksumInfo` | `integer` | `1` | `1` | Use disk checksum info to help speed up transfering valid blocks of data. |
| `/HBR/ChecksumRegionSize` | `integer` | `256` | `256` | Size in blocks of one checksum region, corresponding to one network request. |
| `/HBR/ChecksumZoneSize` | `integer` | `32768` | `32768` | Size in regions of one checksum zone for which allocation information will be cached. |
| `/HBR/ChecksumIoSize` | `integer` | `8` | `8` | Size in blocks of a checksum read I/O. |
| `/HBR/ChecksumMaxIo` | `integer` | `8` | `8` | Maximum number of I/O chunks read in parallel for checksum. |
| `/HBR/ChecksumPerSlice` | `integer` | `2` | `2` | Maximum number of I/O chunks read in each slice for checksum. |
| `/HBR/ChecksumUseAllocInfo` | `integer` | `1` | `1` | Use disk allocation info to help speed up checksumming. |
| `/HBR/TransferDiskPerSlice` | `integer` | `16` | `16` | Maximum number of blocks that will be read in each slice. |
| `/HBR/TransferDiskMaxIo` | `integer` | `32` | `32` | Maximum number of blocks that will be read in parallel. |
| `/HBR/TransferDiskMaxNetwork` | `integer` | `2048` | `2048` | Maximum number of blocks that will be transferred in parallel. |
| `/HBR/TransferDiskMaxCompletion` | `integer` | `0` | `0` | Maximum number of blocks that are allowed in completion phase per disk. |
| `/HBR/TransferMaxContExtents` | `integer` | `16` | `16` | Maximum number of contiguous extents that will be coalesced into a single update. |
| `/HBR/DemandlogTransferIoSize` | `integer` | `8` | `8` | Size in blocks of a demandlog transfer read I/O. |
| `/HBR/DemandlogTransferMaxIo` | `integer` | `32` | `32` | Maximum number of demandlog transfer I/O chunks issued in parallel. |
| `/HBR/DemandlogTransferMaxNetwork` | `integer` | `256` | `256` | Maximum number of demandlog chunks transferred in parallel. |
| `/HBR/DemandlogTransferMaxCompletion` | `integer` | `0` | `0` | Maximum number of demandlog chunks that are allowed in completion phase per disk. |
| `/HBR/DemandlogTransferPerSlice` | `integer` | `16` | `16` | Maximum number of demandlog transfer I/O chunks issued per slice. |
| `/HBR/NetworkUseCubic` | `integer` | `1` | `1` | Use the cubic TCP congestion algorithm for HBR sockets. |
| `/HBR/ErrThrottleDceRead` | `integer` | `1` | `1` | Throttle DCE Read errors. |
| `/HBR/ErrThrottleChecksumIO` | `integer` | `1` | `1` | Throttle Checksum I/O errors. |
| `/HBR/HbrMinExtentBreakGB` | `integer` | `2048` | `2048` | Disks with capacity under this number of gigabytes will have the min extent size. |
| `/HBR/HbrMinExtentSizeKB` | `integer` | `8` | `8` | Minimum extent size used for disks in kilobytes. |
| `/HBR/HbrLowerExtentBreakGB` | `integer` | `8192` | `8192` | Disks with capacity between the min extent break and this number of gigabytes will have the lower extent size. |
| `/HBR/HbrLowerExtentSizeKB` | `integer` | `16` | `16` | Lower extent size used for disks in kilobytes. |
| `/HBR/HbrUpperExtentBreakGB` | `integer` | `32768` | `32768` | Disks with capacity between the lower extent break and this number of gigabytes will have the upper extent size. |
| `/HBR/HbrUpperExtentSizeKB` | `integer` | `32` | `32` | Upper extent size used for disks in kilobytes. |
| `/HBR/HbrMaxExtentSizeKB` | `integer` | `64` | `64` | Maximum extent size in kilobytes. Used for disks with capacity over the upper extent break. |
| `/HBR/HbrMaxGuestXferWhileDeltaMB` | `integer` | `1024` | `1024` | Maximum single SCSI command transfer size (in megabytes) that will be tolerated while a delta is taking place. |
| `/HBR/HbrOptimizeFullSync` | `integer` | `1` | `1` | Skip transfer of changed blocks during full sync to avoid sending them twice between the full sync and the subsequent delta. |
| `/HBR/HbrThrottleGenericErrResetTime` | `integer` | `16384` | `16384` | Time in MS between the last logged generic HBR error and the throttle reset. |
| `/HBR/HbrMaxUpdateSizeKB` | `integer` | `128` | `128` | Maximum size of a single network update in kilobytes. |

</details>

<details><summary><strong>Subsystem: /Hpp (1 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Hpp/HppPReservationCmdRetryTime` | `integer` | `1` | `1` | Time (in secs) to retry on transient errors for Persistent reservation commands for MSCS CAB configs |

</details>

<details><summary><strong>Subsystem: /ISCSI (4 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/ISCSI/MaxIoSizeKB` | `integer` | `128` | `128` | Maximum Software iSCSI I/O size (in KB) (REQUIRES REBOOT!) |
| `/ISCSI/CloseIscsiConnOnTaskMgmtFailure` | `integer` | `1` | `1` | Close iSCSI connection on task management failure |
| `/ISCSI/SocketRcvBufLenKB` | `integer` | `256` | `256` | Socket receive buffer length (in KB) for iSCSI connections |
| `/ISCSI/SocketSndBufLenKB` | `integer` | `600` | `600` | Socket send buffer length (in KB) for iSCSI connections |

</details>

<details><summary><strong>Subsystem: /Irq (6 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Irq/BestVcpuRouting` | `integer` | `0` | `0` | 1: try to route the virtual interrupt to the best vcpu; 0 to disable |
| `/Irq/IRQRebalancePeriod` | `integer` | `50` | `50` | time in ms between attempts to rebalance interrupts |
| `/Irq/IRQBHConflictWeight` | `integer` | `5` | `5` | relative weight for irq/BH conflict |
| `/Irq/IRQVcpuConflictWeight` | `integer` | `3` | `3` | relative weight for irq/vcpu conflict |
| `/Irq/IRQActionAffinityWeight` | `integer` | `5` | `5` | relative weight for action-vcpu affinity |
| `/Irq/IRQAvoidExclusive` | `integer` | `1` | `1` | avoid placing interrupts on physical CPUs with exclusive affinity set |

</details>

<details><summary><strong>Subsystem: /LPage (6 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/LPage/LPageDefragEnable` | `integer` | `1` | `1` | Enable large page defragmentation |
| `/LPage/LPageMarkLowNodes` | `integer` | `1` | `1` | Enable marking of nodes with low large pages free |
| `/LPage/LPageAlwaysTryForNPT` | `integer` | `1` | `1` | Enable always try to alloc large page for NPT |
| `/LPage/MaxSharedPages` | `integer` | `510` | `510` | Maximum number of shared pages in a 2MB region that may be broken to back the region with a large page |
| `/LPage/MaxSwappedPagesInitVal` | `integer` | `10` | `10` | Initial value for maximum number of swapped pages in a 2MB region that may be read to back the region with a large page |
| `/LPage/freePagesThresholdForRemote` | `integer` | `2048` | `2048` | Maximum number of free small pages on local nodes to allow remote lpages |

</details>

<details><summary><strong>Subsystem: /LSOM (9 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/LSOM/lsomSlowTier1DeviceUnmount` | `integer` | `0` | `0` | Whether to auto-unmount un-healthy (pervasively slow) tier 1 devices |
| `/LSOM/blkAttrCacheSizePercent` | `integer` | `0` | `0` | BlkAttr cache size percent growth rate with peak value (100%) caching almost all blkattrs for the diskgroup |
| `/LSOM/lsomPlogEnableDeadmanTimer` | `integer` | `2` | `2` | Config option to act if an I/O is stuck for a long time. (0:No Action 1:PSOD 2:Disk offline) |
| `/LSOM/lsomEnableFullRebuildAvoidance` | `integer` | `1` | `1` | Enable LSOM full rebuild avoidance for transient IO errors. (0:disabled 1:enabled) |
| `/LSOM/lsomDeviceNeedsRepairCount` | `integer` | `3` | `3` | Threshold beyond which a transient error on a device will be categorized as permanent error. |
| `/LSOM/lsomEnableRebuildOnLSE` | `integer` | `1` | `1` | Enable Auto rebuild of disk/DG on detecting LSE errors |
| `/LSOM/lsomRebuildOnEvacFailure` | `integer` | `0` | `0` | Auto rebuild the disk/DG even if evacuation failed during URE handling |
| `/LSOM/enableLargeWb` | `integer` | `0` | `0` | Enable support for large write buffer for new disk groups |
| `/LSOM/lsomEnhancedLatencyHandlingSupport` | `integer` | `0` | `0` | Enable latency handling optimizations in DDH |

</details>

<details><summary><strong>Subsystem: /LoadESX (1 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/LoadESX/generateLiveDump` | `integer` | `0` | `0` | Create a live dump if a Quick Boot attempt fails. |

</details>

<details><summary><strong>Subsystem: /Mem (21 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Mem/TierNvmePct` | `integer` | `25` | `25` | NVMe size for memtiering (in percentage of DRAM) |
| `/Mem/IdleTax` | `integer` | `75` | `75` | idle memory tax rate |
| `/Mem/IdleTaxType` | `integer` | `1` | `1` | idle tax type. 0=flat, 1=variable |
| `/Mem/SampleActivePctMin` | `integer` | `1` | `1` | lower bound for sampled active memory |
| `/Mem/SampleDirtiedPctMin` | `integer` | `0` | `0` | lower bound for sampled active dirtied memory |
| `/Mem/ShareScanGHz` | `integer` | `4` | `4` | max page scan rate in MB/sec per GHz of host CPU, 0 to disable |
| `/Mem/ShareScanTime` | `integer` | `60` | `60` | desired time in minutes to scan entire VM |
| `/Mem/ShareRateMax` | `integer` | `1024` | `1024` | per-VM upper limit on pshare scan rate in pages/sec. (0 to disable) |
| `/Mem/ShareForceSalting` | `integer` | `2` | `2` | PShare salting allows for sharing isolation between multiple VMs and is controlled by the VMX option sched.mem.pshare.salt. Two VMs sharing the same salt will be able to share memory through PShare. This option controls how this VMX option will be used: 0: no salting or isolation between VMs, 1: the value of sched.mem.pshare.salt is honored, 2: each VM will get its own salt unless the sched.mem.pshare.salt is option is non-empty. |
| `/Mem/CtlMaxPercent` | `integer` | `65` | `65` | vmmemctl limit as percentage of VM max size |
| `/Mem/AllocGuestLargePage` | `integer` | `1` | `1` | Enable large page backing of guest memory |
| `/Mem/ShareCOSBufSize` | `integer` | `5` | `5` | Specify number of MPNs to be used by COW P2M buffer |
| `/Mem/VMOverheadGrowthLimit` | `integer` | `4294967295` | `4294967295` | Default limit (in MB) on VM overhead memory growth. Valid values are 0 to maximum memory supported, and 0xffffffff which means "unlimited". |
| `/Mem/MemZipEnable` | `integer` | `1` | `1` | Enable the memory compression cache |
| `/Mem/MemZipMaxPct` | `integer` | `10` | `10` | Sets the maximum target size for the compression cache as a percentage of VM size |
| `/Mem/MemZipMaxAllocPct` | `integer` | `50` | `50` | Sets the maximum size for the compression cache as a percentage of allocated VM memory size |
| `/Mem/MemMinFreePct` | `integer` | `0` | `0` | Percentage of host memory to reserve for accelerating memory allocations when free memory is low, 0 for automatic |
| `/Mem/MemDefragClientsPerDir` | `integer` | `2` | `2` | Clients that are allowed to defrags per directory. |
| `/Mem/MemEagerZero` | `integer` | `0` | `0` | Zero out userworld and guest memory pages immediately after free |
| `/Mem/MemCBTBitmapMaxAlloc` | `integer` | `1024` | `1024` | Maximum memory in MB to allocate for CBT bitmaps. |
| `/Mem/MemMaxResvThreshold` | `integer` | `16384` | `16384` | Max reservation threashold to define the memory health |

</details>

<details><summary><strong>Subsystem: /Migrate (41 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Migrate/Enabled` | `integer` | `1` | `1` | Enable hot migration support |
| `/Migrate/TryToUseDefaultHeap` | `integer` | `1` | `1` | Attempt use the default migration heap when beginning new migrations |
| `/Migrate/VASpaceReserveCount` | `integer` | `64` | `64` | Number of migrations to reserve virtual address space for at module load time |
| `/Migrate/VASpaceReserveSize` | `integer` | `4096` | `4096` | Megabytes of virtual address space to reserve per migration at module load time |
| `/Migrate/PreCopySwitchoverTimeGoal` | `integer` | `500` | `500` | Goal time in milliseconds to send changed pages after pre-copy completes |
| `/Migrate/PreCopyMinProgressPerc` | `integer` | `130` | `130` | Minimum allowed transmit to dirty page ratio per pre-copy iteration |
| `/Migrate/PreCopyPagesPerSend` | `integer` | `32` | `32` | Maximum number of pages to send per precopy transmit |
| `/Migrate/OutstandingReadKBMax` | `integer` | `128` | `128` | Maximum socket-backed mbuf bytes vMotion will allow to be outstanding while drained concurrently with reads, 0 for unlimited |
| `/Migrate/VMotionStreamHelpers` | `integer` | `0` | `0` | Number of helpers to allocate for VMotion streams, 0 to dynamically allocate based on uplink bandwidth |
| `/Migrate/VMotionMaxStreamHelpers` | `integer` | `112` | `112` | Maximum number of helpers to allocate for VMotion streams when using Autoscale |
| `/Migrate/VMotionLatencySensitivity` | `integer` | `1` | `1` | Make vMotion helper worlds latency sensitive, avoid transmit delays. |
| `/Migrate/VMotionResolveSwapType` | `integer` | `1` | `1` | Attempt to resolve swap type during VMotion initialization |
| `/Migrate/CptCacheMaxSizeMB` | `integer` | `544` | `544` | Maximum checkpoint cache size in MB |
| `/Migrate/SdpsEnabled` | `integer` | `2` | `2` | Stuns VMotion source in small increments during precopy, 0=disabled, 1=always enabled, 2=dynamic |
| `/Migrate/SdpsTargetRate` | `integer` | `500` | `500` | Percent by which transmit should be made to exceed dirty |
| `/Migrate/SdpsDynamicDelaySec` | `integer` | `30` | `30` | Delay, in seconds, between polling when considering enabling SDPS in the first preCopy iteration. |
| `/Migrate/PreCopyCountDelay` | `integer` | `10` | `10` | Delay preCopy next action every n action posts |
| `/Migrate/DetectZeroPages` | `integer` | `1` | `1` | Whether vMotion should detect zero pages during page transmission |
| `/Migrate/PreallocLPages` | `integer` | `1` | `1` | Attempt to prealloc destination pages via large page allocation |
| `/Migrate/ProhibitInstantClone` | `integer` | `0` | `0` | Prohibit instant clone from a VM |
| `/Migrate/TcpTsoDeferTx` | `integer` | `0` | `0` | Use TCP tso defer optimization for transmit |
| `/Migrate/LowBandwidthSysAlertThreshold` | `integer` | `0` | `0` | Threshold in KB/s for VMotion bandwidth below which a SysAlert is triggered |
| `/Migrate/NetTimeout` | `integer` | `20` | `20` | Timeout in seconds for migration network operations |
| `/Migrate/NfcNetTimeout` | `integer` | `60` | `60` | Timeout in seconds for NFC migration network operations |
| `/Migrate/NetExpectedLineRateMBps` | `integer` | `133` | `133` | Expected network throughput, in MBps, for bandwidth-delay calculation |
| `/Migrate/NetLatencyModeThreshold` | `integer` | `4` | `4` | Lowest possible round-trip time, in ms, before vMotion must operate in latency-aware mode. |
| `/Migrate/SndBufSize` | `integer` | `562540` | `562540` | TCP send buffer size for the source |
| `/Migrate/RcvBufSize` | `integer` | `562540` | `562540` | TCP receive buffer size for the destination |
| `/Migrate/BindToVmknic` | `integer` | `3` | `3` | Bind the vMotion socket to a specific vmknic.  0 for never, 1 to bind only with FT, 2 to bind with FT or for multi-vmknic support, 3 to always bind |
| `/Migrate/MonActionWaitSysAlertThresholdMS` | `integer` | `2000` | `2000` | Threshold in milliseconds for the monitor to process a pre-copy action after which a SysAlert is triggered |
| `/Migrate/LowMemWaitSysAlertThresholdMS` | `integer` | `10000` | `10000` | Threshold in milliseconds for the dest host to leave the low-memory state above which a SysAlert is triggered |
| `/Migrate/GetPageSysAlertThresholdMS` | `integer` | `10000` | `10000` | Threshold in milliseconds for the source host to prepare a page for transmission above which a SysAlert is triggered |
| `/Migrate/DebugChecksumMismatch` | `integer` | `0` | `0` | Debug checksum mismatch. |
| `/Migrate/PanicOnChecksumMismatch` | `integer` | `0` | `0` | 1 for world panic, 2 for vmkernel panic |
| `/Migrate/MigrateCpuMinPctDefault` | `integer` | `30` | `30` | Desired default shared CPU reservation (in %) for VMotions |
| `/Migrate/MigrateCpuPctPerGb` | `integer` | `10` | `10` | Desired per Gbit shared CPU reservation (in %) for VMotions |
| `/Migrate/MigrateCpuSharesRegular` | `integer` | `30000` | `30000` | CPU shares for a regular VMotion |
| `/Migrate/MigrateCpuSharesHighPriority` | `integer` | `60000` | `60000` | CPU shares for a high priority VMotion |
| `/Migrate/MigrateBitmapEncodingType` | `integer` | `2` | `2` | Encoding type for changed bitmap transfer |
| `/Migrate/MigrateStreamHelperBwUtilMax` | `integer` | `15000` | `15000` | Maximum network bandwidth (Mbps) that each stream helper can saturate |
| `/Migrate/Vmknic` | `string` | `` | `` | vmknic for vMotion vmkernel VNIC |

</details>

<details><summary><strong>Subsystem: /Misc (61 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Misc/LogToSerial` | `integer` | `1` | `1` | Send vmkernel log messages to the serial port |
| `/Misc/PanicLogToSerial` | `integer` | `0` | `0` | Send panic log messages to the serial port |
| `/Misc/DebugLogToSerial` | `integer` | `0` | `0` | Send vmkernel LOG messages to the serial port |
| `/Misc/LogTimestampUptime` | `integer` | `0` | `0` | Use uptime rather than UTC for vmkernel log |
| `/Misc/LogWldPrefix` | `integer` | `1` | `1` | Including running world on every log statement |
| `/Misc/LogDumpShutdownTimeout` | `integer` | `180` | `180` | The maximum amount of time during shutdown that the kernel logger will spend dumping logs from the log buffer |
| `/Misc/MinimalPanic` | `integer` | `0` | `0` | Don't attempt to coredump after PSODing |
| `/Misc/BlueScreenTimeout` | `integer` | `0` | `0` | timeout in seconds, 0 is no timeout |
| `/Misc/HeartbeatTimeout` | `integer` | `5` | `5` | Timeout in seconds, for sending NMI to the locked CPU |
| `/Misc/HeartbeatInterval` | `integer` | `1000` | `1000` | Interval in msec to check CPU lockups |
| `/Misc/HeartbeatPanicTimeout` | `integer` | `10` | `10` | Interval in seconds after which to panic if no heartbeats received |
| `/Misc/HeartbeatPanicIpiCount` | `integer` | `2` | `2` | Number of warnings and stack trace NMI IPIs sent to target pcpu before sending a panic NMI IPI |
| `/Misc/HeapPanicDestroyNonEmpty` | `integer` | `0` | `0` | Panic when a non-empty heap gets destroyed |
| `/Misc/HeapMgrGuardPages` | `integer` | `1` | `1` | Number of guard pages to insert between heap VA regions |
| `/Misc/MCEMonitorInterval` | `integer` | `1000` | `1000` | Interval[0 - 0x7fffffff ms] to poll for Machine Check Errors(0=never) |
| `/Misc/TimerTolerance` | `integer` | `2000` | `2000` | Default timer lateness tolerance in microseconds |
| `/Misc/BHTimeout` | `integer` | `0` | `0` | Timeout for bottom-half handlers in milliseconds |
| `/Misc/HordeEnabled` | `integer` | `0` | `0` | Enables horde mode |
| `/Misc/ScreenSaverDelay` | `integer` | `0` | `0` | Delay in minutes before screensaver kicks in |
| `/Misc/GuestLibAllowHostInfo` | `integer` | `0` | `0` | Allow guest to read host-level metrics |
| `/Misc/NMILint1IntAction` | `integer` | `0` | `0` | Override how a hardware generated NMI is handled: 0=default (panic, unless changed by boot-time option), 1=enter debugger, 2=panic, 3=log and ignore (not recommended), 4=log and ignore if undiagnosed |
| `/Misc/SIOControlLoglevel` | `integer` | `0` | `0` | Storage I/O Control Log Level |
| `/Misc/ShaperStatsEnabled` | `integer` | `1` | `1` | Enable stats in shaper module |
| `/Misc/SIOControlFlag1` | `integer` | `0` | `0` | Storage I/O Control Internal Flag |
| `/Misc/SIOControlFlag2` | `integer` | `0` | `0` | Storage I/O Control Internal Flag |
| `/Misc/APDTimeout` | `integer` | `140` | `140` | Number of seconds a device can be in APD before failing User World IO. |
| `/Misc/EnablePSPLatencyPolicy` | `integer` | `1` | `1` | Enable latency based sub-policy of Round-robin path selection plugin |
| `/Misc/PSPDeactivateFlakyPath` | `integer` | `0` | `0` | Deactivate flaky path if IOs are failing with HOST ERROR |
| `/Misc/NmpManageDegradedPaths` | `integer` | `1` | `1` | Choose paths with less errors for I/Os during transient issues on NMP claimed paths |
| `/Misc/HppManageDegradedPaths` | `integer` | `1` | `1` | Choose paths with less errors for I/Os during transient issues on HPP claimed paths |
| `/Misc/NmpDegradedPathThresholdPer` | `integer` | `20` | `20` | Percentage threshold of transient errors to mark path as degraded |
| `/Misc/DegradedPathEvalTime` | `integer` | `5` | `5` | Evaluation time (in secs) for paths to mark the path as degraded |
| `/Misc/DegradedPathReEvalInterval` | `integer` | `60` | `60` | Re-evaluation interval (in secs) for the degraded paths |
| `/Misc/HppDegradedPathThresholdPer` | `integer` | `20` | `20` | Percentage threshold of transient errors to mark path as degraded |
| `/Misc/APDHandlingEnable` | `integer` | `1` | `1` | Enable Storage APD Handling [default: on] |
| `/Misc/VmfsUnmapThrottle` | `integer` | `0` | `0` | Enable throttling of unmap commands on devices having VMFS datastore |
| `/Misc/EnableNVMeCopyCmd` | `integer` | `1` | `1` | Enable support for NVMe Copy command |
| `/Misc/PowerButton` | `integer` | `1` | `1` | Action to take on a momentary press of the soft power button (0=ignore, 1=request graceful system shutdown and power-off) |
| `/Misc/PowerOffEnable` | `integer` | `1` | `1` | Action to take on system power-off request (0=halt only, 1=power off) |
| `/Misc/IoFilterWatchdogTimeout` | `integer` | `120` | `120` | Timeout for the I/O filter watchdog in seconds. 0 means the watchdog is disabled. 120 seconds is the minimum timeout value. |
| `/Misc/vmmDisableL1DFlush` | `integer` | `0` | `0` | Disable L1D flush on VM entry |
| `/Misc/forceMPTI` | `integer` | `1` | `1` | Force use of Monitor Page Table Isolation. |
| `/Misc/forceBPB` | `integer` | `0` | `0` | Force use of BPB. |
| `/Misc/TestNativeFCPaeCapable` | `integer` | `0` | `0` | native_fc test module is pae capable |
| `/Misc/HyperClockAllowSystemTimeAux` | `integer` | `0` | `0` | Allow auxiliary input to system time HyperClock |
| `/Misc/HwclockPeriodicSync` | `integer` | `1` | `1` | Sync the hardware clock periodically to match the current system time |
| `/Misc/vmknvmeCwYield` | `integer` | `1` | `1` | Yield every n commands in NVMe completion world |
| `/Misc/SevAllowDebugging` | `integer` | `0` | `0` | Allow a SEV guest to enable the debug policy. |
| `/Misc/DumpAllKlmData` | `integer` | `0` | `0` | Dump KLM data for all VMs. |
| `/Misc/vsanWitnessVirtualAppliance` | `integer` | `0` | `0` | Indicates a VSAN witness host running in a Virtual Appliance. VM services (create/register/power on) are blocked |
| `/Misc/LogPort` | `string` | `none` | `none` | Name of serial port to use for logging (none, COM1, COM2) |
| `/Misc/GDBPort` | `string` | `none` | `none` | Name of serial port to use for GDB debugging (none, COM1, COM2) |
| `/Misc/ShellPort` | `string` | `none` | `none` | Name of serial port to use for visor shell (none, COM1, COM2) |
| `/Misc/ConsolePort` | `string` | `none` | `none` | Name of serial port to use for visor console (none, COM1, COM2) |
| `/Misc/DebugShellPort` | `string` | `none` | `none` | Name of serial port to use for debug shell (none, COM1, COM2) |
| `/Misc/HostName` | `string` | `esxi-01.npcsolutions.co.za` | `localhost` | Host name |
| `/Misc/PreferredHostName` | `string` | `` | `` | Preferred Host name |
| `/Misc/SIOControlOptions` | `string` | `` | `` | Storage I/O Control Options |
| `/Misc/DefaultHardwareVersion` | `string` | `` | `` | Default Hardware Version |
| `/Misc/MaximumHardwareVersion` | `string` | `` | `` | Maximum Hardware Version |
| `/Misc/RebootMethod` | `string` | `any` | `any` | Preferred reboot method (any, psci, acpi, rcr_hard, kb, ps2, uefi, or rcr_power) |

</details>

<details><summary><strong>Subsystem: /NFS (20 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/NFS/DiskFileLockUpdateFreq` | `integer` | `10` | `10` | Time (in seconds) between updates to a disk lock file [8-3600] |
| `/NFS/LockBreakTimeout` | `integer` | `10` | `10` | Time (in seconds) to wait to check for expired races when breaking lock [0-3600] |
| `/NFS/LockSharedTimeout` | `integer` | `0` | `0` | Time (in seconds) to wait to check for expired races when sharing (read) lock [0-3600] |
| `/NFS/LockSWMRTimeout` | `integer` | `10` | `10` | Time (in seconds) to wait to check for expired races when acquiring SWMR lock [0-3600] |
| `/NFS/LockUpdateTimeout` | `integer` | `5` | `5` | Time (in seconds) before we abort an outstanding lock update |
| `/NFS/LockRenewMaxFailureNumber` | `integer` | `3` | `3` | Number of update failures before a disk file lock is declared stale |
| `/NFS/HeartbeatFrequency` | `integer` | `12` | `12` | Time in seconds between heartbeats |
| `/NFS/HeartbeatTimeout` | `integer` | `5` | `5` | Time in seconds before we abort an outstanding heartbeat |
| `/NFS/HeartbeatDelta` | `integer` | `5` | `5` | Time in seconds since the last successful update before we send a heartbeat |
| `/NFS/HeartbeatMaxFailures` | `integer` | `10` | `10` | Number of sequential failures before we mark a volume as down |
| `/NFS/ApdStartCount` | `integer` | `3` | `3` | Number of failed heartbeat updates after which APD START timer is triggered |
| `/NFS/MaxVolumes` | `integer` | `32` | `32` | Maximum number of mounted NFS v3 volumes |
| `/NFS/SendBufferSize` | `integer` | `1024` | `1024` | Default size of socket's send buffer in KB |
| `/NFS/ReceiveBufferSize` | `integer` | `1024` | `1024` | Default Size of socket's receive buffer in KB |
| `/NFS/VolumeRemountFrequency` | `integer` | `30` | `30` | Time in seconds before attempting to remount a volume |
| `/NFS/SyncRetries` | `integer` | `25` | `25` | Number of retries before synchronous IO fails (10 seconds per retry) |
| `/NFS/LogNfsStat3` | `integer` | `0` | `0` | Log nfsstat3 code |
| `/NFS/MaxQueueDepth` | `integer` | `4294967295` | `4294967295` | Maximum per-Volume queue depth |
| `/NFS/NFSMaxOutstandingIOs` | `integer` | `65536` | `65536` | Maximum number of NFSv3 outstanding IOs on the host (Requires a REBOOT!) |
| `/NFS/MountTimeout` | `integer` | `30` | `30` | Mount timeout in seconds |

</details>

<details><summary><strong>Subsystem: /NFS41 (9 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/NFS41/MaxRead` | `integer` | `4294967295` | `4294967295` | Maximum read transfer size in bytes (use the smaller of this value and the server advertised value |
| `/NFS41/MaxWrite` | `integer` | `4294967295` | `4294967295` | Maximum write transfer size in bytes (use the smaller of this value and the server advertised value |
| `/NFS41/MountTimeout` | `integer` | `30` | `30` | Mount timeout in seconds |
| `/NFS41/IOTaskRetry` | `integer` | `25` | `25` | Synchronous IO task number of retries |
| `/NFS41/EOSDelay` | `integer` | `30` | `30` | Request EOS safety delay in seconds |
| `/NFS41/MaxVolumes` | `integer` | `32` | `32` | Maximum number of mounted NFS v4.1 volumes |
| `/NFS41/SendBufSize` | `integer` | `1024` | `1024` | Socket send buffer size in kilobytes (using default if set to zero) |
| `/NFS41/RecvBufSize` | `integer` | `1024` | `1024` | Socket receive buffer size in kilobytes (using default if set to zero) |
| `/NFS41/MaxQueueDepth` | `integer` | `4294967295` | `4294967295` | Maximum per-Volume queue depth |

</details>

<details><summary><strong>Subsystem: /Net (234 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Net/MaxGlobalRxQueueCount` | `integer` | `100000` | `100000` | Global max length of rx queues for all virtual ports on a ESX host that support queueing |
| `/Net/MaxPortRxQueueLen` | `integer` | `80` | `80` | Max length of the rx queue for virtual ports whose clients support queueing |
| `/Net/MaxNetifTxQueueLen` | `integer` | `2000` | `2000` | Max length of the tx queue for the physical NICs |
| `/Net/LinkFlappingThreshold` | `integer` | `60` | `60` | Max number of link down events per minute before considering a link unstable (0 to deactivate) |
| `/Net/TeamPolicyUpDelay` | `integer` | `100` | `100` | Delay (ms) before considering an `uplink up' event relevant |
| `/Net/EnableOuterCsum` | `integer` | `1` | `1` | Enable uplink layer outer checksumming |
| `/Net/DontOffloadInnerIPv6` | `integer` | `0` | `0` | Don't offload VXLAN/Geneve inner IPv6 CSO/TSO packets to NICs. |
| `/Net/UplinkKillAsyncTimeout` | `integer` | `10000` | `10000` | Timeout (ms) waiting for async when world is killed. |
| `/Net/UplinkAbortDisconnectTimeout` | `integer` | `5000` | `5000` | Timeout (ms) waiting for pending calls to finish when disconnecting. |
| `/Net/UplinkTSOSplit` | `integer` | `1` | `1` | Split TSO packet into CSO ones on pNIC not supporting TSO but supporting CSO. |
| `/Net/UplinkTxQueuesDispEnabled` | `integer` | `1` | `1` | Enables dispatching of port traffic on multiple tx queues |
| `/Net/NetSchedECNEnabled` | `integer` | `1` | `1` | Enable net scheduler to send congestion notification to switch ports. |
| `/Net/NetSchedECNThreshold` | `integer` | `70` | `70` | Percentage queue utilization at which net scheduler will start sending congestion notifications to switch ports. |
| `/Net/GuestTxCopyBreak` | `integer` | `64` | `64` | transmits smaller than this will be copied rather than mapped |
| `/Net/VmxnetTxCopySize` | `integer` | `256` | `256` | vmxnet tx <= than this will be fully copied with no need for completion. |
| `/Net/VmxnetCopyTxRunLimit` | `integer` | `16` | `16` | non-Win vmxnet2/3 tx will have at most so many fully copied tx's in a row (65536 and larger means never). |
| `/Net/VmxnetWinCopyTxRunLimit` | `integer` | `65535` | `65535` | Win vmxnet2/3 tx will have at most so many fully copied tx's in a row (65536 and larger means never). |
| `/Net/VmxnetWinUDPTxFullCopy` | `integer` | `1` | `1` | whether Windows vmxnet UDP tx is fullCopy. |
| `/Net/VmxnetDoTsoSplit` | `integer` | `1` | `1` | whether to split TSO pkts before LPD; 1: halved; 3: VmxnetTsoSplitSize; 2: hybrid. |
| `/Net/VmxnetTsoSplitSize` | `integer` | `17500` | `17500` | split (byte) size; only used if DoTsoSplit >= 2. |
| `/Net/VmxnetTsoSplitBnd` | `integer` | `12` | `12` | when VmxnetDoTsoSplit is 1 or 2, use targetSize as the tsoSplit threshold if the overall pkt list already has this number of pkts. |
| `/Net/VmxnetBiDirNoTsoSplit` | `integer` | `1` | `1` | For bidirectional traffic, don't do tsoSplit. |
| `/Net/VmxnetBiDirNeedsTsoTx` | `integer` | `1` | `1` | Need to see Tso Tx to qualify for tsoSplit bidirectional traffic condition. |
| `/Net/Vmxnet3WinIntrHints` | `integer` | `1` | `1` | whether intr hints are used for Windows vmxnet3. |
| `/Net/VmxnetDoLroSplit` | `integer` | `1` | `1` | whether for vmxnet LRO avoids aggregating all pkts into a single (> 2 mss) large pkt. |
| `/Net/VmxnetLroSplitBnd` | `integer` | `64` | `64` | when VmxnetDoLroSplit is non-zero, while pktList is larger than this number, lroSplit is not done. |
| `/Net/VmknicDoLroSplit` | `integer` | `0` | `0` | whether for vmknic LRO avoids aggregating all pkts into a single (> 2 ms) large pkt. |
| `/Net/VmknicLroSplitBnd` | `integer` | `12` | `12` | when VmknicDoLroSplit is non-zero, while pktList is larger than this number, lroSplit is not done. |
| `/Net/UseProc` | `integer` | `0` | `0` | whether or not to populate /proc/vmware/net [0 = disabled, 1 = enabled] |
| `/Net/UseLegacyProc` | `integer` | `0` | `0` | whether or not to populate legacy entries in  /proc/vmware/net [0 = disabled, 1 = enabled] |
| `/Net/NotifySwitch` | `integer` | `1` | `1` | Broadcasts an arp request on net handle enable [0 = disabled, 1 = enabled] |
| `/Net/NetTxDontClusterSize` | `integer` | `0` | `0` | transmits smaller than this will not be subject to clustering/coalescing. |
| `/Net/NetPktAllocTries` | `integer` | `5` | `5` | Number of tries for allocating pkt within the page. |
| `/Net/CoalesceTxTimeout` | `integer` | `4000` | `4000` | set the coalesce timeout in micro-seconds |
| `/Net/CoalesceFineTxTimeout` | `integer` | `1000` | `1000` | set the fine coalesce timeout in microseconds |
| `/Net/CoalesceTimeoutType` | `integer` | `2` | `2` | set the coalesce timeout type: fine(1 ms by default) or coarse (4 ms by default) |
| `/Net/CoalesceFineTimeoutCPU` | `integer` | `2` | `2` | Set which cpu the fine timer will run on |
| `/Net/CoalesceDefaultOn` | `integer` | `1` | `1` | whether dynamic coalescing is on by default.[0 = disabled by default, 1 = enabled by default] |
| `/Net/CoalesceLowTxRate` | `integer` | `4` | `4` | No tx coalescing calibration when the number of pkts tx per timeout is lower than this number. |
| `/Net/CoalesceLowRxRate` | `integer` | `4` | `4` | No Rx coalescing calibration when the number of pkts Rx per timeout is lower than this number. |
| `/Net/CoalesceTxAlwaysPoll` | `integer` | `1` | `1` | Whether always poll Tx at coalesce timeout handler. |
| `/Net/CoalesceMatchedQs` | `integer` | `1` | `1` | Whether to use matched TxRxQ-pairs mode when applicable. |
| `/Net/CoalesceMultiRxQCalib` | `integer` | `1` | `1` | When not in matched TxRxQ-pairs mode, whether to uses separate RxQ Calib. |
| `/Net/CoalesceTxQDepthCap` | `integer` | `40` | `40` | Cap of Tx coalescing size. |
| `/Net/CoalesceRxQDepthCap` | `integer` | `40` | `40` | Cap of Rx coalescing size. |
| `/Net/vNicTxPollBound` | `integer` | `192` | `192` | max # normalPkts per poll. |
| `/Net/vNicNumDeferredReset` | `integer` | `12` | `12` | max # normalPkts per poll. |
| `/Net/vmxnetThroughputWeight` | `integer` | `0` | `0` | How far to favor throughput in vmxnet behavior. |
| `/Net/CoalesceNoVmmVmkTx` | `integer` | `1` | `1` | Whether to try disable all vmm->vmk tx transitions. |
| `/Net/CoalesceFavorNoVmmVmkTx` | `integer` | `1` | `1` | Favor disabling all vmm->vmk tx transitions; boost its score by factor of this/64. |
| `/Net/CoalesceMrqLt` | `integer` | `1` | `1` | Whether to set a RxQ's coalesce to zero based on per-RxQ Low Traffic. |
| `/Net/CoalesceMrqTriggerReCalib` | `integer` | `1` | `1` | Whether to let individual RxQ's perf change trigger re-calib. |
| `/Net/CoalesceMrqMetricRxOnly` | `integer` | `0` | `0` | Whether to force individual RxQ's perf metric to be rx pkt cnt only. |
| `/Net/CoalesceMrqMetricAllowTxOnly` | `integer` | `1` | `1` | Whether to allow's individual RxQ's perf metric to be tx pkt cnt only; if not, it will be tx + rx, or rx only. |
| `/Net/CoalesceMrqRatioMetric` | `integer` | `1` | `1` | Whether Tx perf score is attributed to RxQ according to rxPktCnt ratio. |
| `/Net/CoalesceRxLtStopCalib` | `integer` | `0` | `0` | Whether Rx Low Traffic stops Rx calibration. |
| `/Net/CoalesceMrqOverallStop` | `integer` | `0` | `0` | Whether to use overall performance to stop RxQ Calib. |
| `/Net/CoalesceFlexMrq` | `integer` | `1` | `1` | Whether to dynamically switch on/off multiRxQCalib. |
| `/Net/CoalesceRBCRate` | `integer` | `4000` | `4000` | Target event rate for RateBasedCoalescing |
| `/Net/NetLatencyAwareness` | `integer` | `1` | `1` | Whether to check vm's latency settings or not for vmxnet2/3 |
| `/Net/NetTuneInterval` | `integer` | `60` | `60` | Tuning interval in seconds. |
| `/Net/EtherswitchHashSize` | `integer` | `1` | `1` | number of ports on the etherswitch x 2^N is the size of the hash table for looking up MACs |
| `/Net/EtherswitchHeapMax` | `integer` | `512` | `512` | Maximum size (in Megabytes) the etherswitch module can grow to. (REQUIRES REBOOT!) |
| `/Net/EtherswitchNumPerPCPUDispatchData` | `integer` | `3` | `3` | The dispatch data number in the etherswitch per-pCPU dispatch data cache. (REQUIRES REBOOT!) |
| `/Net/EtherswitchAllowFastPath` | `integer` | `0` | `0` | Allow Etherswitch fast path |
| `/Net/NoLocalCSum` | `integer` | `0` | `0` | if set, don't bother checksumming local tx/rx frames |
| `/Net/NetPortFlushIterLimit` | `integer` | `2` | `2` | when input is serialized, this bounds the number of times a thread flushes the deferred list. |
| `/Net/NetPortFlushPktLimit` | `integer` | `64` | `64` | when input is serialized, this bounds the number of pkts a thread flushes from the deferred list. |
| `/Net/NetPortTrackTxRace` | `integer` | `0` | `0` | if enabled(1), collect statistics on potential tx race between concurrent threads. |
| `/Net/PortDisableTimeout` | `integer` | `5000` | `5000` | max timeout delay to wait for ports to complete I/O before disabling. |
| `/Net/TcpipAutoScaleRcvBufSize` | `integer` | `16777216` | `16777216` | Max tcp socket Receive buffer size to scale with auto tuning (REQUIRES REBOOT!) |
| `/Net/TcpipAutoScaleSndBufSize` | `integer` | `16777216` | `16777216` | Max tcp socket Send buffer size to scale with auto tuning (REQUIRES REBOOT!) |
| `/Net/TcpipHeapSize` | `integer` | `8` | `8` | Initial size of the tcpip module heap in megabytes. (REQUIRES REBOOT!) |
| `/Net/TcpipHeapMax` | `integer` | `1024` | `1024` | Max megabytes the tcpip module heap used for packet memory can grow to. (REQUIRES REBOOT!) |
| `/Net/TcpipMaxNetstackInstances` | `integer` | `48` | `48` | Maximum number of TCP/IP stack instances that can exist concurrently. If this number is increased, the TcpipHeapSize should also be increased, by about 2.5 MB per instance. (REQUIRES REBOOT!) |
| `/Net/TcpipRxDispatchQuota` | `integer` | `200` | `200` | Max # of pkts dispatched into the tcpip stack by an execution context |
| `/Net/TcpipRxDispatchQueues` | `integer` | `2` | `2` | Max # of dispatch queues used for RX. For low memory systems, this should be minimum value(REQUIRES REBOOT!) |
| `/Net/TcpipRxDispatchQueueMaxLen` | `integer` | `2000` | `2000` | Max # of pkts queued into a tcpip vmknic by an execution context (applied when vmknic is created) |
| `/Net/TcpipLODispatchQueueMaxLen` | `integer` | `128` | `128` | Max # of pkts queued into the per-protocol queue used for dispatching loopback traffic (REQUIRES REBOOT!) |
| `/Net/TcpipEnsMultipleRxContexts` | `integer` | `0` | `0` | Use multiple ENS contexts for vmknic RX processing. |
| `/Net/TcpipEnsNetQRSS` | `integer` | `1` | `1` | Request NetQ RSS for vmknics. |
| `/Net/TcpipTxDispatchQuota` | `integer` | `100` | `100` | Max # of pkts dispatched from the tcpip stack by an execution context |
| `/Net/TcpipLogPackets` | `integer` | `0` | `0` | Turns on packet logging for a vmknic on debug builds, in a circular & in-memory buffer (Takes effect during vmknic creation time) |
| `/Net/TcpipLogPacketsCount` | `integer` | `24570` | `24570` | Number of packets to log in the in-memory logger. 24570 packets take up about 1.2 MB, and Tx & Rx use separate buffers. (Takes effect during vmknic creation time) |
| `/Net/TcpipDgramRateLimiting` | `integer` | `1` | `1` | Enable Tx rate limiting for UDP sockets |
| `/Net/TcpipPendPktSocketFreeTimeout` | `integer` | `300` | `300` | Time Delay in seconds, for freeing UDP sockets that have pending packets for Tx completion |
| `/Net/MaxPageInQueueLen` | `integer` | `75` | `75` | maximum number of paging requests to queue for guest DMA. |
| `/Net/MaxBeaconsAtOnce` | `integer` | `100` | `100` | maximum number of beacons to send in one beacon cycle. |
| `/Net/MaxBeaconVlans` | `integer` | `100` | `100` | maximum number of VLANs to probe with beacons. |
| `/Net/AdvertisementDuration` | `integer` | `60` | `60` | duration of RARP advertisements |
| `/Net/TcpipNoBcopyRx` | `integer` | `1` | `1` | Avoid bcopy in tcp rx |
| `/Net/TcpipCopySmallTx` | `integer` | `1` | `1` | Copy and tx complete small packets for tcp tx |
| `/Net/TcpipLRONoDelayAck` | `integer` | `1` | `1` | Delayed ack timer not armed for LRO |
| `/Net/TcpipHWLRONoDelayAck` | `integer` | `1` | `1` | Delayed ack timer not armed for Hardware LRO (socket option needs to be set in addition) |
| `/Net/TcpipDefLROEnabled` | `integer` | `1` | `1` | LRO enabled for TCP/IP |
| `/Net/TcpipDefLROMaxLength` | `integer` | `32768` | `32768` | LRO default max length for TCP/IP |
| `/Net/TcpipEnableABC` | `integer` | `1` | `1` | Enable Appropriate Byte Counting for TCP (RFC 3465) |
| `/Net/TcpipEnableFlowtable` | `integer` | `1` | `1` | Enable route caching through the use of flowtable |
| `/Net/TcpipEnableSendScaling` | `integer` | `1` | `1` | Enable Send-Side Scaling (requires RSS) |
| `/Net/TcpipIGMPRejoinInterval` | `integer` | `60` | `60` | Delay in seconds between automatic IGMP rejoins when no querier is present |
| `/Net/TcpipIGMPDefaultVersion` | `integer` | `3` | `3` | Default version of IGMP, in the absence of a querier |
| `/Net/TcpipTxqMaxUsageThreshold` | `integer` | `80` | `80` | Tx queue usage threshold in percent at which to start throttling |
| `/Net/TcpipTxqBackoffTimeoutMs` | `integer` | `70` | `70` | Duration (in milli seconds) for which backoff is effective when the tx queue has reached the NET_TCPIP_TXQ_MAX_USAGE_THRESHOLD |
| `/Net/LinkStatePollTimeout` | `integer` | `500` | `500` | Link State poll timer period in milliseconds. |
| `/Net/E1000TxCopySize` | `integer` | `2048` | `2048` | e1000 tx less than or equal to this will be fully copied with no need for completion. |
| `/Net/E1000TxZeroCopy` | `integer` | `1` | `1` | Use tx zero copy for packets for e1000. |
| `/Net/E1000IntrCoalesce` | `integer` | `1` | `1` | Whether to enable interrupt coalescing for e1000 vNIC. |
| `/Net/MinEtherLen` | `integer` | `60` | `60` | Minimum size ethernet frame to transmit |
| `/Net/EnsEnableDatapathHotswap` | `integer` | `0` | `0` | Enable datapath during in-place upgrade hotswap. |
| `/Net/MaxPktRxListQueue` | `integer` | `3500` | `3500` | Maximum packet we can queue in rxList |
| `/Net/NetBHRxStormThreshold` | `integer` | `320` | `320` | Declare Rx Storm after this number of consecutive rx pkt drops during queuing in NetBH rxList. |
| `/Net/ReversePathFwdCheck` | `integer` | `1` | `1` | Block the multicast/broadcast packets that come back from physical switches in a teamed environment |
| `/Net/ReversePathFwdCheckPromisc` | `integer` | `0` | `0` | Block duplicate packet in a teamed environment when the virtual switch is set to Promiscuous mode. |
| `/Net/Vmxnet2PinRxBuf` | `integer` | `0` | `0` | Pin RX buffers for vmxnet2 clients (windows guest only) |
| `/Net/Vmxnet3usePNICHash` | `integer` | `0` | `0` | Reuse pnic computed RSS hash. |
| `/Net/Vmxnet3RSSHashCache` | `integer` | `1` | `1` | Enable RSS hash cache. |
| `/Net/Vmxnet3RxPollBound` | `integer` | `256` | `256` | max # pkts to receive per timeout for vmxnet3. |
| `/Net/Vmxnet3RxQueueBound` | `integer` | `256` | `256` | Rx max queue size beyond which packets are dropped for vmxnet3. |
| `/Net/Vmxnet3PageInBound` | `integer` | `32` | `32` | max # pageIn requests to handle per helper call for vmxnet3. |
| `/Net/NetVMTxType` | `integer` | `2` | `2` | World for asynchronous Tx for net devices. 1 for 1WDT/NIC. 2 for 1WDT/VM. 3 for 1WDT/Q |
| `/Net/NetTxStaticRelation` | `integer` | `1` | `1` | Whether the world should have a static relation to the VM VCPU |
| `/Net/NetDeferTxCompletion` | `integer` | `1` | `1` | Whether to defer tx completion to tx world. 1 for Try Completion. 2 For Always (Only in MQ Tx World case). |
| `/Net/NetDeferTxCompletionNonPerQ` | `integer` | `1` | `1` | Whether to defer tx completion to tx world when ctxPerDev = '1' or '2'. 1) for Try Completion. 2) For Always. |
| `/Net/NetRxCopyInTx` | `integer` | `0` | `0` | Whether to enable rx copy in tx worldlet/world. |
| `/Net/NetSplitRxMode` | `integer` | `1` | `1` | Whether to enable automatic splitRxMode |
| `/Net/AllowPT` | `integer` | `1` | `1` | Whether to enable UPT/NPA |
| `/Net/PTSwitchingTimeout` | `integer` | `20000` | `20000` | Timeout (in ms) when asking the VMX/guest to switch in/out of passthru |
| `/Net/VmxnetSwLROSL` | `integer` | `1` | `1` | Whether to use ShortLived for vmxnet SW LRO |
| `/Net/Vmxnet3SwLRO` | `integer` | `1` | `1` | Whether to perform SW LRO on pkts going to a LPD capable vmxnet3 |
| `/Net/Vmxnet3HwLRO` | `integer` | `1` | `1` | Whether to enable HW LRO on pkts going to a LPD capable vmxnet3 |
| `/Net/NetpollSwLRO` | `integer` | `1` | `1` | Whether to perform SW LRO on pkts in netpoll |
| `/Net/Vmxnet2SwLRO` | `integer` | `1` | `1` | Whether to perform SW LRO on pkts going to a LPD capable vmxnet2 |
| `/Net/Vmxnet2HwLRO` | `integer` | `1` | `1` | Whether to perform HW LRO on pkts going to a LPD capable vmxnet2 |
| `/Net/VmxnetPromDisableLro` | `integer` | `1` | `1` | Whether to disable SW LRO when vNIC goes into promiscuous mode. |
| `/Net/VmxnetLROThreshold` | `integer` | `4000` | `4000` | After this # packets, evaluate whether to continue SW LRO |
| `/Net/VmxnetLROBackoffPeriod` | `integer` | `8` | `8` | After adaptive LRO decided not to do LRO, how many intervals to wait before trying again. |
| `/Net/VmxnetLROUseRatioNumer` | `integer` | `2` | `2` | If SW LRO reduce pkt count to be smaller than ratio, continue to do LRO. Numerator of ratio. |
| `/Net/VmxnetLROUseRatioDenom` | `integer` | `3` | `3` | If SW LRO reduce pkt count to be smaller than ratio, continue to do LRO. Denominator of ratio. |
| `/Net/VmxnetLROMaxLength` | `integer` | `32000` | `32000` | LRO default max length for TCP/IP |
| `/Net/NetEnableSwCsumForLro` | `integer` | `1` | `1` | Whether enable software checksum for LRO |
| `/Net/TsoDumpPkt` | `integer` | `0` | `0` | detailed dump of every <n> pkts |
| `/Net/IGMPVersion` | `integer` | `3` | `3` | IGMP Version (2 or 3) |
| `/Net/IGMPQueries` | `integer` | `2` | `2` | Number of IGMP Queries to send during after VMotion/Teaming failover |
| `/Net/MLDVersion` | `integer` | `2` | `2` | MLD Version (1 or 2) |
| `/Net/IGMPQueryInterval` | `integer` | `125` | `125` | Interval(in seconds) for IGMP/MLD general query in multicast snooping |
| `/Net/IGMPV3MaxSrcIPNum` | `integer` | `10` | `10` | Max per-group srouce IP number for IGMP V3 |
| `/Net/MLDV2MaxSrcIPNum` | `integer` | `10` | `10` | Max per-group srouce IP number for MLD V2 |
| `/Net/NetRmDistMacFilter` | `integer` | `1` | `1` | Activate/Deactivate the MAC filter on distributed NetRM |
| `/Net/NetRmDistSamplingRate` | `integer` | `0` | `0` | Sampling rate on distributed NetRM |
| `/Net/GuestIPHack` | `integer` | `0` | `0` | Enable guest arp inspection IOChain to get IP |
| `/Net/BlockGuestBPDU` | `integer` | `1` | `1` | Block guest sourced BPDU frames |
| `/Net/NetNetqTxPackKpps` | `integer` | `300` | `300` | Max TX queue load (in thousand packet per second) to allow packing on the corresponding RX queue |
| `/Net/NetNetqTxUnpackKpps` | `integer` | `600` | `600` | Threshold (in thousand packet per second) for TX queue load to trigger unpacking of the corresponding RX queue |
| `/Net/NetNetqNumaIOCpuPinThreshold` | `integer` | `0` | `0` | CPU threshold for pinning device queues in NUMA I/O |
| `/Net/NetNetqRxRebalRSSLoadThresholdPerc` | `integer` | `10` | `10` | Threshold percentage to rebalance RSS(Receive Side Scaling) queue |
| `/Net/NetSchedInFlightMaxBytesDefault` | `integer` | `200000` | `200000` | Number of bytes fed to the nic for nics with a normal (10Gbps) linkspeed |
| `/Net/NetSchedInFlightMaxBytesInsane` | `integer` | `1500000` | `1500000` | Number of bytes fed to the nic for nics that don't support tx completion coalescing |
| `/Net/NetSchedCoalesceTxUsecs` | `integer` | `33` | `33` | Maximum number of microseconds the device can delay tx completions |
| `/Net/NetSchedDefaultResPoolSharesPct` | `integer` | `5` | `5` | Percent share given to unclassified traffic |
| `/Net/NetSchedSpareBasedShares` | `integer` | `1` | `1` | Enable shares scheduling only on spare bandwidth. Don't bill while doing reservation scheduling |
| `/Net/NetSchedHeapMaxSizeMB` | `integer` | `66` | `66` | Size of the netsched subsystem heap in MB |
| `/Net/NetSchedMaxPktSend` | `integer` | `256` | `256` | Maximum number of packets that we can send to the driver at a time |
| `/Net/NetSchedHClkMQ` | `integer` | `2` | `2` | Enable multiple hardware queue for hclk netsched. (0 is off. 1 and 2 means MQ enabled. With 1, user specifies the number of queues, while 2 is dynamic based on link speed.) |
| `/Net/NetSchedHClkVnicMQ` | `integer` | `1` | `1` | Enable multiple vnic queue for hw tx queue selection |
| `/Net/NetSchedHClkMaxHwQueue` | `integer` | `2` | `2` | Maximum number hardware queue that HClock can use. Only used when NetSchedHClkMQ is 1. |
| `/Net/NetSchedHClkLeafQueueDepthPkt` | `integer` | `640` | `640` | Minimum number of packets each HClk leaf node can hold |
| `/Net/NetShaperQueueSizeMin` | `integer` | `10` | `10` | Minimum shaper queue size |
| `/Net/NetShaperQueueSizeMax` | `integer` | `500` | `500` | Maximum shaper queue size |
| `/Net/NetShaperQueuePerL3L4Flow` | `integer` | `1` | `1` | Enable queuing per L3/L4 flow hashing |
| `/Net/VmklnxLROEnabled` | `integer` | `0` | `0` | LRO enabled in vmklinux |
| `/Net/VmklnxLROMaxAggr` | `integer` | `6` | `6` | LRO max aggr in vmklinux |
| `/Net/UseHwIPv6Csum` | `integer` | `1` | `1` | When non-zero, use pNIC HW IPv6 csum offload if available |
| `/Net/UseHwCsumForIPv6Csum` | `integer` | `1` | `1` | When non-zero, use pNIC HW_CSUM, if available, as IPv6 csum offload |
| `/Net/UseHwTSO6` | `integer` | `1` | `1` | When non-zero, use pNIC HW IPv6 TSO offload if available |
| `/Net/UseHwTSO` | `integer` | `1` | `1` | When non-zero, use pNIC HW TSO offload if available |
| `/Net/EnableDMASgCons` | `integer` | `1` | `1` | When non-zero, enable the DMA SG constraints support in uplink layer |
| `/Net/NcpLlcSap` | `integer` | `0` | `0` | beacon/color NCP messages created with this SAP (DSAP/SSAP) |
| `/Net/DVFilterPriorityRdLockEnable` | `integer` | `1` | `1` | Use priority locking in dvfilter to read lock portsets |
| `/Net/FollowHardwareMac` | `integer` | `0` | `0` | If set to 1, the management interface MAC address will update whenever the hardware MAC address changes. |
| `/Net/NetInStressTest` | `integer` | `0` | `0` | If set to 1, suppress certain logs to avoid log spew. |
| `/Net/DCBEnable` | `integer` | `1` | `1` | Enable DCB for FCoE |
| `/Net/NetTraceEnable` | `integer` | `0` | `0` | Enable virtual network tracing |
| `/Net/LRODefThreshold` | `integer` | `4000` | `4000` | After this # packets, evaluate whether to continue SW LRO |
| `/Net/LRODefBackoffPeriod` | `integer` | `8` | `8` | After adaptive LRO decided not to do LRO, how many intervals to wait before trying again. |
| `/Net/LRODefUseRatioNumer` | `integer` | `1` | `1` | If SW LRO reduce pkt count to be smaller than ratio, continue to do LRO. Numerator of ratio. |
| `/Net/LRODefUseRatioDenom` | `integer` | `3` | `3` | If SW LRO reduce pkt count to be smaller than ratio, continue to do LRO. Denominator of ratio. |
| `/Net/LRODefMaxLength` | `integer` | `65535` | `65535` | LRO default max length |
| `/Net/NetDebugRARPTimerInter` | `integer` | `30000` | `30000` | RARP timer will be triggered at this interval. |
| `/Net/NetPTMgrWakeupInterval` | `integer` | `6` | `6` | How often the PTMgr will wakeup and trigger the UPT mode switch in second. |
| `/Net/NetMaxRarpsPerInterval` | `integer` | `128` | `128` | Max number of RARPs dispatched per timer callback. |
| `/Net/NetPktSlabFreePercentThreshold` | `integer` | `2` | `2` | Percent of free network memory pool, below which an event will be reported. |
| `/Net/DVSLargeHeapMaxSize` | `integer` | `300` | `300` | Size (in Mbytes) of the dvsLargeHeap used during serialization/deserialization of dvSwitch and dvPort configs (Requires REBOOT) |
| `/Net/DVSLargeHeapMBPerGB` | `integer` | `2` | `2` | If it is set to none 0, the dvsLargeHeap will be allocated with the setting MB per GB size of physical memory if it is larger than DVSLargeHeapMaxSize. (Requires REBOOT) |
| `/Net/NetEsxfwPassOutboundGRE` | `integer` | `1` | `1` | Whether outbound GRE traffic is passed by ESXi firewall. |
| `/Net/NetSendRARPOnPortEnablement` | `integer` | `1` | `1` | Ensure one RARP is sent immediately when a port is enabled |
| `/Net/NetNiocAllowOverCommit` | `integer` | `1` | `1` | Whether allow NIOC overcommit when a vNIC is in connected state for DVS |
| `/Net/VLANMTUCheckMode` | `integer` | `1` | `1` | VLAN MTU check mode, 0 - broadcast, 1 - unicast |
| `/Net/NetDiscUpdateIntrvl` | `integer` | `300` | `300` | Interval (in seconds) of networking discovery to update the VLAN information |
| `/Net/PktAgingListQuantumSize` | `integer` | `20` | `20` | Quantum size for PktAgingList expressed in power of 2 |
| `/Net/PktagingDropPolicy` | `integer` | `0` | `0` | Dropping policy for vmxnet3 rx burst queue. 0 for PKTAGING_TAIL_DROP. 1 for PKTAGING_RED |
| `/Net/Vmxnet3RxBurstQueueLimit` | `integer` | `512` | `512` | Maximum number of packets allowed to be queued in vmxnet3 vNIC backend in rx path |
| `/Net/Vmxnet3RxBurstQueueEnableThreshold` | `integer` | `64` | `64` | Maximum number of entries allowed in Rx ring buffer after which vmxnet3 Rx burst queuing will be disabled in vNIC backend |
| `/Net/Vmxnet3SetRSSHash` | `integer` | `1` | `1` | While using multiqueue delivery, set RSS hash while delivering the packet to the guest. |
| `/Net/Vmxnet3UDPRSSAllowed` | `integer` | `1` | `1` | Allow RSS for UDP over IPv4/IPv6 if requested by guest/vmx. May result in out-of-order packets for IP fragments. |
| `/Net/Vmxnet3ESPRSSAllowed` | `integer` | `1` | `1` | Allow RSS for IPSEC (ESP) over IPv4 if requested by guest/vmx. |
| `/Net/EnsMbufpoolMinMBPerGB` | `integer` | `10` | `10` | Minimum MB of the ENS slab memory to be allocated per GB of physical memory. |
| `/Net/EnsMbufpoolMaxMBPerGB` | `integer` | `200` | `200` | Maximum MB of the ENS slab memory to be allocated per GB of physical memory. |
| `/Net/PortsetLockModel` | `integer` | `1` | `1` | The lock model version of a portset |
| `/Net/Vmxnet3MaxRxBurstQueueLength` | `integer` | `16384` | `16384` | Maximum length of burst queue allowed when configured via vmx option |
| `/Net/Vmxnet3MaxPendingRxBurst` | `integer` | `128` | `128` | max # packets to drain from Burst Queue per call |
| `/Net/LACPActorSystemPriority` | `integer` | `1` | `1` | The value of LACP system priority |
| `/Net/LACPEnableIndividualPort` | `integer` | `0` | `0` | Enable or Disable the feature to down the LAG port when LAG's all member link status is down |
| `/Net/Vmxnet3NonTsoPacketGtMtuAllowed` | `integer` | `0` | `0` | Allow non-TSO/LRO packets greater than vNic MTU |
| `/Net/NetRCFAllowBPF` | `integer` | `1` | `1` | Allow to run BPF code in RCF |
| `/Net/NetRCFInsnType` | `integer` | `0` | `0` | The instruction type of bytecode in RCF |
| `/Net/Vmxnet3AllowTruncation` | `integer` | `0` | `0` | Allow truncated packets to be delivered to the guest |
| `/Net/Vmxnet3CopyTrailer` | `integer` | `1` | `1` | Copy additional bytes of pkt not included in the total length field of ip header |
| `/Net/TeamingNUMAAware` | `integer` | `1` | `1` | Enable the NUMA awareness in Teaming. |
| `/Net/TeamingIgnoreShotgun` | `integer` | `0` | `0` | Ignore the shotgun capability in Teaming |
| `/Net/SendIGMPReportToUplink` | `integer` | `0` | `0` | SendIGMPReportToUplink. |
| `/Net/BMCNetworkEnable` | `integer` | `1` | `1` | Enable BMC Network for Redfish |
| `/Net/Vmxnet3EnsRxMultipleContexts` | `integer` | `0` | `0` | Use multiple ENS contexts for vnic RX processing. |
| `/Net/CoalesceScheme` | `string` | `rbc` | `rbc` | Set the default vNic coalescing scheme. |
| `/Net/CoalesceParams` | `string` | `` | `` | Set parameters for the default vNic coalescing scheme. |
| `/Net/NetTuneHostMode` | `string` | `default` | `default` | Set tune mode for networking. |
| `/Net/NetTuneThreshold` | `string` | `1n 2n 50` | `1n 2n 50` | Set threshold in #vms, #vcpus, TotalUtil. n => numPCPUs |
| `/Net/IGMPRouterIP` | `string` | `0.0.0.0` | `0.0.0.0` | Router IP Address for IGMP (generally not necessary to set this) |
| `/Net/MLDRouterIP` | `string` | `FE80::FFFF:FFFF:FFFF:FFFF` | `FE80::FFFF:FFFF:FFFF:FFFF` | Router IPv6 Address for MLD (generally not necessary to set this) |
| `/Net/NetSchedDefaultSchedName` | `string` | `fifo` | `fifo` | Default scheduler name |
| `/Net/NetSchedQoSSchedName` | `string` | `hclk` | `hclk` | QoS scheduler name |
| `/Net/DVFilterBindIpAddress` | `string` | `` | `` | DVFilter internal communication endpoint |
| `/Net/TrafficFilterIpAddress` | `string` | `` | `` | DVFilter internal communication endpoint |
| `/Net/ProvisioningVmknics` | `string` | `` | `` | vmknics used by NFC for provisioning operations. |
| `/Net/PVRDMAVmknic` | `string` | `` | `` | Vmknic for PVRDMA |

</details>

<details><summary><strong>Subsystem: /Nmp (3 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Nmp/NmpPReservationCmdRetryTime` | `integer` | `1` | `1` | Time (in secs) to retry on transient errors for Persistent reservation commands for MSCS CAB configs |
| `/Nmp/NmpSatpAluaTransRetryTime` | `integer` | `10` | `10` | Time (in secs) to wait for ALUA transition to complete when target reports ALUA transitioning state |
| `/Nmp/NmpSatpAluaCmdRetryTime` | `integer` | `20` | `20` | Time (in secs) to retry on transient errors |

</details>

<details><summary><strong>Subsystem: /Numa (28 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Numa/RebalancePeriod` | `integer` | `2000` | `2000` | frequency of NUMA node rebalancing, in milliseconds |
| `/Numa/SwapInterval` | `integer` | `3` | `3` | frequency of NUMA node swap rebalancing, in units of NUMA rebalance period |
| `/Numa/SwapConsiderPeriod` | `integer` | `15` | `15` | time between reconsidering a client for swap, in units of NUMA rebalance period |
| `/Numa/SwapMigrateOnly` | `integer` | `2` | `2` | frequency of NUMA VM migration only considerations, in units of NUMA rebalance period, 0 to disable pure migrations |
| `/Numa/MigImbalanceThreshold` | `integer` | `10` | `10` | minimum percent load imbalance between nodes to trigger migration |
| `/Numa/MigThreshold` | `integer` | `2` | `2` | minimum percent load balance improvement to allow single migration/swap |
| `/Numa/MigThrashThreshold` | `integer` | `50` | `50` | maximum post-migration load imbalance, as percentage of pre-migration imbalance, to prevent thrashing |
| `/Numa/SwapLoadEnable` | `integer` | `1` | `1` | 1 to enable VM swaps across nodes to balance CPU load, 0 to disable |
| `/Numa/SwapLocalityEnable` | `integer` | `1` | `1` | 1 to enable VM swaps across nodes to improve memory locality, 0 to disable |
| `/Numa/RebalanceEnable` | `integer` | `1` | `1` | 1 to enable NUMA rebalancer, 0 to disable it |
| `/Numa/RebalanceCoresTotal` | `integer` | `4` | `4` | minimum number of total host cores required to enable NUMA rebalancer |
| `/Numa/RebalanceCoresNode` | `integer` | `2` | `2` | minimum number of cores per node required to enable NUMA rebalancer |
| `/Numa/MonMigEnable` | `integer` | `1` | `1` | 1 to allow NUMASched monitor migrations, 0 to disallow |
| `/Numa/CostopSkewAdjust` | `integer` | `1` | `1` | way to handle costop skew, 0:do nothing, 1:interleave vcpus among clients, 2:allow vcpus on all nodes |
| `/Numa/PageMigEnable` | `integer` | `1` | `1` | 1 to permit NUMASched to manipulate page migration, 0 to disallow it |
| `/Numa/PageMigRateMax` | `integer` | `8000` | `8000` | max page migrations per second |
| `/Numa/PageMigLinearRun` | `integer` | `95` | `95` | page migration candidates for linear scan, 0 to disable |
| `/Numa/PageMigRandomRun` | `integer` | `5` | `5` | page migration candidates for random scan, 0 to disable |
| `/Numa/LTermFairnessInterval` | `integer` | `5` | `5` | duration of long term fairness interval in terms of NUMA rebalance period, 0 indicates that long term fairness is disabled |
| `/Numa/LTermMigImbalThreshold` | `integer` | `10` | `10` | imbalance in long term owed, in percentage, required to trigger migration for long term fairness |
| `/Numa/MigPreventLTermThresh` | `integer` | `0` | `0` | increase in long term imbalance, in percentage, above which NUMA migration and swaps are not allowed |
| `/Numa/CoreCapRatioPct` | `integer` | `90` | `90` | The capacity of a core in percent. When exceeded, locality migration is rejected. Set to 0 to disable this check |
| `/Numa/LocalityWeightMem` | `integer` | `1` | `1` | Benefit of improving memory locality by 1 pct. |
| `/Numa/LocalityWeightActionAffinity` | `integer` | `130` | `130` | Benefit of improving action affinity by 1. |
| `/Numa/LatencyProbePeriod` | `integer` | `500` | `500` | NUMA latency probing period in ms. |
| `/Numa/LargeInterleave` | `integer` | `1` | `1` | Always use large page interleaving; 0 to disable. |
| `/Numa/PreferHT` | `integer` | `0` | `0` | Prefer using HyperThreads on the same NUMA node over full cores on multiple nodes; 0 to disable. |
| `/Numa/FollowCoresPerSocket` | `integer` | `0` | `0` | 1: if the vNUMA topology should strickly follow core-per-socket config, 0: to remove the restriction |

</details>

<details><summary><strong>Subsystem: /Power (12 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Power/UsePStates` | `integer` | `1` | `1` | In Custom policy, use ACPI P-states to save power when processor is busy |
| `/Power/UseCStates` | `integer` | `1` | `1` | In Custom policy, use ACPI C-states when processor is idle |
| `/Power/MaxCpuLoad` | `integer` | `60` | `60` | In Custom policy, CPU utilization threshold below which CPU frequency can be dynamically adjusted |
| `/Power/MinFreqPct` | `integer` | `0` | `0` | In Custom policy, do not use P-states slower than the given percentage of full CPU speed |
| `/Power/MaxFreqPct` | `integer` | `100` | `100` | In Custom policy, do not use P-states faster than the given percentage of full CPU speed, rounded up to the next available P-state |
| `/Power/TimerHz` | `integer` | `100` | `100` | In Custom policy, dynamic power management timer sampling rate |
| `/Power/CStateMaxLatency` | `integer` | `1000` | `1000` | In Custom policy, avoid a C-state whose latency is larger than this value (us) |
| `/Power/CStateResidencyCoef` | `integer` | `5` | `5` | In Custom policy, avoid a C-state whose latency * CStateResidencyCoef > predicted residence time |
| `/Power/CStatePredictionCoef` | `integer` | `110479` | `110479` | In Custom policy, predict non-timer wakeup with error probability p, where CStatePredictionCoef = -ln(1 - p) * (1 << 20) |
| `/Power/PerfBias` | `integer` | `16` | `17` | In Custom policy, Performance Energy Bias Hint, where 0-15 directly specifies preference on a scale where 0=MaxPerf and 15=MinPower, while 16-18 chooses an automatically determined value from a preset policy: 16=Low Power, 17=Balanced, 18=High Performance |
| `/Power/PerfBiasEnable` | `integer` | `1` | `1` | Use Performance Energy Bias Hint |
| `/Power/CpuPolicy` | `string` | `Low Power` | `Balanced` | Host power management policy: High Performance, Balanced, Low Power, or Custom |

</details>

<details><summary><strong>Subsystem: /Scsi (42 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Scsi/PassthroughLocking` | `integer` | `1` | `1` | Disable locking for scsi passthrough devices |
| `/Scsi/LogCmdErrors` | `integer` | `1` | `1` | Log SCSI Device command errors. |
| `/Scsi/TransFailLogPct` | `integer` | `20` | `20` | Percent of Transient failures seen on Scsi Device that will be logged. |
| `/Scsi/LogCmdRCErrorsFreq` | `integer` | `0` | `0` | Number of consecutive RC errors to be seen before logging SCSI Device command. |
| `/Scsi/LogMPCmdErrors` | `integer` | `1` | `1` | Log SCSI Multi-path plugin command errors. |
| `/Scsi/LogScsiAborts` | `integer` | `0` | `0` | Log SCSI abort errors and success. |
| `/Scsi/MaxReserveTime` | `integer` | `200` | `200` | Maximum time (in msecs) a system-initiated reservation is normally held (debug only) |
| `/Scsi/MaxReserveTotalTime` | `integer` | `250` | `250` | Maximum time (in msecs) a system-initiated reservation normally takes from issue to release (debug only) |
| `/Scsi/MaxReserveBacktrace` | `integer` | `0` | `0` | Log a backtrace if caller exceeds SCSI_MAX_RESERVE_TIME or SCSI_MAX_RESERVE_TOTALTIME (debug only) |
| `/Scsi/ReserveBacktrace` | `integer` | `0` | `0` | Log a backtrace for all Reserve/Release pairs (debug only) |
| `/Scsi/SCSITimeout_ScanTime` | `integer` | `1000` | `1000` | time (in ms) to sleep between checking for timed-out async IO |
| `/Scsi/SCSITimeout_ReabortTime` | `integer` | `5000` | `5000` | delay (in ms) after an abort due to timeout before the abort is re-issued |
| `/Scsi/ScanOnDriverLoad` | `integer` | `1` | `1` | Scan new SCSI buses on device driver load |
| `/Scsi/TimeoutTMThreadMin` | `integer` | `1` | `1` | Min number of timeout task-mgmt handler threads |
| `/Scsi/TimeoutTMThreadMax` | `integer` | `16` | `16` | Max number of timeout task-mgmt handler threads |
| `/Scsi/TimeoutTMThreadExpires` | `integer` | `1800` | `1800` | Life in seconds of timeout task mgmt handler thread |
| `/Scsi/TimeoutTMThreadRetry` | `integer` | `2000` | `2000` | Delay in milliseconds before retrying taskmgmt which failed or for which the I/O did not complete |
| `/Scsi/TimeoutTMThreadLatency` | `integer` | `2000` | `2000` | Delay in ms before waking up new task mgmt thread |
| `/Scsi/LunCleanupInterval` | `integer` | `7` | `7` | Timeout interval for lun entries in esx.conf. Any lun entry which was seen more than the configured no. of days ago, will be deleted by the daily cleanup operation |
| `/Scsi/ScsiRestartStalledQueueLatency` | `integer` | `500` | `500` | Delay in ms before restarting a stalled queue |
| `/Scsi/CompareLUNNumber` | `integer` | `1` | `1` | Consider LUN number when determining LUN identity. |
| `/Scsi/UseAdaptiveRetries` | `integer` | `1` | `1` | Use adaptive retries for transient errors. |
| `/Scsi/ChangeQErrSetting` | `integer` | `1` | `1` | Change the QErr value of devices to 0x0. |
| `/Scsi/ScanSync` | `integer` | `0` | `0` | Force LU scanning operations to be synchronous if set. |
| `/Scsi/FailVMIOonAPD` | `integer` | `0` | `0` | Fast fail VM IOs on APD Timeout. |
| `/Scsi/ScsiVVolPESNRO` | `integer` | `256` | `256` | Default schedNumReqOutstanding value for a PE LUN. |
| `/Scsi/SCSIStrictSPCVersionChecksForPEs` | `integer` | `0` | `0` | Only LUNs with version >= SCSI_ANSI_SCSI3_SPC4 can be PEs |
| `/Scsi/SCSIEnableDescToFixedConv` | `integer` | `1` | `1` | Enable or disable conversion of descriptor format sense to fixed for older plugins |
| `/Scsi/EnableCmdSanityCheck` | `integer` | `0` | `0` | Enable Scsi command basic sanity checks. This option can crash the system if Scsi Command signature mismatches. |
| `/Scsi/SCSIioTraceBufSizeMB` | `integer` | `1` | `1` | Logchannel buffer size for per device IO tracing in MB |
| `/Scsi/ScsiPathSplitUseSimpleCloneBuffer` | `integer` | `1` | `1` | Use simple clone buffers to split IOs at path layer whenever possible. |
| `/Scsi/ExtendAPDCondition` | `integer` | `0` | `0` | Trigger APD condition when paths are in unavailable states |
| `/Scsi/ScsiAllowDeviceSpinup` | `integer` | `1` | `1` | Allow device spin up, if device is in spun down state. |
| `/Scsi/ScsiUseVPDXCopyInfo` | `integer` | `1` | `1` | Use Scsi VPD query for XCopy Info. |
| `/Scsi/NvmeLogVerbose` | `integer` | `0` | `0` | Enable verbose logging for NVMe devices. This is a bitwise value and can be combined. 1 = Log every command, 2 = Log ANA log page, 4 = Log ANA log page namespace list, 8 = Verbose logging |
| `/Scsi/ScsiTMHardTimeout` | `integer` | `120000` | `120000` | Timeout in milliseconds before signalling upper layers of wedged I/O (0 = Signalling disabled). |
| `/Scsi/SCSIEnableDeviceLatencyHistogram` | `integer` | `1` | `1` | Enable or disable updation of device latency histograms |
| `/Scsi/SCSIBlockUnsupportedOpcodesAndPages` | `integer` | `1` | `1` | Enable or disable blocking unsupported SCSI opcodes and vpd/mode pages |
| `/Scsi/NvmeAdjustLocalNSQDepth` | `integer` | `1` | `1` | Allow dividing the controller queue depth among the namespaces behind the controller for NVMe Local devices. |
| `/Scsi/PcpusPerCompletionWorld` | `integer` | `4` | `4` | Allocate number of storage adapter completion worlds based on pcpus per world across NUMA nodes. |
| `/Scsi/NvmeMaxUnmapLbaCount` | `integer` | `0` | `0` | Set maximum deallocate(unmap) size limit (in blocks) |
| `/Scsi/NvmeMaxUnmapBlockDescriptorCount` | `integer` | `0` | `0` | Set maximum deallocate(unmap) descriptor count limit |

</details>

<details><summary><strong>Subsystem: /SunRPC (4 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/SunRPC/WorldAffinity` | `integer` | `2` | `2` | TX Affinity: 0 - Disabled, 1 - Issuing world, 2 - Exact RX world |
| `/SunRPC/MaxConnPerIP` | `integer` | `32` | `32` | Max number of TCP/IP connection per IP |
| `/SunRPC/SendLowat` | `integer` | `25` | `25` | Send buffer lowat (%) |
| `/SunRPC/SetNoDelayedAck` | `integer` | `0` | `0` | Set socket option to disable TCP delayed acknowledgements (Set this option under guidance of VMware Support. Requires Remount) |

</details>

<details><summary><strong>Subsystem: /SvMotion (1 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/SvMotion/SvMotionAvgDisksPerVM` | `integer` | `8` | `8` | Initial Storage vMotion Heap Size is proportional to this setting |

</details>

<details><summary><strong>Subsystem: /USB (3 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/USB/arbitratorAutoStartDisabled` | `integer` | `0` | `0` | Disable automatic start of USB Arbitrator.  If set USB passthrough will not be available until USB arbitrator is started at the command line. |
| `/USB/devsShared` | `string` | `0x04b3:0` | `0x04b3:0` | Enable sharing (aka, non-exclusive claiming) of USB devices with specified vendor and model ids.  0x0 is a wild card model which matches all models from the specified vendor.  Default value is IBM and string must contain colon delimited numeric fields, respectively the vendor_id and product id.  If the latter is omitted from the last pair it is assumed to be 0x0. |
| `/USB/quirks` | `string` | `` | `` | USB quirks: 5 (or an integer multiple of 5; e.g., 10) colon delimited fields, 4 numeric (vendor id, product id, lowest revision affected, highest revision affected) followed by a quirk name string of the form UQ_... where ... are a series of uppercase letters and underscores which MUST exactly match an existing quirk name (contact VMware support for a full list of valid quirk names).  Multiple quirks can be concatenated by interposing a SINGLE colon as a delimiter. |

</details>

<details><summary><strong>Subsystem: /UserVars (28 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/UserVars/ActiveDirectoryPreferredDomainControllers` | `string` | `` | `` | Preferred Domain Controllers for Active Directory |
| `/UserVars/ActiveDirectoryVerifyCAMCertificate` | `integer` | `1` | `1` | Enable or disable verification of SSL certificate for vSphere Authentication Proxy server |
| `/UserVars/AuditApiCallEnabled` | `integer` | `0` | `0` | This option controls the emission of the api.call audit event. A reboot is required for this setting to take affect. |
| `/UserVars/DcuiTimeOut` | `integer` | `600` | `600` | Idle time before DCUI is automatically logged out (in seconds, 0 disables). |
| `/UserVars/ESXiShellInteractiveTimeOut` | `integer` | `0` | `0` | Idle time before an interactive shell is automatically logged out (in seconds, 0 disables).  Takes effect only for newly logged in sessions. |
| `/UserVars/ESXiShellTimeOut` | `integer` | `0` | `0` | Time before automatically disabling local and remote shell access (in seconds, 0 disables).  Takes effect after the services are restarted. |
| `/UserVars/ESXiVPsAllowedCiphers` | `string` | `ECDHE+AESGCM:ECDHE+AES` | `ECDHE+AESGCM:ECDHE+AES` | ESXi VPs allowed ciphers. List of allowed ciphers tobe used by the VPs. Must bein the form accepted by theSSL_CTX_set_cipher_list API. |
| `/UserVars/ESXiVPsDisabledProtocols` | `string` | `sslv3,tlsv1,tlsv1.1` | `sslv3,tlsv1,tlsv1.1` | ESXi VPs disabled protocols (Deprecated). All protocols prior to tlsv1.2 are no longer supported and must remain disabled. |
| `/UserVars/EsximageNetRateLimit` | `integer` | `0` | `0` | Set the maximum rate, in bytes/sec, for downloading VIBs (0=no limit) |
| `/UserVars/EsximageNetRetries` | `integer` | `10` | `10` | Set the number of times to retry in case of failure while downloading VIBs |
| `/UserVars/EsximageNetTimeout` | `integer` | `60` | `60` | Set the timeout in seconds for downloading VIBs (0=no timeout) |
| `/UserVars/HardwareHealthIgnoredSensors` | `string` | `` | `` | List of comma-seperated sensor ID's to ignore for alarm generation. |
| `/UserVars/HardwareHealthSyncTime` | `integer` | `360` | `360` | Time to refresh hardware health sensor state with VC(in minutes, 0 disables). |
| `/UserVars/HostClientCEIPOptIn` | `integer` | `2` | `0` | Whether or not to opt-in for CEIP in Host Client, 0 for ask, 1 for yes, 2 for no |
| `/UserVars/HostClientDefaultConsole` | `string` | `webmks` | `webmks` | Default console type in Host Client |
| `/UserVars/HostClientEnableMOTDNotification` | `integer` | `1` | `1` | Whether or not to enable MOTD notification on login for Host Client |
| `/UserVars/HostClientEnableVisualEffects` | `integer` | `1` | `1` | Whether or not to enable visual effects for Host Client |
| `/UserVars/HostClientSessionTimeout` | `integer` | `0` | `900` | Default timeout for Host Client sessions in seconds |
| `/UserVars/HostClientShowOnlyRecentObjects` | `integer` | `0` | `1` | Whether or not to show only recent objects in Host Client |
| `/UserVars/HostClientWelcomeMessage` | `string` | `Welcome to {{hostname}}` | `Welcome to {{hostname}}` | Welcome message displayed on login in Host Client |
| `/UserVars/HostdStatsstoreRamdiskSize` | `integer` | `0` | `0` | Set the size, in megabytes, of the ramdisk used to store hostd stats (0=use default) |
| `/UserVars/SuppressCoredumpWarning` | `integer` | `0` | `0` | Don't show warning for disabled or unconfigured coredump target |
| `/UserVars/SuppressHyperthreadWarning` | `integer` | `1` | `0` | Don't show warning for potential security vulnerability due to hyperthreading |
| `/UserVars/SuppressSgxAddPackageWarning` | `integer` | `0` | `0` | Don't show warning about SGX disabled on host due to the addition of a CPU package. |
| `/UserVars/SuppressSgxDisabledWarning` | `integer` | `0` | `0` | Don't show warning about SGX disabled on host due to Intel Errata CFW101. |
| `/UserVars/SuppressShellWarning` | `integer` | `1` | `0` | Don't show warning for enabled local and remote shell access |
| `/UserVars/ToolsRamdisk` | `integer` | `0` | `0` | Use VMware Tools repository from /tools ramdisk. |
| `/UserVars/ProductLockerLocation` | `string` | `/locker/packages/vmtoolsRepo/` | `/locker/packages/vmtoolsRepo/` | Path to VMware Tools repository |

</details>

<details><summary><strong>Subsystem: /VFLASH (5 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/VFLASH/MaxCacheFileSizeMB` | `integer` | `409600` | `409600` | Maximum VFC cache file size (in MB) supported |
| `/VFLASH/MaxHeapSizeMB` | `integer` | `32` | `32` | Maximum size (in MB) to which the vFlash heap is allowed to grow |
| `/VFLASH/CacheStatsEnable` | `integer` | `1` | `1` | vFlash cache statistics enable ? |
| `/VFLASH/CacheStatsFromVFC` | `integer` | `1` | `1` | Use cache statistics from VFC module ? |
| `/VFLASH/MaxDiskFileSizeGB` | `integer` | `16384` | `16384` | Maximum supported disk size (in GB) with vFlash configuration |

</details>

<details><summary><strong>Subsystem: /VMFS3 (13 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/VMFS3/OpenWithoutJournal` | `integer` | `1` | `1` | Open file system when out of space for journal allocation, allowing reads and no meta-data updates |
| `/VMFS3/MaxHeapSizeMB` | `integer` | `768` | `768` | Maximum size (in MB) to which the VMFS heap is allowed to grow |
| `/VMFS3/MaxextendedTxnsUsingfs3Heap` | `integer` | `20` | `20` | Maximum number of extended transactions for which log space can be allocated from VMFS3 heap when the extendedTxnRegion is full |
| `/VMFS3/StAtExclLockEnd` | `integer` | `0` | `0` | Generate Back Trace in FS3_EndIOExclusive |
| `/VMFS3/MaxAddressableSpaceTB` | `integer` | `32` | `32` | Maximum size of all open files that VMFS cache will support before eviction mechanisms kicks in. |
| `/VMFS3/MinAddressableSpaceTB` | `integer` | `0` | `0` | Minimum size of all open files that VMFS cache will support. |
| `/VMFS3/PBCapMissRatioIntervalSec` | `integer` | `60` | `60` | Frequency (in seconds) that the Capacity Miss Ratio is computed for the VMFS Pointer Block cache. |
| `/VMFS3/HardwareAcceleratedLocking` | `integer` | `1` | `1` | Enable hardware accelerated VMFS locking (requires compliant hardware). Please see http://kb.vmware.com/kb/2094604 before disabling this option. |
| `/VMFS3/FailVolumeOpenIfAPD` | `integer` | `0` | `0` | Fail VMFS volume open operation if the underlying device is deemed to be under an all-paths-down condition |
| `/VMFS3/EnableBlockDelete` | `integer` | `0` | `0` | Enable VMFS block delete when UNMAP is issued from guest OS |
| `/VMFS3/GBLAllowMW` | `integer` | `1` | `1` | Allow multi-writer GBLs. |
| `/VMFS3/UseATSForHBOnVMFS5` | `integer` | `1` | `1` | Use ATS for HB on ATS supported VMFS5 volumes |
| `/VMFS3/LFBCSlabSizeMaxMB` | `integer` | `8` | `8` | Maximum size (in MB) to which the VMFS affinity manager cluster cache is allowed to grow. |

</details>

<details><summary><strong>Subsystem: /VSAN (50 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/VSAN/ClomMaxComponentSizeGB` | `integer` | `255` | `255` | Maximum component size used for new placements |
| `/VSAN/ClomRebalanceThreshold` | `integer` | `80` | `80` | Percentage disk fullness after which rebalancing is triggered |
| `/VSAN/ClomMaxDiskUsageRepairComps` | `integer` | `95` | `95` | Max percentage disk fullness that can be reached for object repairs |
| `/VSAN/ClomForceProvisionPlacements` | `integer` | `0` | `0` | Add force Provision flag to all new object placements |
| `/VSAN/MaxComponentsPerWitness` | `integer` | `0` | `0` | Maximum number of components per witness host (0: default to 64000 with scaling based on memory) |
| `/VSAN/MaxWitnessClusters` | `integer` | `0` | `0` | Max number of clusters on a witness node (0: default to 64 clusters) |
| `/VSAN/AutoRestoreDecomState` | `integer` | `1` | `1` | Whether to restore vSAN node decommission state automatically during vSAN refresh |
| `/VSAN/DomLongOpTraceMS` | `integer` | `1000` | `1000` | Trace ops that take more than the specified value in milliseconds |
| `/VSAN/DomLongOpUrgentTraceMS` | `integer` | `10000` | `10000` | Urgent trace ops that take more than the specified value in milliseconds |
| `/VSAN/DomBriefIoTraces` | `integer` | `0` | `0` | Enables a brief set of per-IO DOM traces for debugging |
| `/VSAN/DomFullIoTraces` | `integer` | `0` | `0` | Enables full set of per-IO DOM traces; if disabled, IO op traces go to the per-op trace table |
| `/VSAN/TraceEnableDom` | `integer` | `1` | `1` | DOM tracing enabled |
| `/VSAN/TraceEnableDomIo` | `integer` | `0` | `0` | DOMIO tracing enabled |
| `/VSAN/TraceEnableLsom` | `integer` | `1` | `1` | LSOM tracing enabled |
| `/VSAN/TraceEnableLsomIo` | `integer` | `0` | `0` | Enables IO tracing for vSAN LSOM component |
| `/VSAN/TraceEnableCmmds` | `integer` | `1` | `1` | CMMDS/CMMDSResolver tracing enabled |
| `/VSAN/TraceEnableRdt` | `integer` | `1` | `1` | RDT tracing enabled |
| `/VSAN/TraceEnablePlog` | `integer` | `1` | `1` | PLOG tracing enabled |
| `/VSAN/TraceEnableSsdLog` | `integer` | `1` | `1` | SSDLOG tracing enabled |
| `/VSAN/TraceEnableVirsto` | `integer` | `1` | `1` | Virsto tracing enabled |
| `/VSAN/TraceEnableVirstoIo` | `integer` | `0` | `0` | Enables IO tracing for vSAN Virsto component |
| `/VSAN/TraceGlobalBandwidthLimit` | `integer` | `0` | `0` | Max number of traces per second (0 to disable limits) |
| `/VSAN/TraceGlobalBandwidthLimitPeriodMs` | `integer` | `10000` | `10000` | Add BANDWIDTH_LIMIT * PERIOD_MS tokens (traces) every PERIOD_MS. |
| `/VSAN/TraceGlobalMaxRolloverPeriods` | `integer` | `360` | `360` | Maximum number of periods where unused bandwidth can accumulate |
| `/VSAN/PerTraceBandwidthLimit` | `integer` | `0` | `0` | Max number of traces per second (0 to disable limits) |
| `/VSAN/PerTraceBandwidthLimitPeriodMs` | `integer` | `10000` | `10000` | Add BANDWIDTH_LIMIT * PERIOD_MS tokens (traces) every PERIOD_MS. |
| `/VSAN/PerTraceMaxRolloverPeriods` | `integer` | `360` | `360` | Maximum number of periods where unused bandwidth can accumulate |
| `/VSAN/TracesPerErrorBandwidthLimit` | `integer` | `1000` | `1000` | Max number of traces per second during specific error conditions (0 to disable limits) |
| `/VSAN/TracesPerErrorBandwidthLimitPeriodMs` | `integer` | `10000` | `10000` | Add BANDWIDTH_LIMIT * PERIOD_MS tokens (traces) every PERIOD_MS |
| `/VSAN/TracesPerErrorMaxRolloverPeriods` | `integer` | `60` | `60` | Maximum number of periods where unused bandwidth can accumulate |
| `/VSAN/RDTChecksumMode` | `integer` | `1` | `1` | Checksum mode for RDT-level checksum. 0 - Off, 1 - Only header, 2 - Header and partial payload, 3 - All. |
| `/VSAN/ObjectScrubsPerYear` | `integer` | `0` | `0` | Config option to set the scrub rate for DOM scrubber. A Non-zero value will override diskgroup utilization based scrubbing. |
| `/VSAN/ObjectScrubsPerYearBase` | `integer` | `36` | `36` | Config option to set scrubs per year for diskgroup usage below ScrubBaseDGUsedCapacity. |
| `/VSAN/VsanSparseEnabled` | `integer` | `1` | `1` | Enable auto-creation of vsanSparse instead of vmfsSparse redologs, for vSAN 2.0 datastore only |
| `/VSAN/VsanSparseCacheThreshold` | `integer` | `1024` | `1024` | Maximum number of nodes in single VsanSparse cache, each node holds up-to 256 entries |
| `/VSAN/VsanSparseCacheOverEvict` | `integer` | `5` | `5` | Percentage of VsanSparseCacheThreshold to add to eviction |
| `/VSAN/VsanSparseSpeculativePrefetch` | `integer` | `4194304` | `4194304` | Number of bytes to add onto each extent interrogation request |
| `/VSAN/VsanSparseMaxExtentsPrefetch` | `integer` | `64` | `64` | Maximum number of extents to fetch during interrogation |
| `/VSAN/VsanSparseParallelLookup` | `integer` | `1` | `1` | Request written extent data from each layer in parallel |
| `/VSAN/TraceEnableVsanSparse` | `integer` | `1` | `1` | VsanSparse tracing enabled |
| `/VSAN/TraceEnableVsanSparseIO` | `integer` | `0` | `0` | VsanSparse per-IO tracing enabled |
| `/VSAN/TraceEnableVsanSparseVerbose` | `integer` | `0` | `0` | VsanSparse very verbose tracing enabled |
| `/VSAN/VsanSparseHeapSize` | `integer` | `65536` | `65536` | Maximum heap size for VsanSparse snapshot consolidation buffers(in KiB) |
| `/VSAN/VsanSparseRetainCacheOnSnapshots` | `integer` | `1` | `1` | Try to retain VsanSparse in-memory cache content when taking VM snapshots |
| `/VSAN/VsanSparseRetainCacheTTL` | `integer` | `20` | `20` | Maximum time to retain VsanSparse in-memory cache content between snapshots, in seconds |
| `/VSAN/DedupScope` | `integer` | `0` | `0` | Dedup Scope for all-flash disk groups |
| `/VSAN/AutoTerminateGhostVm` | `integer` | `1` | `1` | Automatically terminate ghost vm(s) during network partition |
| `/VSAN/TrimDisksBeforeUseGranularity` | `integer` | `0` | `0` | Trim the devices (if supported) before using for vSAN. 0=Disable, 1=MetaData only, 2=Full Disk |
| `/VSAN/WriteZeroOnTrimUnsupported` | `integer` | `0` | `0` | Enable Writing Zero's on capacity devices that do not support TRIM |
| `/VSAN/DefaultHostDecommissionMode` | `string` | `ensureAccessibility` | `ensureAccessibility` | Default host decommission mode for this host |

</details>

<details><summary><strong>Subsystem: /VSAN-iSCSI (1 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/VSAN-iSCSI/iscsiPingTimeout` | `integer` | `5` | `5` | Interval between ping (NOP-Out) requests, in seconds |

</details>

<details><summary><strong>Subsystem: /VVOL (6 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/VVOL/vvolUnbindBatchSize` | `integer` | `16` | `16` | Batch size for the Batch unbinding for VVOLs |
| `/VVOL/vvolConcurrentBatchUnbind` | `integer` | `2` | `2` | Number of concurrent batch unbind requests |
| `/VVOL/vvolMaxRBZRetries` | `integer` | `100` | `100` | Maximum number of times RBZ is retried during Rebind |
| `/VVOL/vvolSpaceStatsCacheSize` | `integer` | `512` | `512` | Size of the swap VVOL cache in (must be <= 1024) VVOLD |
| `/VVOL/allowLegacyCiphers` | `integer` | `0` | `0` | Allow vVOL daemon to use legacy cipher for TLS communication with VASA Provider [Warning: Non-PFS ciphers!] |
| `/VVOL/vvolSwapFilePersist` | `integer` | `1` | `1` | Disable deletion of swap file on vVol datastore when the VM powers off (1 to disable). |

</details>

<details><summary><strong>Subsystem: /Virsto (11 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/Virsto/Enabled` | `integer` | `1` | `1` | Use Virsto format for new disks |
| `/Virsto/DiskFormatVersion` | `integer` | `20` | `20` | Virsto Disk Format version |
| `/Virsto/SharedHeapLimit` | `integer` | `4` | `4` | Shared heap limit for Virsto module in MB |
| `/Virsto/InstanceHeapLimit` | `integer` | `130` | `130` | Heap limit for each Virsto instance in MB |
| `/Virsto/MsecBeforeMetaFlush` | `integer` | `10000` | `10000` | Force Virsto metadata flush after this many msec |
| `/Virsto/GweFetchExtentsFactor` | `integer` | `3` | `3` | Multiplier controlling how many on-disk extents fetched based on GWE request size |
| `/Virsto/MapBlocksMin` | `integer` | `16384` | `16384` | Map block cache minimum for each Virsto instance (in count of 4KB blocks) |
| `/Virsto/MapBlocksFlushThreshold` | `integer` | `90` | `90` | Map block cache dirty entries threshold when metadata flush is forced (percent) |
| `/Virsto/FlusherRegistryThreshold` | `integer` | `95` | `95` | Flusher registry data size threshold (percentage) when metadata flush is forced |
| `/Virsto/RecordsPerFormatWrite` | `integer` | `16` | `16` | Number of (LSAR) records written per format write operation |
| `/Virsto/MaxMFRetryCount` | `integer` | `3` | `3` | How many times Virsto metadata flusher would retry in case of transient error |

</details>

<details><summary><strong>Subsystem: /XvMotion (1 options)</strong></summary>

| Path | Type | Current Value | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/XvMotion/VMFSOptimizations` | `integer` | `1` | `1` | Enable VMFS-specific IO optimizations |

</details>
