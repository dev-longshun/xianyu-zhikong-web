---
title: 闲鱼虚拟商品怎么自动发货？网盘链接、卡密、多规格四种做法 · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/virtual-goods-delivery/
description: 在闲鱼卖网盘资料、兑换码这类虚拟商品，买家付款后怎么自动发出去：每单一样的用固定内容，每单不同的用卡密库存，多规格、收货后再送、卡密单独发一条也一并讲清。
---

Seller Notes

# 闲鱼虚拟商品怎么自动发货

在闲鱼卖网盘资料、兑换码这类虚拟商品，买家付款后怎么自动发出去：每单一样的用固定内容，每单不同的用卡密库存，多规格、收货后再送、卡密单独发一条也一并讲清。

卖家经验 适用版本 1.6.0 更新于 2026-11-09

闲鱼上的虚拟商品不用寄快递：买家付款后，把网盘链接、兑换码或使用说明发到聊天里，就算交付完成。想做到半夜付款也能秒发，需要一个一直在线的卖家工具，看到付款就自动把内容发出去。按交付内容不同，有四种做法，下面一种一种讲，截图来自闲鱼智控电脑客户端。

## 一、先分清你卖的是哪一类

| 你卖的东西 | 每单发的内容 | 用哪种发货方式 |
| --- | --- | --- |
| 网盘资料、教程文档、模板素材 | 每位买家都一样 | 固定内容模板 |
| 兑换码、激活码、卡密 | 每单一张，不能重复 | 卡种库存 + 动态卡密 |
| 月卡、年卡这类多规格商品 | 按买家选的规格发 | 每个规格绑自己的卡种 |
| 你自己系统实时生成的码 | 每单现取 | 接你自己的发卡接口 |

## 二、每单内容一样：用固定内容模板

网盘链接、资料说明这类，写一份内容模板，绑到商品上，买家付款后原样发出。

1. 在「发货」→「内容模板」新建模板，正文写完整的链接、提取码和使用说明。
2. 到「发货」→「销售中」找到商品，在「付款后发货」一栏点「设置」。
3. 发货内容来源选「固定内容」，选好刚才的模板，打开启用，保存。

