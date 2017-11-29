# Tuples
# an immutable (unchangeable) sequence of Python objects.

t1 = ('a','b','c')
t2 = (1, 2, 3)

set_of_tuples = set()

set_of_tuples.add(t1)
set_of_tuples.add(t2)

print(set_of_tuples)

# error with list (not working)
L1 = ['a','b','c']
L2 = [1, 2, 3]

set_of_lists = set()

set_of_lists.add(L1)
set_of_lists.add(L2)

print(set_of_lists)
=================================
# namedtuple
from collections import namedtuple
# here we define Point as a new type of thing.
# It has properties x and y.
Point = namedtuple("Point", ["x", "y"])

# here we actually instantiate a point
p1 = Point(5, -3)

print(p1) # Point(x=5, y=-3)
=================================
# Counter
from collections import Counter

string = "the quick brown fox jumped over the lazy dog"

character_counter = Counter()
for character in string:
    character_counter[character] += 1

character_counter.most_common()

==================================
# defaultdict
TICKET_BOXES = {
    "low"    : [],
    "medium" : [],
    "high"   : []
}

unfiled_tickets = [
    {
        "priority"    : "high",
        "description" : "slammed on brakes"
    },
    {
        "priority"    : "low",
        "description" : "windshield chipped"
    },
    {
        "priority"    : "low",
        "description" : "failed to use turn signal"
    }
    ,
    {
        "priority"    : "medium",
        "description" : "did not come to complete stop at stop sign"
    }
]

new_ticket = {
    "priority" : "highest",
    "description": "vehicle crashed!"
}


def file_ticket(ticket):
    priority = ticket['priority']
    TICKET_BOXES[priority].append(ticket)

for ticket in unfiled_tickets:
    file_ticket(ticket)

print(TICKET_BOXES)

# new function with priority highest
def file_ticket_fixed(ticket):
    priority = ticket['priority']

    if priority not in TICKET_BOXES:
        TICKET_BOXES[priority] = []

    TICKET_BOXES[priority].append(ticket)

file_ticket_fixed(new_ticket)
print(TICKET_BOXES)

# OR we can use a "defaultdict"
from collections import defaultdict

TICKET_BOXES = defaultdict(list)

def file_ticket(ticket):
    priority = ticket['priority']
    TICKET_BOXES[priority].append(ticket)

for ticket in unfiled_tickets:
    file_ticket(ticket)

file_ticket(new_ticket)

print(TICKET_BOXES)
