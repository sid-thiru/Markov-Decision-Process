# MARKOV DECISION PROCESS - Finding the optimal policy

* The aim here is to implement an MDP planning algorithm. The class accepts an MDP object, and returns the optimal policy for the given MDP object.
* An MDP object consists of the set of states, set of actions, rewards and the transition probabilities.
* The approach used to find the optimal policy is value iteration. The underlying principle behind value iteration is: the utility of being in a state is the immediate utility of that state plus the expected reward from moving to the adjacent states (assuming that an optimal policy is used in making moves) The utilities are calculated using the Bellman equation: 𝑈(𝑠)=𝑅(𝑠)+ 𝛾maxΣ𝑃(𝑠′|𝑠,𝑎)𝑈(𝑠′)𝑠′
* These utilities are iteratively updated until the change drops below a certain threshold.

solver.py: Contains code for finding the optimal policy

test.py: Contains code to create MDP objects to test the solver on