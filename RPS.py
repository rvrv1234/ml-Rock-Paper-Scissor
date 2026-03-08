def player(prev_play, opponent_history=[], play_order={}):
    # Reset state for a new match 
    if not prev_play:
        prev_play = 'R'
        opponent_history.clear()
        play_order.clear()

    # Track what the opponent just played
    opponent_history.append(prev_play)
    
    # Default prediction if it is early in the match
    prediction = 'S'

    # Wait until have a 5-move history to start pattern matching
    if len(opponent_history) >= 5:
        # Grab the exact sequence of their last 5 moves
        last_five = "".join(opponent_history[-5:])
        
        # Log this 5-move sequence in our dictionary
        play_order[last_five] = play_order.get(last_five, 0) + 1

        # Look at the last 4 moves to guess the upcoming 5th move
        last_four = "".join(opponent_history[-4:])
        
        # Create a list of the 3 possible ways this sequence could end
        potential_plays = [
            last_four + "R",
            last_four + "P",
            last_four + "S",
        ]

        # Filter history to see which of these 3 endings actually happens the most
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        # If we have seen this pattern before, predict the most common ending
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    #  Play the exact counter to our prediction
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]