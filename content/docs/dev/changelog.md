---
title: 更新日志
toc: true
weight: 2
---

当前使用的 0.1.0 系列 libLoL 使用一份特殊版本的 Glibc 运行时库，直接载入新世界系统运行时来实现应用兼容性。

详见[实现原理](/docs/dev/design)。

## 0.1.10

- glibc 版本更新至 2.42
- libxcrypt 版本更新至 4.5.2

## 0.1.9

- glibc 版本更新至 2.41
- 修复 Binutils 2.44 构建的 libLoL 存在分页对齐错误的问题

## 0.1.6

- Glibc 版本更新至 2.40；
- 修正了 `lxstat64` 的实现，使之使用 `statx` 系统调用。

## 0.1.5

- Glibc 版本更新至 2.39
- 编译时新增 ABI 及符号完整性检查-
- `libcrypt` 库实现更改为 `libxcrypt`

## 0.1.4

- 提供 Debian 软件包。
- 适配 AOSC OS 的 Autobuild4 构建工具。
- 提供 `libanl`, `libutil`, `libnsl` 兼容库。
- 为新世界缺失的 `*stat(at)?` 系统调用提供备用调用。

## 0.1.3

- 优先使用 libLoL 运行时目录中的库，改善兼容性。

## 0.1.2

- 通过提供 `ld-linux-loongarch-lp64d.so` 库（仅包含重定向），修复如腾讯会议等应用无法使用的问题。

## 0.1.1

- 修复 .NET 应用兼容性。

## 0.1.0

- 重新设计后发布的初版。

## 0.0.x 系列

0.1.0 版之前的 libLoL 使用一个自行编译的 GNU 工具链和 Glibc 运行时库，并通过编译和预装来自 Loongnix 的各类运行时库来提供兼容性。

该版虽能解决一部分兼容性问题，但空间占用较大且某些组件（如非开源的 GCC）存在许可和潜在安全性问题。
