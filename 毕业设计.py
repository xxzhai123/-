#!/usr/bin/env python        可以让这个py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-      使用标准UTF-8编码；

' 毕业设计计算 '            #表示模块的文档注释

__author__ = 'Lawrence Wonder'  #作者名

import sys                   #导入其他模块
from core import *
from config import *
product = get_yield(yields)
kg,kmol = get_pure_yield_day(168.5,specification,work_day_year,productive_ability) #日纯品量产物摩尔质量为168.5
m0 = kmol*175/product # 纯2,6-二氯苯甲醛的质量 kmol为日纯品量，175为相对分子质量，product为产率
print('每天需纯2,6-二氯苯甲醛（分子量175）投料量为：%.2fkg'%m0)
print('环合工段')
m1 = m0/175*240.5
print(indent+'中间体4-氯苯并[b]噻吩-2-甲酸乙酯的理论产量：%.2fkg'%m1)
m2 = m1 * yields[0]
m3 = m1 - m2
print(indent*2+'实际产量：%.2fkg'%m2)
print(indent*2+'损失量：%.2fkg'%m3+'(副反应损失，转化为杂质)')
m4 = m0/175*36.5
print(indent+'氯化氢的生成量：%.2fkg'%m4)
m5 = m0/175*18
print(indent+'水的生成量：%.2fkg'%m5)

m8 = m0/0.99
print(indent*1+snA(1)+'2,6-二氯苯甲醛(%.2fkg)'%m8)
print(indent*2+sna(1)+'纯：%.2fkg'%m0)
print(indent*2+sna(2)+'杂质：%.2fkg'%(m8-m0))

m9 = solution_ratio*m0      # 投料比以折纯量为基准
print(indent*1+snA(2)+'DMF(%.2fkg)'%m9)
print(indent*2+sna(1)+'纯：%.2fkg'%(m9*0.99))
print(indent*2+sna(2)+'杂质：%.2fkg'%(m9*0.01))

m10 = feed_ratio*m0      # 巯基乙酸乙酯
print(indent*1+snA(3)+'巯基乙酸乙酯(%.2fkg)'%m10)
print(indent*2+sna(1)+'纯：%.2fkg'%(m10*0.99))
print(indent*2+sna(2)+'杂质：%.2fkg'%(m10*0.01))

m11 = catalyst_ratio*m0      # 碳酸钾
print(indent*1+snA(4)+'碳酸钾(%.2fkg)'%m11)
print(indent*2+sna(1)+'纯：%.2fkg'%(m11*0.99))
print(indent*2+sna(2)+'杂质：%.2fkg'%(m11*0.01))

m12 = m2+m9*0.99+m10*0.99-m0/175*120+m11*0.99+m4+m5+m3+(0.01*(m8+m9+m10+m11))      # 环合液
print(indent*1+snA(5)+'环合液(%.2fkg)'%m12)
print(indent*2+sna(1)+'4-氯苯并[b]噻吩-2-甲酸乙酯：%.2fkg'%m2)
print(indent*2+sna(2)+'DMF：%.2fkg'%(m9*0.99))
print(indent*2+sna(3)+'巯基乙酸乙酯：%.2fkg'%(m10*0.99-m0/175*120))
print(indent*2+sna(4)+'碳酸钾：%.2fkg'%(m11*0.99))
print(indent*2+sna(5)+'氯化氢：%.2fkg'%(m4))
print(indent*2+sna(6)+'水：%.2fkg'%(m5))
print(indent*2+sna(7)+'总杂质：%.2fkg'%(m3+(0.01*(m8+m9+m10+m11))))
print()
print(indent*1+'环合液比容约为：1000kg/m3')
print(indent*1+'所需反应釜的体积约为：%.2fL'%(m12))

print('水解工段')
print(indent+od(1)+'减压蒸馏')
print(indent*2+snA(1)+'环合液(%.2fkg)：组分量如上述E所示'%m12)

