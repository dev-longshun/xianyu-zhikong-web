---
title: 闲鱼自动发货怎么设置：卡密、网盘链接、虚拟商品 · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/auto-delivery/
description: 分清固定内容和动态卡密，准备模板与库存，为商品开启付款后发货，再核对消息和出库记录。
---

Step-by-step Guide

# 付款后自动发货怎么设置

分清固定内容和动态卡密，准备模板与库存，为商品开启付款后发货，再核对消息和出库记录。

图文教程 · 11 张操作截图 适用版本 1.5.0 更新于 2026-11-08

适用版本：1.5.0。以下为本地示例环境的操作截图，店铺、商品、买家、订单和金额均为虚构；示例兑换码不可使用，示例链接无真实下载。

交付网盘链接、资料说明时，每位买家可以收到同一份固定内容；交付兑换码时，则需要从卡种库存为每单取出对应的码。下面分别把两种方式配好，并检查实际交付结果。

## 一、确认商品已发布、店铺在线

1. 先在平台发布商品，确认自己要交付的是相同的链接或说明，还是每单不同的卡密。
2. 打开客户端「店铺」，确认对应店铺已经登录且显示在线。
3. 保持电脑开机、联网，客户端持续运行。

**完成检查：**目标店铺在线，能够在「发货」→「发货」→「销售中」找到要配置的商品。

[![确认要配置的店铺在线](https://xianyu.dongeai.com/img/tutorials/auto-delivery/01-online.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/01-online.webp)

确认要配置的店铺在线 · 点击图片可放大

## 二、每单内容相同：先建固定内容模板

1. 打开左侧「发货」→「内容模板」，点击「创建内容模板」。
2. 填写容易辨认的名称，例如「文档模板下载说明」。
3. 正文填写自己的有效链接、提取码、使用说明，核对无误后点「确定」。示例中的 example.com 不能作为实际交付链接。

**完成检查：**模板列表能找到新模板，正文包含买家需要的完整内容。

[![填写名称和完整交付正文，再保存](https://xianyu.dongeai.com/img/tutorials/auto-delivery/02-fixed-template.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/02-fixed-template.webp)

填写名称和完整交付正文，再保存 · 点击图片可放大

## 三、把固定模板绑定到商品

1. 在「发货」→「发货」切到「销售中」，找到目标商品。
2. 点击该商品「付款后发货」一栏的「设置」；已有配置时点「编辑」。
3. 「发货内容来源」选「固定内容」，「内容模板」选刚创建的模板。
4. 确认「启用该发货模板」打开，点「确定」。

**完成检查：**商品的付款后发货栏显示正确模板且已开启。

[![选择固定内容、对应模板并确认启用](https://xianyu.dongeai.com/img/tutorials/auto-delivery/03-fixed-setting.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/03-fixed-setting.webp)

选择固定内容、对应模板并确认启用 · 点击图片可放大

## 四、每单发不同兑换码：建卡种、导入库存

1. 打开「发货」→「卡种」，点击「创建卡种」，填写名称。卡种用来存放一组同类兑换码。
2. 按自己的卡密格式设置前缀等字段，保存。
3. 在该卡种点「添加卡密」，按照导入框要求粘贴卡密；本例只有兑换码，每行一张。
4. 确认导入，检查未售数量；需要预警时，编辑卡种设置库存预警值。

**完成检查：**兑换码进入正确卡种，未售数量与导入数量一致。软件不提供卡密货源，需要使用你自己的合法库存。

[![为同类兑换码创建卡种](https://xianyu.dongeai.com/img/tutorials/auto-delivery/04-kind-form.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/04-kind-form.webp)

为同类兑换码创建卡种 · 点击图片可放大

[![每行一张，导入前核对内容与格式](https://xianyu.dongeai.com/img/tutorials/auto-delivery/05-import.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/05-import.webp)

每行一张，导入前核对内容与格式 · 点击图片可放大

[![导入后在卡种列表检查未售库存](https://xianyu.dongeai.com/img/tutorials/auto-delivery/06-stock.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/06-stock.webp)

导入后在卡种列表检查未售库存 · 点击图片可放大

## 五、准备卡密模板，并绑定商品

1. 在「内容模板」新建或编辑交付模板，填写感谢语和使用说明。
2. 用变量菜单插入「卡密信息」，正文会出现 {$卡密信息}，保存。发货时该变量替换为本次出库内容。
3. 回到「发货」→「销售中」，打开兑换码商品的付款后发货设置。
4. 使用「动态卡密」，选择刚准备好的「发货卡种」和「内容模板」，确认启用后保存。

**完成检查：**商品绑定的是正确卡种，模板保留卡密信息变量，库存充足且设置已启用。

[![卡密模板中保留卡密信息变量](https://xianyu.dongeai.com/img/tutorials/auto-delivery/07-card-template.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/07-card-template.webp)

卡密模板中保留卡密信息变量 · 点击图片可放大

[![商品选择对应卡种和内容模板](https://xianyu.dongeai.com/img/tutorials/auto-delivery/08-card-setting.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/08-card-setting.webp)

商品选择对应卡种和内容模板 · 点击图片可放大

## 六、核对买家消息与出库记录

1. 在正常付款订单中检查买家会话：固定内容是否发出完整链接和说明；动态卡密是否发出了本次兑换码。
2. 检查订单已发货和发货凭证。
3. 动态卡密还要进入对应卡种的「管理卡密」→「已售」核对出库记录，并确认可用库存已相应减少。

没有自动发货时，依次检查店铺在线状态、商品配置是否启用、绑定的模板与卡种，以及库存是否充足。补货仍从对应卡种「添加卡密」进入。

[![固定内容示例：链接和说明完整发出](https://xianyu.dongeai.com/img/tutorials/auto-delivery/09-fixed-result.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/09-fixed-result.webp)

固定内容示例：链接和说明完整发出 · 点击图片可放大

[![动态卡密示例：消息中带本次出库码](https://xianyu.dongeai.com/img/tutorials/auto-delivery/10-card-result.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/10-card-result.webp)

动态卡密示例：消息中带本次出库码 · 点击图片可放大

[![在已售列表核对本次出库记录](https://xianyu.dongeai.com/img/tutorials/auto-delivery/11-sold.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/11-sold.webp)

在已售列表核对本次出库记录 · 点击图片可放大

## 观看操作视频

需要看连续操作过程，可以打开对应的视频演示。

[去 B 站看完整演示 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/)

时长 2 分 44 秒。点击章节可打开对应时间点。

- [ 00:00付款后自动发货效果 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=0)
- [ 00:13固定内容和动态卡密怎么选 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=13)
- [ 00:28接入店铺与运行条件 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=28)
- [ 00:44准备下载链接和说明 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=44)
- [ 01:02为链接商品设置付款后发货 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=62)
- [ 01:18创建卡种、导入与库存预警 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=78)
- [ 01:37为卡密商品设置付款后发货 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=97)
- [ 01:59检查实际交付与已售记录 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=119)
- [ 02:18常见问题与补货说明 ↗](https://www.bilibili.com/video/BV1U8x46oEmJ/?t=138)

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/auto-delivery/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
