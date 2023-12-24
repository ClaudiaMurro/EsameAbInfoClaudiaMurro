#importo moduli
import numpy as np
import matplotlib.pyplot as mpl
import statistics as stat

#----------------------------------------------------estrazione dati

	#data_filename = "/home/s258303@DS.UNITS.IT/Desktop/lez10/datidiagramma.dat"
	#data_filename = "/home/claudia/Scrivania/AbInfo/esame/datidiagramma.dat"

#assegnazione del path del file
path=input('Inserire il path che leggi nella riga precedente: ')
data_filename = str(path)

#apro il file e leggo i dati
data = np.loadtxt(data_filename, delimiter=' ',unpack=True)
M_ass=data[4]
b_y=data[8]
age_parent=data[12]
MsuH=data[0]
m_ini=data[1]

#----------------------------------------------------------------diagramma H-R
#creazione diagramma H-R dividendo le stelle in base all'età
mpl.figure(figsize=(10, 7))
for i in np.arange(0,13,0.65):
		indici = np.where((age_parent<=i+0.65) & (age_parent>i))[0]
		etich = str(i)+'Gyr-'+str(0.65+i)+'Gyr'
		mpl.scatter(b_y[indici], M_ass[indici], marker='.', edgecolors='black', s=40, label=etich)

#configurazione grafico
mpl.xlim(-0.1,1)
mpl.ylim(9,-4)

mpl.xlabel('Colore')
mpl.ylabel('Magnitudine')
mpl.legend()
mpl.title('Diagramma H-R')

mpl.savefig('diagHR.png')
mpl.show()

#---------------------------------------------------------------istogramma metallicità 1 
#questa parte di esercizio non è svolta con un ciclo for per poter impostare per ogni popolazione stellare il numero di bin ottimale e le caratteristiche di ogni grafico in maniera indipendente

mpl.figure(figsize=(10, 7))

#divisione delle stelle in 3 popolazioni in base all'età
pop1 = np.where(age_parent<=1)[0]
pop2 = np.where((age_parent<=5) & (age_parent>1))[0]
pop3 = np.where(age_parent>5)[0]

#etichette per le tre popolazioni stellati
etich1 = 'pop1: <'+str(1)+'Gyr'
etich2 = 'pop2: '+str(1)+'Gyr-'+str(5)+'Gyr'
etich3 = 'pop3: >'+str(5)+'Gyr'

#istogramma della metallicità delle popolazioni stellari
hist1, bin_edges1 = np.histogram(MsuH[pop1], bins = 9)
hist2, bin_edges2 = np.histogram(MsuH[pop2], bins = 19)
hist3, bin_edges3 = np.histogram(MsuH[pop3], bins = 7)

#il valore del bin viene centrato
bin_centers1=(bin_edges1[:-1]+bin_edges1[1:])
bin_centers2=(bin_edges2[:-1]+bin_edges2[1:])
bin_centers3=(bin_edges3[:-1]+bin_edges3[1:])

#creazione istogramma con barre piene
mpl.bar(bin_centers1, hist1,color='magenta',label=etich1, alpha=0.4)
mpl.bar(bin_centers2, hist2,color='green',label=etich2, alpha=0.3)
mpl.bar(bin_centers3, hist3,color='red',label=etich3, alpha=0.4)

#configurazione grafico
mpl.autoscale()
mpl.xlabel('Metallicità')
mpl.ylabel('Numero di stelle')
mpl.legend()
mpl.title('Popolazioni stellari')

mpl.savefig('pop_distrib1.png')
mpl.show()

#----------------------------------------------------------------------------------istogramma metallicità 2 + statistica
#creazione istogramma con barre vuote
mpl.plot(bin_centers1, hist1, drawstyle = 'steps-mid', marker='',color='blue',linewidth=2,label=etich1, alpha=0.6)
mpl.plot(bin_centers2, hist2, drawstyle = 'steps-mid', marker='',color='green',linewidth=2,label=etich2, alpha=0.6)
mpl.plot(bin_centers3, hist3, drawstyle = 'steps-mid', marker='',color='red',linewidth=2,label=etich3, alpha=0.6)

#media e mediana per ogni popolazione stellare, graficate con linea continua
	#pop1
