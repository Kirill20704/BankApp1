# Банкомат
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scatter import Scatter
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'resizable', False)

# макеты кнопок управления
class Img1Button(ButtonBehavior, Image):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.source = 'spy.png'
      self.size_hint = [.064, .047]

class ImgLngButton(ButtonBehavior, Image):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.source = 'spy_long.png'
      self.size_hint = [.135, .045]

class ImgSqButton(ButtonBehavior, Image):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.source = 'spy1_1.png'
      self.size_hint = [.025, .025]
# основная часть
class BankApp(App):
   def build(self):
      self.cnt = 0
      self.step = 0
      self.true_pin = '0000'
      self.pin = ''
      self.balance = 100000
      self.cur = 'USD'

      self.root = ScreenManager()
      # экран заявки на выпуск карты
      sc1 = Screen(name='Sc1')
      bxl = BoxLayout(orientation='vertical')
      mainl = FloatLayout()
      site = BoxLayout()
      img1 = Image(source='site.jpg')
      site.add_widget(img1)
      lb1 = Label(text='Заявка на карту',  color=[0, 0, 0, 1], pos=(0, 260), font_size=30)
      self.sp1 = Spinner(text='платёжная система', values=('VISA', 'MasterCard'), size_hint=(.25, .2), pos=(5, 420))
      self.sp2 = Spinner(text='валюта', values=('RUB', 'USD', 'EUR'), size_hint=(.1, .2), pos=(250, 420))
      lb2 = Label(text='Ваш PIN: 0000\nизменить PIN можно в банкомате',  color=[0, 0, 0, 1], pos=(140, 320), font_size=20)
      lb3 = Label(text='Пополнить с текущего счёта:',  color=[0, 0, 0, 1], pos=(0, -40), font_size=20)
      self.sld = Slider(min=0, max=100000, value_track=True, value_track_color=[0, 1, 0, 1], value_normalized=.25, sensitivity='handle', on_touch_move=self.get_balance)
      self.lb4 = Label(text=str(self.sld.value), color=[0, 1, 0, 1], pos=(0, -110), font_size=20, bold=True)

      bxres = BoxLayout(orientation='vertical')
      bxsp = BoxLayout()
      splt = FloatLayout()
      splt.add_widget(self.sp1)
      splt.add_widget(self.sp2)
      splt.add_widget(lb2)
      bxsp.add_widget(splt)
      bxres.add_widget(bxsp)
      bxres.add_widget(self.sld)
      bn = Button(text='оформить заявку', size_hint=(1, .4), on_press=self.switch_sc1)
      bxres.add_widget(bn)
      bxl.add_widget(site)
      flres = FloatLayout(size_hint=(1., .2))
      flres.add_widget(Image(source='spy_long.png'))
      bxl.add_widget(flres)
      mainl.add_widget(bxl)
      mainl.add_widget(lb1)
      mainl.add_widget(lb3)
      mainl.add_widget(self.lb4)
      mainl.add_widget(bxres)
      sc1.add_widget(mainl)
      # промежуточный экран
      sc2 = Screen(name='Sc2')
      sc2.add_widget(Button(halign='center', text='ЗАЯВКА ОДОБРЕНА\n\nнажмите, чтобы продолжить', on_press=self.switch_sc2, font_size=40, bold=True))
      # основной экран: банкомат
      sc3 = Screen(name='Sc3')
      self.lbl = Label(halign='center', text='ПОДНЕСИТЕ\nКАРТУ', font_size=20, pos=(-40, -15), color=[0, 0, 0, 1])
      # создание кнопок управления по ранее созданным макетам
      imb1 = Img1Button(pos=(134, 106), on_press=self.onp1, on_release=self.onr1)
      imb2 = Img1Button(pos=(178, 106), on_press=self.onp2, on_release=self.onr2)
      imb3 = Img1Button(pos=(223, 106), on_press=self.onp3, on_release=self.onr3)
      imb4 = Img1Button(pos=(134, 82), on_press=self.onp4, on_release=self.onr4)
      imb5 = Img1Button(pos=(178, 82), on_press=self.onp5, on_release=self.onr5)
      imb6 = Img1Button(pos=(223, 82), on_press=self.onp6, on_release=self.onr6)
      imb7 = Img1Button(pos=(134, 58), on_press=self.onp7, on_release=self.onr7)
      imb8 = Img1Button(pos=(178, 58), on_press=self.onp8, on_release=self.onr8)
      imb9 = Img1Button(pos=(223, 58), on_press=self.onp9, on_release=self.onr9)
      imb_m = Img1Button(pos=(134, 33), on_release=self.onr_m)
      imb0 = Img1Button(pos=(178, 33), on_press=self.onp0, on_release=self.onr0)
      imb_p = Img1Button(pos=(223, 33), on_release=self.onr_p)

      imb_cn = ImgLngButton(pos=(285, 105), on_release=self.onr_cn)
      imb_cl = ImgLngButton(pos=(285, 82), on_release=self.onr_cl)
      imb_hp = ImgLngButton(pos=(285, 58), on_release=self.onr_hp)
      imb_ent = ImgLngButton(pos=(285, 33), on_release=self.onr_ent)

      imb_l1 = ImgSqButton(pos=(90, 297), on_release=self.onr_l1)
      imb_l2 = ImgSqButton(pos=(89, 273), on_release=self.onr_l2)
      imb_l3 = ImgSqButton(pos=(88, 250), on_release=self.onr_l3)
      imb_l4 = ImgSqButton(pos=(87, 226), on_release=self.onr_l4)
      imb_r1 = ImgSqButton(pos=(307, 296), on_release=self.onr_r1)
      imb_r2 = ImgSqButton(pos=(307, 272), on_release=self.onr_r2)
      imb_r3 = ImgSqButton(pos=(308, 249), on_release=self.onr_r3)
      imb_r4 = ImgSqButton(pos=(308, 225), on_release=self.onr_r4)

      self.lbl_l1 = Label(text='', pos=(-105, -25), halign='right')
      self.lbl_l2 = Label(text='', pos=(-90, -48), halign='right')
      self.lbl_l3 = Label(text='', pos=(-100, -73), halign='right')
      self.lbl_l4 = Label(text='', pos=(-80, -96), halign='right')
      self.lbl_r1 = Label(text='', pos=(30, -25), halign='left')
      self.lbl_r2 = Label(text='', pos=(35, -48), halign='left')
      self.lbl_r3 = Label(text='', pos=(8, -73), halign='left')
      self.lbl_r4 = Label(text='', pos=(-7, -96), halign='left')

      bank = Image(source='bank1.png')

      self.flb = FloatLayout()
      self.flb.add_widget(bank)
      # добавление виджетов
      for i in [self.lbl_l1, self.lbl_l2, self.lbl_l3, self.lbl_l4, self.lbl_r1, self.lbl_r2, self.lbl_r3, self.lbl_r4]:
         self.flb.add_widget(i)
      for i in [imb1, imb2, imb3, imb4, imb5, imb6, imb7, imb8, imb9, imb0, imb_m, imb_p]:
         self.flb.add_widget(i)
      for i in [imb_cn, imb_cl, imb_hp, imb_ent]:
         self.flb.add_widget(i)

      for i in [imb_l1, imb_l2, imb_l3, imb_l4, imb_r1, imb_r2, imb_r3, imb_r4]:
         self.flb.add_widget(i)

      self.flb.add_widget(self.lbl)

      self.bx = BoxLayout(pos=(400, -15), size_hint=(.17, .17))
      self.bx.add_widget(Image(source='wallet.png'))
      self.flb.add_widget(self.bx)

      self.s1 = Scatter(scale_min=.75, scale_max=1.25, on_touch_move=self.sc_pos2, pos=(405, 0))

      sc3.add_widget(self.flb)

      self.root.add_widget(sc1)
      self.root.add_widget(sc2)
      self.root.add_widget(sc3)
      self.root.current = 'Sc1'

      return self.root

   def get_balance(self, *args):
      '''получение значения со шкалы баланса'''
      self.lb4.text = str(round(self.sld.value))

   def switch_sc1(self, *args):
      '''преключение на 2 экран'''
      if self.sp1.text != 'платёжная система' and self.sp1.text != 'валюта':
         self.root.current = 'Sc2'

   def switch_sc2(self, *args):
      '''преключение на 3 экран'''
      Window.size = (484, 659)
      self.s2 = Scatter(scale_min=.75, scale_max=1.25, on_touch_move=self.sc_pos, pos=(415, 0))
      self.fl2 = FloatLayout(size=(90, 90))
      self.imgv2 = Image(source='visa1.png')
      if self.sp1.text == 'MasterCard':
         self.imgv2 = Image(source='mastercard1.png')
         self.s2.pos = (405, 10)
      self.fl2.add_widget(self.imgv2)
      self.s2.add_widget(self.fl2)
      self.flb.add_widget(self.s2)
      self.cur = self.sp2.text
      self.balance = round(self.sld.value)
      self.root.current = 'Sc3'

   def sc_pos(self, instance, *args):
      '''взаимодействие с картой, включая изменение масштаба при отдалении (стр.184)'''
      # self.lbl.text = str(instance.pos)
      self.fl2.size = (90-round(instance.pos[1]*60/659), 90-round(instance.pos[1]*60/659))
      if self.step == 0:
         if 375 < instance.pos[0] < 385 and 185 < instance.pos[1] < 210:
            self.step = 1
            instance.do_translation = False
            try:
               self.flb.remove_widget(self.bx)
            except:
               pass
            self.lbl.text = 'ВВЕДИТЕ PIN\n'
            self.pin = ''
         if 375 < instance.pos[0] < 385 and 235 < instance.pos[1] < 250:
            self.step = 1
            instance.do_translation = False
            self.flb.remove_widget(self.s2)
            try:
               self.flb.remove_widget(self.bx)
            except:
               pass
            self.lbl.text = 'ВВЕДИТЕ PIN\n'
            self.pin = ''
      elif self.step == 0.1:
         try:
            self.flb.add_widget(self.bx)
         except:
            pass
         if 380 < instance.pos[0] and instance.pos[1] < 40:
            self.lbl.text = 'ПОДНЕСИТЕ\nКАРТУ'
            self.step = 0
            self.lbl_l1.text = ''
            self.lbl_l2.text = ''
            self.lbl_l3.text = ''
            self.lbl_l4.text = ''
            self.lbl_r1.text = ''
            self.lbl_r2.text = ''
            self.lbl_r3.text = ''
            self.lbl_r4.text = ''

   def sc_pos2(self, instance, *args):
      '''взаимодействие с деньгами'''
      if self.step == 3:
         if 270 < instance.pos[0] < 360 and 80 < instance.pos[1] < 120:
            self.flb.remove_widget(self.s1)
            try:
               self.flb.remove_widget(self.bx)
            except:
               pass
            c = 1000
            if self.cur == 'RUB':
               c = 10000
            self.balance += c
            self.lbl.text = 'успешно\n'
            self.pin = ''
      elif self.step > 4:
         if 380 < instance.pos[0] and instance.pos[1] < 40:
            self.step = 0.1
            self.flb.remove_widget(self.s1)
            self.lbl.text = 'успешно\nзаберите карту'
            try:
                self.flb.add_widget(self.s2)
            except:
                pass

   # назначение действий ввода цифр
   for j in range(10):
      exec("def onp"+str(j)+"(self, instance):\n\tif self.step == 1 or self.step == 1.1:\n\t\tfor i in range(5):\n\t\t\tif 'PIN' in self.lbl.text and len(self.pin) < 4:\n\t\t\t\tself.lbl.text += '"+str(j)+"'\n\t\t\t\tbreak\n\telif self.step > 3:\n\t\tself.lbl.text += '"+str(j)+"'\n\t\tself.pin += "+"'"+str(j)+"'")

   for j in range(10):
      exec("def onr"+str(j)+"(self, instance):\n\tif self.step == 1 or self.step == 1.1:\n\t\tfor i in range(5):\n\t\t\tif 'PIN' in self.lbl.text and len(self.pin) < 4:\n\t\t\t\tself.lbl.text = self.lbl.text[:-1]+'*'\n\t\t\t\tself.pin += "+"'"+str(j)+"'"+"\n\t\t\t\tbreak")
   # назначение остальных кнопок
   def onr_p(self, instance):
      if self.step > 3:
         if self.pin == '':
            self.pin = '0'
         self.pin = str(int(self.pin)+100)
         self.lbl.text = 'введите сумму\n'+self.pin

   def onr_m(self, instance):
      if self.step > 3:
         if self.pin == '':
            self.pin = '0'
         if int(self.pin) > 200:
            self.pin = str(int(self.pin)-100)
            self.lbl.text = 'введите сумму\n' + self.pin
         elif 100 < int(self.pin) <= 200:
            self.pin = '100'
            self.lbl.text = 'введите сумму\n' + self.pin

   def onr_cn(self, instance):
      if self.step == 1 or self.step == 1.1:
         self.pin = ''
         self.lbl.text = 'ВВЕДИТЕ PIN\n'

   def onr_cl(self, instance):
      if self.step == 1 or self.step > 4 or self.step == 1.1:
         if 0 < len(self.pin):
            self.pin = self.pin[:-1]
            self.lbl.text = self.lbl.text[:-1]

   def onr_hp(self, instance):
      if self.step == 1:
         self.lbl.text = 'если не работает\nввод, нажмите\ncancel'
      elif self.step == 2:
         self.lbl.text = 'выбирите пункт\nменю'

   def onr_ent(self, instance):
      '''действия при нажатии Enter'''
      if self.step == 1:
         if self.cnt > 3:
            self.lbl.text = 'карта\nзаблокирована'
            self.true_pin += 'b'
            self.finish()
         if self.pin == self.true_pin:
            self.step = 2
            self.lbl.text = ''
            self.pin = ''
            self.lbl_l1.text = 'внести'
            self.lbl_l2.text = 'сменить PIN'
            self.lbl_l3.text = 'перводы'
            self.lbl_l4.text = ''
            self.lbl_r1.text = 'баланс'
            self.lbl_r2.text = 'снять'
            self.lbl_r3.text = 'блокировать'
            self.lbl_r4.text = 'завершить сеанс'
         elif 'b' in self.true_pin:
            self.lbl.text = 'ваша карта\nзаблокирована'
            self.s2.do_translation = True
         else:
            self.lbl.text = 'НЕВЕРНЫЙ PIN\nВВЕДИТЕ PIN\n'
            self.pin = ''
            self.cnt += 1
            self.lbl_l4.text = 'вернуть карту'
      elif self.step == 4.1:
         self.lbl_l1.text = ''
         self.lbl_l2.text = ''
         self.lbl_l3.text = ''
         self.lbl_l4.text = ''
         self.lbl_r1.text = ''
         self.lbl_r2.text = ''
         self.lbl_r3.text = ''
         self.lbl_r4.text = ''
         if 0 < int(self.pin) and int(self.pin) % 100 != 0:
            a = str((int(self.pin)//100)*100)
            if int(a) < 100:
               a = '100'
            self.lbl.text = 'введите сумму\n' + a
            self.pin = a
         elif 0 < int(self.pin) <= self.balance:
            try:
               self.lbl.text = 'возьмите\nденьги'
               fl = FloatLayout(size=(120, 120))
               fl.add_widget(Image(source=str(str(self.cur)) + '.png'))
               self.s1.add_widget(fl)
               self.s1.pos = (280, 100)
               self.flb.add_widget(self.s1)
               try:
                  self.flb.add_widget(self.bx)
               except:
                  pass
               self.s2.do_translation = True
               self.balance -= int(self.pin)
               self.pin = ''
            except:
               pass
         else:
            self.lbl.text = 'недостаточно\nсредств\n'
            self.pin = ''
            self.lbl_r1.text = 'назад'
      elif self.step == 1.1:
         self.lbl.text = 'успешно\nзаберите\nкарту'
         self.true_pin = self.pin
         self.finish()
   # назначение кнопок покраям экрана
   def onr_l1(self, instance):
      if self.step == 2:
         self.step = 3
         self.lbl.text = 'положите\nбанкноты'
         fl = FloatLayout(size=(120, 120))
         fl.add_widget(Image(source=str(str(self.cur))+'.png'))
         self.s1.add_widget(fl)
         self.s1.pos = (405, 0)
         self.flb.add_widget(self.s1)
         self.lbl_l1.text = ''
         self.lbl_l2.text = ''
         self.lbl_l3.text = ''
         self.lbl_l4.text = ''
         self.lbl_r1.text = 'назад'
         self.lbl_r2.text = ''
         self.lbl_r3.text = ''
         self.lbl_r4.text = ''

   def onr_l2(self, instance):
      if self.step == 2:
         self.step = 1.1
         self.pin = ''
         self.lbl.text = 'новый PIN\n'
         self.lbl_l1.text = ''
         self.lbl_l2.text = ''
         self.lbl_l3.text = ''
         self.lbl_l4.text = ''
         self.lbl_r1.text = 'назад'
         self.lbl_r2.text = ''
         self.lbl_r3.text = ''
         self.lbl_r4.text = ''

   def onr_l3(self, instance):
      if self.step == 2:
         self.lbl.text = 'услуга\nвременно\nнедоступна'
         self.step = 2.1
         '''
         self.lbl_l1.text = '     рубли'
         self.lbl_l2.text = '   доллары'
         self.lbl_l3.text = 'евро'
         '''
         self.lbl_l1.text = ''
         self.lbl_l2.text = ''
         self.lbl_l3.text = ''
         self.lbl_l4.text = ''
         self.lbl_r1.text = 'назад'
         self.lbl_r2.text = ''
         self.lbl_r3.text = ''
         self.lbl_r4.text = ''

   def onr_l4(self, instance):
      if self.lbl_l4.text == 'вернуть карту':
         self.finish()

   def onr_r1(self, instance):
      if self.step == 2:
         self.step = 2.2
         self.lbl.text = 'ваш баланс:\n'+str(self.balance)+'\n'+str(self.cur)
         self.lbl_l1.text = ''
         self.lbl_l2.text = ''
         self.lbl_l3.text = ''
         self.lbl_l4.text = ''
         self.lbl_r1.text = 'назад'
         self.lbl_r2.text = ''
         self.lbl_r3.text = ''
         self.lbl_r4.text = ''
      elif self.step >= 3 or self.step == 1.1 or 2.1 <= self.step <= 2.2:
         self.step = 2
         self.pin = ''
         self.lbl.text = ''
         self.lbl_l1.text = 'внести'
         self.lbl_l2.text = 'сменить PIN'
         self.lbl_l3.text = 'перводы'
         self.lbl_l4.text = ''
         self.lbl_r1.text = 'баланс'
         self.lbl_r2.text = 'снять'
         self.lbl_r3.text = 'блокировать'
         self.lbl_r4.text = 'завершить сеанс'
         try:
            self.flb.remove_widget(self.s1)
         except:
            pass

   def onr_r2(self, instance):
      if self.step == 2:
         self.step = 4.1
         self.lbl.text = 'введите сумму\n'
         self.lbl_l1.text = ''
         self.lbl_l2.text = ''
         self.lbl_l3.text = ''
         self.lbl_l4.text = ''
         self.lbl_r1.text = 'назад'
         self.lbl_r2.text = ''
         self.lbl_r3.text = ''
         self.lbl_r4.text = ''

   def onr_r3(self, instance):
      if self.step == 2:
         self.step = 3.3
         self.lbl.text = 'заблокировать\nкарту?'
         self.lbl_l1.text = ''
         self.lbl_l2.text = ''
         self.lbl_l3.text = ''
         self.lbl_l4.text = ''
         self.lbl_r1.text = 'назад'
         self.lbl_r2.text = ''
         self.lbl_r3.text = 'блокировать'
         self.lbl_r4.text = ''
      elif self.step == 3.3:
         self.lbl.text = 'карта\nзаблокирована'
         self.true_pin += 'b'
         self.finish()

   def onr_r4(self, instance):
      if self.step == 2:
         self.finish()

   def finish(self):
      '''вспомогательная функция возврата карты'''
      self.step = 0.1
      self.pin = ''
      self.lbl.text = 'заберите карту'
      try:
         self.flb.add_widget(self.bx)
      except:
         pass
      try:
         self.flb.add_widget(self.s2)
      except:
         pass
      self.s2.do_translation = True
      self.lbl_l1.text = ''
      self.lbl_l2.text = ''
      self.lbl_l3.text = ''
      self.lbl_l4.text = ''
      self.lbl_r1.text = ''
      self.lbl_r2.text = ''
      self.lbl_r3.text = ''
      self.lbl_r4.text = ''

if __name__ == '__main__':
   BankApp().run()
