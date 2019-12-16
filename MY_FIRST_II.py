from numpy import exp, array, random, dot, mean, abs
import json
import time


# shape[1])

class UU():
    def __init__(self, start, end=1, activ='sigma'):
        random.seed(228)

        shape = (start, end)
        self.lays = [shape]
        self.activs = [activ]
        self.w = []

    def add(self, nerv=1, end=1, activ='sigma'):
        if nerv == 0:
            nerv = 1
            print("nerv can not be 0, so we make it 1")
        q = self.lays.pop()
        self.lays.append((q[0], nerv))
        self.activs.append(activ)
        self.lays.append((nerv, end))

    def weight(self):
        for i in self.lays:
            self.w.append(2 * random.random(i) - 1)

    def activator(self, x, act='sigma', T=True):
        if act == 'sigma':
            if T:
                return 1 / (1 + exp(-x))
            else:
                return x * (1 - x)
        else:
            raise NameError('activator')

    def mtd(data, ans, train_part=80):
        a = int(len(data) * train_part / 100)
        return data[:a], data[a:], ans[:a], ans[a:]

    def train(self, X, Y, how=20000, bash=35):
        if bash > len(X):
            print('bash too big')
            bash = len(x)

        self.weight()
        lay = len(self.w)
        l = [0 for i in range(lay + 1)]
        delta = [0 for i in range(lay + 1)]
        for i in range(how):
            for b in range(0, len(X) - bash + 1, bash):

                data = array(X[b:bash + b])
                ans = array([Y[b:bash + b]]).T

                l[0] = data
                for j in range(lay):
                    l[j + 1] = self.activator(dot(l[j], self.w[j]), act=self.activs[j])
                error = ans - l[lay]
                delta[lay] = error * self.activator(l[lay], T=False)
                # if i == how-1:
                # print(error,end='\n\n\n')
                # print(self.lays)
                # print(delta, self.w,l,sep='\n\n\n')
                for j in range(lay, 1, -1):
                    e = delta[j].dot(self.w[j - 1].T)
                    delta[j - 1] = e * self.activator(l[j - 1], T=False)

                for j in range(lay):
                    self.w[j] += l[j].T.dot(delta[j + 1])

    def say(self, what, act1='sigma'):
        l = [0 for i in range(len(self.w) + 1)]
        l[0] = what
        # print (self.w,'\n\n\n')
        for j in range(len(self.w)):
            l[j + 1] = self.activator(dot(l[j], self.w[j]), act=act1)
        return l  # [int(round(i[0],1)) for i in l[len(self.w)]]len(self.w)

    def find_nerv(self, X, Y, start=1, fin=10, ech=20000):
        '''
        find_nerv(self,X,x,Y,y,dip=3,fin=10,ech=2000,mi=0,q=[]):
        if dip >0:
            dip -=1
            for i in range(2,fin):
                self.find_nerv(X,x,Y,y,dip,fin,ech,mi,q)
                self.add(i)
                self.train(X,Y,ech)
                A = self.say(x)
                err = y - A
                m = mean(abs(err))
                print(q)

                if (m < mi)or mi==0:
                    mi = m
                    q = self.lays
        # xt = array([[1,0,0,0],[0,1,1,0],[1,1,1,0],[0,0,0,1]])
        # yt = array([[1,0,0,0]]).T
        '''
        q = (0, 0, 0)
        mi = 0
        x, xt, y, yt = UU.mtd(X, Y)

        for i in range(start, fin):
            print('i = ', i)
            print(q)
            print("{:g} s".format(time.clock() - start_time))
            for j in range(start, fin):
                print(j)
                for ij in range(start, fin):
                    self.__init__(X.shape[1])
                    self.add(i)
                    self.add(j)
                    self.add(ij)
                    self.train(x, y, ech)
                    A = self.say(xt)

                    err = yt - A

                    m = mean(abs(err))
                    if (m < mi) or mi == 0:
                        mi = m
                        q = (i, j, ij)
                        with open(f'q{i}{j}{ij}.txt', 'w') as f:
                            f.write(str(q))
        return q

    def MakeAll(X, Y):
        u = UU(X.shape[1])
        sloy = u.find_nerv(X, Y)
        print(sloy)
        u.__init__(X.shape[1])
        for i in range(len(sloy)):
            print('dd', sloy[i])
            u.add(sloy[i])
        print(u.lays)
        u.train(X, Y)
        print("Готово!")
        return u


if __name__ == "__main__":
    # start_time = time.clock()
    # print(l,self.w,data,delta,sep='\n\n\n')
    with open('data.txt') as f:
        data = f.read()
    print(type(data))
    data = array(json.loads(data))
    X, Y = data[:, 0:24], data[:, 24]
    # print(X[:5])
    # print(array([Y[:5]]).T)
    # print(Y)
    u = UU(X.shape[1])
    # print ("{:g} s".format(time.clock() - start_time))

    u.add(12)
    u.add(19)
    u.add(9)
    u.train(X, Y, 1000)

    # print(u.find_nerv(X,Y,start=7, fin=20,ech=10000))
    # print ("{:g} s".format(time.clock() - start_time))
    # print(u.say([[0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],[0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0]]))
    print(u.say(X))

    '''

    X = array([[0,0,0,0],
               [0,0,1,0],
               [0,1,0,0],
               [1,1,1,1],
               [1,0,0,0],
               [0,0,1,1],
               [0,1,1,0],
               [1,1,0,1]])

    x = array([[2,1],
               [0,1],
               [2,0],
               [0,0],
               [1,0],
               [0,0]])
    y = array([[1,1,0,0,1,0]]).T

    u=UU(X.shape[1])
    u.add(1)
    u.add(3)
    u.add(7)
    u.train(X,Y)

    # u=UU.MakeAll(X,Y)
    # x,xt,y,yt = UU.mtd(X,Y)
    # print(u.find_nerv(X,Y))
    #print(u.say([[2,2],[0,2],[1,1],[0,1]]))
    #print(0,0,0,1)
    # print(1,0,0,0)
    print(u.say([[1,0,0,0],[0,1,1,0],[1,1,1,0],[0,0,0,1]]))
    '''



