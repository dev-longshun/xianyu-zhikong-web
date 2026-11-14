---
title: 闲鱼多规格商品怎么自动发货（月卡、年卡分别发） · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/multi-spec-delivery/
description: 同一个商品有月卡、年卡等规格，按步骤准备库存、绑定卡种与模板，再检查付款后是否发出对应的兑换码。
---

Step-by-step Guide

# 多规格商品怎么设置自动发货

同一个商品有月卡、年卡等规格，按步骤准备库存、绑定卡种与模板，再检查付款后是否发出对应的兑换码。

图文教程 · 10 张操作截图 适用版本 1.5.0 更新于 2026-11-08

适用版本：1.5.0。截图中的店铺、商品、买家和兑换码均为示例数据；DEMO 兑换码不可兑换。

同一个商品，但是有月卡、年卡几个规格，希望买家拍月卡就收到月卡，拍年卡就收到年卡。可以给每个规格分别设置付款后发货，绑定各自的卡种库存。

本教程以兑换码为例，只设置**付款后发货**。完成后，两种规格可以共用使用说明，但实际兑换码来自不同库存。

## 一、发布好规格，准备两组库存

1. 先在闲鱼发布好商品及其规格，例如「月卡」「年卡」。在闲鱼智控的「店铺」页确认对应店铺在线。
2. 打开左侧「发货」→「卡种」，为月卡、年卡分别创建卡种，例如「演示工具月卡」「演示工具年卡」。
3. 进入各自的「管理卡密」，放入对应的兑换码。月卡库存只放月卡码，年卡库存只放年卡码，不要混在一起。

**完成检查：**卡种列表有两组独立库存，打开月卡库存时，看到的都是月卡兑换码。

