
# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


# 格式轉換
def convert(lines):
    allen_wc = 0
    allen_sc = 0
    allen_ic = 0
    viki_wc = 0
    viki_sc = 0
    viki_ic = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sc += 1
            elif s[2] == '圖片':
                allen_ic += 1
            else:
                for msg in s[2:]:
                    allen_wc += len(msg)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sc += 1
            elif s[2] == '圖片':
                viki_ic += 1
            else:
                for msg in s[2:]:
                    viki_wc += len(msg)

    print('Allen說了', allen_wc, '字，', allen_sc,'個貼圖，傳', allen_ic, '張圖片')
    print('Viki說了', viki_wc, '字，', viki_sc,'個貼圖，傳', viki_ic, '張圖片')      
    return 


def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    filename = 'LINE-Viki.txt'
    lines = read_file(filename)
    lines = convert(lines)
    #write_file('output.txt', lines)


main()