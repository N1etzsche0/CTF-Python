
import numpy as np

def calc_pv(lv, i, n):
    '''
    计算固定支付贷款每期还款金额
    @lv : 贷款金额
    @i  : 贷款利率
    @n  : 贷款期数
    '''
    qn = np.power(1 + i, n)
    fp = qn * lv * i
    fp = fp / (qn - 1)
    return fp

# 按年付款
print("贷款10万, 利率0.07, 20年还清，每年需还款: %f 元" % calc_pv(5000, 0.049, 1))

# 按月付款
print('若按月还款的话，每月需还款 %f 元' % calc_pv(800, 0.049/12, 1))
