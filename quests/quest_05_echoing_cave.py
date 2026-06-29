# This variable stores the player's starting health.
player_health = 100

# The player is attacked by a monster, so 25 health points are lost.
player_health -= 25

# The player drinks a health potion, restoring 10 health points.
player_health += 10

# Display the player's final health after the attack and healing.
print(f"The player's final health is {player_health}.")