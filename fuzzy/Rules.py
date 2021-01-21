class Rules:
    antecedants_rf = [['near', 'near'], ['near', 'medium'], ['near', 'far'],
                      ['medium', 'near'], ['medium', 'medium'], ['medium', 'far'],
                      ['far', 'near'], ['far', 'medium'], ['far', 'far']]
    consequents_rf = [['slow', 'left'], ['slow', 'left'], ['slow', 'left'],
                      ['medium', 'right'], ['fast', 'zero'], ['medium', 'right'],
                      ['medium', 'right'], ['medium', 'right'], ['fast', 'right']]
    ants_oa = [['near', 'near', 'near'], ['near', 'near', 'medium'], ['near', 'near', 'far'],
               ['near', 'medium', 'near'], ['near', 'medium', 'medium'], ['near', 'medium', 'far'],
               ['near', 'far', 'near'], ['near', 'far', 'medium'], ['near', 'far', 'far'],
               ['medium', 'near', 'near'], ['medium', 'near', 'medium'], ['medium', 'near', 'far'],
               ['medium', 'medium', 'near'], ['medium', 'medium', 'medium'], ['medium', 'medium', 'far'],
               ['medium', 'far', 'near'], ['medium', 'far', 'medium'], ['medium', 'far', 'far'],
               ['far', 'near', 'near'], ['far', 'near', 'medium'], ['far', 'near', 'far'],
               ['far', 'medium', 'near'], ['far', 'medium', 'medium'], ['far', 'medium', 'far'],
               ['far', 'far', 'near'], ['far', 'far', 'medium'], ['far', 'far', 'far']]
    cons_oa = [['slow', 'left'], ['slow', 'right'], ['slow', 'right'],
               ['slow', 'left'], ['medium', 'right'], ['medium', 'right'],
               ['slow', 'zero'], ['medium', 'right'], ['fast', 'right'],
               ['slow', 'left'], ['slow', 'left'], ['slow', 'left'],
               ['medium', 'left'], ['medium', 'left'], ['medium', 'right'],
               ['medium', 'left'], ['medium', 'zero'], ['fast', 'right'],
               ['slow', 'left'], ['slow', 'left'], ['slow', 'left'],
               ['medium', 'left'], ['medium', 'left'], ['medium', 'left'],
               ['medium', 'left'], ['fast', 'left'], ['fast', 'zero']]
    ants_behaviour = [['near', 'near'], ['near', 'medium'], ['near', 'far'],
                      ['medium', 'near'], ['medium', 'medium'], ['medium', 'far'],
                      ['far', 'near'], ['far', 'medium'], ['far', 'far']]
    cons_behaviour = [['low', 'high'], ['low', 'high'], ['low', 'high'],
                      ['high', 'medium'], ['low', 'medium'], ['low', 'medium'],
                      ['high', 'low'], ['medium', 'low'], ['medium', 'low']]

    def __init__(self, behaviour=None, mode=None):
        if behaviour == 'RF':
            self.ants = Rules.antecedants_rf
            self.cons = Rules.consequents_rf
        elif behaviour == 'OA':
            self.ants = Rules.ants_oa
            self.cons = Rules.cons_oa
        else:
            self.ants = Rules.ants_behaviour
            self.cons = Rules.cons_behaviour
        if mode == 'OA':
            Rules.cons_behaviour[-1] = ['low', 'medium']

    def rules_fired(self, ants):
        rules_fired = [self.cons[self.ants.index(a)] for a in ants]
        return rules_fired
