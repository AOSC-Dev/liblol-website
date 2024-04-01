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

由于不同发行版的目录布局各异，不同发行版上的 libLoL 库搜索路径之间也存在不同。AOSC OS 上 libLoL 的库搜索路径如下：

<!-- see https://github.com/AOSC-Dev/liblol/blob/v0.1.5_pre6/autobuild/build -->

|加载阶段|路径（从上到下顺序搜索）|
|:------:|:---|
|优先|<ul><li><code>/opt/lol/local/preload-lib</code></li><li><code>/opt/lol/support/lib/loongarch64-aosc-linux-gnuow</code></li></ul>|
|正常|<ul><li><code>/opt/lol/local/lib</code></li><li><code>/opt/lol/lib/loongarch64-aosc-linux-gnuow</code></li><li><code>/opt/lol/lib</code></li></ul>|

其中带有 `local` 字样的目录可供用户自助放置一些库文件，以便绕过个别应用所存在的问题。

### Debian

首先，下载内核模块包 [liblol-dkms_0.1.0_loong64.deb](https://github.com/AOSC-Dev/la_ow_syscall/releases/download/debian%2F0.1.0/liblol-dkms_0.1.0_loong64.deb) 并执行如下命令安装：

```
sudo apt install ./liblol-dkms_0.1.0_loong64.deb
```

安装完成后，下载 libLoL 运行时包 [liblol_0.1.4-1_loong64.deb](https://github.com/AOSC-Dev/liblol/releases/download/debian%2Fv0.1.4-1/liblol_0.1.4-1_loong64.deb)，随后执行如下命令安装：

```
sudo apt install ./liblol_0.1.4-1_loong64.deb
```

由于不同发行版的目录布局各异，不同发行版上的 libLoL 库搜索路径之间也存在不同。Debian 上 libLoL 的库搜索路径如下：

<!-- see https://github.com/AOSC-Dev/liblol/blob/debian/v0.1.5_pre6-1/debian/rules -->

|加载阶段|路径（从上到下顺序搜索）|
|:------:|:---|
|优先|<ul><li><code>/usr/local/lib/loongarch64-debian-linux-gnuow/preload</code></li><li><code>/usr/lib/loongarch64-debian-linux-gnuow/preload</code></li></ul>|
|正常|<ul><li><code>/usr/local/lib/loongarch64-debian-linux-gnuow</code></li><li><code>/usr/lib/loongarch64-debian-linux-gnuow</code></li></ul>|

其中带有 `local` 字样的目录可供用户自助放置一些库文件，以便绕过个别应用所存在的问题。

### Gentoo

目前，libLoL 的打包工作在 [`gentoo-zh` overlay](https://github.com/microcai/gentoo-zh)
进行。如果您尚未引入此 overlay，可执行以下命令配置：

```shell-session
# eselect repository enable gentoo-zh
# emerge --sync
```

如果您不想放行 overlay 中的其他包，可以配置仅允许 libLoL 相关的包：

```
# /etc/portage/package.mask
*/*::gentoo-zh

# /etc/portage/package.unmask
app-emulation/la-ow-syscall::gentoo-zh
app-emulation/liblol::gentoo-zh
app-emulation/liblol-glibc::gentoo-zh
app-emulation/liblol-libxcrypt::gentoo-zh
virtual/loong-ow-compat::gentoo-zh
```

后续对于 `RDEPEND` 内含 `virtual/loong-ow-compat` 标记的软件包，直接安装即可。libLoL
会被拉入依赖关系图，从而受到 Portage 自动管理，无需手工干预。

如您确有需要显式安装、手工管理 libLoL，也可执行如下命令实现：

```shell-session
# emerge app-emulation/liblol
```

由于不同发行版的目录布局各异，不同发行版上的 libLoL 库搜索路径之间也存在不同。Gentoo
的 `loong` LP64D profiles 上，libLoL 的库搜索路径如下：

|加载阶段|路径（从上到下顺序搜索）|
|:------:|:---|
|优先|<ul><li><code>/opt/lol/local/lib64/preload</code></li><li><code>/opt/lol/lib64/preload</code></li></ul>|
|正常|<ul><li><code>/opt/lol/local/lib64</code></li><li><code>/opt/lol/lib64</code></li></ul>|

其中带有 `local` 字样的目录可供用户自助放置一些库文件，以便绕过个别应用所存在的问题。

### Loong Arch Linux

Loong Arch Linux 在其软件仓库中提供 libLoL，使用如下命令即可安装：

```
sudo pacman -S la_ow_syscall-dkms liblol
```

由于不同发行版的目录布局各异，不同发行版上的 libLoL 库搜索路径之间也存在不同。Loong Arch Linux 上 libLoL 的库搜索路径如下：

<!-- see https://github.com/loongarchlinux/laur/blob/69696a07a29c270f19def53e985e98fe25949ee1/liblol/PKGBUILD -->

|加载阶段|路径（从上到下顺序搜索）|
|:------:|:---|
|优先|<ul><li><code>/opt/lol/local/preload-lib</code></li><li><code>/opt/lol/support/lib/loongarch64-aosc-linux-gnuow</code></li></ul>|
|正常|<ul><li><code>/opt/lol/local/lib</code></li><li><code>/opt/lol/lib/loongarch64-aosc-linux-gnuow</code></li><li><code>/opt/lol/lib</code></li></ul>|

其中带有 `local` 字样的目录可供用户自助放置一些库文件，以便绕过个别应用所存在的问题。

## 安装应用

您可在[龙芯应用合作社](http://app.loongapps.cn/#/home)或其他分发渠道下载和安装旧世界应用。

## 应用兼容性

考虑到 libLoL 仍在开发过程中，应用程序兼容性尚不完善，测试工作也有待完善。

因此，一部分应用可能无法运行或需要执行额外操作才能运行。详情请参考[应用兼容性数据库](/docs/apps)。

## 运行应用

在完成上述步骤后您就可以在“新世界”享受“旧世界”应用了！

如果您在使用过程中遇到问题，请向我们[报告兼容性问题](/docs/report/)。
