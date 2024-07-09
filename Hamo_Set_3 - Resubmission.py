'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''
#1 - Relationship Status
social_graph = {
        "@bongolpoc":{"first_name":"Joselito",
                      "last_name":"Olpoc",
                      "following":[
                      ]
        },
        "@joaquin":  {"first_name":"Joaquin",
                      "last_name":"Gonzales",
                      "following":[
                      "@chums","@jobenilagan"
                      ]
        },
        "@chums" : {"first_name":"Matthew",
                    "last_name":"Uy",
                    "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                    ]
        },
        "@jobenilagan":{"first_name":"Joben",
                       "last_name":"Ilagan",
                       "following":[
                        "@eeebeee","@joeilagan","@chums","@joaquin"
                       ]
        },
        "@joeilagan":{"first_name":"Joe",
                      "last_name":"Ilagan",
                      "following":[
                        "@eeebeee","@jobenilagan","@chums"
                      ]
        },
        "@eeebeee":  {"first_name":"Elizabeth",
                      "last_name":"Ilagan",
                      "following":[
                        "@jobenilagan","@joeilagan"
                      ]
        },
    }

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    to_member = str(to_member)
    from_member = str(from_member)
    relationship_update = ""
    
    if to_member in social_graph[from_member]["following"]:
        if from_member not in social_graph[to_member]["following"]:
            relationship_update += "follower"
            
    if to_member not in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            relationship_update += "followed by"
            
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            relationship_update += "friends"
        
    if to_member not in social_graph[from_member]["following"]:
        if from_member not in social_graph[to_member]["following"]:
            relationship_update += "no relationship"

    return str(relationship_update)
    
relationship_status("@bongolpoc","@joeilagan",social_graph)

#2 - tic tac toe
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # How do you win in tic_tac_toe

    # because this is a square board, we can assume that the number of "elements" in one row = number of columns for the board
    col_no = len(board)

    # way 1 of winning tic_tac_toe --> all elements in a row match (strikethrough in a straight horizontal line)
    for row in board:
        symbol = row[0]
        if all(square_grid == symbol for square_grid in row) and row[0] != '':
            return symbol

    # way 2 of winning tic_tac_toe --> all elements in a column match (strikethrough in a straight vertical line)
    for col in range(col_no):
        if all(board[row][col] == board[0][col] for row in range(col_no)) and board[0][col] != '':
            return board[0][col]
    
    # way 3 of winning tic_tac_toe --> all elements in a diagonal line match
    if all(board[i][i] == board[0][0] for i in range(col_no)) and board[0][0] != '':
        return board[0][0]
    
    # checking for the anti diagonal (horizontally flipping the diagonal we checked b4)
    if all(board[i][col_no-1-i] == board[0][col_no-1] for i in range(col_no)) and board[0][col_no-1] != '':
        return board[0][col_no-1]

    else: 
        return "NO WINNER"

tic_tac_toe(board1)

#3 bus ETA (this was really hard :<<< )
legs1 = {
    # is this counted as 1 key?
    ("upd","admu"):{
    "travel_time_mins":10
    },
    ("admu","dlsu"):{
    "travel_time_mins":35
    },
    ("dlsu","upd"):{
    "travel_time_mins":55
    }
}

legs2 = {
    ('a1', 'a2'): {
    'travel_time_mins': 10
    },
    ('a2', 'b1'): {
    'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
    'travel_time_mins': 1
    }
}


def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # the stop that the shuttle will leave
    first_stop = str(first_stop)
    # the stop that the shuttle will arrive at
    second_stop = str(second_stop)
    # the data describing the routes
    route_map = route_map

    # scenario 1: person follows the prescribed, existing travel routes in the given route maps (default, basic scenario)
    if (first_stop,second_stop) in route_map.keys():
        travel_time = route_map[(first_stop,second_stop)]["travel_time_mins"]
        return travel_time

    # scenario 2: the inputted first_stop, second_stop refers to the same location --> no travel time
    if first_stop == second_stop:
        travel_time = 0
        return travel_time

    # scenario 3: "disjointed" stops: first_stop and second_stop is NOT in the route_map --> have to find accumulated travel time. 
    if (first_stop,second_stop) not in route_map.keys():
        current_stop = first_stop
        accumulated_travel_time = 0
        while True:
            for tuple, data in route_map.items():
                start, end = tuple
                
                # If the current stop is the start of this leg
                if current_stop == start:
                    accumulated_travel_time += data["travel_time_mins"]
                    current_stop = end
                
                    # Check if we've reached the second_stop
                    if current_stop == second_stop:
                        return accumulated_travel_time
    
eta("upd", "dlsu",legs1)