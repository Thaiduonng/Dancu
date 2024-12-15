
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem
from kivymd.uix.screen import MDScreen
#from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.button import MDIconButton, MDTextButton
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
#from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from docutils.nodes import contact
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.app import MDApp


class LoginScreen(Screen):
    pass
class CreateAccScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class UploadScreen(Screen):
    pass
class HelpScreen(Screen):
    pass
class FindScreen(Screen):
    pass




class Quan_liApp(MDApp):
    dialog = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = None
        global contacts
        contacts = []
    def build(self):
        #Các màu chủ đề: ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’,
        # ‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’,
        # ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’,
        # ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray’
        self.theme_cls.primary_palette = "Teal"
        #self.theme_cls.theme_style = "Dark"
        global sc
        sc = ScreenManager()
        sc.add_widget(Builder.load_file('Login.kv'))
        sc.add_widget(Builder.load_file('Menu.kv'))
        sc.add_widget(Builder.load_file('Profile.kv'))
        sc.add_widget(Builder.load_file('Upload.kv'))
        sc.add_widget(Builder.load_file('Appinfor.kv'))
        sc.add_widget(Builder.load_file('main.kv'))
        sc.add_widget(Builder.load_file('update.kv'))
        sc.add_widget(Builder.load_file('add.kv'))
        sc.add_widget(Builder.load_file('CreateAcc.kv'))
        return sc

    def add_datatable(self):
        import sqlite3
        vt = sqlite3.connect('Dancuxa.db')
        im = vt.cursor()
        im.execute("select * from person")
        data=im.fetchall()
        self.data_tables = MDDataTable(
            size_hint=(0.8, 0.5),
            use_pagination=True,
            check=True,
            column_data=[
                ("Số thứ tự", dp(30)),
                ("Căn cước", dp(30)),
                ("Tên", dp(30)),
                ("Tuổi", dp(30)),
                ("Địa chỉ", dp(40)),
                ("Số điện thoại", dp(40)),
                ("mật khẩu", dp(40))
            ],
            row_data=[
                (
                i[:][0],
                i[:][1],
                i[:][2],
                i[:][3],
                i[:][4],
                i[:][5],
                i[:][6],

                )
                for i in data
            ],
        )
        self.data_tables.bind(on_check_press=self.on_check_press)
        sc.get_screen("page").ids.datatable.add_widget(self.data_tables)
    def on_start(self):
        self.add_datatable()

    def on_check_press(self, instance_stable, current_row):
        if current_row[0] not in contacts:
            contacts.append(current_row[0])
        else:
            contacts.remove(current_row[0])
        print(contacts)


    def delete(self):
        self.dialog = MDDialog(
            text = "Bạn xóa toàn bộ thông tin của tài khoản",
            buttons=[
                MDFlatButton(text = "đóng", on_release = self.close),
                MDRectangleFlatButton(text = "xóa", on_release = self.open)
            ],
        )
        self.dialog.open()
    def close(self,obj):
        self.dialog.dismiss()
    def open(self,obj):
        for i in contacts:
            if i:
                import sqlite3
                vt = sqlite3.connect("Dancuxa.db")
                im = vt.cursor()
                im.execute(f"delete from person where person_id = {i}")
                vt.commit()
                sc.get_screen("page").ids.datatable.remove_widget(self.data_tables)
                self.add_datatable()
        self.dialog.dismiss()
        contacts.clear()

    def updatenewpage(self):
        for i in contacts:
            if i:
                import sqlite3
                vt=sqlite3.connect("Dancuxa.db")
                im=vt.cursor()
                im.execute("select * from person where person_id=?",(i))
                data=im.fetchall()
                for j in data:
                    sc.get_screen("upd").ids.cccd.text=j[1]
                    sc.get_screen("upd").ids.name.text=j[2]
                    sc.get_screen("upd").ids.age.text=j[3]
                    sc.get_screen("upd").ids.city.text=j[4]
                    sc.get_screen("upd").ids.sdt.text=j[5]
                    sc.get_screen("upd").ids.mk.text=j[6]

        sc.current = "upd"
    def addnewpage(self):
        sc.current = "add"
    def back(self, instance):
        sc.current = "page"
    def update(self,cccd,username,age,city,sdt,mk):
        for i in contacts:
            if i:
                import sqlite3
                vt = sqlite3.connect("Dancuxa.db")
                im = vt.cursor()
                im.execute("update person set cccd=?, username=?, age=?, city=?, sdt=?, mk=? where person_id=?",(cccd,username,age,city,sdt,mk,i))
                vt.commit()
                sc.get_screen("page").ids.datatable.remove_widget(self.data_tables)
                self.add_datatable()
        contacts.clear()
        sc.current = "page"
    def add(self,cccd,username,age,city,sdt,mk):
        import sqlite3
        vt = sqlite3.connect("Dancuxa.db")
        im = vt.cursor()
        im.execute("insert into person(cccd,username,age,city,sdt,mk) VALUES(?,?,?,?,?,?)",(cccd,username,age,city,sdt,mk))
        vt.commit()
        sc.get_screen("page").ids.datatable.remove_widget(self.data_tables)
        self.add_datatable()
        contacts.clear()
        sc.current = "page"




    def logger(self):
        self.root.get_screen('man_hinh_dang_nhap').ids.quan_li.text = f"Chào {self.root.get_screen('man_hinh_dang_nhap').ids.user.text}"
    '''def clear(self):
        self.root.get_screen('man_hinh_dang_nhap').ids.quan_li.text = "QUẢN LÍ NHÂN KHẨU"
        self.root.get_screen('man_hinh_dang_nhap').ids.user.text = ""
        self.root.get_screen('man_hinh_dang_nhap').ids.password.text =""'''
    def showdata(self, instance):
        if self.root.get_screen('man_hinh_dang_nhap').ids.user.text == "" or self.root.get_screen('man_hinh_dang_nhap').ids.password.text == "":
            check_string = 'Vui lòng nhập tên tài khoản và mật khẩu'
        else:
            check_string = f"tên tài khoản: {self.root.get_screen('man_hinh_dang_nhap').ids.user.text} \nmật khẩu: {self.root.get_screen('man_hinh_dang_nhap').ids.password.text}"
        close_button = MDIconButton(icon='close', on_release=self.close_dialog)
        login_button = MDIconButton(icon='login', on_release= self.interface)
        self.dialog = MDDialog(
            title='Kiểm tra thông tin',
            text = check_string,

            buttons=[close_button, login_button]
        )
        self.dialog.open()

    def close_dialog(self, instance):
        # Đảm bảo nhận tham số instance
        self.dialog.dismiss()
    def interface(self, instance):
        self.dialog.dismiss()
        self.root.get_screen('man_hinh_dang_nhap').manager.current = 'giao_dien_chinh'


if __name__ == '__main__':
    Quan_liApp().run()
