# ------------------------------------------------------
# Alpha–Beta Search WITH TRACE OUTPUT
# ------------------------------------------------------

def alpha_beta_search(state, actions, result, terminal_test, utility):

    def max_value(state, alpha, beta, depth):
        print("  " * depth + f"MAX at {state}, α={alpha}, β={beta}")

        if terminal_test(state):
            u = utility(state)
            print("  " * depth + f"Terminal → utility {u}")
            return u

        v = float('-inf')
        for a in actions(state):
            print("  " * depth + f"MAX considers action {a}")
            v = max(v, min_value(result(state, a), alpha, beta, depth+1))
            print("  " * depth + f"MAX updated v={v}")
            if v >= beta:
                print("  " * depth + f"MAX cutoff (v={v} ≥ β={beta})")
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        print("  " * depth + f"MIN at {state}, α={alpha}, β={beta}")

        if terminal_test(state):
            u = utility(state)
            print("  " * depth + f"Terminal → utility {u}")
            return u

        v = float('inf')
        for a in actions(state):
            print("  " * depth + f"MIN considers action {a}")
            v = min(v, max_value(result(state, a), alpha, beta, depth+1))
            print("  " * depth + f"MIN updated v={v}")
            if v <= alpha:
                print("  " * depth + f"MIN cutoff (v={v} ≤ α={alpha})")
                return v
            beta = min(beta, v)
        return v

    # Top-level decision
    alpha, beta = float('-inf'), float('inf')
    best_score = float('-inf')
    best_action = None

    print("ROOT MAX NODE")
    for a in actions(state):
        print(f"ROOT considering action {a}")
        v = min_value(result(state, a), alpha, beta, 1)
        print(f"ROOT result for action {a}: {v}")
        if v > best_score:
            best_score, best_action = v, a
        alpha = max(alpha, best_score)

    print(f"\nBest move = {best_action} with value {best_score}")
    return best_action


# ------------------------------------------------------
# SAME SAMPLE GAME AS BEFORE
# ------------------------------------------------------

initial_state = (5, 0)

def actions(state):
    return [+1, -1]

def result(state, action):
    value, depth = state
    return (value + action, depth + 1)

def terminal_test(state):
    return state[1] >= 2

def utility(state):
    value, depth = state
    return value


# ------------------------------------------------------
# RUN SAMPLE
# ------------------------------------------------------

alpha_beta_search(initial_state, actions, result, terminal_test, utility)
