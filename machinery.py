"""
This document houses the State and Autoymaton classes. Autoymata consist of States

By: Heikal Badrulhisham, October 21, 2016
"""

"""
State class. Each state keeps track its label, transitions and whether it's an accepting state
"""
class State:
	
	def __init__(self, given_label):
		self.label = given_label
		self.transitions = {}
		self.is_accept = False

	#Label as a state's String representation
	def __str__(self):
		return self.label

	#Adds to the states transition dictionary: key is symbol, value is the next state
	def add_transition(self, symbol, next_state):
		self.transitions[symbol] = next_state

	#Returns the next state for a given symbol
	def get_next_state(self, symbol):
		return self.transitions[symbol]

	#Set this state as an accept state
	def set_accept(self):
		self.is_accept = True

	#Set this as a non-accept state
	def set_not_accept(self):
		self.is_accept = False

"""
Autoymaton class. Automata keep track of their states via a list.
"""	
class Autoymaton:

	def __init__(self):
		self.states = []
		self.accept_states = []
		
	#Add a state to the machine
	def add_state(self, state):
		self.states.append(state)
		
	#Set the start state
	def set_start_state(self, state):
		self.start_state = state
	
	#Return the start state
	def get_start_state(self):
		return self.start_state	
	
	#Tells if the machine has a state with a given label
	def has_state_label(self, label):
		return label in [s.label for s in self.states]

	#Get a state with a given label
	def get_state(self, label):
		x = [s for s in self.states if s.label == label]
		return x[0]
	
	#String representation of the machine
	def __str__(self):
		string_rep = '\nMachine:\nStates: '
		for s in self.states: string_rep += (str(s) + ', ')
		string_rep += "\nTransitions: \n"

		for s in self.states:
			string_rep += "%s : {"%(str(s))
			for sym in s.transitions:
				string_rep += "%s -> %s,"%(sym, s.transitions[sym])
			string_rep += '}\n'

		return string_rep

	#Runs a string on the machine and tells if it is accepted
	def run_string(self, string, state):

		if len(string) == 0 and state.is_accept:
			return True
		if len(string) == 0 and not state.is_accept:
			return False

		curr_char = string[0]
		next_state = state.get_next_state(curr_char)

		return self.run_string(string[1:], next_state)