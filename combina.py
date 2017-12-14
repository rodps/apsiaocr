import csv
import numpy as np
import sys

class combina(object):
    
    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        
    def execute(self):
        classes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                   'o','p','q','r','s','t','u','v','w','x','y','z']
        
        csvfile = open(self.c1)
        reader = csv.reader(csvfile, delimiter=',')
        result_c1 = []
        result = []
        for row in reader:
            result.append(row)
        csvfile.close()

        for r in result:
            result_c1.append(map(float,r[1:]))
        
        csvfile = open(self.c2)
        reader = csv.reader(csvfile, delimiter=',')
        result_c2 = []
        for row in reader:
            result_c2.append(map(float,row[1:]))
        csvfile.close()
        
        csvfile = open(self.c3)
        reader = csv.reader(csvfile, delimiter=',')
        result_c3 = []
        for row in reader:
            result_c3.append(map(float,row[1:]))
        csvfile.close()
        
        sum_total = np.add(result_c1, result_c2)
        sum_total = np.add(sum_total, result_c3)
        sum_total = sum_total.tolist()
        
        acertos = 0
        for i in range(len(sum_total)):
            if classes[sum_total[i].index(max(sum_total[i]))] == result[i][0]:
                acertos += 1
        
        print(float(acertos)/len(result))
        
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python combina.py 'c1' 'c2' 'c3'")
        sys.exit(1)
    c = combina(sys.argv[1], sys.argv[2], sys.argv[3])
    c.execute()
            
        
        
    
    