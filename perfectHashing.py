
#to generate random numbers
import random


class perfectHashing:
    'Class for perfect hashing'

    #creating the class
    def __init__(self, inputArray) :

        #checking if ther are collision
        #self.isCollision = False
        
        #getting first-level hash table length
        self.m = len(inputArray)

        #determine prime number next to the highest key value
        max = inputArray[0]
        for i in range (0, self.m) :
            if (inputArray[i] > max) :
                max = inputArray[i] #to find the highest key   

        #the fastest way to get a prime number greater than the max key
        self.p = 2*max + 1 #so we have 0 <= k <= p-1        
        

        #getting a and b
        self.a = random.randint(0, self.p-1)
        self.b = random.randint(0, self.p) 

        #counting how many elements are in the same position
        C = [0]*self.m  #C stand for counter
        for i in range(0, self.m) :
            C[((self.a*inputArray[i]+self.b)%self.p)%self.m] += 1 #now we have how many elements are in the i position        
        
        #creating first and second hash tables
        self.S = [None]*self.m

        for i in range(0, self.m) :
            if(C[i] > 0) : #we use this statement to connect second-level hash tables to the first-level hash table
                           #(and avoid the inisialisation of empty S cells)     
                self.S[i] = secondHashTable(C[i], self.p)

        #inserting keys in second-level hash table     
        for i in range(0, self.m) :
            if(self.S[((self.a*inputArray[i]+self.b)%self.p)%self.m].m > 0) : #we are checking if the table slot is not empty
                #checking for collisions
                #self.collisionChecking(self.S[((self.a*inputArray[i]+self.b)%self.p)%self.m], inputArray[i])

                #first value is the second-level hash table, the second is the key
                self.insertSecondHash(self.S[((self.a*inputArray[i]+self.b)%self.p)%self.m], inputArray[i])

        #print("searching success? ", self.searchElements(self.S, inputArray))        

    #inserting method for second-level hash table
    def insertSecondHash(self, table, key) : 
        table.s2[((table.a*key+table.b)%self.p)%table.m] = key

    #veryfing that there are no collisions
    def collisionChecking(self, table, key) :
        if(table.s2[((table.a*key+table.b)%self.p)%table.m] != None) :
            self.isCollision = True

    #searching all elements of the inserted list for checking if there are any collisions   
    def searchElements(self, array) :
        for i in range(0, len(array)) :
            j = self.S[((self.a*array[i]+self.b)%self.p)%self.m]
            if(j.s2[((j.a*array[i]+j.b)%self.p)%j.m] != array[i]) :#i'm checking if input array element is not correctly inserted in the hash table
                return False
        return True            

#creating second-level hash table class
class secondHashTable:
    'class for second hashing table'
    
    def __init__(self, m, p) :
        if (m > 1) :
            self.m = m**2
            self.a = random.randint(0, p-1)
            self.b = random.randint(0, p)
            self.s2 = [None]*self.m
        else:
            self.m = m
            self.a = 0
            self.b = 0
            self.s2 = [None]*self.m     

#main
if __name__ == "__main__" :
    #setting list's dimensions
    q = 100

    #creating a random list           
    K = random.sample(range(q), q)

    #counting how many tries we need to remove collisions
    counter = 0

    #counting how much space is occupied by all the arrays
    dimensions = 0

    #generating perfect hashing
    P = perfectHashing(K)

    print("searching success? ", P.searchElements(K)) 

    #we loop perfect hash until we have no collisions
    while(not P.searchElements(K)) :
        del P
        P = perfectHashing(K)
        counter += 1

    #printing the results
    print("Total tries: ", counter)
    #print("\nRandom list generated K: ", K)
    #print("\nFirst-level perfect hashing table: ", P.S)
    #print("\nFirst-level p: ", P.p)
    #print("\nFirst-level m: ", P.m)
    dimensions += P.m
    #print("\nFirst-level a and b: a -> ",P.a,"  b -> ", P.b)
    for i in range(0, P.m) :
        if(P.S[i]) :
            #print("\nSecond-level perfect hashing table ",i,": ", P.S[i].s2)
            #print("\nSecond-level m ",i,": ", P.S[i].m)
            dimensions += P.S[i].m
            #print("\nSecond-level a and b ",i," : a -> ", P.S[i].a, "  b -> ", P.S[i].b)
    print("\nTotal space occupied by arrays : ", dimensions)


    #print("\n Do we have collision? ", P.isCollision)        