m13 = m10*0.99-m0/175*120 + m4 + m5 + m9*0.99*0.6
print(indent*2+snA(2)+'DMF溶液(%.2fkg)'%m13)
print(indent*3+sna(1)+'巯基乙酸乙酯：%.2fkg'%(m10*0.99-m0/175*120)) # 全部蒸出
print(indent*3+sna(2)+'氯化氢：%.2fkg'%m4) # 全部蒸出
print(indent*3+sna(3)+'水：%.2fkg'%m5) # 全部蒸出
print(indent*3+sna(4)+'DMF：%.2fkg'%(m9*0.99*0.6)) # 蒸出 60%的DMF

m14 = m2 + m9*0.99*0.4 + m11*0.99 + m3+(0.01*(m8+m9+m10+m11))
print(indent*2+snA(3)+'浓缩溶液(%.2fkg)'%m14)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩-2-甲酸乙酯：%.2fkg'%m2)
n1 = m9*0.99*0.4
print(indent*3+sna(2)+'DMF：%.2fkg'%n1) # 剩下 40%的DMF
n2 = m11*0.99
print(indent*3+sna(3)+'碳酸钾：%.2fkg'%n2)
o1 = m3+(0.01*(m8+m9+m10+m11))
print(indent*3+sna(4)+'杂质：%.2fkg'%o1)

print(indent+od(2)+'水解')
m15 = m2/240.5*234.5
print(indent*2+'中间体4-氯苯并[b]噻吩-2-甲酸钠的理论产量：%.2fkg'%m15)
m16 = m15 * yields[1]
m17 = m15 - m16
print(indent*2+'实际产量：%.2fkg'%m16)
print(indent*2+'损失量：%.2fkg'%m17+'(副反应损失，转化为杂质)')
m18 = m2/240.5*46
print(indent*2+'乙醇生成量：%.2fkg'%m18)
print(indent*2+snA(1)+'蒸馏后溶液(%.2fkg)：组分量如上述C所示'%m14)

o2 =  NaOH_equal*m2/240.5*40                  # 计算所需NaOH的质量
o3 =  NaOH_water_ratio*m2                     # 计算所需水的质量
n3 =  o2*0.01                                 # 计算所需NaOH溶液的杂质的质量，取1%
m19 = o2 + o3 + n3    # 5当量水,2当量氢氧化钠,以4-氯苯并[b]噻吩-2-甲酸乙酯m2为基准
print(indent*2+snA(2)+'NaOH水溶液(%.2fkg)'%m19)
print(indent*3+sna(1)+'NaOH：%.2fkg'%o2)
print(indent*3+sna(2)+'水：%.2fkg'%o3)
print(indent*3+sna(3)+'NaOH水溶液的杂质：%.2fkg'%n3)


m20 = m16 + m2/240.5*46 + o2 - m2/240.5*40 + NaOH_water_ratio*m2 + n1 + n2 + o1 + m17 + n3
print(indent*2+snA(3)+'水解液(%.2fkg)'%m20)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩-2-甲酸钠：%.2fkg'%m16)
m21 = m2/240.5*46
print(indent*3+sna(2)+'乙醇生成：%.2fkg'%m21)
m22 = o2 - m2/240.5*40
print(indent*3+sna(3)+'氢氧化钠剩余：%.2fkg'%m22)
n4 = NaOH_water_ratio*m2
print(indent*3+sna(4)+'水：%.2fkg'%n4)
print(indent*3+sna(5)+'DMF：%.2fkg'%n1)
print(indent*3+sna(6)+'碳酸钾：%.2fkg'%n2)
m23 = o1 + m17 + n3
print(indent*3+sna(7)+'杂质：%.2fkg'%m23)

