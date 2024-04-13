from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from sympy import *
from math import *
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.audio import SoundLoader 
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty 
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.base import runTouchApp
x=symbols('x')
class S(ScreenManager):
	pass
class C(Screen):
	def l(self):
		n=int(eval(self.ids.ok.text))
		for i in range(1,n):
			if n%i==0:
				j=str(i)
				self.ids.ok.text=j
				self.ids.ok.text= f'{i}'		
			else:
				pass
	def m(self):
		k=int(eval(self.ids.ko.text))
		w=int(eval(self.ids.koo.text))
		for i in range(1,k+1):
			for j in range(1,w+1):
				if k%i==0 and w%j==0:					
					if i==j:
						self.ids.h.text=str(j)
					else:
						pass
				else:
					pass			
	pass

runTouchApp(Builder.load_string('''
S:
	C:
<C>:
	name:"^^"
	BoxLayout:
		orientation:'vertical'
		TextInput:
			text:"écris le chiffre "
		    id:ok
		Button:
			text:"click pour trouver le grand diviseur "
			on_press:
				root.l()
		GridLayout:
			cols:2
			spacing:10
			TextInput:
				text:"le premier"
				id:ko
			TextInput:
				text:"le deuxième"
				id:koo
		TextInput:
			text:"le nombre est:  "
			id:h
		Button:
			text:"clique pour trouver le grand diviseur commun "
			on_press:
				root.m()
		Button:
			on_press:
				root.v()
'''))