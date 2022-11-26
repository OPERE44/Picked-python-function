
from models import Person
import pickle

picklefile = open('test_pickle', 'rb')
#unpickle the dataframe
person_pickle = pickle.load(picklefile)
t=person_pickle('john', 10)
print(t.myfunc())

# @app.route('/')
# def index():
#    return render_template('index.html')
# if __name__ == '__main__':
#     print('File okay')
#     picklefile = open('test_pickle', 'rb')
#     #unpickle the dataframe
#     laptop1 = pickle.load(picklefile)
#     t=laptop1('john', 10)
#     print(t.myfunc())  
	
