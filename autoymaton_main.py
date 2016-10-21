from machinery import State, Autoymaton

#Methods to represent different aspect of the interaction
def ask_num_states(mach):

    while True:

        num_states = input('Enter number of states: ')

        try:
            num_states = int(num_states)
        except Exception:
            print('Invalid input')
            continue

        if num_states > 0:
            break
        else:
            print('Invalid input')

    #Add states to machine
    for s in range(1, num_states + 1): mach.add_state(State(str(s)))

def ask_start_state(mach):
    while True:
        start_state = input("What is the start state? ")

        if mach.has_state_label(start_state): break

        print("Your machine doesn't have that state")

    start_state = our_machine.get_state(start_state)
    mach.set_start_state(start_state)

def ask_accept_states(mach):
    while True:
        accept_states = input("Please list the accept state(s) ")
        accept_states = accept_states.split(',')

        if set(accept_states) <= set([s.label for s in mach.states]):
            break
        else:
            print('Invalid input')

    accept_states = [mach.get_state(a) for a in accept_states]
    for s in accept_states: s.set_accept()

def ask_transitions(mach):
    while True:
        input_trans = input('Enter transitions (format: current,symbol,next) or enter "done": ')

        if input_trans == 'done':
            break

        input_trans = input_trans.split(',')

        if len(input_trans) != 3:
            print('Invalid input')
            continue

        q = input_trans[0]
        qN = input_trans[2]

        #Reject if either state given is not part of the machine
        if not mach.has_state_label(q) or not mach.has_state_label(qN):
            print('Invalid input')
        else:
            q = mach.get_state(q)
            qN = mach.get_state(qN)
            q.add_transition(input_trans[1], qN)

def ask_string(mach):
	while True:
		input_string = input('Enter a string for your machine, or enter "done": ')
		if input_string == 'done':
			break
		try:
			result = mach.run_string(input_string, mach.get_start_state())
			if result: print('String accepted!')
			else: print ('String rejected!')
		except KeyError:
			print ('String rejected!')

#Main machine the user will create
our_machine = Autoymaton()

print('Welcome to Autoymaton')
print('Create a DFA')

#ask for number of states
ask_num_states(our_machine)
#Get start state
ask_start_state(our_machine)
#Ask for accept states
ask_accept_states(our_machine)
#Ask for transitions
ask_transitions(our_machine)

print(our_machine)

#Ask for strings and run them on the machine
ask_string(our_machine)

print('Exiting....see you again!')