print('酸化工段')
print(indent+od(1)+'脱色、压滤')
print(indent*2+snA(1)+'水解后溶液(%.2fkg)：组分量如上述C所示'%m20)
m24 = m15*actvd_cbn_ratio
print(indent*2+snA(2)+'活性炭：%.2fkg'%m24)

print(indent*2+snA(3)+'滤饼：%.2fkg'%m24)
print(indent*3+sna(1)+'活性炭：%.2fkg'%m24)

m25 = m16 + m21 + m22 + n1 + n2 + n3 + n4
print(indent*2+snA(4)+'滤液：%.2fkg'%m25)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩-2-甲酸钠：%.2fkg'%m16)
print(indent*3+sna(2)+'乙醇：%.2fkg'%m21)
print(indent*3+sna(3)+'氢氧化钠：%.2fkg'%m22)
print(indent*3+sna(4)+'水：%.2fkg'%n4)
print(indent*3+sna(5)+'DMF：%.2fkg'%n1)
print(indent*3+sna(6)+'碳酸钾：%.2fkg'%n2)
print(indent*3+sna(7)+'杂质：%.2fkg'%m23)

print(indent+od(2)+'酸化')
m26 = m16/234.5*212.5
print(indent*2+'中间体4-氯苯并[b]噻吩-2-甲酸的理论：%.2fkg'%m26)
m27 = m26*yields[2]
m28 = m26 - m27
print(indent*3+'实际产量：%.2fkg'%m27)
print(indent*3+'损失量：%.2fkg'%m28+'(副反应损失，转化为杂质)')
m29 = m16/234.5*58.5
print(indent*2+'生成的氯化钠产量：%.2fkg'%m29)
print(indent*2+snA(1)+'过滤后溶液：(%.2fkg)：组分量如上述D所示'%m25)

m30 = HCL_equal*m16/234.5*36.5                  # 盐酸的质量
m31 = m30/0.36-m30                              # 水的质量
m32 = m30*0.01                                  # 杂质的质量
m33 = m30 + m31 + m32
print(indent*2+snA(2)+'6N盐酸溶液(%.2fkg)'%m33)  # 12N 盐酸质量比为36%，6N 盐酸质量比为18%
print(indent*3+sna(1)+'盐酸：%.2fkg'%m30)
print(indent*3+sna(2)+'水：%.2fkg'%m31)
print(indent*3+sna(3)+'盐酸溶液杂质：%.2fkg'%m32)

m34 = m30 - m16/234.5*36.5                                           # 盐酸剩余
m35 = m23 + m28 + m32                                                # 杂质总量
p1 = n4 + m31                                                        # 水混合后总量
m36 = m27 +m21 +m22 +p1 +n1 +n2 +m29 +m34 +m35                       # 酸化后的溶液
print(indent*2+snA(3)+'酸化后的溶液(%.2fkg)'%m36)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩-2-甲酸：%.2fkg'%m27)
print(indent*3+sna(2)+'乙醇：%.2fkg'%m21)
print(indent*3+sna(3)+'氢氧化钠：%.2fkg'%m22)
print(indent*3+sna(4)+'水：%.2fkg'%p1)
print(indent*3+sna(5)+'DMF：%.2fkg'%n1)
print(indent*3+sna(6)+'碳酸钾：%.2fkg'%n2)
print(indent*3+sna(7)+'氯化钠：%.2fkg'%m29)
print(indent*3+sna(8)+'盐酸剩余：%.2fkg'%m34)
print(indent*3+sna(9)+'杂质：%.2fkg'%m35)

print(indent+od(3)+'结晶、离心')
print(indent*2+snA(1)+'酸化后的溶液(%.2fkg)：组分量如上述C所示'%m36)

