from game.logic.game_logic import GameLogic, GameMode
from game.logic.district import District, DISTRICT_DEFAULT, TRIBUTES_DEFAULT
from game.logic.tribute import LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT, COWARDICE_DEFAULT


def init_simulation(rows, columns, game):
    game.new_game(rows, columns)
    # Set by default every stat.
    district = District()
    life, force, alliance, cowardice = LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT, COWARDICE_DEFAULT
    cant_tributes = TRIBUTES_DEFAULT
    print_board(rows, columns, DISTRICT_DEFAULT)
    yes, points = 'y', 10
    while yes == 'y':
        print_stats(points)
        try:
            choice = int(input("¿Where do you want to spend your points? Choose a number (1 - 5): "))
            # Choice 1 Life
            if choice == 1:
                points, life = stat_points_life_force(points, "Life", life, 5)
            # Choice 2 Force
            elif choice == 2:
                points, force = stat_points_life_force(points, "Force", force, 2)
            # Choice 3 Alliance
            elif choice == 3:
                points, alliance = stat_points_alli_cowardice(points, "Alliance", alliance, 10, 7)
            # Choice 4 Tributes
            elif choice == 4:
                points, cant_tributes = stat_points_tributes(points, cant_tributes)
            # Choice 5 Cowardice            
            elif choice == 5:
                points, cowardice = stat_points_alli_cowardice(points, "Cowardice", cowardice, 5, 5)
            else:
                print("Invalid input. Please enter a valid number (1 - 5).")

        except ValueError:
            print("Invalid input. Please enter a valid number (1 - 5).")
        # If you spent all points then it asks if you want to reconfigure the district
        if points <= 0:
            print("\nYou have spent all your points.")
            print("The stats of your district are: \nLife:", life, "\nForce:", force, "\nAlliance:", alliance,
                    "\nTributes:", cant_tributes, "\nCowardice:", cowardice)
            yes = input("Do you want to redistribute the points (y / n)?: ").strip().lower()
            while yes not in ('y', 'n'):
                yes = input("Invalid input. Enter (y / n): ").strip().lower()

            # Choice y, then sets all stats like in beginning
            if yes == 'y':
                life, force, alliance, cowardice = LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT, COWARDICE_DEFAULT
                # Remove tributes
                for tribute in district.tributes:
                    district.remove_tribute(tribute)
                cant_tributes, points = TRIBUTES_DEFAULT, 10

    if rows * columns < cant_tributes + 20:
        print("You must creat a board more bigger.")
        return
    # Configure own district
    district.set_config(life, force, alliance, DISTRICT_DEFAULT, cant_tributes, cowardice)
    game.districts.append(district)
    # Configure others districts
    game.configure_random_districts()
    # Distribute potions and weapons
    game.distribute_items()
    # Distribute tributes
    game.distribute_district_tributes()
    # Distribute neutrals
    game.distribute_neutral_tributes(10)

    game.mode = GameMode.SIMULATION
    print(game.to_string())
    game.heuristic_of_game()
        
# Calculate life and force with spending points.        
def stat_points_life_force(points, stat_string, stat, mult):
    while True:
        stat_point = int(input(f"How many points do you want to spend on {stat_string}?: "))
        if 1 <= stat_point <= points:
            stat += (mult * stat_point)
            points -= stat_point
            print(f"{stat_string} increased to:", stat)
            return points, stat # return update points and stat
        else:
            print("Invalid input. You have", points, "points.")

# Calculate alliance and cowardice with spending points.
def stat_points_alli_cowardice(points, stat_string, stat, stat_limit, point_limit):
    while True:
        if stat == stat_limit: #stat_limit can be 5(cowardice) or 10(alliance)
            print(f"{stat_string} is at {stat_limit}. You can't spend more points on it.")
            return points, stat
        stat_points = int(input(f"How many points do you want to spend on {stat_string}?: "))
        if 1 <= stat_points <= points and stat_points <= point_limit: #point_limit can be 5(cowardice) or 7(alliance)
            stat += stat_points
            points -= stat_points
            print(f"{stat_string} increased by:", stat)
            return points, stat
        elif point_limit < stat_points <= 10:
            print(f"The limit for spending points on {stat_string} is {point_limit}.")
            return points, stat
        else:
            print("Invalid input. You have", points, "points.")

# Calculate tributes of own district with spending points.
def stat_points_tributes(points, cant_tributes):
    while True:
        tributes_points = int(
            input("How many points do you want to spend on Tributes? Each tribute costs 4 points: "))
        if tributes_points in (4, 8):
            required_points = tributes_points
            num_tributes = tributes_points // 4 # divide tributes_points in four
            if points >= required_points:
                cant_tributes += num_tributes
                points -= required_points
                print("The number of tributes increased to:", cant_tributes)
                return points, cant_tributes
            else:
                print("You don't have enough points for this operation. You have", points, "points.")
                return points, cant_tributes
        else:
            print("Invalid input. You should enter 4 or 8 points to spend on Tributes.")

# Print all stats of tributes.
def print_stats(points):
    print(
        f"\nYou have {points} points available to distribute on:\n"
        "1. Life\n"
        "2. Force\n"
        "3. Alliance\n"
        "4. Tributes\n"
        "5. Cowardice"
    )

# Print size of board and own district.
def print_board(rows, columns, own_district):
    print(f"Board is {rows} x {columns}.")
    print("\nBy default, your number of district is", own_district)

if __name__ == '__main__':
    game = GameLogic()
    init_simulation(25, 25, game)