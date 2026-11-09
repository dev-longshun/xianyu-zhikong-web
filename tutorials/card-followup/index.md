---
title: 闲鱼自动发货后，卡密或链接怎么单独再发一条 · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/card-followup/
description: 编辑正在使用的内容模板，填写单独消息，保存后核对标签和实际发送效果，让买家更方便复制卡密或链接。
---

Step-by-step Guide

# 卡密或链接怎么单独再发一条

编辑正在使用的内容模板，填写单独消息，保存后核对标签和实际发送效果，让买家更方便复制卡密或链接。

图文教程 · 8 张操作截图 适用版本 1.5.0 更新于 2026-11-08

适用版本：1.5.0。以下为本地示例环境的操作截图，店铺、商品、买家、订单和金额均为虚构；示例兑换码不可使用，示例链接无真实下载。

卡密夹在感谢语和使用说明中，买家复制时容易多选或少选字符。可以在发货正文之后，再发一条只包含卡密或链接的消息。这项设置从 1.5.0 开始提供。

## 一、确认版本和正在使用的模板

1. 确认客户端版本为 1.5.0 或以上；旧版在「关于与更新」检查更新。
2. 确认店铺在线，商品的自动发货、卡种库存和模板绑定已经可用。
3. 打开「发货」→「内容模板」，找到商品当前绑定的模板，点「编辑模板」。不要只修改一个未被使用的模板。

[![使用自动发货时保持店铺在线](https://xianyu.dongeai.com/img/tutorials/card-followup/01-online.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/01-online.webp)

使用自动发货时保持店铺在线 · 点击图片可放大

[![编辑商品实际绑定的内容模板](https://xianyu.dongeai.com/img/tutorials/card-followup/02-template-list.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/02-template-list.webp)

编辑商品实际绑定的内容模板 · 点击图片可放大

## 二、给动态卡密插入卡密原文变量

1. 在编辑弹窗找到选填的「发完后再单独发一条」。
2. 点击这个输入框工具栏自己的「插入变量」。
3. 选择「卡密原文」，输入框出现 {$卡密原文}。
4. 希望买家整条复制时，这个框只留该变量，不添加感谢语、前缀或使用说明。

「卡密原文」不带卡号、密码等前缀；购买多件时，单独消息中按一行一张排列。

[![在单独消息输入框的变量菜单选择卡密原文](https://xianyu.dongeai.com/img/tutorials/card-followup/03-variable.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/03-variable.webp)

在单独消息输入框的变量菜单选择卡密原文 · 点击图片可放大

[![单独消息仅保留卡密原文变量](https://xianyu.dongeai.com/img/tutorials/card-followup/04-followup-field.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/04-followup-field.webp)

单独消息仅保留卡密原文变量 · 点击图片可放大

## 三、保存并检查含单独消息标签

1. 正文仍填写正常的感谢语和使用说明；需要卡密的正文位置可保留原有变量。
2. 点「确定」保存。
3. 在模板列表核对这条模板出现「含单独消息」标签。

**完成检查：**修改的是商品正在使用的模板，且设置已经保存。这个选填框留空时不额外发送消息。

[![保存后模板显示含单独消息标签](https://xianyu.dongeai.com/img/tutorials/card-followup/05-saved.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/05-saved.webp)

保存后模板显示含单独消息标签 · 点击图片可放大

## 四、核对正文与单独消息

1. 检查一笔正常付款发货的订单：先收到正文，再收到单独消息。
2. 买多件时，核对每张卡密在单独消息中各占一行，买家可长按、全选、复制。
3. 检查发货凭证仍是正常发货正文，额外那条消息不计入凭证。

单独消息里写了卡密变量时，正文不会再自动追加一遍卡密；如果正文主动写了卡密变量，则仍按正文模板发送。

[![正文按原模板发送感谢语和说明](https://xianyu.dongeai.com/img/tutorials/card-followup/06-body.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/06-body.webp)

正文按原模板发送感谢语和说明 · 点击图片可放大

[![同一单两张卡密在额外一条消息里逐行排列](https://xianyu.dongeai.com/img/tutorials/card-followup/07-clean-codes.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/07-clean-codes.webp)

同一单两张卡密在额外一条消息里逐行排列 · 点击图片可放大

## 五、固定链接可以直接填写

1. 如果商品交付的是固定网盘链接等内容，编辑该商品使用的固定内容模板。
2. 把自己的有效链接直接填入「发完后再单独发一条」，不用卡密变量。
3. 保存后检查买家收到的单独链接可完整复制。

截图使用 example.com 示例域名；实际交付请替换为自己的有效资源地址。

[![固定内容的单独消息可直接粘贴链接](https://xianyu.dongeai.com/img/tutorials/card-followup/08-fixed-link.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/08-fixed-link.webp)

固定内容的单独消息可直接粘贴链接 · 点击图片可放大

## 六、没有多发这条消息时检查什么

- 版本是否支持，选填框是否填写并保存。
- 商品绑定的模板是不是刚修改的这一条。
- 自动发货本身是否成功，动态卡密是否有足够库存。
- 对照正常订单的正文、额外消息和凭证核对；不要为验证额外消息反复给同一笔订单补发。

## 观看操作视频

需要看连续操作过程，可以打开对应的视频演示。

[去 B 站看完整演示 ↗](https://www.bilibili.com/video/BV19u446NEMc/)

时长 1 分 54 秒。点击章节可打开对应时间点。

- [ 00:00买家复制不对，不是码错了 ↗](https://www.bilibili.com/video/BV19u446NEMc/?t=0)
- [ 00:14解释一遍，再手动补发一次 ↗](https://www.bilibili.com/video/BV19u446NEMc/?t=14)
- [ 00:21这个需求是卖家提的 ↗](https://www.bilibili.com/video/BV19u446NEMc/?t=21)
- [ 00:36设置：发完后再单独发一条 ↗](https://www.bilibili.com/video/BV19u446NEMc/?t=36)
- [ 00:53买两件：正文 + 干净的一条 ↗](https://www.bilibili.com/video/BV19u446NEMc/?t=53)
- [ 01:11买家长按 → 全选 → 复制 ↗](https://www.bilibili.com/video/BV19u446NEMc/?t=71)
- [ 01:18效果与几个放心点 ↗](https://www.bilibili.com/video/BV19u446NEMc/?t=78)
- [ 01:34版本、价格与免费试用 ↗](https://www.bilibili.com/video/BV19u446NEMc/?t=94)

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/card-followup/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