m37 = m35*centrfg_ratio                                                  # 杂质计算
m38 = m35 - m37                                                          # 杂质剩余
m39 = m21 +m22 +p1 +n1 +n2 +m29 +m34 +m37                                # 滤液总量
print(indent*2+snA(2)+'滤液(%.2fkg)'%m39)
print(indent*3+sna(1)+'乙醇：%.2fkg'%m21)
print(indent*3+sna(2)+'氢氧化钠：%.2fkg'%m22)
print(indent*3+sna(3)+'水：%.2fkg'%p1)
print(indent*3+sna(4)+'DMF：%.2fkg'%n1)
print(indent*3+sna(5)+'碳酸钾：%.2fkg'%n2)
print(indent*3+sna(6)+'氯化钠：%.2fkg'%m29)
print(indent*3+sna(7)+'盐酸：%.2fkg'%m34)
print(indent*3+sna(8)+'杂质：%.2fkg'%m37)

m40 = m27 + m38
print(indent*2+snA(3)+'滤饼(%.2fkg)'%m40)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩-2-甲酸：%.2fkg'%m27)
print(indent*3+sna(2)+'杂质：%.2fkg'%m38)

m41 = wash_ratio*m27                              # 计算需水量
m42 = wash_deimpty_ratio*m38                      # 计算洗涤杂质去除量
m43 = m38 - m42                                   # 计算杂质去除后剩余量
m44 = m41 + m42                                   # 洗涤液出去总量
m45 = m27 + m43                                   # 洗涤后滤饼总量
print(indent+od(4)+'洗涤')
print(indent*2+snA(1)+'滤饼(%.2fkg)：组分量如上述C所示'%m40)
print(indent*2+snA(2)+'洗涤液(%.2fkg)'%m41)
print(indent*3+sna(1)+'水：%.2fkg'%m41)
print(indent*2+snA(3)+'洗涤液出水(%.2fkg)'%m44)
print(indent*3+sna(1)+'水：%.2fkg'%m41)
print(indent*3+sna(2)+'杂质去除：%.2fkg'%m42)
print(indent*2+snA(4)+'洗涤后滤饼(%.2fkg)'%m45)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩-2-甲酸：%.2fkg'%m27)
print(indent*3+sna(2)+'杂质剩余：%.2fkg'%m43)

print('脱羧反应工段')
print(indent+od(1)+'脱羧')
o4 = m27/212.5*168.5
o5 = o4 * yields[3]
o6 = o4 - o5
o7 = m27/212.5*44          #二氧化碳生成量
print(indent*2+'中间体4-氯苯并[b]噻吩的理论产量：%.2fkg'%o4)
print(indent*3+'实际产量：%.2fkg'%o5)
print(indent*3+'损失量：%.2fkg'%o6+'(副反应损失，转化为杂质)')
print(indent*2+'二氧化碳生成量：%.2fkg'%o7)

m46 = solution_ratio*m27                            # 计算喹啉用量，投料比以折纯量为基准
n5 = m46*0.99                                       # 喹啉纯量
n6 = m46*0.01                                       # 喹啉杂质
m47 = Cu2O_equal*m27                                # 氧化亚铜用量
n7 = m47*0.99                                       # 氧化亚铜纯量
n8 = m47*0.01                                       # 氧化亚铜杂质
print(indent*2+snA(1)+'4-氯苯并[b]噻吩-2-甲酸粗品(%.2fkg)'%m45)
print(indent*3+sna(1)+'纯：%.2fkg'%m27)
print(indent*3+sna(2)+'杂质：%.2fkg'%m43)
print(indent*2+snA(2)+'喹啉(%.2fkg)'%m46)
print(indent*3+sna(1)+'纯：%.2fkg'%n5)
print(indent*3+sna(2)+'杂质：%.2fkg'%n6)
print(indent*2+snA(3)+'氧化亚铜(%.2fkg)'%m47)
print(indent*3+sna(1)+'纯：%.2fkg'%n7)
print(indent*3+sna(2)+'杂质：%.2fkg'%n8)