[![闲鱼虚拟商品发货内容模板：填写网盘链接、提取码和使用说明](https://xianyu.dongeai.com/img/tutorials/auto-delivery/02-fixed-template.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/02-fixed-template.webp)

闲鱼虚拟商品发货内容模板：填写网盘链接、提取码和使用说明 · 点击图片可放大

[![闲鱼商品付款后发货设置：发货内容来源选固定内容并启用](https://xianyu.dongeai.com/img/tutorials/auto-delivery/03-fixed-setting.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/03-fixed-setting.webp)

闲鱼商品付款后发货设置：发货内容来源选固定内容并启用 · 点击图片可放大

[![买家付款后，闲鱼聊天里自动收到网盘链接和说明](https://xianyu.dongeai.com/img/tutorials/auto-delivery/09-fixed-result.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/09-fixed-result.webp)

买家付款后，闲鱼聊天里自动收到网盘链接和说明 · 点击图片可放大

## 三、每单发不同的码：卡种库存加动态卡密

兑换码、激活码要一单一张。先把码导入「卡种」当库存，每来一单从库存里取一张，发过的自动标成已售，不会重复发。

1. 在「发货」→「卡种」创建卡种，点「添加卡密」，每行一张粘贴进去。
2. 内容模板里插入「卡密信息」变量，发货时它会换成本次取出的码。
3. 商品的付款后发货选「动态卡密」，选好卡种和模板，启用保存。
4. 需要的话给卡种设库存预警，库存不够时弹窗提醒；补货后可以一键补发没发出去的单。

[![闲鱼卡密自动发货：把兑换码每行一张导入卡种库存](https://xianyu.dongeai.com/img/tutorials/auto-delivery/05-import.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/05-import.webp)

闲鱼卡密自动发货：把兑换码每行一张导入卡种库存 · 点击图片可放大

[![闲鱼商品付款后发货选择动态卡密、卡种和内容模板](https://xianyu.dongeai.com/img/tutorials/auto-delivery/08-card-setting.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/08-card-setting.webp)

闲鱼商品付款后发货选择动态卡密、卡种和内容模板 · 点击图片可放大

[![买家付款后自动收到本单的兑换码](https://xianyu.dongeai.com/img/tutorials/auto-delivery/10-card-result.webp)](https://xianyu.dongeai.com/img/tutorials/auto-delivery/10-card-result.webp)

买家付款后自动收到本单的兑换码 · 点击图片可放大

软件不提供卡密货源，库存要用你自己合法取得的码。也可以不导入库存，接你自己的发卡接口，每单实时取一张。完整步骤见[付款后自动发货怎么设置](https://xianyu.dongeai.com/tutorials/auto-delivery/)。

## 四、一个商品多个规格：每个规格绑自己的卡种

同一个链接卖月卡和年卡，买家选月卡就该发月卡的码。做法是月卡、年卡各建一个卡种，在商品的规格里分别绑定，说明模板可以共用。

[![闲鱼多规格商品自动发货：月卡规格对应月卡库存，年卡规格对应年卡库存](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/07-mapping.webp)](https://xianyu.dongeai.com/img/tutorials/multi-spec-delivery/07-mapping.webp)

闲鱼多规格商品自动发货：月卡规格对应月卡库存，年卡规格对应年卡库存 · 点击图片可放大

详细步骤见[多规格商品怎么设置自动发货](https://xianyu.dongeai.com/tutorials/multi-spec-delivery/)。

## 五、收货后、好评后再送一份

除了付款后发货，同一个商品还可以设「收货后赠送」和「好评后赠送」：比如付款先发资料，确认收货再发使用指南，好评后再送一份扩展素材。三个时间点各选各的模板。

[![同一个闲鱼商品分别设置付款后发货、收货后赠送、好评后赠送三份内容](https://xianyu.dongeai.com/img/tutorials/delivery-timing/08-settings-result.webp)](https://xianyu.dongeai.com/img/tutorials/delivery-timing/08-settings-result.webp)

同一个闲鱼商品分别设置付款后发货、收货后赠送、好评后赠送三份内容 · 点击图片可放大

详细步骤见[付款发货、收货赠送、好评赠送怎么设置](https://xianyu.dongeai.com/tutorials/delivery-timing/)。

## 六、让买家好复制：卡密单独再发一条

买家说「码不对」，很多时候是复制时连感谢语一起带上了。可以在内容模板里加一条「单独消息」：正文照常发，隔一下再发一条只有卡密的消息，买家长按就能全选复制。

[![闲鱼自动发货后单独再发一条只有卡密的消息，两张卡密逐行排列](https://xianyu.dongeai.com/img/tutorials/card-followup/07-clean-codes.webp)](https://xianyu.dongeai.com/img/tutorials/card-followup/07-clean-codes.webp)

闲鱼自动发货后单独再发一条只有卡密的消息，两张卡密逐行排列 · 点击图片可放大

详细步骤见[卡密或链接怎么单独再发一条](https://xianyu.dongeai.com/tutorials/card-followup/)。

## 七、没有自动发出去，先查这几项

1. 店铺在不在线：客户端「店铺」页要显示在线，电脑开机联网、客户端在运行。
2. 商品的付款后发货有没有启用，绑的模板和卡种对不对。
3. 卡种库存够不够。
4. 漏掉的单可以手动补发；掉线重连后，客户端会提示离线期间付款的单。

## 常见问题

### 闲鱼虚拟商品自动发货，电脑要一直开着吗？

要。闲鱼智控是电脑客户端，电脑开机联网、客户端保持运行，才能看到付款并自动发货。Mac 可以打开「挂机不休眠」，笔记本合上盖子也能接着跑。

### 买家半夜付款，能马上发出去吗？

能。只要客户端在运行，买家付款后就会按你设好的模板自动发出，不用人守着。

### 卡密从哪里来？

用你自己的库存：把码导入卡种，或者接你自己的发卡接口每单实时取。软件不提供卡密货源。

### 库存发完了怎么办？

库存不够会弹窗预警。补货后可以一键补发因为没库存而没发出去的单，漏掉的单也能手动补发。

### 几个闲鱼店铺能一起自动发货吗？

能。一个客户端可以登录多个闲鱼店铺，每个店铺的商品各自设置发货。基础版每台电脑登录 1 个店铺，高级版不限，见[价格](https://xianyu.dongeai.com/pricing/)。

想直接试试？下载闲鱼智控，联系作者可以先领 7 天免费试用。

[下载客户端 →](https://xianyu.dongeai.com/download/)

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/virtual-goods-delivery/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
