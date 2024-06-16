MAX_FRAME = 30
m = 0           # 地图大小
n = 0
airCrafts = []  # 战斗机         （x坐标，y坐标，油箱容量gas，最大载弹量missile）
blueBases = []  # 蓝方基地       （x坐标，y坐标，燃油储备gas，导弹储备missile，防御数值defence，军事价值value）
redBases = []   # 红方基地       （x坐标，y坐标，燃油储备gas，导弹储备missile，防御数值defence，军事价值value）
fieldMap = []        # 地图


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
            # 判断每个战斗机的动作
            for airCraft in airCrafts:
                break
                # 如果在基地，加油并补充导弹

                # 如果前后左右有红方基地，发动攻击

                # 
            # 下一帧
            print('OK', file=f)
            frame = frame + 1
    # 返回
    return score
