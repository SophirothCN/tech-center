kvm
#########



在 Centos7 的KVM上启用嵌套虚拟化
```````````````````````````````````

嵌套虚拟化意味着在虚拟机内配置虚拟化环境。换句话说，我们可以说嵌套虚拟化是虚拟机管理程序hypervisor的一个特性，它允许我们通过虚拟化管理程序（宿主机）的硬件加速在虚拟服务器内安装和运行虚拟机。

在这篇文章中，我们将讨论如何在 CentOS 7 / RHEL 7 的 KVM 上启用嵌套虚拟化。我假定您已经配置过 KVM 管理程序。如果您不熟悉如何安装和配置 KVM 管理程序，请参考以下文章。

在 CentOS 7.x 和 RHEL 7.x 安装 KVM 管理程序
让我们进入虚拟化管理程序，验证您的 KVM 宿主机是否启用了嵌套虚拟化。

基于 Intel 的处理器运行以下命令：

[root@kvm-hypervisor ~]# cat /sys/module/kvm_intel/parameters/nested
N
基于 AMD 的处理器运行以下命令：

[root@kvm-hypervisor ~]# cat /sys/module/kvm_amd/parameters/nested
N
上述命令输出 N 表示嵌套虚拟化是禁用的。如果我们得到的输出是 Y 则表示在您的宿主机已启用嵌套虚拟化。

现在启用嵌套虚拟化，使用以下内容创建一个文件名为 /etc/modprobe.d/kvm-nested.conf 的文件：

[root@kvm-hypervisor ~]# vi /etc/modprobe.d/kvm-nested.conf
options kvm-intel nested=1
options kvm-intel enable_shadow_vmcs=1
options kvm-intel enable_apicv=1
options kvm-intel ept=1
保存并退出文件。

现在移除 kvm_intel 模块然后通过 modprobe 命令添加同样的模块。在移除模块之前，确保虚拟机已关机，否则我们会得到像 “modprobe: FATAL: Module kvm_intel is in use” 这样的错误信息。

[root@kvm-hypervisor ~]# modprobe -r kvm_intel
[root@kvm-hypervisor ~]# modprobe -a kvm_intel
现在验证嵌套虚拟化功能是否启用。

[root@kvm-hypervisor ~]# cat /sys/module/kvm_intel/parameters/nested
Y