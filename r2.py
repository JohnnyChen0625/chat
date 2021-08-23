import os 


def read_file(filename):
    lines = []
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    person = None
    John_word_count = 0
    John_sticker_count = 0
    John_image_count = 0
    Guava_word_count = 0
    Guava_sticker_count = 0
    Guava_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'John':
            if s[2] == '貼圖':
                John_sticker_count += 1
            elif s[2] == '圖片':
                John_image_count += 1     
            else:
                for m in (s[2:]):
                    John_word_count += len(m)
        elif name == 'Guava':
            if s[2] == '貼圖':
                Guava_sticker_count += 1
            elif s[2] == '圖片':
                Guava_image_count += 1
            else:
                for m in (s[2:]):
                    Guava_word_count += len(m)
    print('John說了',John_word_count, '個字') 
    print('John傳了', John_sticker_count, '個貼圖')
    print('John傳了', John_image_count, '張圖片')
    print('Guava說了',Guava_word_count, '個字')
    print('Guava傳了',  Guava_sticker_count, '個貼圖')
    print('Guava傳了', Guava_image_count, '張圖片')            


def write_file(filename, lines):
	with open(filename, 'w') as f :
		for line in lines:
			f.write(line + '\n')


def main():
    lines = read_file('[LINE]Guava.txt')
    lines = convert(lines) 


main()