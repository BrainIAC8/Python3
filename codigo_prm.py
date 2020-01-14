from tkinter import *
import os
from PIL import ImageTk, Image


def gerar_prm():
    nome_arquivo = v_nome_mapa.get() + '.prm'
    arquivo_saida = open(nome_arquivo, 'w')

    arquivo_saida.write(f'[EXT-SAUDE-' + v_num_etl.get() + '-EE.WF:wkf_' + v_num_job.get() + '_' + v_num_etl.get() + '_extrai_' + v_nome_mapa.get() + ']\n\n')
    arquivo_saida.write(f'$PMWorkflowLogDir=/powercenter/P001/EXT/EE/' + v_PMWorkflowLogDir.get() + '\n')
    arquivo_saida.write(f'$PMSessionLogDir=/powercenter/P001/EXT/EE/SESSLOGS/' + v_PMSessionLogDir.get() + '\n')
    arquivo_saida.write(f'$PMBadFileDir=/powercenter/P001/EXT/EE/BADFILES/' + v_PMBadFileDir.get() + '\n')
    arquivo_saida.write(f'$PMCacheDir=/powercenter/P001/EXT/EE/CACHE/' + v_PMCacheDir.get() + '\n')
    arquivo_saida.write(f'$PMTempDir=/powercenter/P001/EXT/EE/TEMP/' + v_PMTempDir.get() + '\n')
    arquivo_saida.write(f'$PMTargetFileDir=/powercenter/P001/EXT/EE/ENTRADA/PROCESSADO/' + v_PMTargetFileDir.get() + '\n')
    arquivo_saida.write(f'$PMSourceFileDir=/powercenter/P001/EXT/EE/ENTRADA/PROCESSAR/' + v_PMSourceFileDir.get() + '\n\n')

    arquivo_saida.write(f'[EXT-SAUDE-' + v_num_etl.get() + '-EE.WF:s_m_' + v_num_job.get() + '_' + v_num_etl.get() + '_extrai_' + v_nome_mapa.get() + ']\n\n')
    arquivo_saida.write(f'$PMSessionLogFile=' + v_num_job.get() + '_' + v_data.get() + '.log\n')
    arquivo_saida.write(f'OutputFilename=FF_' + v_num_job.get() + '_' + v_data.get() + '.dat\n')
    arquivo_saida.write(f'BadFilename='+ v_num_job.get() + '_' + v_data.get() + '.log\n')

    arquivo_saida.close()


root = Tk()
root.title('GERADOR DE ARQUIVO PRM')

window_width = 350
window_height = 620
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordenada = int((screen_width / 2) - (window_width / 2))
y_coordenada = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordenada, y_coordenada))

titulo_nome_mapa = Label(text='Digite o nome do mapa: ').pack()
v_nome_mapa = StringVar()
c_nome_mapa = Entry(root, width=45, textvariable=v_nome_mapa).pack()
nome_mapa = v_nome_mapa.get()

titulo_num_job = Label(text='Digite o número do JOB: ').pack()
v_num_job = StringVar()
c_num_job = Entry(root, width=45, textvariable=v_num_job).pack()
num_job = v_num_job.get()

titulo_num_etl = Label(text='Digite o ETL: ').pack()
v_num_etl = StringVar()
c_num_etl = Entry(root, width=45, textvariable=v_num_etl).pack()
num_etl = v_num_etl.get()

titulo_PMWorkflowLogDir = Label(text='Digite a pasta PMWorkflowLogDir: ').pack()
v_PMWorkflowLogDir = StringVar()
c_PMWorkflowLogDir = Entry(root, width=45, textvariable=v_PMWorkflowLogDir).pack()
PMWorkflowLogDir = v_PMWorkflowLogDir.get()

titulo_PMSessionLogDir = Label(text='Digite a pasta PMSessionLogDir: ').pack()
v_PMSessionLogDir = StringVar()
c_PMSessionLogDir = Entry(root, width=45, textvariable=v_PMSessionLogDir).pack()
PMSessionLogDir = v_PMSessionLogDir.get()

titulo_PMBadFileDir = Label(text='Digite a pasta PMBadFileDir: ').pack()
v_PMBadFileDir = StringVar()
c_PMBadFileDir = Entry(root, width=45, textvariable=v_PMBadFileDir).pack()
PMBadFileDir = v_PMBadFileDir.get()

titulo_PMCacheDir = Label(text='Digite a pasta PMCacheDir: ').pack()
v_PMCacheDir = StringVar()
c_PMCacheDir = Entry(root, width=45, textvariable=v_PMCacheDir).pack()
PMCacheDir = v_PMCacheDir.get()

titulo_PMTempDir = Label(text='Digite a pasta PMTempDir: ').pack()
v_PMTempDir = StringVar()
c_PMTempDir = Entry(root, width=45, textvariable=v_PMTempDir).pack()
PMTempDir = v_PMTempDir.get()

titulo_PMTargetFileDir = Label(text='Digite a pasta PMTargetFileDir: ').pack()
v_PMTargetFileDir = StringVar()
c_PMTargetFileDir = Entry(root, width=45, textvariable=v_PMTargetFileDir).pack()
PMTargetFileDir = v_PMTargetFileDir.get()

titulo_PMSourceFileDir = Label(text='Digite a pasta PMSourceFileDir: ').pack()
v_PMSourceFileDir = StringVar()
c_PMSourceFileDir = Entry(root, width=45, textvariable=v_PMSourceFileDir).pack()
PMSourceFileDir = v_PMSourceFileDir.get()

session_label = Label(text='').pack()
session_label2 = Label(text='-------SESSION-------').pack()
session_label3 = Label(text='').pack()

titulo_data = Label(text='Digite a data: ').pack()
v_data = StringVar()
c_data = Entry(root, width=45, textvariable=v_data).pack()
data = v_data.get()

button = Button(root,
                text="GERAR",
                font=('Tohama', 10, 'bold'),
                command=gerar_prm).pack()

root.mainloop()
