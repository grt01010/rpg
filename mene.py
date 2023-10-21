import PySimpleGUI as ps
wit = [
    [ps.Text('ведите имя'),ps.InputText()],
    [ps.Text('размер плиток'),ps.OptionMenu([16,32,48,64,])],
    [ps.Text('выбор управлением'),ps.Radio('a,w,d,s',group_id=1),ps.Radio('стрелки',group_id=1)],
    [ps.InputText(),ps.ColorChooserButton('цвет')],
    [ps.Button('старт'),ps.Button('выход')]

]
okno = ps.Window('dasdasdfas',wit)
s = 0
while s == 0:
    a = okno.read()
    f = a[0]
    fg = a[1]
    if f == 'старт' or f == 'выход':
        s = 1