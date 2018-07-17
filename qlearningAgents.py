# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        #init the 5x5 array
        self.QValues = []
        Blank = [0.1, 0.0, 0.0, 0.0]
        for x in range(5):
            self.QValues.append([])
            for y in range(5):
                if (x,y) == (3,2):
                    self.QValues[x].append(1)
                else if (x,y) == (3,1):
                    self.QValues[x].append(-1)
                else:
                    self.QValues[x].append(Blank)

        
        print self.QValues
        self.getQV = lambda i: self.QValues if not i else(self.QValues[i[0]][i[1]])
        #self.setQV = lambda i,v: self.QValues if not i else(self.QValues[i[0]][i[1]] = v)
        "*** YOUR CODE HERE ***"

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        #print "state: ", state, "\naction: ", action
        try:
            QMatrix = self.getQV(state)
            action_values = {
                'north': QMatrix[0],
                'south': QMatrix[1],
                'east' : QMatrix[2],
                'west' : QMatrix[3],
            }
            print action_values
            return action_values[action]
        except:
            #print "Never seen this state, ret 0"
            #add state and action to matrix
            print "Error in retrieving QValue"
            print "state: ", state, "\naction: ", action
            print "val: ", self.getQV(state)
            return self.getQV(state)

            # Blank = [0.1, 0.0, 0.0, 0.0]
            # try:
            #     Yelems = self.QValues[state[0]]
            #     print "No Y matrix exists, lets create it"
            #     for i in range(len(Yelems), state[1]):
            #         Yelems.append(Blank)
            #     self.Qvalues[state[0]] = Yelems
            #     return 0.0
            # except:
            #     print "no X matrix exists, lets create it"
            #     XElem = [Blank]
            #     for i in range(1,state[1]):
            #         XElem.append(Blank)
            #     # might want to check if X index is negative or 
            #     # less than the starting value then insert this X 
            #     # matrix accordingly. But as long as we start at 0,Y 
            #     # and X index (state[0]) is never negative 
            #     self.QValues.append(XElem)
            #     return 0.0
        #print len(self.QValues), len(self.QValues[0]), len(self.QValues[0][0])
        #return 0.0
        "util.raiseNotDefined()"
        
        


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        return 0.0

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        return 'north'

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        if legalActions[0] == 'exit':
            return 'exit'
        print legalActions
        #roll a random number to see if its in epsilon
        if random.uniform(0,1) < self.epsilon:
            #explore, choose random legal action
            return random.choice(legalActions)
        else:
            #choose policy
            return self.getPolicy(state)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        return 0.0

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)