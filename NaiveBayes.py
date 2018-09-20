import numpy, pandas, sys, random

def naive_b(train_base, test_item, debug):

    #debug
    if debug:
        print("training started")
        print("train base lenght: ", len(train_base))

    #survivors and dead count    
    class_options, count_options = numpy.lib.arraysetops.unique([train_base[index][-1] for index in range(len(train_base))], return_counts=True)
    total_elements = sum(count_options)

    #debug
    if debug:
        print("class_options:")
        for index in range(len(class_options)):
            print("op:",class_options[index], ": total:" ,count_options[index])
        print("total data: ",total_elements)

    #class separation for element item test    
    class_type = [elem[-1] for elem in train_base if elem[0] == test_item]
    item_options, count_i_options = numpy.lib.arraysetops.unique(class_type, return_counts=True)
    
    #debug
    if debug:
        print("element: ", test_item)        
        for index in range(len(item_options)):
            print("\top:",item_options[index], ": total:" ,count_i_options[index])
    
    #probability func
    prob = lambda x,y,z: (z*x)/y

    #option probability
    probability = []
    for index in range(len(item_options)):
        if count_i_options[index] != 0:            
            probability.append([item_options[index], prob((count_i_options[index]/sum(count_options)), len(item_options)/sum(count_options), count_i_options[index])])
        else:            
            probability.append([item_options[index], prob(1/sum(count_options), 1/sum(count_options), 0)])
    
    #returns the most probable
    probability.sort(key=lambda x: x[-1])
    #debug
    if debug:
        for item in probability:
            print("\tprob: ", item)
        print("result: ", probability[-1][0])

    return probability[-1][0]

#1 for survived, 0 for deceased
titanic_base = pandas.read_csv('train.csv')

train_base = [[titanic_base.age[index], titanic_base.survived[index]] for index in range(len(titanic_base.age))]

if len(sys.argv) < 2:
    debug_controller = False
    while True:
        test_case = input("[death]: Say the age...\n[you]:")
        if test_case == "random":
            age = random.randint(0,100)
            if age > 80:
                print("[death]:", int(age), "This person will already find me...")                
            elif age <= 0:
                print("[death]:", int(age), "This person is not even born yet...")                
            else:
                if naive_b(train_base, age, debug_controller) == 0:
                    print("[death]:", int(age) ,"This person DIE!")
                else:
                    print("[death]:", int(age) ,"This person unfortunately SURVIVED!")
        elif test_case == "quit":
            print("[death]: See you soon...")
            break
        elif test_case == "debug":
            if debug_controller:
                print("[death]: Debug disabled...")
                debug_controller = False
            else:
                print("[death]: Debug activated ...")
                debug_controller = True
        else:
            try:
                age = float(test_case)
                if age > 80:
                    print("[death]:", int(age), "This person will already find me...")                    
                elif age <= 0:
                    print("[death]:", int(age), "This person is not even born yet...")                    
                else:
                    if naive_b(train_base, age , debug_controller) == 0:
                        print("[death]:", int(age) ,"This person DIE!")
                    else:
                        print("[death]:", int(age) ,"This person unfortunately survived!")
            except:
                print("[death]: Type a number or I'll go to you...")
else:
    if len(sys.argv) >= 3:
        if(sys.argv[2].lower() == "true"):
            age = float(sys.argv[1])
            if age > 80:
                print("[death]:", int(age), "This person will already find me...")                
            elif age <= 0:
                print("[death]:", int(age), "This person is not even born yet...")                
            else:
                if naive_b(train_base, age, True) == 0:
                    print("[death]:", int(age) ,"This person DIE!")
                else:
                    print("[death]:", int(age), "This person unfortunately survived!")
        else:
            age = float(sys.argv[1])
            if age > 80:
                print("[death]:", int(age), "This person will already find me...")                
            elif age <= 0:
                print("[death]:", int(age), "This person is not even born yet...")                
            else:
                if naive_b(train_base, age , False) == 0:
                    print("[death]:", int(age) ,"This person DIE!")
                else:
                    print("[death]:", int(age) ,"This person unfortunately survived!")
    else: 
        age = float(sys.argv[1])
        if age > 80:
            print("[death]:", int(age), "This person will already find me...")            
        elif age <= 0:
            print("[death]:", int(age), "This person is not even born yet...")            
        else:
            if naive_b(train_base, age , False) == 0:
                print("[death]:", int(age) ,"This person DIE!")
            else:
                print("[death]:", int(age) ,"This person unfortunately survived!")
 



