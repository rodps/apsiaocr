from sklearn import svm, neighbors, tree, metrics
import csv
import sys
import numpy as np

class ocr(object):

    def __init__ (self, classifier, ftreino, fteste, fout):
        self.classifier = classifier
        self.ftreino = ftreino
        self.fteste = fteste
        self.fout = fout
    
    def execute(self):
    
        print('lendo arquivos')        
        
        csvfile = open(self.ftreino)
        reader = csv.reader(csvfile, delimiter=',')
        classes_treino = []
        features_treino = []
        classes_treino = reader.next()
        for row in reader:
            features_treino.append(row)
        csvfile.close()
        
        csvfile = open(self.fteste)
        reader = csv.reader(csvfile, delimiter=',')
        classes_teste = []
        features_teste = []
        classes_teste = reader.next()
        for row in reader:
            features_teste.append(row)
        csvfile.close()
        
        print('classificando')
        
        if self.classifier == 'svm':
            clf = svm.SVC()
        elif self.classifier == 'knn':
            clf = neighbors.KNeighborsClassifier(5)
        elif self.classifier == 'dtree':
            clf = tree.DecisionTreeClassifier()
        else:
            print('classifier: svm, knn or dtree')
            sys.exit(1)
        
        clf.fit(features_treino, classes_treino)
        
        print('prediction')

        predict = clf.predict(features_teste) 
        
        print('accuracy: {}'.format(metrics.accuracy_score(classes_teste, predict)))
        print(metrics.classification_report(classes_teste,predict))
        
        if self.classifier == 'svm':
            prob = clf.decision_function(features_teste)
        else:
            prob = clf.predict_proba(features_teste)
            
        result = np.c_[classes_teste, prob]         
        
        csvfile = open(self.fout, 'wb')
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(result)
        csvfile.close()
        
        matrix = metrics.confusion_matrix(classes_teste, predict)
        csvfile = open('confusion_'+self.fout[:-4]+'.csv', 'wb')
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(matrix)
        csvfile.close()
        

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Uso: python teste.py 'classifier' 'treino' 'teste' 'saida'")
        sys.exit(1)
    o = ocr(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    o.execute()