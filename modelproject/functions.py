

def price(q1, q2, a, b): #Overall inverse demand function as a function of all quantities and the relevant parameters
    price = a-b*(q1+q2)
    return price

def cost(q, c): #A cost function for a given firm
    cost = q*c
    return cost

def profit(q1, q2, a, b, c): #Profit for a given firm with production q1 and costs c
    profit = price(q1, q2, a, b)*q1-cost(q1, c)
    return profit


def best_response(q2, c1, a, b): #best response for firm 1 - found by maximising profits taking q2 as given
    from scipy import optimize
    q1 =  optimize.fminbound(lambda x: -profit(x, q2, a, b, c1), # minimizing minus profits
                             0, #lower bound is zero
                             a, #upper bound is a (should maybe include a-b*x ?)
                             full_output=True,
                            disp=True)
    return q1[0]

def best_reponse_plot(a, b, c1): #plots the best response function
    from scipy import optimize, arange
    import matplotlib.pyplot as plt
    
    range_q2 = arange(0, a, 0.01)
    range_q1 = [best_response(q2, c1, a, b) for q2 in range_q2]
    
    plt.plot(range_q1, range_q2)
    plt.xlabel("best response q1")
    plt.ylabel('q2')
    plt.title("Firm 1's best response to firm 2")


def help_br(q, c, a, b): #defining a help function that finds where the Best response functions - q are equal to 0 (i.e. fixed points)
    return [q[0]-best_response(q[1], c[0], a, b),q[1]-best_response(q[0], c[1], a, b)]


def production_eq(c, initial_guess, a, b): #Equilibrium function 
    from scipy import optimize
    Q = optimize.fsolve(lambda q: help_br(q, c, a, b), initial_guess)
    return Q


def summary(c, a, b, initial_guess):
    q1,q2 = production_eq(c, initial_guess, a, b) #Equilibrium productions   
     
    output = print('\n Industry output is ' + str("{:.0f}".format(q1+q2)) + ' with firm 1 producing ' + str("{:.0f}".format(q1)) + ' units and firm 2 producing ' +
                   str("{:.0f}".format(q2)) + ' units.' + 
                   '\n The equilibrium price per unit becomes ' + str("{:.0f}".format(price(q1, q2, a, b))) +
                  "\n Firm 1's profit will be " + str("{:.0f}".format(profit(q1, q2, a, b, c[0]))) + " while firm 2's profit will be " + str("{:.0f}".format(profit(q1, q2, a, b, c[1]))))
    return output