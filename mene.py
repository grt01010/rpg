import PySimpleGUI as ps

wit = [
    [ps.Text('ведите имя'),ps.InputText(key='имя',default_text='ярик')],
    [ps.Text('размер плиток'),ps.OptionMenu([16,32,48,64,],key='размер плиток',default_value=32)],
    [ps.Text('выбор управлением'),ps.Radio('a,w,d,s',group_id=1,key='выбор управлением',default=True),ps.Radio('стрелки',group_id=1,key='выбор управлением2')],
    [ps.InputText(key='цвет'),ps.ColorChooserButton('цвет')],
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