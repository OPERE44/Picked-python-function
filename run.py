
from models import Person
import pickle

picklefile = open('test_pickle', 'rb')
#unpickle the dataframe
person_pickle = pickle.load(picklefile)
t=person_pickle('john', 10)
print(t.myfunc())


if __name__ == '__main__':
    print('File okay')
	
