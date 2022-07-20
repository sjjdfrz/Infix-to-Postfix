import sys
from Sort import *

sort1 = Sort()

class Convertion:
    priority = {'sin': 5, 'cos': 5, 'tan': 5, 'cot': 5, '?': 4, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': -1,
                ')': -1}
    history = {'InfixToPostfix': [0, 0], 'PostfixToInfix': [0, 0], 'InfixToPrefix': [0, 0], 'PrefixToInfix': [0, 0],
               'PostfixToPrefix': [0, 0],
               'PrefixToPostfix': [0, 0]}

    def __init__(self):
        self.myStr = ''
        self.splitStr = []
        self.operatorStack = []
        self.outputStack = []

    def isOperand(self, element):
        return (element.replace('.', '', 1).isdigit() or element.isalpha()) and not self.isFunction(element)

    def isFunction(self, element):
        return element == 'sin' or element == 'cos' or element == 'tan' or element == 'cot'

    def isOperator(self, element):
        return element == '+' or element == '-' or element == '*' or element == '/' or element == '^' or element == '?'

    def isRight_Associative(self, element):
        return element == '^'

    def isLeft_Associative(self, element):
        return element == '+' or element == '-' or element == '*' or element == '/' or '?'

    def Negative_operator(self, arr):

        if arr[0] == "-":
            arr[0] = '?'

        for i in range(1, len(arr)):

            if arr[i] == "-":
                if arr[i - 1] == '(' or (arr[i - 1] == '(' and self.isFunction(arr[i - 2])):
                    arr[i] = '?'

        return arr

    def menu(self):
        self.outputStack.clear()
        self.operatorStack.clear()
        self.splitStr.clear()
        self.myStr = ''

        print('1: Convertion')
        print('2: Sort')
        print('3: exit')
        print('please enter your choice: ', end='')
        choose = int(input())
        counter = 0

        if choose == 1:

            print('1: infix to postfix')
            print('2: postfix to infix')
            print('3: infix to prefix')
            print('4: prefix to infix')
            print('5: postfix to prefix')
            print('6: prefix to postfix')
            print('7: show history')
            print('please enter your choice: ', end='')
            chooseConvert = int(input())

            if chooseConvert == 1:
                print('enter the infix expression: ', end='')
                self.myStr = input()
                self.splitStr = self.Negative_operator(self.myStr.split(' '))
                self.infix_To_postfix()
                counter += 1
                Convertion.history['InfixToPostfix'][0] += 1
                Convertion.history['InfixToPostfix'][1] = counter

            elif chooseConvert == 2:
                print('enter the postfix expression: ', end='')
                self.myStr = input()
                self.splitStr = self.myStr.split(' ')
                self.postfix_To_infix()
                counter += 1
                Convertion.history['PostfixToInfix'][0] += 1
                Convertion.history['PostfixToInfix'][1] = counter

            elif chooseConvert == 3:
                print('enter the infix expression: ', end='')
                self.myStr = input()
                self.splitStr = self.Negative_operator(self.myStr.split(' '))
                self.infix_To_prefix()
                counter += 1
                Convertion.history['InfixToPrefix'][0] += 1
                Convertion.history['InfixToPrefix'][1] = counter

            elif chooseConvert == 4:
                print('enter the prefix expression: ', end='')
                self.myStr = input()
                self.splitStr = self.myStr.split(' ')
                self.prefix_to_infix()
                counter += 1
                Convertion.history['PrefixToInfix'][0] += 1
                Convertion.history['PrefixToInfix'][1] = counter

            elif chooseConvert == 5:
                print('enter the postfix expression: ', end='')
                self.myStr = input()
                self.splitStr = self.myStr.split(' ')
                self.postfix_to_prefix()
                counter += 1
                Convertion.history['PostfixToPrefix'][0] += 1
                Convertion.history['PostfixToPrefix'][1] = counter

            elif chooseConvert == 6:
                print('enter the prefix expression: ', end='')
                self.myStr = input()
                self.splitStr = self.myStr.split(' ')
                self.prefix_to_postfix()
                counter += 1
                Convertion.history['PrefixToPostfix'][0] += 1
                Convertion.history['PrefixToPostfix'][1] = counter

            elif chooseConvert == 7:
                print('enter 1 for ascending history or enter 2 for descending history: ', end='')
                chooseHistory = int(input())
                if chooseHistory == 1:
                    self.showHistoryAscending()
                elif chooseHistory == 2:
                    self.showHistoryDescending()
                else:
                    print('wrong input!')
            else:
                print('wrong input!')

        elif choose == 2:

            print('1: bubble Sort')
            print('2: selection Sort')
            print('3: insertion Sort')
            print('4: merge Sort')
            print('5: quick Sort')
            print('please enter your choice: ', end='')
            chooseSort = int(input())

            if chooseSort == 1:
                print('Please enter your array: ', end='')
                arr = list(map(int, input().split(' ')))
                sort1.bubbleSort(arr)

            elif chooseSort == 2:
                print('Please enter your array: ', end='')
                arr = list(map(int, input().split(' ')))
                sort1.selectionSort(arr)

            elif chooseSort == 3:
                print('Please enter your array: ', end='')
                arr = list(map(int, input().split(' ')))
                sort1.insertionSort(arr)

            elif chooseSort == 4:
                print('Please enter your array: ', end='')
                arr = list(map(int, input().split(' ')))
                sort1.mergeSort(arr)

            elif chooseSort == 5:
                print('Please enter your array: ', end='')
                arr = list(map(int, input().split(' ')))
                sort1.quickSort(0, len(arr) - 1, arr)
                print('Sorted array: ', end='')
                print(arr)

            else:
                print('wrong input!')

        elif choose == 3:
            sys.exit(0)

        else:
            print("wrong input!")

        self.menu()

    def display(self):
        print('operatorstack: ', end='')
        print(self.operatorStack)
        print('output: ' + ' '.join(self.outputStack))

    def showHistoryDescending(self):
        history = list(self.history.items())
        n = len(history)
        for i in range(n):
            for j in range(0, n - i - 1):

                if history[j][1][0] < history[j + 1][1][0]:
                    history[j], history[j + 1] = history[j + 1], history[j]

                elif history[j][1][0] == history[j + 1][1][0]:
                    if history[j][1][1] < history[j + 1][1][1]:
                        history[j], history[j + 1] = history[j + 1], history[j]

        for x in history:
            if x[1][0] != 0:
                print(x[0] + ' : ' + str(x[1][0]))

    def showHistoryAscending(self):
        history = list(self.history.items())
        n = len(history)
        for i in range(n):
            for j in range(0, n - i - 1):

                if history[j][1][0] > history[j + 1][1][0]:
                    history[j], history[j + 1] = history[j + 1], history[j]

                elif history[j][1][0] == history[j + 1][1][0]:
                    if history[j][1][1] < history[j + 1][1][1]:
                        history[j], history[j + 1] = history[j + 1], history[j]

        for x in history:
            if x[1][0] != 0:
                print(x[0] + ' : ' + str(x[1][0]))

    def infix_To_postfix(self):

        for element in self.splitStr:

            if self.isOperand(element):
                self.outputStack.append(element)

            elif self.isFunction(element):
                self.operatorStack.append(element)

            elif element == '(':
                self.operatorStack.append(element)

            elif element == ')':

                while self.operatorStack and self.operatorStack[-1] != '(':
                    self.outputStack.append(self.operatorStack.pop())

                if not self.operatorStack:
                    print('invalid expression')
                    self.menu()

                self.operatorStack.pop()

            # if token is a operator
            elif self.isOperator(element):
                if self.isLeft_Associative(element):
                    while self.operatorStack and Convertion.priority[self.operatorStack[-1]] >= Convertion.priority[
                        element]:
                        self.outputStack.append(self.operatorStack.pop())
                    self.operatorStack.append(element)

                elif self.isRight_Associative(element):
                    while self.operatorStack and Convertion.priority[self.operatorStack[-1]] > Convertion.priority[
                        element]:
                        self.outputStack.append(self.operatorStack.pop())
                    self.operatorStack.append(element)

            else:
                print('invalid expression')
                self.menu()

            self.display()

        while self.operatorStack:

            if self.operatorStack[-1] == '(':
                print("This expression is invalid")
                self.menu()
            self.outputStack.append(self.operatorStack.pop())

        self.display()

    def postfix_To_infix(self):

        for element in self.splitStr:

            if self.isOperand(element):
                self.outputStack.append(element)

            elif self.isOperator(element):

                op2 = self.outputStack.pop()
                op1 = self.outputStack.pop()
                self.outputStack.append("(" + op1 + ' ' + element + ' ' + op2 + ")")

            else:
                print('invalid expression')
                self.menu()

            self.display()

        if len(self.outputStack) == 1:
            self.display()
        else:
            print("invalid expression!")

    def infix_To_prefix(self):

        for element in self.myStr[::-1].split(' '):

            if self.isOperand(element):
                self.outputStack.append(element)

            elif element == ')':
                self.operatorStack.append(element)

            elif element == '(':
                while self.operatorStack and self.operatorStack[-1] != ')':
                    self.outputStack.append(self.operatorStack.pop())

                if not self.operatorStack:
                    print('invalid expression')
                    self.menu()

                self.operatorStack.pop()


            elif self.isOperator(element):
                if self.isLeft_Associative(element):
                    while self.operatorStack and Convertion.priority[self.operatorStack[-1]] > Convertion.priority[
                        element]:
                        self.outputStack.append(self.operatorStack.pop())
                    self.operatorStack.append(element)

                elif self.isRight_Associative(element):
                    while self.operatorStack and Convertion.priority[self.operatorStack[-1]] >= Convertion.priority[
                        element]:
                        self.outputStack.append(self.operatorStack.pop())
                    self.operatorStack.append(element)

            else:
                print('invalid expression')
                self.menu()

            self.display()

        while self.operatorStack:
            if self.operatorStack[-1] == ')':
                print("This expression is invalid")
                self.menu()

            self.outputStack.append(self.operatorStack.pop())

        self.outputStack.reverse()
        self.display()

    def prefix_to_infix(self):

        for element in self.splitStr[::-1]:

            if self.isOperand(element):
                self.outputStack.append(element)

            elif self.isOperator(element):

                op2 = self.outputStack.pop()
                op1 = self.outputStack.pop()
                self.outputStack.append('(' + op2 + ' ' + element + ' ' + op1 + ')')

            else:
                print('invalid expression')
                self.menu()

            self.display()

        if len(self.outputStack) == 1:
            self.display()
        else:
            print("invalid expression!")

    def postfix_to_prefix(self):

        for element in self.splitStr:

            if self.isOperand(element):
                self.outputStack.append(element)

            elif self.isOperator(element):

                op2 = self.outputStack.pop()
                op1 = self.outputStack.pop()
                self.outputStack.append(element + ' ' + op1 + ' ' + op2)

            else:
                print('invalid expression')
                self.menu()

            self.display()

        if len(self.outputStack) == 1:
            self.display()
        else:
            print("invalid expression!")

    def prefix_to_postfix(self):

        for element in self.splitStr[::-1]:

            if self.isOperand(element):
                self.outputStack.append(element)


            elif self.isOperator(element):

                op2 = self.outputStack.pop()
                op1 = self.outputStack.pop()
                self.outputStack.append(op2 + ' ' + op1 + ' ' + element)

            else:
                print('invalid expression')
                self.menu()

            self.display()

        if len(self.outputStack) == 1:
            self.display()
        else:
            print("invalid expression!")


c1 = Convertion()
c1.menu()
