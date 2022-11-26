import pickle
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)
        
#create a pickle file
picklefile = open('test_pickle', 'wb')
#pickle the dictionary and write it to file
pickle.dump(Person, picklefile)
#close the file
picklefile.close()
       
