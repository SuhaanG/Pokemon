strengths = {
    "Fire": ["Grass", "Ice"],
    "Water": ["Fire"],
    "Electric": ["Water"],
    "Normal": [],
    "Grass": ["Water"],
    "Ice": ["Grass"]
}
weaknesses = {
    "Normal": [],
    "Fire": ["Fire", "Water"],
    "Water": ["Water", "Grass"],
    "Electric": ["Electric", "Grass"],
    "Grass": ["Fire", "Grass"],
    "Ice": ["Fire", "Water", "Ice"]
}
class Pokemon:
    def __init__(self, name, health, pokemon_type, moves):
        self.name = name
        self.health = health
        self.pokemon_type = pokemon_type
        self.moves = {move: [data[0], data[1], 5] for move, data in moves.items()}  # Add a counter (5 uses)

    def attack(self, other_pokemon, move):
        if self.moves[move][2] <= 0:  # Check if the move has uses left
            print(f"{self.name} tried to use {move}, but it has no uses left!")
            return
        new_damage = self.multiplier(other_pokemon, move)
        other_pokemon.health = other_pokemon.health - new_damage
        self.moves[move][2] -= 1  # Decrement the move's counter
        print(f"{self.name} attacked {other_pokemon.name} using {move} which deals {new_damage} damage.")
        print(f"{move} has {self.moves[move][2]} uses left.")
        
        if other_pokemon.health > 0:
            print(f"{other_pokemon.name} has {other_pokemon.health} health left.")
        else:
            print(f"{other_pokemon.name} is dead, {self.name} wins!")

    def multiplier(self, other_pokemon, move):
        move_type = self.moves[move][1]
        other_pokemon_type = other_pokemon.pokemon_type
        if other_pokemon_type in strengths[move_type]:
            new_damage = self.moves[move][0] * 2
        elif other_pokemon_type in weaknesses[move_type]:
            new_damage = self.moves[move][0] / 2
        else:
            new_damage = self.moves[move][0]
        return new_damage


# Pokémon Initialization
pikachu = Pokemon(
    "Pikachu",              
    100,                    
    "Electric",             
    {                       
        "Thunderbolt": [30, "Electric"],
        "Quick Attack": [15, "Normal"]
    }
)

squirtle = Pokemon(
    "Squirtle",
    200,
    "Water",
    {
        "Water Gun": [20, "Water"],
        "Tackle": [10, "Normal"],
    }
)

Tankaroo = Pokemon(
    "Tankaroo",
    150,
    "Normal",
    {
        "Mega Slam": [40, "Normal"],
        "Hyper Punch": [50, "Normal"],
    }
)

Inferon = Pokemon(
    "Inferon",
    150,
    "Fire",
    {
        "Flame Burst": [40, "Fire"],
        "Inferno Blitz": [60, "Fire"],
    }
)

Verdantusk = Pokemon(
    "Verdantusk",
    150,
    "Grass",
    {
        "Leaf Storm": [45, "Grass"],
        "Nature's Fury": [55, "Grass"],
    }
)

Glacimaw = Pokemon(
    "Glacimaw",
    150,
    "Ice",
    {
        "Frost Fang": [40, "Ice"],
        "Arctic Wave": [60, "Ice"],
    }
)

# Example Attack
pikachu.attack(squirtle, "Thunderbolt")
pikachu.attack(squirtle, "Thunderbolt")
pikachu.attack(squirtle, "Thunderbolt")
pikachu.attack(squirtle, "Thunderbolt")
pikachu.attack(squirtle, "Thunderbolt")
pikachu.attack(squirtle, "Thunderbolt")  # Should print that Thunderbolt has no uses left