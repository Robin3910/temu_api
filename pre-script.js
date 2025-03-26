const crypto = require('crypto-js');

// 获取请求体中的JSON参数
let params = JSON.parse(pm.request.body.raw);

// 检查并获取环境或全局变量的值
params.timestamp = pm.variables.replaceIn('{{$timestamp}}');
params.app_key = "4ebbc9190ae410443d65b4c2faca981f";
params.data_type = "JSON";
params.access_token = "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7";

// 添加app_secret，这个需要你自己定义或从服务器获取
let app_secret = "4782d2d827276688bf4758bed55dbdd4bbe79a79";

// 对参数名进行ASCII升序排序
let sortedKeys = Object.keys(params).sort();

// 拼接字符串
let baseString = app_secret;
sortedKeys.forEach(key => {
    let value = params[key];
    // 检查值类型并适当处理
    if (typeof value === 'object' && value !== null) {
        baseString += `${key}${JSON.stringify(value)}`;
    } else {
        baseString += `${key}${value}`;
    }
});
baseString += app_secret;

console.log(baseString);

// 计算MD5值
let hash = crypto.MD5(baseString);

// 转大写
let sign = hash.toString(crypto.enc.Hex).toUpperCase();

// 将签名添加到请求体
params["sign"] = sign;
console.log(sign);

// 更新请求体
pm.request.body.raw = JSON.stringify(params);