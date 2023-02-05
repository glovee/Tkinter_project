from tkinter import Tk, IntVar, Button, Entry, Text, Label, END


# Постоянные значения
filename = str(input('Укажите полный путь к файлу - '))

def clicked1():  
    my_file = open(filename, 'a+')
    my_file.write(str(txt_help.get()) + '\n')
    my_file.write(str(main_txt.get('1.0', 'end') + '\n'))
    if clicks.get() == 0:
        lbl.configure(text='II - III абзац - Расширенная информация по этих вопросах \n Цитата организатора или иного лица')
    elif clicks.get() == 1:
        lbl.configure(text='III (IV) абзац - Малозначительная информация или анонсы')
    elif clicks.get() == 2:
        lbl.configure(text='IV (V) абзац - Информация для справки')
    elif clicks.get() == 3:
        window.destroy()
        print('Готово!')
        print('Вот как я чувствовал себя после завершения этого говнища: https://youtube.com/clip/UgkxgOaLHXSQU5I9bV4LlS0_11EP-o76OWIr')
    txt_help.delete(0, END)
    main_txt.delete('1.0', END)
    clicks.set(clicks.get() + 1)

window = Tk()
window.title('Пресс-релиз')
window.geometry('1000x800+150+50')

clicks = IntVar(value=0)

btn = Button(window, text='Готово', bg='Green', command=clicked1)
btn.place(x=450, y=700)

txt_help = Entry(window, width=35, font=('Impact', 20))
txt_help.grid(column=0, row=1)

main_txt = Text()
main_txt.grid(column=0, row=2)

lbl = Label(window, text='I абзац - Когда? Где? Кто? Почему? Как? \n', font=('Arial Bold', 25))
lbl.grid(column=0, row=0)


window.mainloop()