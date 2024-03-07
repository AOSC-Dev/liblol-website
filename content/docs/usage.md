---
title: 使用教程
toc: true
weight: 1
---

## 安装libLoL

本节介绍各系统环境下安装 libLoL 的方式。

### AOSC OS

AOSC OS 在主软件仓库提供 libLoL，使用如下命令安装即可使用：

```
oma install liblol
```

### Debian

首先，下载内核模块包 [liblol-dkms_0.1.0_loong64.deb](https://github.com/AOSC-Dev/la_ow_syscall/releases/download/debian%2F0.1.0/liblol-dkms_0.1.0_loong64.deb) 并执行如下命令安装：

```
sudo apt install ./liblol-dkms_0.1.0_loong64.deb
```

安装完成后，下载 libLoL 运行时包 [liblol_0.1.4-1_loong64.deb](https://github.com/AOSC-Dev/liblol/releases/download/debian%2Fv0.1.4-1/liblol_0.1.4-1_loong64.deb)，随后执行如下命令安装：

```
sudo apt install ./liblol_0.1.4-1_loong64.deb
```

### Loong Arch Linux

Loong Arch Linux 在其软件仓库中提供 libLoL，使用如下命令即可安装：

```
sudo pacman -S la_ow_syscall-dkms liblol
```

## 安装应用

您可在[龙芯应用合作社](http://app.loongapps.cn/#/home)或其他分发渠道下载和安装旧世界应用。

## 应用兼容性

考虑到 libLoL 仍在开发过程中，应用程序兼容性尚不完善，测试工作也有待完善。

因此，一部分应用可能无法运行或需要执行额外操作才能运行。详情请参考[应用兼容性数据库](/docs/apps)。

## 运行应用

在完成上述步骤后您就可以在“新世界”享受“旧世界”应用了！

如果您在使用过程中遇到问题，请向我们[报告兼容性问题](/docs/report/)。
