from fuzzy.Controller import Controller


from fuzzy.Rules import Rules

if __name__ == '__main__':
    obj = Controller()
    front_left = 2.5
    front_center = 2.59
    front_right = 2.919

    right_front = 2.262
    right_back = 1.9
    '''speed = 0.059 steer = 0.021'''
    print('Final result: ', obj.controller(front_left, front_center, front_right, right_front, right_back, 'OA'))
