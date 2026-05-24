class Animal:
    def fazer_som(self):
        print('som generico')
        
class Cachorro(Animal):
    def fazer_som (self):
        print('latir')
        
dog = Cachorro()
dog.fazer_som()
        
        
