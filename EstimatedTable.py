import pandas as pd

Budget = 3000 # 總預算 (限定整數, 每1000+)
LoopBudget = 500 # 每組迴圈預算
Commission = 40 # 設定傭金的金額
InitialAccountBudget = 1000
AverageLotsPerLoop = 0.25 # 每組迴圈平均手數
SubAccountNumbers = 5 # 子帳號數目
WeeklyNumbers = 104 # 左側總計週數
WeeklyLots = 0 # 每週手數
# AccumulationLots = 0  # 累積手數
AutoAddLoop = True # 複利 or 單利

titlearr = ['週數', '每週總手數', '累積手數','新增迴圈數', '累積500美金加開一迴圈']

for i in range(1, SubAccountNumbers + 1):
    titlearr.insert(0 + i, '帳戶{index}'.format(index = i))

print(titlearr)

dataList = []
def EstimatedTable(WeeklyNumbers, LoopBudget, AverageLotsPerLoop, SubAccountNumbers, AutoAddLoop, Commission):
    
    AccountList = []
    AccumulationLots = 0 # 累積手數
    OverLots = LoopBudget / Commission
    
    # 週數
    for week in range(1, WeeklyNumbers + 1):
        data = {}
        data['週數'] = week
        data['每週總手數'] = 0
        data['累積手數'] = 0
        
        # 初始資金及手數配置
        if data['週數'] == 1 :
            OriginalAccountNumbers = int(Budget / InitialAccountBudget)
            for i in range(1, OriginalAccountNumbers + 1):
                money = InitialAccountBudget
                lots = money/LoopBudget*AverageLotsPerLoop
                AccountList.append({'帳戶{}總資金'.format(i) : money, '帳戶{}手數'.format(i) : lots})
                
                # data['帳戶{}總資金'.format(i)] = InitialAccountBudget
                # data['帳戶{}手數'.format(i)] = data['帳戶{}總資金'.format(i)]/LoopBudget*AverageLotsPerLoop

            for i in range(OriginalAccountNumbers + 1, SubAccountNumbers + 1):
                AccountList.append(['帳戶{}總資金'.format(i), '帳戶{}手數'.format(i)])
                data['帳戶{}總資金'.format(i)] = 0
                data['帳戶{}手數'.format(i)] = data['帳戶{}總資金'.format(i)]/LoopBudget*AverageLotsPerLoop
                
            # 每週總手數
            for i in range(1, SubAccountNumbers + 1):
                data['每週總手數'] = data['每週總手數'] + data['帳戶{}手數'.format(i)]
            
            # 累積手數
            AccumulationLots = data['每週總手數']
            data['累積手數'] = AccumulationLots

        # 當不是初始週時
        else:
            # 當累積手數能夠加碼時
            if AccumulationLots > OverLots:
                AccumulationLots =- OverLots
                

            OriginalAccountNumbers = int(Budget / InitialAccountBudget)
            for i in range(1, OriginalAccountNumbers + 1):
                data['帳戶{}總資金'.format(i)] = InitialAccountBudget
                data['帳戶{}手數'.format(i)] = data['帳戶{}總資金'.format(i)]/LoopBudget*AverageLotsPerLoop
            for i in range(OriginalAccountNumbers + 1, SubAccountNumbers + 1):
                data['帳戶{}總資金'.format(i)] = 0
                data['帳戶{}手數'.format(i)] = data['帳戶{}總資金'.format(i)]/LoopBudget*AverageLotsPerLoop
                
            # 每週總手數
            for i in range(1, SubAccountNumbers + 1):
                data['每週總手數'] = data['每週總手數'] + data['帳戶{}手數'.format(i)]

            # 累積手數
            AccumulationLots = AccumulationLots + data['每週總手數']
            data['累積手數'] = AccumulationLots

        dataList.append(data)
        pass
    # print(dataList)
    print(AccountList)
EstimatedTable(WeeklyNumbers, LoopBudget, AverageLotsPerLoop, SubAccountNumbers, AutoAddLoop, Commission)