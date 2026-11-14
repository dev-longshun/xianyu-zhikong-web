---
title: 买家拍多件，怎么自动发货 · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/multi-quantity-delivery/
description: 单规格兑换码商品，从拍1件、拍10件到缺货提醒，按真实操作截图核对库存、消息和手动补发。
---

Step-by-step Guide

# 买家拍多件，怎么自动发货

单规格兑换码商品，从拍1件、拍10件到缺货提醒，按真实操作截图核对库存、消息和手动补发。

图文教程 · 16 张操作截图 适用版本 1.7.0 更新于 2026-11-13

适用版本：1.7.0。

在闲鱼卖卡密，买家一次拍多件，需要按实际件数发出对应数量的兑换码。本教程用一个单规格商品，把付款后发货、缺货提醒、补卡和手动补发连起来检查。

## 一、准备卡密库存和付款后发货绑定

1. 先在闲鱼发布单规格的兑换码商品，并在闲鱼智控中确认店铺在线。
2. 打开「发货」→「卡种」，创建对应卡种，在「管理卡密」中添加自己的兑换码，一行一张。
3. 在「内容模板」中准备正文，插入 {$卡密信息} 变量；如果希望买家方便复制，在「发完后再单独发一条」填入 {$卡密原文}。
4. 进入「发货」→「发货」→「销售中」，找到商品，在付款后发货设置中选择对应卡种和内容模板，打开「启用该发货模板」后保存。

**完成检查：**商品绑定了正确卡种、内容模板，且付款后发货已启用。拍几件发几张，不用另外设置。

[![核对卡种、内容模板及启用状态](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/01-binding.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/01-binding.webp)

核对卡种、内容模板及启用状态 · 点击图片可放大

## 二、拍1件：核对消息、库存和已售记录

先检查一笔购买1件的订单。付款后，会话里收到1张兑换码；卡种未售库存减少1张，已售记录增加1条。

1. 在会话中核对正文和兑换码。
2. 回到卡种，核对未售、已售数量。
3. 打开「管理卡密」→「已售列表」，核对卡号、买家昵称及出库类型。

**完成检查：**收到的兑换码与已售列表一致。本次17张库存，发出1张后，未售16张、已售1张。

[![拍1件付款后，收到1张兑换码](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/02-one-delivery.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/02-one-delivery.webp)

拍1件付款后，收到1张兑换码 · 点击图片可放大

[![发出1张后，未售16张、已售1张](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/03-one-stock.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/03-one-stock.webp)

发出1张后，未售16张、已售1张 · 点击图片可放大

[![已售列表显示本单的兑换码与买家昵称](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/04-one-sold.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/04-one-sold.webp)

已售列表显示本单的兑换码与买家昵称 · 点击图片可放大

## 三、拍10件：一次发齐，单独一条方便复制

购买10件时，软件向闲鱼订单核实实际件数，再从绑定卡种一次取出10张。

1. 正文里包含本单10张兑换码，中间用分割线隔开。
2. 若开启了「发完后再单独发一条」并填写 {$卡密原文}，还会发出一条只有兑换码的消息，一行一张，没有分割线。
3. 买家长按单独那条消息，就能一次复制本单全部兑换码。
4. 回到卡种和已售列表，核对库存减少10张，10张记录的买家信息相符。

**完成检查：**本次发出10张后，未售库存从16张变为6张，已售合计11张。

[![一条正文包含本单10张兑换码](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/05-ten-body.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/05-ten-body.webp)

一条正文包含本单10张兑换码 · 点击图片可放大

[![兑换码之间用分割线隔开](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/06-ten-separators.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/06-ten-separators.webp)

兑换码之间用分割线隔开 · 点击图片可放大

[![单独那条只有兑换码，一行一张](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/07-ten-raw.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/07-ten-raw.webp)

单独那条只有兑换码，一行一张 · 点击图片可放大

[![发出10张后，未售6张、已售11张](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/08-ten-stock.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/08-ten-stock.webp)

发出10张后，未售6张、已售11张 · 点击图片可放大

[![已售列表核对卡号和买家昵称](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/09-ten-sold.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/09-ten-sold.webp)

已售列表核对卡号和买家昵称 · 点击图片可放大

## 四、只剩6张却拍10件：整单不发并提醒

库存不足时，软件不会先发一部分。本次只剩6张，买家购买10件，整单不出库，会话里没有发出兑换码，库存仍是6张。

即使停在店铺等其他页面，最上层也会弹出「库存预警，请尽快补充卡密」，列出缺货未发货的订单和需要张数。只要有缺货订单，无论卡种预警值设多少都会提醒。

**完成检查：**库存未减少，预警列出1单缺货未发，所需10张。

[![缺货前，卡种只剩6张](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/10-six-stock.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/10-six-stock.webp)

缺货前，卡种只剩6张 · 点击图片可放大

[![买家付款后，会话没有发出兑换码](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/11-shortage-chat.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/11-shortage-chat.webp)

买家付款后，会话没有发出兑换码 · 点击图片可放大

[![店铺页面上方弹出真实库存预警](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/12-stock-alert.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/12-stock-alert.webp)

店铺页面上方弹出真实库存预警 · 点击图片可放大

## 五、补够兑换码，再进入这单的会话

1. 在库存预警中直接点「补卡密」。
2. 添加足够的兑换码。本次原有6张，再补4张，凑够这单需要的10张。
3. 添加成功后，回到缺货订单对应的买家会话。
4. 在会话头部点击「去发货」。

补够库存后需要手动补发，不会自动再次发送。

[![补4张，把可用库存补到10张](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/13-refill.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/13-refill.webp)

补4张，把可用库存补到10张 · 点击图片可放大

[![进入缺货订单的会话，点击头部「去发货」](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/14-redeliver-entry.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/14-redeliver-entry.webp)

进入缺货订单的会话，点击头部「去发货」 · 点击图片可放大

## 六、手动补发前核对状态和件数

1. 在发货弹窗中选择「手动补发」。
2. 等待软件重新核实订单状态和件数：仍是待发货、购买10件，且库存足够。
3. 核对后点击「确定补发」。
4. 回到会话核对本单10张兑换码已经发齐，订单已经发货。

**完成检查：**正文和单独那条均包含10张，出库记录对应本单，缺货订单从预警中消失。不要重复补发。

[![手动补发预检核对10件，确认后再补发](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/15-redeliver-check.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/15-redeliver-check.webp)

手动补发预检核对10件，确认后再补发 · 点击图片可放大

[![本单10张兑换码补发完成](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/16-redelivered.webp)](https://xianyu.dongeai.com/img/tutorials/multi-quantity-delivery/16-redelivered.webp)

本单10张兑换码补发完成 · 点击图片可放大

## 七、件数查不到、退款和发送中断时怎么办

- **查不到实际件数：**先不取卡、不发送，不按默认1件随意发货。
- **订单已退款：**核实订单不再待发货或正在退款时，停止发货。
- **发送中断：**发到一半断网，不自动重发。按提示核对聊天和已售卡密，再人工处理，避免重复交付。
- **持续运行：**店铺保持在线，电脑开机联网，软件保持运行。

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/multi-quantity-delivery/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
