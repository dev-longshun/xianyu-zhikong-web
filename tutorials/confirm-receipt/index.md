---
title: 闲鱼自动提醒买家确认收货怎么设置 · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/confirm-receipt/
description: 配置首次提醒时间、间隔和上限，选择系统卡片或文本，保留售后跳过条件，并在台账核对提醒结果。
---

Step-by-step Guide

# 自动提醒收货怎么设置

配置首次提醒时间、间隔和上限，选择系统卡片或文本，保留售后跳过条件，并在台账核对提醒结果。

图文教程 · 9 张操作截图 适用版本 1.5.0 更新于 2026-11-08

适用版本：1.5.0。以下为本地示例环境的操作截图，店铺、商品、买家、订单和金额均为虚构；示例兑换码不可使用，示例链接无真实下载。

对已经发货、还未确认收货的订单，可以按设定节奏提醒。下面以首次发货后 3 天、之后间隔 1 天、最多 3 次为例；这些是演示参数，按实际业务调整。

## 一、打开提醒收货台账

1. 在「店铺」确认账号在线，保持电脑联网、客户端持续运行。
2. 打开左侧「营销」，在提醒收货入口点「去提醒」。
3. 查看待提醒订单，点「自动提醒收货设置」。

[![检查店铺在线](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/01-online.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/01-online.webp)

检查店铺在线 · 点击图片可放大

[![从提醒台账进入自动提醒设置](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/02-ledger.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/02-ledger.webp)

从提醒台账进入自动提醒设置 · 点击图片可放大

## 二、设置系统卡片提醒

1. 打开「自动提醒收货开关」。
2. 提醒方式选择「系统卡片」。
3. 设置首次提醒延迟，例如发货后 3 天；设置下次提醒延迟，例如 1 天；设置提醒上限，例如 3 次。
4. 核对后点「确定」保存。

**完成检查：**自动提醒已开启，参数正确。系统卡片是平台交易提醒，每单每天一次。

[![自动提醒开关、首次延迟与次数上限](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/03-card-settings.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/03-card-settings.webp)

自动提醒开关、首次延迟与次数上限 · 点击图片可放大

## 三、需要文本提醒时，配置文案与频次

1. 重新打开自动提醒设置，将提醒方式换成「文本消息」。
2. 设置每天最多提醒次数及提醒间隔小时数，按合理节奏提醒。
3. 保存后，在台账页头打开「提醒文案模板」，编写并勾选要使用的文案，保存。

文本方式从可用模板中随机取一条发送到会话；卡片与文本的提醒次数合并计算。

[![文本方式可以设置每日次数和小时间隔](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/04-text-settings.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/04-text-settings.webp)

文本方式可以设置每日次数和小时间隔 · 点击图片可放大

[![选择可用提醒文案，避免只写了却未勾选](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/06-templates.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/06-templates.webp)

选择可用提醒文案，避免只写了却未勾选 · 点击图片可放大

## 四、保留售后、投诉、纠纷跳过条件

1. 在自动提醒设置中找到「存在售后、投诉、纠纷记录的订单不提醒收货」。
2. 确认勾选后保存。
3. 在台账中检查相应订单显示的跳过原因，避免对正在处理售后的买家自动催收货。

[![确认售后等异常订单不自动提醒](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/05-skip-refund.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/05-skip-refund.webp)

确认售后等异常订单不自动提醒 · 点击图片可放大

## 五、从台账核对结果

1. 切到「提醒成功」，查看成功提醒次数、提醒方式与最近提醒时间。
2. 有失败时查看「提醒失败」及原因，先处理账号、网络或订单状态问题。
3. 切到「已收货」，核对买家收货时间；订单完成后不应继续提醒。

[![提醒成功记录包含次数与方式](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/07-records.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/07-records.webp)

提醒成功记录包含次数与方式 · 点击图片可放大

[![已收货页核对确认收货时间](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/08-received.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/08-received.webp)

已收货页核对确认收货时间 · 点击图片可放大

## 六、开启前的老订单手动批量补提醒

1. 自动提醒开启前已经发货的订单，不会自动补提醒。
2. 在「待提醒」中核对订单，勾选需要提醒的单，点「批量提醒」。
3. 在弹窗选择提醒方式并确认，留在此页等批量任务结束。
4. 回到台账核对结果，不要反复点击造成重复操作。

**完成检查：**自动设置保持启用；需要补提醒的旧订单有明确处理结果。

[![核对批量提醒方式后确认，等待处理完成](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/09-batch.webp)](https://xianyu.dongeai.com/img/tutorials/confirm-receipt/09-batch.webp)

核对批量提醒方式后确认，等待处理完成 · 点击图片可放大

## 观看操作视频

需要看连续操作过程，可以打开对应的视频演示。

[去 B 站看完整演示 ↗](https://www.bilibili.com/video/BV1NUx968E3J/)

时长 2 分 26 秒。点击章节可打开对应时间点。

- [ 00:00货发了，买家就是不点确认收货 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=0)
- [ 00:13为什么钱一直到不了账 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=13)
- [ 00:22手动提醒为什么麻烦 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=22)
- [ 00:36打开提醒收货页 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=36)
- [ 00:43设置自动提醒：发货后 3 天、每天 1 次、最多 3 次 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=43)
- [ 00:59换成文本消息，一天多次、文案随机换着发 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=59)
- [ 01:16有售后、投诉、纠纷的单不提醒 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=76)
- [ 01:30台账记录：提醒次数、方式、收货时间 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=90)
- [ 01:40开启前的老订单批量提醒 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=100)
- [ 01:52收货后自动好评，发货后求小红花 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=112)
- [ 02:01作者店铺的执行记录 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=121)
- [ 02:08版本、价格与免费试用 ↗](https://www.bilibili.com/video/BV1NUx968E3J/?t=128)

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/confirm-receipt/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
