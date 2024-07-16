def part_c(initial_deposit):
    #########################################################################
    cost_of_dream_home = 800000
    portion_down_payment = 0.25
    down_payment = cost_of_dream_home * portion_down_payment
    months = 36
    amount_saved = 0.0
    epsilon = 100  # Acceptable margin of error for savings

    ##################################################################################################
    ## Determine the lowest rate of return needed to get the down payment for your dream home below ##
    ##################################################################################################
    # Bisection search to find the minimum rate of return
    low = 0.0
    high = 1.0
    steps = 0
    r = (high + low) / 2

    # Check if the initial deposit is sufficient without any return
    if initial_deposit >= down_payment - epsilon:
        r = 0.0
    else:
        while low <= high:
            steps += 1
            r = (high + low) / 2
            amount_saved = initial_deposit
            for _ in range(months):
                amount_saved += amount_saved * (r / 12)

            if abs(amount_saved - down_payment) < epsilon:
                break
            elif amount_saved < down_payment:
                low = r
            else:
                high = r

            # To avoid infinite loop, check for convergence
            if high - low < 1e-8:
                break

        # If it is not possible to save the required amount
        if amount_saved < down_payment - epsilon:
            r = None

    print(f"Best savings rate: {r} [or very close to this number]\n")
    print(f"Steps in bisection search: {steps} [or very close to this number]\n")
    return r, steps
