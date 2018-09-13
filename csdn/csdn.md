# 模拟登录 CSDN

1. 首先请求 `https://passport.csdn.net/`, 获取到 `lt`、 `execution`、`_eventId` 等参数 (参数的作用后续会说明)
2. 请求 `https://passport.csdn.net/account/verify`, POST 请求, 携带上步骤一的参数以及你的账户密码
3. 你会看到 response 源码中有一个 js 方法, `var redirect = "http://www.csdn.net/";` 是转跳到你的 CSDN 首页。 我这边也打印出了 cookies 信息, 会看到 UserName、 UserNick、 UserToken 等, 表明以成功登录

# 参数说明

**lt**: 该参数可以理解成每个需要登录的用户都有一个流水号。只有有了webflow发放的有效的流水号，用户才可以说明是已经进入了webflow流程。否则，没有流水号的情况下，webflow会认为用户还没有进入webflow流程，从而会重新进入一次webflow流程，从而会重新出现登录界面。

**execution**: 带上就行

**_eventId**: 按钮提交状态 submit

**fkid**: 源码中有, 但是不知道这个参数是干嘛的


