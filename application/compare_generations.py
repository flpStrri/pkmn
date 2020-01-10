from domain.pokemon import Pokemon
from service.pkmn_image_manager import PkmnImageManager


def calculate_gen_one():
    pokemons = [Pokemon(i) for i in range(151)]
    paths = [pokemon.image_path for pokemon in pokemons]
    pkmn_colors = [PkmnImageManager.get_colors_from_path(path) for path in paths]
    for pokemon in pokemons:
        print("Pokemon: " + str(pokemon.name))
        print("Colors: ")
        print(pkmn_colors[pokemon.number])
