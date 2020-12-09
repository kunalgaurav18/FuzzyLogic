class Rules:
    antecedants_rf = [['near', 'near'], ['near', 'medium'], ['near', 'far'], ['medium', 'near'], ['medium', 'medium'],
                      ['medium', 'far'], ['far', 'near'], ['far', 'medium'], ['far', 'far']]
    consequents_rf = [['slow', 'left'], ['slow', 'left'], ['slow', 'left'], ['slow', 'right'],
                      ['medium', 'zero'], ['medium', 'right'], ['medium', 'right'], ['medium', 'right'],
                      ['fast', 'right']]
    ants_oa = [['near'], ['medium'], ['far']]
    cons_oa = [['slow', 'extreme_left'], ['medium', 'mid_left'], ['fast', 'left']]
    ants_behaviour = [['near', 'near'], ['near', 'medium'], ['near', 'far'], ['medium', 'near'], ['medium', 'medium'],
                      ['medium', 'far'], ['far', 'near'], ['far', 'medium'], ['far', 'far']]
    cons_behaviour = [['low', 'high'], ['low', 'high'], ['low', 'high'], ['low', 'high'], ['low', 'high'],
                      ['low', 'high'], ['high', 'low'], ['medium', 'low'], ['high', 'low']]

    def __init__(self, behaviour=None):
        if behaviour == 'RF':
            self.ants = Rules.antecedants_rf
            self.cons = Rules.consequents_rf
        elif behaviour == 'OA':
            self.ants = Rules.ants_oa
            self.cons = Rules.cons_oa
        else:
            self.ants = Rules.ants_behaviour
            self.cons = Rules.cons_behaviour

    def rules_fired(self, ants):
        rules_fired = [self.cons[self.ants.index(a)] for a in ants]
        return rules_fired
