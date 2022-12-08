class Data:
   

    expressions = [
        "-11+1"
        , "2+2"
        , "12*3+3+5+2*2"
        , "1+2*(3+5)"
        , "15/(7-(1+1))*3-(2+(1+1))"
        , "1/2+1/3"
        , "-2*5"
        , "-2^5"
        , "2+2"
        , "1+2*3"
        , "1-4*3"
        , "1+5*3"
        , "(1+2)*3"
        , "2^5"
        , "1-22/22-2/2*2+1"
        , "3+3"
    ]

    def __init__(self):
        self.counter = 0

    def __iter__(self):  
        return self

    def __next__(self):  
        if self.counter < len(self.expressions):
            self.counter += 1
            return self.expressions[self.counter - 1]
        else:
            raise StopIteration