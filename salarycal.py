'This is a script to help me calculate my salary'
def get(msg):
    
    r = float(input(msg))
    if r is None:
        return float(0)
    return r

base = get('please input your basic salary(yuan): ')
workaday = get('please input your worday overtime(hrs): ')
holiday = get('please input your holiday overtime(hrs)')
subsidy = float(248+600+1280)
pay = float(202+74+365+165+60)
overtimePay = (base/174)*(1.5*workaday+2*holiday)

salary = base+overtimePay+subsidy-pay

print (salary)
if input("按任意键退出程序")!="":exit()
