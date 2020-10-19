import xlrd
import numpy as np
import gnu

def LoadExcel(fname):
	wb = xlrd.open_workbook(fname)
	sheet = wb.sheet_by_name('Export')
	start = 0
	end = 0
	for i in range(sheet.nrows):
		row = sheet.row(i)
		if 'Begin Data' == row[0].value:
			start = i + 1
			break
	for i in range(sheet.nrows):
		row = sheet.row(i)
		if 'End Data' == row[0].value:
			end = i
			break
			
	ldata = []

	for i in range(1651, 1651+1600):	
		row = sheet.row(i)
		t = []
		for j in (0,5,8,9,20,21):
			t.append(row[j].value)		#lista list. Najpierw tworzy liste, ktora potem
		ldata.append(t)					#przekazuje do kolejnej listy, sprytne.
	return ldata
	
	
def Ldata2Array(ldata):
	N = len(ldata)
	intens = np.zeros((N,2))		#stworzenie pustych macierzy
	backg = np.zeros((N,2))
	for i in range(N):				#wypelnienie macierzy
		intens[i,0] = ldata[i][2]	#zastap 1 kolumne wierszami z ldata ch1 intensity
		intens[i,1] = ldata[i][4]	#zastap 2 kolumne wierszami z ldata ch2 intensity
		backg[i,0] = ldata[i][3]	#zastap 1 kolumne wierszami z ldata ch1 backg
		backg[i,1] = ldata[i][5]	#zasatp 1 kolumne wierszami z ldata ch2 backg
	
	return intens, backg
	
def MA(intens, backg):
	vals = intens - backg
	mask = vals > 0					#usuniecie wartosci mniejszych od zera -> True (1) of False (0) (podstawienie za mask 1 da nam nasza liczbe, podstawienie 0 da nam zawsze 1)
	vals = mask*vals + (1-mask)*1	#i wstawienie (przez te zajebiste dzialanie) w miejsce mniejszych od zera 1 (z ktorej log2 wynosi 0)
	rg = vals[:,0] / vals[:,1]		#Ratio R/G ... dzielimy kolumnami odczyt 1 (red) przez 2 (green) (celem przedstawienia wynikow w ladniejszy sposob)
	inte = (vals[:,0] + vals[:,1]) / 2	#Average I ... kolejne przekszatalcenia dla kolejnego przedstawienia
	M = np.log2(rg)		#wynikowe logarytmy dla roznych przedstawien (rg i inte) 
	A = np.log2(inte)	
	return M,A
	
	
	
fname = 'GSM151667.xls'
ldata = LoadExcel(fname)		#ldata przechodzi z wnetrza funkcji na zewnatrz i moze byc odczytana przez Ldata2Array
intens, backg = Ldata2Array(ldata)
M, A = MA(intens, backg)

