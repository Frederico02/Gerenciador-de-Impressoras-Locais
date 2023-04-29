from tkinter import Canvas
from tkinter import messagebox
import tkinter as tk
import subprocess
import psutil
import socket


def get_ip_address():
    ip_local = socket.gethostbyname(socket.gethostname())
    return ip_local

def get_mac_address():
    # Obtém o endereço MAC do adaptador de rede principal
    mac_address = ''
    for iface in psutil.net_if_addrs().values():
        for addr in iface:
            if addr.family == psutil.AF_LINK:
                mac_address = addr.address
                break
        if mac_address:
            break
    return mac_address

def get_hostname():
    # Obtém o nome do host do computador
    return socket.gethostname()

def reiniciar_spool():
    para_sap()
    messagebox.showinfo("status", "Reiniciando fila de impressão")
    subprocess.run(["net", "stop", "spooler"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.run(["net", "start", "spooler"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    volta_sap()
    messagebox.showinfo("status", "Fila de impressão Reiniciada!")

def para_sap():
    subprocess.run(["net", "stop", "SAPSprint"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

def volta_sap():
    subprocess.run(["net", "start", "SAPSprint"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

def reinicia_sap():
    messagebox.showinfo("status", "Reiniciando SAPSprint")
    subprocess.run(["net", "stop", "SAPSprint"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.run(["net", "start", "SAPSprint"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    messagebox.showinfo("status", "SAPSprint Reinciado")

def limpar_spool():
    para_sap()
    messagebox.showinfo("status", "Limpando fila de impressão")
    subprocess.run(["cmd", "/c", "net stop spooler && del /F /Q %systemroot%\\System32\\spool\\PRINTERS\\* && net start spooler"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    messagebox.showinfo("status", "Fila de impressão LIMPA!")
    volta_sap()

def geral():
    subprocess.run(["net", "stop", "SAPSprint"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    messagebox.showinfo("status", "Parando SAPSprint")
    subprocess.run(["cmd", "/c", "net stop spooler && del /F /Q %systemroot%\\System32\\spool\\PRINTERS\\* && net start spooler"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    messagebox.showinfo("status", "Limpando fila de impressão")
    messagebox.showinfo("status", "Reinciando fila de impressão")
    subprocess.run(["net", "start", "SAPSprint"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    messagebox.showinfo("status", "Iniciando SAPSprint")

def encerrar():
    janela.destroy()

def atualizar_info():
    messagebox.showinfo("status", "IPV4 Atualizado!" )
    ipv4 = get_ip_address()
    mac = get_mac_address()
    hostname = get_hostname()
    label_ip.config(text="IP: {}".format(ipv4))
    label_mac.config(text="MAC: {}".format(mac))
    label_hostname.config(text="Hostname: {}".format(hostname))


# Cria uma janela
janela = tk.Tk()
janela.geometry("250x450")  # aumenta a altura da janela para 400 pixels
janela.title("Destrava de Impressoras")

ipv4 = get_ip_address()
mac = get_mac_address()
hostname = get_hostname()

frame_botoes = tk.Frame(janela)
frame_botoes.pack()

botao_reiniciar_spool = tk.Button(frame_botoes, text="Reiniciar Spooler", command=reiniciar_spool)
botao_reiniciar_spool.pack(pady=5, padx=10, fill=tk.X)

botao_reinicia_sap = tk.Button(frame_botoes, text="Reiniciar SAPSprint", command=reinicia_sap)
botao_reinicia_sap.pack(pady=5, padx=10, fill=tk.X)

botao_limpar_spool = tk.Button(frame_botoes, text="Limpar Fila", command= limpar_spool)
botao_limpar_spool.pack(pady=5, padx=10, fill=tk.X)

botao_geral = tk.Button(frame_botoes, text="Execultar Todas opçoes", command= geral)
botao_geral.pack(pady=5, padx=10, fill=tk.X)

botao_sair = tk.Button(janela, text="Encerrar programa", command=janela.quit)
botao_sair.pack(side=tk.BOTTOM, pady=5)

label_ip = tk.Label(janela, text="IP: {}".format(ipv4))
label_ip.pack(pady=5)

label_mac = tk.Label(janela, text="MAC: {}".format(mac))
label_mac.pack(pady=5)

label_hostname = tk.Label(janela, text="Hostname: {}".format(hostname))
label_hostname.pack(pady=5)

botao_atualizar = tk.Button(janela, text="Atualizar IP", command=atualizar_info)
botao_atualizar.pack(pady=5)

canvas = tk.Canvas(janela, width=200, height=100)
canvas.pack(pady=5)

copyright = canvas.create_text(100, 90, text="© DEV Frederico- MULTITECH 2023")

janela.mainloop()
