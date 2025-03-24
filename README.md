# Liblol-website
## 运行环境

- [hugo v0.122.0](https://github.com/gohugoio/hugo/releases/tag/v0.122.0)

- python 3.10+ 

## 更新数据
运行爬虫：

```
cd scripts
pip install -r requirements.txt
python spider.py
```

生成的数据文件：

- loongapplist-latest.csv: 所有应用数据
- loongapplist-new: 新上架应用
- loongapplist-upgrade: 升级应用 
- loongapplist-down.csv: 下架应用
- loongapplist-update.csv: new + upgrade + down - "开源软件" - "3A4000" - "二进制翻译软件" - "开源软件（云顶书院迁移）"

## 更新文档

对于来自[龙芯应用合作社](https://app.loongapps.cn/home)的增量应用信息（loongapplist-update.csv），执行：

```
cd scripts
pip install -r requirements.txt
python main.py
```

对于其他来源的应用，需手动创建文档。

## 构建及预览

安装 [hugo v0.122.0](https://github.com/gohugoio/hugo/releases/tag/v0.122.0)，并执行：
```
hugo server
```
> 建议在构建前删除已生成的站点数据 public/*

## 文档内容

### 文件名

一般情况下取`应用编号.md`作为文件名。

1. 龙芯应用合作社

跟随[龙芯应用合作社](https://app.loongapps.cn/home) 编号，应用编号也为该应用的文档名。

2. 其他来源

按报告顺序由1递增的正整数为编号。


### 文档头(Front-matter)

```
---
title: 应用名称      //也作为文档的一级标题
toc: true/false    //侧边栏开启/关闭，一般情况下为true。
weight: 应用编号    //文档的排列顺序。一般情况下，取应用编号的值。
draft: true/false  //当值为true时文档作为草稿，不渲染。
compatibility: 1/2/3/4 //兼容性数据，其中新世界可用为 4，可用为 3,存在问题为 2,不可用为 1，此项缺失则表示未测试
---
```

### 标题

内容的最高级标题应为 H2，H1 为文档头的 `title: 应用名称` 渲染生成。

### 基本内容

使用 [Markdown](https://en.wikipedia.org/wiki/Markdown) 来书写内容，创建列表等。

### LaTex公式

参考 [latex-project.org](https://www.latex-project.org/) 。

### Mermaid图表

参考 [Mermaid | Diagramming and charting tool](https://mermaid.js.org/) 。

### 引用代码仓库中的文件

1. 静态内容

静态内容存放于仓库目录 `static/` 中，以**绝对路径**方式引用。

例如：

- 引用 `static/images` 中的 `logo.svg`:

```
![logo.svg](/images/logo.svg)
```

- 引用 `/static/data` 中的 `loongapplist-latest.csv`:

```
[loongapplist-latest.csv](/data/loongapplist-latest.csv)
```

2. 引用文档

文档存放于仓库目录 `/content`，以**绝对路径**方式引用，无需添加文件扩展名。

- 引用 `/content/docs/dev/liblol.md`

```
[libLoL](/docs/dev/liblol)
```
###

更多内容请参考主题 [Hextra](https://imfing.github.io/hextra/zh-cn/docs/) 文档。
