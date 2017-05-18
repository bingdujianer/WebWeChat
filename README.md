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
        
    返回数据格式
    window.QRLogin.code = 200; window.QRLogin.uuid = "xxxx"
    
    
 

