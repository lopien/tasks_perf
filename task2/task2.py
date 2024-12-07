circle_file = input('Введите путь к файлу c координатами и радиусом окружности:')
circle = open(circle_file, "r")
content = circle.read().split()
circle.close()

dots_file = input('Введите путь к файлу c координатами точек:')
dots = open(dots_file, "r")
contents = dots.read().split('\n')
dots.close()

center_x = int(content[0])
center_y = int(content[1])
r = int(content[2])

def task_2(x, y):
    if (x - center_x)**2 + (y - center_y)**2 < r**2:
        print(1)
    elif  (x - center_x)**2 + (y - center_y)**2 == r**2:
        print(0)
    elif  (x - center_x)**2 + (y - center_y)**2 > r**2:
        print(2)

for i in range(len(contents)):
    x = int(contents[i].split()[0])
    y = int(contents[i].split()[1])
    task_2(x,y)