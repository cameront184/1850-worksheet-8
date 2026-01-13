"""
Exercise 3.2: Simulate a Turn-Based Battle (Class-Based)

In this exercise, you will create a Pokemon class and use it to simulate battles.
This demonstrates object-oriented programming principles: encapsulation, methods, and clear responsibilities.
"""

import httpx


class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    """

    def __init__(self, name):
        """
        Initialise a Pokemon by fetching its data from the API and calculating its stats.

        Args:
            name (str): The name of the Pokemon (e.g., "pikachu")
        """
        # TODO: Store the Pokemon's name (lowercase)

        # TODO: Fetch Pokemon data from PokeAPI
        # - Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # - Make GET request
        # - Check response status code (raise error if not 200)
        # - Store the JSON data
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = httpx.get(url)

        if response.status_code != 200:
            print("Pokemon not found")

        data = response.json()

        # TODO: Calculate and store stats
        # - Use _calculate_stat() for attack, defense, speed
        # - Use _calculate_hp() for max HP
        # - Store stats in a dictionary
        # - Set current_hp = max_hp

        base_stats = {
        entry["stat"]["name"]: entry["stats"]
        for entry in data["base_stats"]
        }

        self.stats = {
            "attack": self._calculate_stat(base_stats["attack"]),
            "defense": self._calculate_stat(base_stats["defnse"]),
            "speed" : self._calculate_stat(base_stats["speed"])
        }

        self.max_hp = self._calculate_hp(base_stats["hp"])
        self.current_hp = self.max_hp


        

    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's stat at a given level.
        Helper method (note the underscore prefix).

        Args:
            base_stat (int): The base stat value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated stat
        """
        # TODO: Implement the stat calculation formula
        # Formula: int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)
        
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)
    
    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's HP at a given level.
        HP uses a different formula than other stats.

        Args:
            base_stat (int): The base HP value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated HP
        """
        # TODO: Implement the HP calculation formula
        # Formula: int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

    def attack(self, defender):
        """
        Attack another Pokemon, dealing damage based on stats.

        Args:
            defender (Pokemon): The Pokemon being attacked

        Returns:
            int: The amount of damage dealt
        """
        # TODO: Calculate damage using the damage formula
        # Formula: int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)
        # Where 50 is level and 60 is base_power

        # TODO: Make the defender take damage
        # Call defender.take_damage(damage)

        # TODO: Return the damage amount

        damage = int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)
        
        defender.take_damage(damage)
        return damage


    def take_damage(self, amount):
        """
        Reduce this Pokemon's HP by the damage amount.

        Args:
            amount (int): The damage to take
        """
        # TODO: Reduce current_hp by amount
        # Make sure HP doesn't go below 0
        self.current_hp -= amount
        self.current_hp >= 0

    

    def is_fainted(self):
        """
        Check if this Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, False otherwise
        """
        # TODO: Return True if current_hp <= 0, False otherwise
        if self.current_hp <= 0:
            return True
        else:
            return False


    def __str__(self):
        """
        String representation of the Pokemon for printing.

        Returns:
            str: A nice display of the Pokemon's name and HP
        """
        # TODO: Return a string like "Pikachu (HP: 95/120)"
        return f"{self.name} HP: {self.current_hp/self.max}"


def simulate_battle(pokemon1_name, pokemon2_name):
    """
    Simulate a turn-based battle between two Pokemon.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects
    pokemon1 = pokemon1_name
    pokemon2 = pokemon2_name
    # TODO: Display battle start message
    # Show both Pokemon names and initial HP
    Print("BATTLE STARTING")
    print("pokemon1.name HP: pokemon1.current_hp / pokemon1.max_hp")
    print("pokemon2.name HP: pokemon2.current_hp / pokemon2.max_hp")


    # TODO: Determine who attacks first based on speed
    # The Pokemon with higher speed goes first
    # Hint: Compare pokemon1.stats['speed'] with pokemon2.stats['speed']
    if pokemon1.stats["speed"] >= pokemon2.stats["speed"]:
        attacker=pokemon1
        defender=pokemon2
    print("{attacker.name} strikes first(Speed:,
          attacker.stats["speed"], "vs", defender.stats["speed"], ")")

    # TODO: Battle loop
    # - Keep track of round number
    # - While neither Pokemon is fainted:
    #   - Display round number
    #   - Attacker attacks defender
    #   - Display damage and remaining HP
    #   - Check if defender fainted
    #   - If not, swap attacker and defender
    #   - Increment round number

    # TODO: Display battle result
    # Show which Pokemon won and their remaining HP
    while attacker.is_fainted() == False and defender.is_fainted() == False:
        damage = attacker.attack(defender)
        print(attacker.name.title(), "attacks", defender.name.title(),
              "for", damage, "damage!")
        print(defender.name.title(), "HP:", defender.current_hp, "/", defender.max_hp)

        if defender.is_fainted() == True:
            print(defender.name.title(), "fainted!")
            break
        temp = attacker
        attacker = defender
        defender = temp

        round_number = round_number + 1 
        
    print("\n=== BATTLE END ===")
    print("Winner:", attacker.name.title())
    print("Remaining HP:", attacker.current_hp, "/", attacker.max_hp)

if __name__ == "__main__":
    # Test your battle simulator
    simulate_battle("pikachu", "bulbasaur")

    # Uncomment to test other battles:
    # simulate_battle("charmander", "squirtle")
    # simulate_battle("eevee", "jigglypuff")
