import logging
logging.basicConfig(filename='task.log',level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')
class task:
    try:
        def print_pattern(self):
            for i in range(5):
                for j in range(0, i):
                    print("ineuron", end=" ")
                print("\n")
            logging.info('the pattern has been printed')
    except Exception as e:
        print('there is an exception')
        logging.error('there is exception in code')
    def print_pattern2(self):
        try:
            n = 4
            for i in range(n):
                print(" " * len("ineuron") * (n - i - 1), end='')
                for j in range(i):
                    print("ineuron" + " " * len("ineuron"), end='')
                print("\n", end='')
            for i in range(n - 2, -1, -1):
                print(" " * len("ineuron") * (n - i - 1), end='')
                for j in range(i):
                    print("ineuron" + " " * len("ineuron"), end='')
                print("\n", end='')
            logging.info('the pattern is printed properly')
        except Exception as e:
            logging.exception('there is an exception')
    def all_list(self,l):
        try:
            self.l=l
            for i in l:
                if type(i) == list:
                    print(i)
            logging.info('finding list is done')
        except Exception as e:
            print('there is an exception')
            logging.warning('there is an exception')
    def all_dict(self,l):
        try:
            for i in l:
                if type(i) == dict:
                    print(i)
            logging.info('all the dict entities has been printed')
        except Exception as e:
            print('there is an exception')
            logging.exception('there is an exception')
    def all_tuples(self,l):
        try :
            for i in l:
                if type(i) == tuple:
                    print(i)
            logging.info("all the tuples are printed from the list")
        except Exception as e:
            print('there is an exception')
            logging.exception('there is an exception')
    def all_num_from_l(self,l):
        try:
            li = []
            for i in l:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            li.append(j)
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            li.append(j)
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            li.append(j)
                if type(i) == dict:
                    for j in i:
                        if type(j) == int:
                            li.append(j)
                        if type(i[j]) == int:
                            li.append(i[j])
            print(li)
            logging.info('the numbers are extracted')
        except Exception as e:
            logging.exception(e)
    def extract_ineuron(self,l):
        try :
            la = list()
            for i in l:
                if type(i) == list:
                    for j in i:
                        if j == 'ineuron':
                            la.append(j)
                if type(i) == tuple:
                    for j in i:
                        if j == 'ineuron':
                            la.append(j)
                if type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                            la.append(j)
                if type(i) == dict:
                    for j in i:
                        if j == 'ineuron':
                            la.append(j)
                        if i[j] == 'ineuron':
                            la.append(i[j])
            logging.info('the ineuron is extracted from the list')
        except Exception as e:
            logging.exception(e)
    def occurances_of_data(self,l):
        try :
            di = dict()
            for i in l:
                if type(i) == list:
                    for j in i:
                        if j in di:
                            di[j] = di[j] + 1
                        else:
                            di[j] = 1
                if type(i) == tuple:
                    for j in i:
                        if j in di:
                            di[j] = di[j] + 1
                        else:
                            di[j] = 1
                if type(i) == set:
                    for j in i:
                        if j in di:
                            di[j] = di[j] + 1
                        else:
                            di[j] = 1
                if type(i) == dict:
                    for j in i:
                        if j in di:
                            di[j] = di[j] + 1
                        else:
                            di[j] = 1
                        if i[j] in di:
                            di[i[j]] = di[i[j]] + 1
                        else:
                            di[i[j]] = 1
            print(di)
            logging.info('the occurances are extracted')
        except Exception as e:
            logging.exception(e)
    def find_no_keys(self,l):
        try :
            for i in l:
                if type(i) == dict:
                    for j in i:
                        print(j)
            logging.info('the number of keys are extracted')
        except Exception as e:
            logging.exception(e)
    def find_out_stringdata(self,l):
        try :
            for i in l:
                if type(i) == dict:
                    for j in i:
                        print(j)
            logging.info('the string data is extracted')
        except Exception as e:
            logging.exception(e)
    def find_alphanumdata(self,l):
        try:
            lan = []
            for i in l:
                if type(i) == list:
                    for j in i:
                        if type(j) == str:
                            if j.isalnum():
                                lan.append(j)
                if type(i) == tuple:
                    for j in i:
                        if type(j) == str:
                            if j.isalnum():
                                lan.append(j)
                if type(i) == set:
                    for j in i:
                        if type(j) == str:
                            if j.isalnum():
                                lan.append(j)
                if type(i) == dict:
                    for j in i:
                        if type(j) == str:
                            if j.isalnum():
                                lan.append(j)
                        if type(i[j]) == str:
                            if i[j].isalnum():
                                lan.append(i[j])
            print(lan)
            logging.info('the alphanum data is extracted')
        except Exception as e:
            logging.exception(e)
    def unwarp_data(self,l):
        try :
            lcc = []
            for i in l:
                if type(i) == list:
                    for j in i:
                        lcc.append(j)
                if type(i) == tuple:
                    for j in i:
                        lcc.append(j)
                if type(i) == set:
                    for j in i:
                        lcc.append(j)
                if type(i) == dict:
                    for j in i:
                        lcc.append(j)
                        lcc.append(i[j])
            print(lcc)
            logging.info('the data is unwraped')
        except Exception as e:
            logging.exception(e)

obj=task()
obj.print_pattern()
obj.print_pattern2()
obj.all_list([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.all_dict([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.all_tuples([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])

obj.all_num_from_l([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.extract_ineuron([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.find_alphanumdata([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.find_no_keys([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.occurances_of_data([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.unwarp_data([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.find_out_stringdata([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj.extract_ineuron([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])

