# WebWeChat
通过Django程序实现对WeChat接口的请求，可以和微信联系人实现收发消息

登录

    API 	获取 UUID
    url 	https://login.weixin.qq.com/jslogin
    params
        method         GET
        appid:         应用ID
        redirect_uri   上次访问的url
        fun:           new 应用类型
        lang:          zh_CN 语言
        _:             时间戳
        
    获取UUID返回数据格式
    window.QRLogin.code = 200; window.QRLogin.uuid = "xxxxxxxx"
    
    获取二维码
    API 	生成二维码
    url 	https://login.weixin.qq.com/l/ uuid
    
    二维码扫描
    API 	二维码扫描登录
    url 	https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/login
    params 	
        method      GET
        loginicon   true
        tip:        1 未扫描 0 已扫描
        uuid:       xxxxxxxx
        r:          140686053
        _           时间戳
    
    返回数据格式(String)
    window.code=xxx;
    xxx:
	    408 登陆超时
	    201 扫描成功
	    200 确认登录
        当返回200时，还会有
        window.redirect_uri="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=xxx&uuid=xxx&lang=xxx&scan=xxx";
 

