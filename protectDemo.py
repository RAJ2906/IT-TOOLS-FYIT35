class protecteddemo:

    _name = None
    _roll = None
    _branch = None

    # constructor

    def __init__(self, name, roll, branch, ):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function

    def displayRollAndBranch(self):

        print ('roll:', self._roll)
        print ('branch:', self._branch)


# derived class

class student(protecteddemo):

    # constructor

    def __init__(self, name, roll, branch, ):
        protecteddemo.__init__(self, name, roll, branch)

    def displaydetails(self):
        print ('name:', self._name)
        self.displayRollAndBranch()


obj = student('Amit', 130, 'Information Technology')
print ('name:', obj._name)
obj.displaydetails()
