from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
# from kivy.lang.builder import Builder

class Gerenciador(ScreenManager):
	pass

class TrancarMatricula(Screen):
	pass

class AutenticacaoSeguranca(Screen):
	pass

class ConsultarMatricula(Screen):
	pass

class Historico(Screen):
	pass

class Horario(Screen):
	pass
	
class Notas(Screen):
	pass

class Faltas(Screen):
	pass

class Cadastro(Screen):
	def on_pre_enter(self):
		Window.bind(on_keyboard=self.tecla)

	def tecla(self, window, key, *args):
		if key == 27:
			App.get_running_app().root.current = 'menu'
		if key == 13:
			if (self.ids.cpf.text != '' or self.ids.email.text != '' or self.ids.senha.text != '') and (self.ids.senha.text == self.ids.confsenha.text):
				App.get_running_app().root.current = 'painel'
			else:
				print("Favor, preencha todas os campos")
		print(key) # para descobrir a tecla pressionada
		return True

	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.tecla)

class RecoverPass(Screen):
	def on_pre_enter(self):
		Window.bind(on_keyboard=self.voltar)

	def voltar(self, window, key, *args):
		if key == 27:
			App.get_running_app().root.current = 'menu'
		if key == 13:
			if self.ids.email.text != '':
				App.get_running_app().root.current = 'painel'
			else:
				print("Favor, preencha o campo de e-mail corretamente")
		print(key) # para descobrir a tecla pressionada
		return True

	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.voltar)

class Painel(Screen):
	def on_pre_enter(self):
		Window.bind(on_keyboard=self.voltar)

	def voltar(self, window, key, *args):
		if key == 27:
			App.get_running_app().root.current = 'menu'
		print(key) # para descobrir a tecla pressionada
		return True

	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.voltar)

class Menu(Screen):
	def on_pre_enter(self):
		Window.bind(on_keyboard=self.entrar)

	def entrar(self, window, key, *args):
		if key == 13:
			print (window)
			#if self.ids.email.text == 'admin' and self.ids.senha.text == 'admin':
			#	self.ids.email.text = self.ids.senha.text = ''
			App.get_running_app().root.current = 'painel'
		return True

	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.entrar)

class Tarefas(Screen):
	def __init__(self, tarefas=[], **kwargs):
		super().__init__(**kwargs)
		for tarefa in tarefas:
			self.ids.box.add_widget(Tarefa(text=tarefa))


	def on_pre_enter(self):
		Window.bind(on_keyboard=self.voltar)

	def voltar(self, window, key, *args):
		if key == 27:
			App.get_running_app().root.current = 'menu'
		return True

	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.voltar)


	def addWidget(self):
		texto = self.ids.texto.text
		self.ids.box.add_widget(Tarefa(text=texto))
		self.ids.texto.text = ''

class Tarefa(BoxLayout):
	def __init__(self, text='',**kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = text

class Test(App):
	def build(self):
		# Builder.load_string(open('test.kv', encoding="utf-8").read(), rulesonly=True)
		return Gerenciador()

Test().run()