[![① 月卡卡种、② 年卡卡种分别保管对应的兑换码](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/01-inventories.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/01-inventories.webp)

① 月卡卡种、② 年卡卡种分别保管对应的兑换码 · 点击图片可放大

[![进入月卡的管理卡密，核对库存内容属于月卡](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/02-month-stock.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/02-month-stock.webp)

进入月卡的管理卡密，核对库存内容属于月卡 · 点击图片可放大

## 二、准备一条内容模板

1. 在「发货」→「内容模板」里点击「创建内容模板」，填写容易辨认的模板名称。
2. 正文写上感谢购买、使用说明等文字。
3. 从变量菜单插入「卡密信息」，正文中会出现 {$卡密信息}。保存模板。

两个规格可以共用这条模板。模板控制消息样式，真正发出去的兑换码由各自绑定的卡种决定。示例中的「DEMO 演示码，不可兑换」用于演示，实际使用时填写自己的使用说明。

[![内容模板中保留卡密信息变量，发货时替换为本次出库的兑换码](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/03-template.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/03-template.webp)

内容模板中保留卡密信息变量，发货时替换为本次出库的兑换码 · 点击图片可放大

## 三、打开商品的规格设置面板

1. 打开「发货」中的「发货」，切到「销售中」。
2. 找到要配置的商品，确认显示多规格标记。
3. 点击商品「付款后发货」一栏的「设置」，进入规格面板。

面板一行对应一个规格。本教程只操作「付款后发货」列，再点月卡这一行的「设置」。

[![① 找到付款后发货列，② 点击月卡行的设置](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/04-spec-panel.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/04-spec-panel.webp)

① 找到付款后发货列，② 点击月卡行的设置 · 点击图片可放大

## 四、给月卡绑定月卡库存

1. 检查弹窗顶部显示的是这个商品的**月卡规格**。
2. 发货内容来源选「动态卡密」，发货卡种选月卡对应的卡种。
3. 内容模板选刚才创建的说明模板。
4. 确认「启用该发货模板」打开，点击「确定」保存。

**完成检查：**回到规格面板，月卡行显示月卡卡种、所选模板和「已开启」。

[![① 月卡卡种、② 内容模板、③ 启用状态，保存前逐项核对](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/05-month-setting.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/05-month-setting.webp)

① 月卡卡种、② 内容模板、③ 启用状态，保存前逐项核对 · 点击图片可放大

## 五、给年卡绑定年卡库存，再对照检查

1. 在年卡这一行点击「设置」，检查弹窗顶部是年卡规格。
2. 发货内容同样用动态卡密，把发货卡种改为年卡对应的卡种；使用说明相同，可以继续用同一条内容模板。
3. 确认启用并保存。
4. 回到规格面板，对照两行：月卡对应月卡库存，年卡对应年卡库存，两行都是「已开启」。

如果用复制粘贴省操作，粘贴后也要检查卡种。月卡和年卡发不同内容时，不能把月卡设置原样留给年卡。

[![① 年卡选择年卡卡种，② 使用说明可以共用同一条模板](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/06-year-setting.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/06-year-setting.webp)

① 年卡选择年卡卡种，② 使用说明可以共用同一条模板 · 点击图片可放大

[![保存后核对：① 月卡对应月卡库存，② 年卡对应年卡库存](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/07-mapping.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/07-mapping.webp)

保存后核对：① 月卡对应月卡库存，② 年卡对应年卡库存 · 点击图片可放大

## 六、核对付款后的实际发货结果

设置完成后，按购买规格检查实际交付。下面是两笔示例订单：月卡订单收到 DEMO-M- 开头的月卡码，年卡订单收到 DEMO-Y- 开头的年卡码。

1. 在消息里核对：买家购买的规格与收到的兑换码是否一致，使用说明是否正确。
2. 核对订单已经发货，并查看发货凭证。
3. 打开对应卡种的「管理卡密」→「已售列表」，核对出库的兑换码和订单记录。

**完成检查：**购买规格、消息内容、订单状态和已售记录全部对得上。

[![月卡示例订单付款后，消息中发出月卡库存的兑换码](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/08-month-delivery.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/08-month-delivery.webp)

月卡示例订单付款后，消息中发出月卡库存的兑换码 · 点击图片可放大

[![年卡示例订单付款后，消息中发出年卡库存的兑换码](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/09-year-delivery.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/09-year-delivery.webp)

年卡示例订单付款后，消息中发出年卡库存的兑换码 · 点击图片可放大

[![在年卡卡种的已售列表中核对出库兑换码和订单](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/10-sold-record.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/10-sold-record.webp)

在年卡卡种的已售列表中核对出库兑换码和订单 · 点击图片可放大

## 七、没有自动发货，先检查这几项

- **规格是否配置：**付款后发货一旦开始按规格设置，没设置或已经关闭的规格就不会自动发货，不会回退使用整商品或关键词设置。
- **卡种是否选对：**逐个规格确认绑定的库存，复制粘贴后也重新检查。
- **库存是否备好：**不同规格的兑换码分别放入对应卡种，避免混码。
- **运行条件是否满足：**店铺保持在线，电脑开机联网，软件保持运行。

需要销售的规格都检查完成后，再让这套设置持续运行。

## 观看操作视频

需要看连续操作过程，可以打开对应的视频演示。

[去 B 站看完整演示 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/)

时长 2 分 13 秒。点击章节可打开对应时间点。

- [ 00:00一个商品，月卡年卡两个规格 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=0)
- [ 00:13先准备两组独立库存 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=13)
- [ 00:26内容模板：使用说明加卡密 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=26)
- [ 00:37销售中 → 多规格设置 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=37)
- [ 00:52月卡规格绑定月卡库存 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=52)
- [ 01:07年卡规格绑定年卡库存 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=67)
- [ 01:24两笔示例订单：按规格发货 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=84)
- [ 01:39没设置的规格不会发 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=99)
- [ 01:51版本、价格与免费试用 ↗](https://www.bilibili.com/video/BV1wWWs6TEMn/?t=111)

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/multi-spec-delivery/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
