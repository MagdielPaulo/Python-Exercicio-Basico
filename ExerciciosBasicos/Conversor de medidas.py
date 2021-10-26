#### Um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.(Vou fazer de todos só por charme) ####

medida = float(input('Uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {} metros corresponde a:\n {:.0f}mm\n {:.0f}cm\n {:.0f}dm\n {}dam\n {}hm\n {}km'.format(medida,mm,cm,dm,dam,hm,km))
