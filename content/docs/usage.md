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

### Debian / Loongnix 25 beta

首先，在[此页面](https://github.com/AOSC-Dev/la_ow_syscall/releases)下载最新版本的内核模块包 [liblol-dkms_0.1.1_loong64.deb](https://github.com/AOSC-Dev/la_ow_syscall/releases/download/debian%2Fv0.1.1/liblol-dkms_0.1.1_loong64.deb) 并执行如下命令安装：

```
sudo apt install ./liblol-dkms_0.1.1_loong64.deb
```

安装完成后，在[此页面](https://github.com/AOSC-Dev/liblol/releases)下载最新版本的 libLoL 运行时包 [liblol_0.1.10-1_loong64.deb](https://github.com/AOSC-Dev/liblol/releases/download/debian%2Fv0.1.10-1/liblol_0.1.10-1_loong64.deb)，随后执行如下命令安装：

```
sudo apt install ./liblol_0.1.10-1_loong64.deb
```

由于不同发行版的目录布局各异，不同发行版上的 libLoL 库搜索路径之间也存在不同。Debian 上 libLoL 的库搜索路径如下：

<!-- see https://github.com/AOSC-Dev/liblol/blob/debian/v0.1.5_pre6-1/debian/rules -->

|加载阶段|路径（从上到下顺序搜索）|
|:------:|:---|
|优先|<ul><li><code>/usr/local/lib/loongarch64-debian-linux-gnuow/preload</code></li><li><code>/usr/lib/loongarch64-debian-linux-gnuow/preload</code></li></ul>|
|正常|<ul><li><code>/usr/local/lib/loongarch64-debian-linux-gnuow</code></li><li><code>/usr/lib/loongarch64-debian-linux-gnuow</code></li></ul>|

其中带有 `local` 字样的目录可供用户自助放置一些库文件，以便绕过个别应用所存在的问题。

### deepin

deepin 在主软件仓库提供 libLoL，使用如下命令安装即可使用：

```
sudo apt install liblol liblol-dkms
```

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

### Slackwareloong

Slackwareloong 在 SlackBuilds 软件仓库提供 libLoL，使用如下命令即可安装：

```bash
slackpkg install liblol

```

加载 la_ow_syscall 内核模块，若没有此模块请更新内核

```bash
insmod /lib/modules/`uname -r`/kernel/arch/loongarch/ow_syscall/la_ow_syscall.ko
```

由于不同发行版的目录布局各异，不同发行版上的 libLoL 库搜索路径之间也存在不同。Slackwareloong 上 libLoL 的库搜索路径如下：

|加载阶段|路径（从上到下顺序搜索）|
|:------:|:---|
|优先|<ul><li><code>/opt/lol/local/preload-lib64</code></li><li><code>/opt/lol/support/lib64/loongarch64-aosc-linux-gnuow</code></li></ul>|
|正常|<ul><li><code>/opt/lol/local/lib64</code></li><li><code>/opt/lol/lib64/loongarch64-aosc-linux-gnuow</code></li><li><code>/opt/lol/lib64</code></li></ul>|

其中带有 `local` 字样的目录可供用户自助放置一些库文件，以便绕过个别应用所存在的问题。

## 安装应用

您可在[龙芯应用合作社](https://app.loongapps.cn/home)或其他分发渠道下载旧世界应用。


<p>{{< compatibility-icon 5 >}} 

请[点此](https://raw.githubusercontent.com/AOSC-Dev/scriptlets/refs/heads/master/loong64-it/loong64-it.bash)下载 `loong64-it` 脚本，并执行如下命令：

```
bash loong64-it.bash [PACKAGE1] [PACKAGE2] ...
# 其中 [PACKAGE1] [PACKAGE2] 为软件包的路径及文件名
```

## 应用兼容性

考虑到 libLoL 仍在开发过程中，应用程序兼容性尚不完善，测试工作也有待完善。

因此，一部分应用可能无法运行或需要执行额外操作才能运行。详情请参考[应用兼容性数据库](/docs/apps)。

## 运行应用

在完成上述步骤后您就可以在“新世界”享受“旧世界”应用了！

如果您在使用过程中遇到问题，请向我们[报告兼容性问题](/docs/report/)。
