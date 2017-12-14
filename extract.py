from PIL import Image
import csv
import sys
import math
import os.path

class extract(object):
    
    def __init__(self, y, x, fin, fout):
        self.fin = fin
        self.fout = fout
        self.x = int(x)
        self.y = int(y)
    
    def execute(self):
        print('Lendo o arquivo...')
        
        try:
            arq = open(self.fin)
        except IOError:
            print('Erro ao abrir o arquivo')
        text = arq.readlines()
        arq.close()
        
        features = []
        classes = []

        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        i=0
        for line in text:
            img = Image.open(script_dir+line.replace('\r','').replace('\n',''))
            features.append(self.zoning(img))
            classes.append(line[1])
            sys.stdout.write('\rExtraindo caracteristicas... {}%'.format(100*i/len(text)))
            sys.stdout.flush()
            i=i+1

        print('\nEscrevendo no arquivo de saida...')
        csvfile = open(self.fout,'w')
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(classes)
        writer.writerows(features)
        csvfile.close()
        print('Concluido.')
        
    def zoning(self, img):

        l, c = img.size
        x_size = int(math.ceil(c/self.x))
        y_size = int(math.ceil(l/self.y))

        zones = []

        for i in range(self.y):
            for j in range(self.x):

                if i == self.y-1:
                    k = l-1
                else:
                    k = (i+1)*y_size -1
                if j == self.x-1:
                    m = c-1
                else:
                    m = (j+1)*x_size -1

                z = img.crop([j*x_size, i*y_size, m, k])
                h = z.histogram()[:2]
                if (h[0]+h[1])>0:
                    zones.append(float(h[1])/(h[0]+h[1]))
                else:
                    zones.append(0.0)

        return zones
        

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print ("Modo de usar: python extract.py 'y' 'x' 'entrada.txt' 'saida.csv'")
        sys.exit(1)
    e = extract(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    e.execute()
 
    