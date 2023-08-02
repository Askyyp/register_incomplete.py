from tkinter import *

root = Tk()

class Aplicattion():
    def __init__(self):
        self.root = root
        self.Tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()

    def Tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width= 500, height= 400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd= 4, bg= '#dfe3ee',  
                             highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd= 4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text= "clean", bd= 4, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15 )

        self.bt_buscar = Button(self.frame_1, text= "search", bd= 4, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15 )

        self.bt_novo = Button(self.frame_1, text= "New", bd= 4, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15 )

        self.bt_alterar = Button(self.frame_1, text= "alter", bd= 4, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15 )

        self.bt_apagar = Button(self.frame_1, text= "Erase", bd= 4, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15 )
        # entrada do codigo
        self.lb_code = Label(self.frame_1, text= "Code", bg= '#dfe3ee', fg= '#107db2')
        self.lb_code.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.frame_1, bg= '#dfe3ee', fg= '#107db2')
        self.codigo_entry.place(relx= 0.05, rely= 0.20, relwidth= 0.08)
        # entrada do nome
        self.lb_name = Label(self.frame_1, text= "name", bg= '#dfe3ee', fg= '#107db2')
        self.lb_name.place(relx= 0.05, rely= 0.35)

        self.name_entry = Entry(self.frame_1, bg= '#dfe3ee', fg= '#107db2')
        self.name_entry.place(relx= 0.05, rely= 0.50, relwidth= 0.85)
        # entrada do telefone
        self.lb_phone = Label(self.frame_1, text= "phone", bg= '#dfe3ee', fg= '#107db2')
        self.lb_phone.place(relx= 0.05, rely= 0.7)

        self.phone_entry = Entry(self.frame_1, bg= '#dfe3ee', fg= '#107db2')
        self.phone_entry.place(relx= 0.05, rely= 0.8, relwidth= 0.3)
        # entrada de cidade
        self.lb_city = Label(self.frame_1, text= "city", bg= '#dfe3ee', fg= '#107db2')
        self.lb_city.place(relx= 0.5, rely= 0.7)

        self.city_entry = Entry(self.frame_1, bg= '#dfe3ee', fg= '#107db2')
        self.city_entry.place(relx= 0.5, rely= 0.8, relwidth= 0.4)




Aplicattion()
