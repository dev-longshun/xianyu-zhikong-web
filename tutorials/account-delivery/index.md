---
title: 闲鱼卖账号，设置账号密码自动发货 · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/account-delivery/
description: 创建两段卡种，分别粘贴账号和密码，按行配对后自动发货。
---

Step-by-step Guide

# 闲鱼卖账号，设置账号密码自动发货

创建两段卡种，分别粘贴账号和密码，按行配对后自动发货。

图文教程 · 7 张操作截图 适用版本 1.9.1 更新于 2026-11-17

适用版本：1.9.1。

账号和密码需要成对保存、成对发出。本教程从创建卡种到买家收到，核对完整的一次付款自动发货。

## 一、创建两段卡种

进入「发货」→「卡种」→「创建卡种」，填写卡种名称。卡密格式选「两段（卡号 + 密码）」，卡号前缀填「账号：」，密码前缀填「密码：」，分隔符选「换行」。

[![两段格式与前缀设置](https://xianyu.dongeai.com/img/tutorials/account-delivery/01-two-segments.webp)](https://xianyu.dongeai.com/img/tutorials/account-delivery/01-two-segments.webp)

两段格式与前缀设置 · 点击图片可放大

## 二、先看发货预览

向下查看「发货预览」。应显示账号和密码两行、各带前缀，星号是真实卡密的占位；确认格式正确，再点「创建」。

[![买家收到的格式随填写实时变化](https://xianyu.dongeai.com/img/tutorials/account-delivery/02-preview.webp)](https://xianyu.dongeai.com/img/tutorials/account-delivery/02-preview.webp)

买家收到的格式随填写实时变化 · 点击图片可放大

## 三、左右粘贴，核对头尾配对

卡种点击「添加卡密」。左边粘贴账号、一行一个，右边粘贴密码、一行一个。出现「已配对 N 组」后，检查开头几组和最后一组是否错位。

[![两列行数一致，核对首尾配对](https://xianyu.dongeai.com/img/tutorials/account-delivery/03-paired.webp)](https://xianyu.dongeai.com/img/tutorials/account-delivery/03-paired.webp)

两列行数一致，核对首尾配对 · 点击图片可放大

## 四、行数不一致，先修正再添加

若右侧少一行，软件会显示卡号与密码行数及哪边多几行。点添加也不会入库；核对两列、补齐缺失行，确认配对无误后再添加。不要随便补一个不对应的密码。

[![行数不一致时被阻止，库存不变](https://xianyu.dongeai.com/img/tutorials/account-delivery/04-mismatch.webp)](https://xianyu.dongeai.com/img/tutorials/account-delivery/04-mismatch.webp)

行数不一致时被阻止，库存不变 · 点击图片可放大

## 五、已有一行一组的数据

如果原数据已经是「账号 密码」一行一组，切换「整段粘贴（一行一组）」并选择与原数据相符的分隔符。切换填写方式会清空当前输入，粘贴后重新核对。

[![整段模式适用于已配好的一行一组数据](https://xianyu.dongeai.com/img/tutorials/account-delivery/05-whole.webp)](https://xianyu.dongeai.com/img/tutorials/account-delivery/05-whole.webp)

整段模式适用于已配好的一行一组数据 · 点击图片可放大

## 六、商品绑定并启用付款后发货

进入「发货」→「发货」→「销售中」，找到商品，在付款后发货列点「设置」（已有设置时点「编辑」）。选择刚创建的卡种和包含 {$卡密信息} 的内容模板，启用该发货模板并保存。

[![绑定正确卡种和内容模板，启用模板](https://xianyu.dongeai.com/img/tutorials/account-delivery/06-binding.webp)](https://xianyu.dongeai.com/img/tutorials/account-delivery/06-binding.webp)

绑定正确卡种和内容模板，启用模板 · 点击图片可放大

## 七、检查买家收到的消息

买家付款后，应收到两行：账号：实际账号、密码：对应密码。检查卡种库存减少一组，已售记录挂在该订单下。

[![买家收到的账号和密码各一行](https://xianyu.dongeai.com/img/tutorials/account-delivery/07-delivered.webp)](https://xianyu.dongeai.com/img/tutorials/account-delivery/07-delivered.webp)

买家收到的账号和密码各一行 · 点击图片可放大

## 观看操作视频

需要看连续操作过程，可以打开对应的视频演示。

[去 B 站看完整演示 ↗](https://www.bilibili.com/video/BV1PrsC6hEd9/)

时长 1 分 49 秒。

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/account-delivery/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
