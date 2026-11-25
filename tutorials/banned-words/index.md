---
title: 闲鱼违禁词不回复：命中后整个会话停，检查后再恢复 · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/banned-words/
description: 在闲鱼卖东西，买家先发违禁词再问「有吗」，关键词回复容易回出「有的」。设置词表后，命中就停止整个会话的自动回复，看过拦截记录后可手动恢复。
---

Step-by-step Guide

# 闲鱼违禁词不回复：命中后整个会话停，检查后再恢复

在闲鱼卖东西，买家先发违禁词再问「有吗」，关键词回复容易回出「有的」。设置词表后，命中就停止整个会话的自动回复，看过拦截记录后可手动恢复。

图文教程 · 11 张操作截图 适用版本 2.2.0 更新于 2026-11-22

适用版本：2.2.0。

按当前2.2.0界面设置回复管理中的违禁词规则。

## 一、打开回复管理中的违禁词卡片

设置→智能回复→回复管理，顶部有「违禁词不回复」。默认关闭、词表为空，不打开就不生效。

[![打开回复管理中的违禁词卡片](https://xianyu.dongeai.com/img/tutorials/banned-words/01-default.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/01-default.webp)

打开回复管理中的违禁词卡片 · 点击图片可放大

## 二、编辑词表，再打开开关

点「编辑词表」，一行一个填写词。最多500个、单个最多50字，重复的保存时自动去掉。填好保存后打开开关，优先于API、关键词、AI、首次和默认兜底回复。词表只认填进去的词，其他说法需要自己补。

[![编辑词表，再打开开关](https://xianyu.dongeai.com/img/tutorials/banned-words/02-word-list.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/02-word-list.webp)

编辑词表，再打开开关 · 点击图片可放大

[![编辑词表，再打开开关](https://xianyu.dongeai.com/img/tutorials/banned-words/03-enabled.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/03-enabled.webp)

编辑词表，再打开开关 · 点击图片可放大

## 三、命中后整个会话停止自动回复

买家消息包含任一词，整条自动回复链路都不发。先发品名再问「有吗」，第二句也不会回；连续发几条时每句都检查。其他普通咨询照常回复。匹配前会全角转半角、转小写，并去掉空白、标点和符号。

[![命中后整个会话停止自动回复](https://xianyu.dongeai.com/img/tutorials/banned-words/04-hit.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/04-hit.webp)

命中后整个会话停止自动回复 · 点击图片可放大

[![命中后整个会话停止自动回复](https://xianyu.dongeai.com/img/tutorials/banned-words/05-stopped.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/05-stopped.webp)

命中后整个会话停止自动回复 · 点击图片可放大

[![命中后整个会话停止自动回复](https://xianyu.dongeai.com/img/tutorials/banned-words/06-burst.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/06-burst.webp)

命中后整个会话停止自动回复 · 点击图片可放大

[![命中后整个会话停止自动回复](https://xianyu.dongeai.com/img/tutorials/banned-words/07-normal.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/07-normal.webp)

命中后整个会话停止自动回复 · 点击图片可放大

## 四、看过拦截记录后手动恢复

点「拦截记录」，查看买家、店铺、时间、命中的词和原消息。确认没问题再点「恢复自动回复」，之后的新消息恢复回复。关闭店铺自动回复或会话暂停时也会检查并记录。开关与词表跟云端配置同步，记录仅保留本机处理过的会话。

[![看过拦截记录后手动恢复](https://xianyu.dongeai.com/img/tutorials/banned-words/08-records.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/08-records.webp)

看过拦截记录后手动恢复 · 点击图片可放大

[![看过拦截记录后手动恢复](https://xianyu.dongeai.com/img/tutorials/banned-words/09-resumed.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/09-resumed.webp)

看过拦截记录后手动恢复 · 点击图片可放大

[![看过拦截记录后手动恢复](https://xianyu.dongeai.com/img/tutorials/banned-words/11-shop-off.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/11-shop-off.webp)

看过拦截记录后手动恢复 · 点击图片可放大

## 五、拉黑由卖家手动处理

功能只挡自动回复，不会自动拉黑。需要拉黑时，到会话顶部自己点。

[![拉黑由卖家手动处理](https://xianyu.dongeai.com/img/tutorials/banned-words/10-manual-blacklist.webp)](https://xianyu.dongeai.com/img/tutorials/banned-words/10-manual-blacklist.webp)

拉黑由卖家手动处理 · 点击图片可放大

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/banned-words/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
