import random
CHOICES = ['b','c']
global f1
f1 = random.choice(CHOICES)

team_name = 'Checkmate' # Only 10 chars displayed.
strategy_name = 'RNJesus take the wheel'
strategy_description = 'Completely randomly'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
   
    return f1

def test_move(my_history, their_history, my_score, their_score, result):
    
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
    if test_move(my_history='',
              their_history='', 
              my_score = 0,
              their_score = 0,
              result= f1):
         print 'Test passed'
   
    test_move(my_history='bbb',
              their_history='ccc', 
              my_score=0, 
              their_score=0,
              result= f1) 
