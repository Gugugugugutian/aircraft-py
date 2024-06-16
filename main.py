from interface import Go

# 输入路径
dataRoot = './data'
# 输出路径
logRoot = './log'

if __name__ == "__main__":
    while True:
        print("Welcome to Aircraft Py.")
        print("Type 'quit' to quit.")
        # 选择输入数据
        print("Choose a data set: 1-10")
        choice = input('> ').strip()
        if choice == 'quit':
            break
        else:
            dataPath = dataRoot + '/testcase' + choice + '.in'
            logPath = logRoot + '/result' + choice + '.log'
            print(dataPath, logPath)
            # 功能运行
            final = Go(dataPath, logPath)
            print('Total: ', final)