mpl.plot([stat.median(MsuH[pop1]),stat.median(MsuH[pop1])],[0,np.max(hist1)],color='darkblue',linewidth=2, linestyle = 'solid',label='pop1 mediana')
mpl.plot([stat.mean(MsuH[pop1]),stat.mean(MsuH[pop1])],[0,np.max(hist1)],color='cyan',linewidth=2, linestyle = 'solid',label='pop1 media')

	#pop2
mpl.plot([stat.median(MsuH[pop2]),stat.median(MsuH[pop2])],[0,np.max(hist2)],color='darkgreen',linewidth=2, linestyle = 'solid',label='pop2 mediana')
mpl.plot([stat.mean(MsuH[pop2]),stat.mean(MsuH[pop2])],[0,np.max(hist2)],color='lime',linewidth=2, linestyle = 'solid',label='pop2 media')

	#pop3
mpl.plot([stat.median(MsuH[pop3]),stat.median(MsuH[pop3])],[0,np.max(hist3)],color='darkred',linewidth=2, linestyle = 'solid',label='pop3 mediana')
mpl.plot([stat.mean(MsuH[pop3]),stat.mean(MsuH[pop3])],[0,np.max(hist3)],color='orangered',linewidth=2, linestyle = 'solid',label='pop3 media')

#configurazione grafico
mpl.autoscale()
mpl.xlabel('Metallicità')
mpl.ylabel('Numero di stelle')
mpl.legend()
mpl.title('Popolazioni stellari')

mpl.savefig('pop_distrib2.png')
mpl.show()

#valori di media e mediana per ogni popolazione
print('POP1 median metallicity:{}, mean metallicity:{}'.format( stat.median(MsuH[pop1]), stat.mean(MsuH[pop1]) ) )
print('POP2 median metallicity:{}, mean metallicity:{}'.format( stat.median(MsuH[pop2]), stat.mean(MsuH[pop2]) ) )
print('POP3 median metallicity:{}, mean metallicity:{}'.format( stat.median(MsuH[pop3]), stat.mean(MsuH[pop3]) ) )

#--------------------------------------------------------------------------------------------------------metallicità vs massa
#grafico metallicità in funzione della massa per ogni popolazione stellare
mpl.figure(figsize=(10, 7))
	#con 'alpha' viene impostata trasparenza per rendere il grafico leggibile
mpl.scatter(m_ini[pop1], MsuH[pop1], color = 'blue',marker = '.', s = 50, label=etich1, alpha=0.6) 
mpl.scatter(m_ini[pop2], MsuH[pop2], color = 'green', marker = '.', s = 50, label=etich2, alpha=0.4)
mpl.scatter(m_ini[pop3], MsuH[pop3], color = 'red', marker = '.', s = 50, label=etich3, alpha=0.5)

#configurazione grafico
mpl.xlim(0.5,7)
mpl.ylim(0.65,-2)
mpl.autoscale()
mpl.xlabel('Massa')
mpl.ylabel('Metallicità')
mpl.legend()
mpl.title('Popolazioni stellari')

mpl.savefig('metallicity_mass.png')
mpl.show()

#---------------------------------------------------------------------------------------------ottimizzazione visualizzazione
#la visualizzazione del grafico precedente viene ottimizzata spacchettandolo in 3 subplots, graficati vicini per rendere facile il confronto tra loro e il grafico complessivo

fig, (ax1, ax2, ax3) = mpl.subplots(3, 1, figsize=(10, 9))
fig.suptitle('Metallicità vs Massa')

#configurazione grafico pop1
ax1.scatter(m_ini[pop1], MsuH[pop1],color = 'blue',marker = '.', s = 10,label=etich1, alpha=0.6)
ax1.set_ylabel('pop1')
ax1.set(xlim=(0.5,7), ylim=(0.65,-2))

#configurazione grafico pop2
ax2.scatter(m_ini[pop2], MsuH[pop2],color = 'green',marker = '.', s = 10,label=etich2, alpha=0.4)
ax2.set(xlim=(0.5,7), ylim=(0.65,-2))
ax2.set_ylabel('pop2')

#configurazione grafico pop3
ax3.scatter(m_ini[pop3], MsuH[pop3],color = 'red',marker = '.', s = 10,label=etich3, alpha=0.5)
ax3.set(xlim=(0.5,7), ylim=(0.65,-2))
ax3.set_ylabel('pop3')
mpl.savefig('pop_metallicity_mass.png')
mpl.show()


#link dei dati
#https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat

