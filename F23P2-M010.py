import random


# Get random number for a normal distribution with
# mean of H1 and standard deviation of D1.


def exploitOnly() -> float:
    means = [7, 4, 10, 5]  # holds average happiness values for each of the four cafeterais
    deviations = [3, 10, 6, 2]  # holds standard deviation values  for corresponding cafeterias
    total_happiness = 0  # keeps track of cumulative happiness values

    for i in range(4):  # iterates over lists four times through each cafeteria
        happiness = random.normalvariate(means[i], deviations[
            i])  # generates random happiness value for current cafeteria, i. Samples from normal distribution with mean and standard deviation corresponding to current index.
        total_happiness += happiness  # adds happiness value obtained in current iteration to total happiness

    best_cafeteria = means.index(
        max(means))  # after visiting each cafeteria once, finds caf w highest average happiness and assigns its index in means list to best_cafeteria

    for _ in range(196):  # runs for remaining 196 days
        happiness = random.normalvariate(means[best_cafeteria], deviations[
            best_cafeteria])  # generates random happiness value based on best cafeteria
        total_happiness += happiness  # adds happiness value from current day to total_happiness
    return total_happiness  # sum of happiness obtained over 200 day simulation


total_happiness = exploitOnly()  # assigns returned total happiness value to variable and calls function
print(total_happiness)


def exploreOnly() -> float:
    means = [7, 4, 10, 5]  # holds average happiness values for each of the four cafeterais
    deviations = [3, 10, 6, 2]  # holds standard deviation values  for corresponding cafeterias
    total_happiness = 0  # keeps track of cumulative happiness values

    for i in range(4):
        for _ in range(50):
            happiness = random.normalvariate(means[i], deviations[i])
            total_happiness += happiness

    return total_happiness


total_happiness = exploreOnly()
print(total_happiness)


def eGreedy(e=10) -> float:  # optional by assigning a value to it

    means = [7, 4, 10, 5]  # holds average happiness values for each of the four cafeterais
    deviations = [3, 10, 6, 2]  # holds standard deviation values  for corresponding cafeterias
    total_happiness = 0  # keeps track of cumulative happiness values

    # Initialize counters to keep track of how many times each cafeteria was visited
    cafeteria_counts = [0, 0, 0, 0]
    cafeteria_happiness = [0, 0, 0, 0]

    for i in range(4):
        for _ in range(4):
            # Visit each cafeteria once to initialize data
            happiness = random.normalvariate(means[i], deviations[i])
            cafeteria_counts[i] += 1
            cafeteria_happiness[i] += happiness

    for _ in range(196):
        r = random.random()
        if r < (e / 100):
            # choose random cafeteria
            current_cafeteria = random.randint(0, 3)
        else:
            # choose best cafeteria based on average happiness
            current_cafeteria = cafeteria_happiness.index(max(cafeteria_happiness))

        # generate happiness value based on chosen cafeteria
        happiness = random.normalvariate(means[current_cafeteria], deviations[current_cafeteria])

        # Update data for chosen cafeteria
        cafeteria_counts[current_cafeteria] += 1
        cafeteria_happiness[current_cafeteria] += happiness

        total_happiness += happiness

    return total_happiness


total_happiness = eGreedy()
print("Total Happiness for 200 Days:", total_happiness)


def simulation(t: int, e=10):
    opH = 0
    total_happiness_exploit = 0
    total_happiness_explore = 0
    total_happiness_egreedy = 0

    total_regret_exploit = 0
    total_regret_explore = 0
    total_regret_egreedy = 0

    for _ in range(t):
        # Run each strategy for one trial
        happiness_exploit = exploitOnly()
        happiness_explore = exploreOnly()
        happiness_egreedy = eGreedy(e)

        total_happiness_exploit += exploitOnly()
        total_happiness_explore += exploreOnly()
        total_happiness_egreedy += eGreedy(e)

        # Calculate optimal happiness
        opH = max(happiness_exploit, happiness_explore, happiness_egreedy)

        # Calculate regret for strategy
        total_regret_exploit += opH - happiness_exploit
        total_regret_explore += opH - happiness_explore
        total_regret_egreedy += opH - happiness_egreedy

    # Calculate average happiness
    avg_happiness_exploit = total_happiness_exploit / t
    avg_happiness_explore = total_happiness_explore / t
    avg_happiness_egreedy = total_happiness_egreedy / t

    # Calculate average regret for strategy
    avg_regret_exploit = total_regret_exploit / t
    avg_regret_explore = total_regret_explore / t
    avg_regret_egreedy = total_regret_egreedy / t

    print(f"Optimal Happiness: {opH}\n")

    print("Explore Only:")
    print(f"Expected Happiness: {avg_happiness_explore}")
    print(f"Expected Regret: {avg_regret_explore}")
    print(f"Simulated Happiness: {total_happiness_explore}")
    print(f"Simulated Regret: {total_regret_explore}")
    print()

    print("Exploit Only:")
    print(f"Expected Happiness: {avg_happiness_exploit}")
    print(f"Expected Regret: {avg_regret_exploit}")
    print(f"Simulated Happiness: {total_happiness_exploit}")
    print(f"Simulated Regret: {total_regret_exploit}")
    print()

    print("eGreedy:")
    print(f"Expected Happiness: {avg_happiness_egreedy}")
    print(f"Expected Regret: {avg_regret_egreedy}")
    print(f"Simulated Happiness: {total_happiness_egreedy}")
    print(f"Simulated Regret: {total_regret_egreedy}")
    print()

simulation(200)
