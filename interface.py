MAX_FRAME = 15000
m = 0           # 地图大小
n = 0
airCrafts = []  # 战斗机         （x坐标，y坐标，油箱容量gas，最大载弹量missile）
blueBases = []  # 蓝方基地       （x坐标，y坐标，燃油储备gas，导弹储备missile，防御数值defence，军事价值value）
redBases = []   # 红方基地       （x坐标，y坐标，燃油储备gas，导弹储备missile，防御数值defence，军事价值value）
fieldMap = []   # 地图


# 读取文件
def readFile(dataPath):
    with open(dataPath, 'r') as f:
        global airCrafts, blueBases, redBases, fieldMap, m, n
        # 读取地图部分
        fieldMap = []
        line1 = f.readline().strip().split(' ')
        m = int(line1[0])
        n = int(line1[1])
        for i in range(m):
            line = f.readline().strip()
            fieldMap.append(line)
        print('地图读取完成', fieldMap)
        # 读取蓝方基地信息
        blueBases = []
        blueBaseCount = int(f.readline().strip())
        for i in range(blueBaseCount):
            line1 = f.readline().strip().split(' ')
            line2 = f.readline().strip().split(' ')
            blueBases.append([
                int(line1[0]),  # x
                int(line1[1]),  # y
                int(line2[0]),  # gas
                int(line2[1]),  # missile
                int(line2[2]),  # defence
                int(line2[3]),  # value
            ])
        print('蓝方基地读取完成', blueBases)
        # 读取红方基地信息
        redBases = []
        redBaseCount = int(f.readline().strip())
        for i in range(redBaseCount):
            line1 = f.readline().strip().split(' ')
            line2 = f.readline().strip().split(' ')
            redBases.append([
                int(line1[0]),  # x
                int(line1[1]),  # y
                int(line2[0]),  # gas
                int(line2[1]),  # missile
                int(line2[2]),  # defence
                int(line2[3]),  # value
            ])
        print('红方基地读取完成', redBases)
        # 读取战斗机信息
        airCrafts = []
        airCraftCount = int(f.readline().strip())
        for i in range(airCraftCount):
            line1 = f.readline().strip().split(' ')
            # line2 = f.readline().strip().split(' ')
            airCrafts.append([
                int(line1[0]),  # x
                int(line1[1]),  # y
                int(line1[2]),  # gas
                int(line1[3]),  # missile
                0,              # current gas
                0,              # current missile
                i,              # id
            ])
        print('战斗机读取完成', airCrafts)


# 运行
def Go(dataPath, logPath):
    # 读取dataPath下的输入文件
    readFile(dataPath)
    # 运行算法
    global airCrafts, blueBases, redBases, fieldMap, m, n
    frame = 0   # 帧
    score = 0   # 总成绩
    with open(logPath, 'w') as f:
        # 最大运行15000帧
        while frame <= MAX_FRAME:
            # 打印信息
            print('[INFO] Frame:', frame, ' Score: ', score)
            # 战斗结束提前退出
            if len(redBases) == 0:
                break

            # 在这里实现算法
            for airCraft in airCrafts:
                # 计算最近的蓝方基地
                closestBlue = []
                closestBlueDistance = 999999
                for blueBase in blueBases:
                    distance = abs(blueBase[0] - airCraft[0]) + abs(blueBase[1] - airCraft[1])
                    if distance < closestBlueDistance:
                        closestBlue = blueBase
                        closestBlueDistance = distance
                # 计算最近的红方基地
                closestRed = []
                closestRedDistance = 999999
                for redBase in redBases:
                    distance = abs(redBase[0] - airCraft[0]) + abs(redBase[1] - airCraft[1])
                    if distance < closestRedDistance:
                        closestRed = redBase
                        closestRedDistance = distance
                # 如果在蓝方基地，加油并补充导弹
                if closestBlueDistance == 0:
                    # 加油
                    if airCraft[2]-airCraft[4] < closestBlue[2]:
                        fuelRefill = airCraft[2] - airCraft[4]
                    else:
                        fuelRefill = closestBlue[2]
                    print('fuel', airCraft[6], fuelRefill, file=f)
                    closestBlue[2] -= fuelRefill
                    airCraft[4] += fuelRefill
                    # 补充导弹
                    if airCraft[3] - airCraft[5] < closestBlue[3]:
                        missileRefill = airCraft[3] - airCraft[5]
                    else:
                        missileRefill = closestBlue[3]
                    print('missile', airCraft[6], missileRefill, file=f)
                    closestBlue[3] -= missileRefill
                    airCraft[5] += missileRefill
                # 如果有红方基地，攻击
                if closestRedDistance == 1:
                    # 计算要发射的导弹
                    missileCount = closestRed[4]
                    if closestRed[4]-airCraft[3] > 0:
                        missileCount = airCraft[3]
                    # 发射导弹
                    airCraft[3] -= missileCount
                    closestRed[4] -= missileCount
                    if closestRed[4] <= 0:
                        # 红方基地摧毁
                        score += closestRed[5]
                        redBases.remove(closestRed)
                    print('attack', airCraft[6], 0, missileCount, file=f)
                # 移动
                if airCraft[4] < closestRedDistance | airCraft[5] <= 0:
                    # 如果燃油不足或missile为0，向最近蓝方基地移动
                    moveTo = closestBlue
                elif closestRed:
                    # 向最近红方基地移动
                    moveTo = closestRed
                moveDirection = 0
                # 用moveTo计算移动方向
                if closestRedDistance >= 1:
                    if airCraft[0] - moveTo[0] > 0:
                        airCraft[0] -= 1
                        moveDirection = 3  # 向左
                    elif airCraft[0] - moveTo[0] < 0:
                        airCraft[0] += 1
                        moveDirection = 4  # 向右
                    else:
                        if airCraft[1] - moveTo[1] > 0:
                            airCraft[1] -= 1
                            moveDirection = 1   # 向上
                        else:
                            airCraft[1] += 1
                            moveDirection = 2   # 向下
                    airCraft[4] -= 1    # 消耗燃油
                    print('move', airCraft[6], moveDirection-1, file=f)
            # 下一帧
            print('OK', file=f)
            frame = frame + 1
    # 返回
    return score
