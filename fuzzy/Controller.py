from fuzzy.FuzzySets import FuzzySets
from fuzzy.Rules import Rules


class Controller:
    def __init__(self):
        self.distance_sets = None
        self.speed_sets = None
        self.steering_sets = None
        self.behaviour_strength = None
        # self.front_ants = None
        # self.back_ants = None
        self.mv = []
        self.ants = []
        self.cons = None
        self.create_sets()

    def create_sets(self):
        self.distance_sets = [FuzzySets([0.0, 0.0, 0.3, 0.8], "near"),
                              FuzzySets([0.5, 1.0, 1.0, 1.5], "medium"),
                              FuzzySets([1.0, 1.5, 6.0, 6.0], "far")]
        self.speed_sets = [FuzzySets([0.0, 0.0, 0.15, 0.25], "slow"),
                           FuzzySets([0.25, 0.35, 0.45, 0.55], "medium"),
                           FuzzySets([0.45, 0.55, 0.65, 0.8], "fast")]
        self.steering_sets = [FuzzySets([-3.0, -3.0, -2.0, 0], "left"),
                              FuzzySets([-2.0, 0.0, 0.0, 2.0], "zero"),
                              FuzzySets([0.0, 2.0, 3.0, 3.0], "right")]
        # self.steering_sets_oa = [FuzzySets([-3.0, -3.0, -2.0, -1.5], "extreme_left"),
        #                          FuzzySets([-1.0, -0.75, -0.75, -0.5], "mid_left"),
        #                          FuzzySets([-0.75, -0.5, -0.5, -0.25], "left")]
        self.behaviour_sets = [FuzzySets([0.0, 0.15, 0.15, 0.3], "low"),
                               FuzzySets([0.15, 0.3, 0.3, 0.45], "medium"),
                               FuzzySets([0.3, 0.45, 0.45, 0.6], "high")]


    def calc_mv(self, value):
        mv = {i.label: i.membership(value) for i in self.distance_sets}
        # back_mv = {i.label: i.membership(back) for i in self.distance_sets}
        return mv

    def derive_ants(self, mv):
        ants = [k for k in mv if mv[k] > 0]
        # back_ants = [k for k in back_mv if back_mv[k] > 0]
        return ants

    def compute_firing_strength(self, mv):
        result = []
        for ants in self.ants:
            temp = []
            for i, a in enumerate(ants):
                temp.append(mv[i][a])
            result.append(min(temp))
        # print('result: ', min(result))
        return result

    def defuzzification(self, strength, steering_set):
        # print(strength)
        # print(self.cons)
        speed = 0.0
        steer = 0.0
        for v, con in zip(strength, self.cons):
            # print([i for i in self.speed_sets if i.label == con[0]][0].label,v)
            # print([i for i in steering_set if i.label == con[1]][0].label, v)
            speed += [i for i in self.speed_sets if i.label == con[0]][0].center*v
            steer += [i for i in steering_set if i.label == con[1]][0].center*v
        result = [speed/sum(strength), steer/sum(strength)]
        return result

    def defuzzification_oa(self, strength):
        # print(strength)
        # print(self.cons)
        speed = 0.0
        steer = 0.0
        for v, con in zip(strength, self.cons):
            # print([i for i in self.speed_sets if i.label == con[0]][0].label,v)
            # print([i for i in self.steering_sets_oa if i.label == con[1]][0].label, v)
            speed += [i for i in self.speed_sets if i.label == con[0]][0].center*v
            steer += [i for i in self.steering_sets if i.label == con[1]][0].center*v
        result = [speed/sum(strength), steer/sum(strength)]
        return result

    def final_calc(self):
        #self.behaviour_strength
        #self.oa_res
        #self.rf_res
        if len(self.behaviour_strength) > 2:
            a = max(self.behaviour_strength)
            b = min(self.behaviour_strength)
            self.behaviour_strength[0] = a
            self.behaviour_strength[1] = b
        final_speed = (self.behaviour_strength[0] * self.rf_res[0] + self.behaviour_strength[1]
                       * self.oa_res[0])/sum(self.behaviour_strength)
        final_steer = (self.behaviour_strength[0] * self.rf_res[1] + self.behaviour_strength[1]
                       * self.oa_res[1])/sum(self.behaviour_strength)

        # print(final_speed, final_steer)
        return [final_speed, final_steer]


    def controller(self, front_left, front_center, front_right, right_front, right_back, mode):
        # self.inputs = [front, back]
        self.mv = []
        self.mv.append(self.calc_mv(min(front_left, front_center, front_right)))
        self.mv.append(self.calc_mv(right_front))
        self.mv.append(self.calc_mv(right_back))
        self.mv.append(self.calc_mv(front_left))
        self.mv.append(self.calc_mv(front_center))
        self.mv.append(self.calc_mv(front_right))
        print(self.mv)
        ants_local = [self.derive_ants(mv) for mv in self.mv[:2]]
        # print(ants_local)
        self.ants = [[x, y] for x in ants_local[0] for y in ants_local[1]]
        print('Ants of Behaviour: ',self.ants)
        r = Rules(mode=mode)
        self.cons = r.rules_fired(self.ants)
        print('Cons of Behaviour: ', self.cons)
        self.behaviour_strength = self.compute_firing_strength(self.mv[0:2])
        if 'low' in self.cons[0]:
            self.behaviour_strength.insert(self.cons[0].index('low'), 0)
        elif 'medium' in self.cons[0]:
            self.behaviour_strength.insert(self.cons[0].index('medium'), 0)
        print('Behaviour St: ', self.behaviour_strength)
        # ###########Calculation for OA
        ants_local = [self.derive_ants(mv) for mv in self.mv[-3:]]
        print('Ants local of OA: ',ants_local)
        self.ants = [[x, y, z] for x in ants_local[0] for y in ants_local[1] for z in ants_local[2]]
        print('Ants of OA: ',self.ants)
        oa = Rules('OA', mode=mode)
        self.cons = oa.rules_fired(self.ants)
        print('Cons of oa: ',self.cons)
        oa_strength = self.compute_firing_strength(self.mv[-3:])
        print(oa_strength)
        self.oa_res = self.defuzzification_oa(oa_strength)
        print('OA res: ', self.oa_res)
        # ##########Calculation for RF
        ants_local = [self.derive_ants(mv) for mv in self.mv[1:3]]
        # print(ants_local)
        self.ants = [[x, y] for x in ants_local[0] for y in ants_local[1]]
        print('Ants of RF: ',self.ants)
        rf = Rules('RF', mode=mode)
        self.cons = rf.rules_fired(self.ants)
        print('Cons of RF: ',self.cons)
        rf_strength = self.compute_firing_strength(self.mv[1:])
        print(rf_strength)
        self.rf_res = self.defuzzification(rf_strength, self.steering_sets)
        print('RF res: ', self.rf_res)
        result = self.final_calc()
        return result