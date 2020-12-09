from fuzzy.Controller import Controller


from fuzzy.Rules import Rules

if __name__ == '__main__':
    obj = Controller()
    front_center = 0.3
    right_front = 1.2
    right_back = 1.4
    print('Final result: ', obj.controller(front_center, right_front, right_back))
