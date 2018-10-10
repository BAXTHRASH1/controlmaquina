from django.shortcuts import render
import socket 
from django.http import HttpResponseRedirect,HttpResponse
from controlapp import models
import json


def index(request):
	return render(request ,'base.html')
def Admin(request):
	return render(request ,'admin.html')
	
def estado(request):
	if request.method == 'POST':
		if request.is_ajax():
			keyMaquina = request.POST['keyUsuario']
			key = models.Maquina.objects.get(key_maquina=keyMaquina)
			modeloMaquina = str(key.modelo_maquina)
			ip_maquina= str(key.ip_maquina)
			SERVER = ip_maquina
			PORT = 7000
			estadoNavegador=''
			try:
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.connect((SERVER, PORT))
				print('se conecto a la maquina preguntando por la key')
			except Exception as e:
				modeloMaquina='error'
			try:
				client.sendall(bytes('4.5','UTF-8'))
				estadoPanel = client.recv(1024)
				estadoPanel = estadoPanel.decode()
				client.close()
			except Exception as e:
				estadoPanel='error'
			try:
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.connect((SERVER, PORT))
				client.sendall(bytes('4.6','UTF-8'))
				estadoNavegador = client.recv(1024)
				estadoNavegador = estadoNavegador.decode()
				client.close()
			except Exception as e:
				estadoNavegador= 'error'
			try:
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.connect((SERVER, PORT))
				client.sendall(bytes('4.7','UTF-8'))
				estadoNucleo = client.recv(1024)
				estadoNucleo = estadoNucleo.decode()
				client.close()
			except Exception as e:
				estadoNucleo='error'

	print('respuesta panel : '+estadoPanel)
	print('respuesta navegador :'+estadoNavegador)
	mydata=[{'modeloMaquina':modeloMaquina,'estadoPanel':str(estadoPanel),'estadoNavegador':str(estadoNavegador),'estadoNucleo':estadoNucleo}]
	return HttpResponse(json.dumps(mydata))

def buscarsocket(request):
	msg=''
	if request.method == 'POST':
		if request.is_ajax():
			keyMaquina = request.POST['keyBusqueda']
			key = models.Maquina.objects.get(key_maquina=keyMaquina)
			ip_maquina = str(key.ip_maquina)
			SERVER = ip_maquina
			PORT = 7000
			try:
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.connect((SERVER, PORT))
				comando = request.POST['comandoSocket']
				client.sendall(bytes(str(comando),'UTF-8'))
				msg = client.recv(1024)
				print(msg.decode())
				mensajeSocket=msg.decode()
				client.close()
			except Exception as e:
				mensajeSocket='error'
	mydata=[{'mensajeSocket':mensajeSocket}]
	return HttpResponse(json.dumps(mydata))
