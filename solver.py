#References:
#http://aima.cs.berkeley.edu/python/mdp.html
#https://people.eecs.berkeley.edu/~pabbeel/cs287-fa12/slides/mdps-exact-methods.pdf

class Solver:
    def __init__(self, mdp):
        self.mdp = mdp
        self.S = mdp.S()
        self.A = mdp.A()
        self.gamma = mdp.gamma()
        self.state_utility = dict([(s, 0) for s in self.S])
        self.epsilon = 0.01
        self.best_policy = {}

    def expected_utility(self):
        delta = []
        for s in self.S:
            u1 = self.state_utility[s]
            u2 = self.state_utility[s]
            for a in self.A:
                value = 0
                for u in self.S:
                    value += self.mdp.P(s,a,u)*(self.mdp.R(u) + self.gamma * self.state_utility[u])
                if value > u1:
                    u1 = value
            delta.append(abs(u2 - u1))
            self.state_utility[s] = u1

        if max(delta) < self.epsilon * (1-self.gamma)/self.gamma:
            return self.state_utility
        else:
            self.expected_utility()


    def solve(self):
        self.expected_utility()
        for s in self.S:
            temp = 0
            for a in self.A:
                value = 0
                for u in self.S:
                    value += self.mdp.P(s, a, u) * (self.mdp.R(u) + self.gamma * self.state_utility[u])
                if value > temp:
                    temp = value
                    self.best_policy[s] = a

        print(self.best_policy)
        return self.best_policy
