import datetime #引用datetime模块
try:
   year = int(input('输入年份\n'))#输入相关数值
   month = int(input('输入月份\n'))
   day = int(input('输入日\n'))
   result = datetime.datetime(year,month,day)#套用datetime函数
   print("这一天是这一年的第" + result.strftime("%j") + "天")#在strftime函数中"%j"表示年内的一天（001-366）
   print("且为" + result.strftime("%A"))#在strftime函数中"%A"表示星期
except:
   print("数据有误，请重新输入")