m48 = m43 + n6 + n8 + o6                                              # 杂质总量计算
m49 = o5 + n5 + n7 + o7 + m48                                              # 脱羧反应液总量计算
print(indent*2+snA(4)+'脱羧反应液(%.2fkg)'%m49)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩：%.2fkg'%o5)
print(indent*3+sna(2)+'喹啉：%.2fkg'%n5)
print(indent*3+sna(3)+'氧化亚铜：%.2fkg'%n7)
print(indent*3+sna(4)+'二氧化碳：%.2fkg'%o7)
print(indent*3+sna(5)+'杂质：%.2fkg'%m48)

m50 = n5*quinoline_steamed                  # 喹啉蒸出量
m51 = n5 - m50                              # 喹啉剩余量
m52 = qench_HCl_equal*o5/168.5*36.5         # 盐酸量
m53 = qench_HCl_water_ratio*o5              # 水量
m54 = m52*0.01                              # 盐酸杂质
m55 = m52 + m53 + m54                       # 盐酸溶液总量
m56 = m48 + m54                             # 总杂质量=脱羧反应液+盐酸杂质
m57 = o5 + m51 + n7 + o7 + m52 + m53 + m56  # 剩余溶液总量
print(indent+od(2)+'减压蒸馏、淬灭')
print(indent*2+snA(1)+'脱羧反应溶液(%.2fkg)：组分量如上述D所示'%m49)
print(indent*2+snA(2)+'喹啉回收溶剂(%.2fkg)'%m50)
print(indent*3+sna(1)+'喹啉：%.2fkg'%m50)
print(indent*2+snA(3)+'盐酸溶液(%.2fkg)'%m55)
print(indent*3+sna(1)+'盐酸：%.2fkg'%m52)
print(indent*3+sna(2)+'水：%.2fkg'%m53)
print(indent*3+sna(3)+'盐酸溶液杂质：%.2fkg'%m54)
print(indent*2+snA(4)+'剩余溶液(%.2fkg)'%m57)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩：%.2fkg'%o5)
print(indent*3+sna(2)+'喹啉：%.2fkg'%m51)
print(indent*3+sna(3)+'氧化亚铜：%.2fkg'%n7)
print(indent*3+sna(4)+'二氧化碳：%.2fkg'%o7)
print(indent*3+sna(5)+'盐酸：%.2fkg'%m52)
print(indent*3+sna(6)+'水：%.2fkg'%m53)
print(indent*3+sna(7)+'杂质：%.2fkg'%m56)

m58 = m56 * centrfg_ratio                    # 离心杂质去除比例20%
m59 = m56 - m58                              # 离心杂质剩余80%
m60 = n7 + m58                              # 滤饼总量
m61 = o5 + m51 +o7 +m52 +m53 +m59             # 滤液总量
print(indent+od(3)+'离心压滤')
print(indent*2+snA(1)+'母液(%.2fkg)：组分量如上述D所示'%m57)
print(indent*2+snA(2)+'滤饼(%.2fkg)'%m60)
print(indent*3+sna(1)+'氧化亚铜：%.2fkg'%n7)
print(indent*3+sna(2)+'杂质：%.2fkg'%m58)
print(indent*2+snA(3)+'滤液(%.2fkg)'%m61)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩：%.2fkg'%o5)
print(indent*3+sna(2)+'喹啉：%.2fkg'%m51)
print(indent*3+sna(3)+'二氧化碳：%.2fkg'%o7)
print(indent*3+sna(4)+'盐酸：%.2fkg'%m52)
print(indent*3+sna(5)+'水：%.2fkg'%m53)
print(indent*3+sna(6)+'杂质：%.2fkg'%m59)

