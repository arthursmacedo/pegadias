"""
Created on Thu Oct 29 13:18:56 2020

@author: Arthur
"""

def lista_dias_req(arquivo):
    with open(arquivo, 'r') as arq:
        dado = arq.readlines()
        dias_lista = list()
        for i in range(1, len(dado)):
            lista = dado[i].split(',')
            data = lista[0]
            data = data.split()
            data = data[0].split('/') 
            dia = data[0]
            mes = data[1]
            ano = data[2]
            
            #if int(ano) > 50:
                #ano = '19' + ano
            #else:
                #ano = '20' + ano
    
            dado_saida = ano + '/' + str(mes).zfill(2) + '/' + str(dia).zfill(2)
        
            dias_lista.append(dado_saida)
        return dias_lista


def req(lista_dias, estacao):
    with open('run_nmsclient.sh', 'a') as run:
      
        for i in range(len(lista_dias)):
            data_req = lista_dias[i].split('/')
           
            fil = estacao.upper() +'_' + data_req[0] + '_' + data_req[1] + '_'  + data_req[2] +'.req'
            
            with open(fil, 'w') as req:    
                req.write('begin ims2.0'+ '\n') 
                req.write('msg_type request'+ '\n')
                req.write('msg_id mseed_'+ estacao.lower() + '\n')
                req.write('time ' + lista_dias[i] + ' 00:00:00 to ' + lista_dias[i] + ' 23:59:59' + '\n')
                req.write('sta_list '+ estacao.upper() + '\n')
                req.write('chan_list BDF'+ '\n')
                req.write('waveform ims2.0:ms_st2_512'+ '\n')
                req.write('stop')
            
            run.write('nms_client.sh '+ estacao.upper() + '_' + data_req[0] + '_' + data_req[1] + '_'  + data_req[2] +'.req' + ' -f ' + estacao.upper() +'_' + data_req[0] + '_' + data_req[1] + '_'  + data_req[2] +'.mseed\n')


lista_req = lista_dias_req('viena.csv')
print(lista_req)

with open('run_nmsclient.sh', 'w') as run:
    run.write('#!/bin/bash \n\n')
    
req(lista_req, 'i01ar')
req(lista_req, 'i11cv')
req(lista_req, 'i42pt')
req(lista_req, 'i37no')
req(lista_req, 'i56us')
