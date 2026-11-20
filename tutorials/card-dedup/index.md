---
title: 闲鱼卡密查重：补货防重复，老库存找出多余记录 · 闲鱼智控
url: https://xianyu.dongeai.com/tutorials/card-dedup/
description: 添加前查本批、库存和已售重复；只入库新卡密，再检查老库存并停用多余记录。
---

Step-by-step Guide

# 闲鱼卡密查重：补货防重复，老库存找出多余记录

添加前查本批、库存和已售重复；只入库新卡密，再检查老库存并停用多余记录。

图文教程 · 8 张操作截图 适用版本 2.1.0 更新于 2026-11-20

适用版本：2.1.0。

自动发货按库存的每一行取卡，同一个码重复入库两行，就可能被两张订单各取一次。补货先查重，老库存也检查一次。

## 一、添加卡密，先看查重结果

进入「发货 → 卡种 → 管理卡密」，点「添加卡密」，粘贴一批后点「添加」。有重复时先不入库，弹出分类计数：本批里重复、库存里已有、已经卖出过、别的卡种里有。只有首尾空格会忽略，大小写不同算不同。

[![查出重复后先不入库](https://xianyu.dongeai.com/img/tutorials/card-dedup/01-import-duplicates.webp)](https://xianyu.dongeai.com/img/tutorials/card-dedup/01-import-duplicates.webp)

查出重复后先不入库 · 点击图片可放大

## 二、三个选择怎么选

一般点「只添加不重复的 N 条」：本批里重复的保留第一条，库存已有和卖出过的跳过。需要重新编辑就点「返回修改」。确实要导入重复内容时，才选「仍然全部添加」。别的卡种里有的只提醒，仍会添加。完成后核对添加和重复跳过条数。

[![确认是修改、全部添加还是仅添加不重复的](https://xianyu.dongeai.com/img/tutorials/card-dedup/02-three-options.webp)](https://xianyu.dongeai.com/img/tutorials/card-dedup/02-three-options.webp)

确认是修改、全部添加还是仅添加不重复的 · 点击图片可放大

[![核对添加成功和重复跳过数量](https://xianyu.dongeai.com/img/tutorials/card-dedup/03-added.webp)](https://xianyu.dongeai.com/img/tutorials/card-dedup/03-added.webp)

核对添加成功和重复跳过数量 · 点击图片可放大

## 三、卡号密码分开的，只看卡号

两段卡密按卡号判断，密码不参与。相同卡号配不同密码，也算重复。只有一段的卡密按整条内容判断。

[![相同卡号配不同密码](https://xianyu.dongeai.com/img/tutorials/card-dedup/04-pair-input.webp)](https://xianyu.dongeai.com/img/tutorials/card-dedup/04-pair-input.webp)

相同卡号配不同密码 · 点击图片可放大

[![仍查出库存已有](https://xianyu.dongeai.com/img/tutorials/card-dedup/05-pair-duplicate.webp)](https://xianyu.dongeai.com/img/tutorials/card-dedup/05-pair-duplicate.webp)

仍查出库存已有 · 点击图片可放大

## 四、老库存点查重

打开某卡种的「管理卡密」，点击右上角「查重」。只检查当前卡种，列表显示未售、已卖出和多余条数。未卖过的同码留最早入库一条；已经卖出过的，未售记录全部算多余。

[![查找当前卡种的多余记录](https://xianyu.dongeai.com/img/tutorials/card-dedup/06-old-scan.webp)](https://xianyu.dongeai.com/img/tutorials/card-dedup/06-old-scan.webp)

查找当前卡种的多余记录 · 点击图片可放大

## 五、把多余的标记暂不可用

核对后点「多余的 N 条标记为暂不可用」。这些记录不会再被自动发货取到，仍留在库存里，之后可以筛选「暂不可用」再恢复。此操作不自动删除卡密。

[![多余记录已标记暂不可用](https://xianyu.dongeai.com/img/tutorials/card-dedup/07-disabled.webp)](https://xianyu.dongeai.com/img/tutorials/card-dedup/07-disabled.webp)

多余记录已标记暂不可用 · 点击图片可放大

## 六、同一个码反复卖的情况

如果本来就是同一条网盘链接反复卖，可以不处理这类重复。勾选「可添加重复卡密」或使用「重复卡密」批量生成，表示明确允许重复，不会走添加前的查重提示。

[![同一码反复卖时无需处理](https://xianyu.dongeai.com/img/tutorials/card-dedup/08-repeat-note.webp)](https://xianyu.dongeai.com/img/tutorials/card-dedup/08-repeat-note.webp)

同一码反复卖时无需处理 · 点击图片可放大

[← 返回教程中心](https://xianyu.dongeai.com/tutorials/)[下载客户端 →](https://xianyu.dongeai.com/download/)

---

网页版：https://xianyu.dongeai.com/tutorials/card-dedup/　·　闲鱼智控是第三方闲鱼卖家工具，与闲鱼官方无关。
