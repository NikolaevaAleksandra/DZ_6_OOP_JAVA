class Calculator:
    operators = '+-/*^'  

    def my_parse(self, string):  
        ret = []
        num = ''
        for char in string:
            if char in '.0123456789':
                num += char
            elif char in self.operators or char in '()':
                if len(num) > 0:
                    ret.append(num)
                    num = ''
                ret.append(char)
        if len(num) > 0:
            ret.append(num)
        return ret

    def solver2operand(self, expression):  
        match expression[1]:
            case '+':
                return str(float(expression[0]) + float(expression[2]))
            case '-':
                return str(float(expression[0]) - float(expression[2]))
            case '*':
                return str(float(expression[0]) * float(expression[2]))
            case '/':
                return str(float(expression[0]) / float(expression[2]))
            case '^':
                return str(pow(float(expression[0]), float(expression[2])))
            case _:
                print('Ошибка в выражении (1)')
                exit()
        return '0'

    def get_operand_index(self, expression, op):  
        try:
            return expression.index(op)
        except ValueError:  
            return -1

    def iterator(self, expression):  
        if expression[0] == '-':  
            expression.insert(0, '0')
        match len(expression):
            case 0:
                return []  
            case 1:
                return expression 
            case 2:
                return expression[0]  
            case 3:
                return [str(self.solver2operand(expression))]  
            case _:
                mypos = self.get_operand_index(expression, ')') 
                if mypos == -1:  

                    mypos = self.get_operand_index(expression, '^')  
                    if mypos == -1 or \
                            ((self.get_operand_index(expression,
                                                     '*') < mypos)  
                             and self.get_operand_index(expression,
                                                        '*') > -1):  
                        mypos = self.get_operand_index(expression, '*')  
                    if mypos == -1 or \
                            ((self.get_operand_index(expression, '/') < mypos)  
                             and self.get_operand_index(expression, '/') > -1):  
                        mypos = self.get_operand_index(expression, '/')  

                    if mypos == -1:  
                        mypos = self.get_operand_index(expression, '-')
                    if mypos == -1:
                        mypos = self.get_operand_index(expression, '+')

                    if mypos > -1:
                        expression[mypos - 1] = str(
                            self.solver2operand(expression[mypos - 1:mypos + 2]))  
                       
              
                        del expression[mypos:mypos + 2]  
                        return expression
                else:  
                    open_bracket = mypos  
                    for i in range(mypos, -1, -1):  
                        if expression[i] == '(':
                            open_bracket = i  
                            break

                    
                    expr1 = expression[0:open_bracket]  
                    expr3 = expression[mypos + 1:] 

                    expr2 = self.iterator(expression[open_bracket + 1:mypos])  
                    
                    expression = []  

                    if len(expr1) > 0:  
                        expression.extend(expr1)
                    expression.extend(expr2)
                    if len(expr3) > 0:  
                        expression.extend(expr3)
                    return expression

    def my_solver(self, expression):
        while len(expression) > 1:  
            expression = self.iterator(expression)
        return expression

    def calculate(self, expession):  
        return self.my_solver(self.my_parse(expession))[0]