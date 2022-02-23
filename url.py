import urllib.request
import urllib.parse


url = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login"
data = {}
data['uid'] = '202012172013059'   #账号
data['upw'] = '09274742'   #密码
data['smbtn'] = '进入健康状况上报平台'
data['hh28'] = '762'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
strlist = html.split('\n')

strlist = ['<html>\r', '<head>\r', '<meta http-equiv="Content-Language" content="zh-cn">\r', '<meta http-equiv="Content-Type" content="text/html; charset=gb2312">\r', '<title></title>\r', '<script language="javascript">\r', ' var secs=0;\r', ' for(var i=secs;i>=0;i--)\r', ' {window.setTimeout("doUpdate(" + i + ")", (secs-i) * 1000);}\r', ' function doUpdate(num)\r', ' {if (num == 0){parent.window.location="https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first6?ptopid=s23D0F29DD3A04B5187CBA2D3EB589F84&sid=210415214616165408"}}\r', '</script>\r', '</head>\r', '<body topmargin="0" leftmargin="0">\r', '</body>\r', '</html>']

for i in strlist:
    if 'https' in i:
       global list
       list = i
list = list.split('?')
for i in list:
    if 'ptopid' in i:
       global list1
       list1= i
list1 = list1.split('&')

global dict
dict = {}
for i in list1:
    if '\"' in i:
        i = i.replace("\"", "=")
    global result
    result = []
    result = i.split('=')
    dict[result[0]] = result[1]
print(dict)


url1 = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
data1={}
data1['day6'] = 'b'
data1['did'] = '1'
data1['door'] = ''
data1['men6'] = 'a'
data1['ptopid'] = dict['ptopid']   #该参数和下面的参数是随机的
data1['sid'] = dict['sid']
data1 = urllib.parse.urlencode(data1).encode('utf-8')
response1 = urllib.request.urlopen(url1, data1)
html1 = response1.read().decode('utf-8')
#print(html1)


url2 = "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb"
data2={}
data2['myvs_1'] = '否'
data2['myvs_2'] = '否'
data2['myvs_3'] = '否'
data2['myvs_4'] = '否'
data2['myvs_5'] = '否'
data2['myvs_6'] = '否'
data2['myvs_7'] = '否'
data2['myvs_8'] = '否'
data2['myvs_9'] = '否'
data2['myvs_10'] = '否'
data2['myvs_11'] = '否'
data2['myvs_12'] = '否'
data2['myvs_13a'] = '41'
data2['myvs_13b'] = '4101'
data2['myvs_13c'] = '中原区科学大道100号'
data2['myvs_14'] = '否'
data2['myvs_14b'] = ''
data2['myvs_30'] = '在校'
data2['memo22'] = '请求超时'
data2['did'] = '2'
data2['door'] =''
data2['day6'] = 'b'
data2['men6'] = 'a'
data2['sheng6'] = ''
data2['shi6'] = ''
data2['fun3'] = ''
data2['jingdu'] = '113.526700'
data2['weidu'] = '34.824000'
data2['ptopid'] = dict['ptopid'] #该参数和下面的参数是随机的
data2['sid'] = dict['sid']

data2 = urllib.parse.urlencode(data2).encode('utf-8')
response2 = urllib.request.urlopen(url2, data2)
html2 = response2.read().decode('utf-8')
print(html2)