m62 = ea_ratio*o5                                  # 乙酸乙酯投料量
m63 = m62*0.99                                     # 纯乙酸乙酯
m64 = m62*0.01                                     # 杂质乙酸乙酯
m65 = separation_deimpty_ratio*m59                 # 水层杂质
m66 = o7 + m52 + m53 +m65                          # 水层总量
m67 = m59 - m65 +m64                               # 有机层杂质,乙酸乙酯中的杂质全部归入有机层
m68 = o5 + m51 + m63 + m67                         # 有机层总量
print(indent+od(4)+'萃取')
print(indent*2+snA(1)+'离心液体(%.2fkg)：组分量如上述C所示'%m61)
print(indent*2+snA(2)+'乙酸乙酯(%.2fkg)'%m62)
print(indent*3+sna(1)+'纯乙酸乙酯：%.2fkg'%m63)
print(indent*3+sna(2)+'杂质乙酸乙酯：%.2fkg'%m64)
print(indent*2+snA(3)+'水层(%.2fkg)'%m66)
print(indent*3+sna(1)+'二氧化碳：%.2fkg'%o7)
print(indent*3+sna(2)+'盐酸：%.2fkg'%m52)
print(indent*3+sna(3)+'水：%.2fkg'%m53)
print(indent*3+sna(4)+'水层杂质：%.2fkg'%m65)
print(indent*2+snA(4)+'有机层(%.2fkg)'%m68)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩：%.2fkg'%o5)
print(indent*3+sna(2)+'喹啉：%.2fkg'%m51)
print(indent*3+sna(3)+'乙酸乙酯：%.2fkg'%m63)
print(indent*3+sna(4)+'有机层杂质：%.2fkg'%m67)

m69 = NaCl_solution_ratio * o5          # 氯化钠溶液总量 氯化钠溶液投料比为5
m70 = NaCl_conc * m69                   # 氯化钠纯量
m71 = m70 * 0.01                        # 氯化钠杂质
m72 = m69 - m70 -m71                    # 氯化钠溶液含水量
n9 = m67 + m71                          # 总杂质
m73 = n9 * separation_deimpty_ratio     # 水层杂质
m74 = n9 - m73                          # 有机层杂质
m75 = m70 + m72 + m73                   # 水层总量
m76 = o5 + m51 + m63 + m74              # 有机层总量
print(indent+od(5)+'洗涤，分液')
print(indent*2+snA(1)+'有机层液体(%.2fkg)：组分量如上述E所示'%m68)
print(indent*2+snA(2)+'氯化钠溶液(%.2fkg)'%m69)
print(indent*3+sna(1)+'NaCl：%.2fkg'%m70)
print(indent*3+sna(2)+'水：%.2fkg'%m72)
print(indent*3+sna(3)+'NaCl杂质：%.2fkg'%m71)
print(indent*2+snA(3)+'水层(%.2fkg)'%m75)
print(indent*3+sna(1)+'NaCl：%.2fkg'%m70)
print(indent*3+sna(2)+'水：%.2fkg'%m72)
print(indent*3+sna(3)+'水层杂质：%.2fkg'%m73)
print(indent*2+snA(4)+'有机层(%.2fkg)'%m76)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩：%.2fkg'%o5)
print(indent*3+sna(2)+'喹啉：%.2fkg'%m51)
print(indent*3+sna(3)+'乙酸乙酯：%.2fkg'%m63)
print(indent*3+sna(4)+'有机层杂质：%.2fkg'%m74)

m77 = m51 + m63 + m74           # 溶剂回收
print(indent+od(6)+'减压蒸馏')
print(indent*2+snA(1)+'有机层(%.2fkg)：组分量如上述D所示'%m76)
print(indent*2+snA(2)+'溶剂回收(%.2fkg)'%m77)
print(indent*3+sna(1)+'喹啉：%.2fkg'%m51)
print(indent*3+sna(2)+'乙酸乙酯：%.2fkg'%m63)
print(indent*3+sna(3)+'有机层杂质：%.2fkg'%m74)
print(indent*2+snA(3)+'产物(%.2fkg)'%o5)
print(indent*3+sna(1)+'4-氯苯并[b]噻吩：%.2fkg'%o5)








