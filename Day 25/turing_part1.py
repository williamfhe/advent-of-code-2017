from collections import defaultdict

state_actions = {
    'A': { 
        0: { "write": 1, "move": +1, "next": 'B' },
        1: { "write": 0, "move": -1, "next": 'B' }
    },
    'B': { 
        0: { "write": 1, "move": -1, "next": 'C' },
        1: { "write": 0, "move": +1, "next": 'E' }
    },
    'C': { 
        0: { "write": 1, "move": +1, "next": 'E' },
        1: { "write": 0, "move": -1, "next": 'D' }
    },
    'D': { 
        0: { "write": 1, "move": -1, "next": 'A' },
        1: { "write": 1, "move": -1, "next": 'A' }
    },
    'E': { 
        0: { "write": 0, "move": +1, "next": 'A' },
        1: { "write": 0, "move": +1, "next": 'F' }
    },
    'F': { 
        0: { "write": 1, "move": +1, "next": 'E' },
        1: { "write": 1, "move": +1, "next": 'A' }
    }
}

diag_steps = 12861455
tape = defaultdict(int)
cursor_pos = 0
current_state = 'A'

for _ in range(diag_steps):
    action = state_actions[current_state][tape[cursor_pos]]
    tape[cursor_pos] = action["write"]
    cursor_pos += action["move"]
    current_state = action["next"]

print(list(tape.values()).count(1))
