from domain.pokemon import Pokemon
from service.pkmn_image_manager import PkmnImageManager


def calculate_gen_one():
    pokemons = [Pokemon(i) for i in range(1, 151)]
    pkmn_color_complexities = []
    for i, pokemon in enumerate(pokemons):
        print(i, pokemon.name)
        pkmn_color_complexities.append(PkmnImageManager.get_complexity_from_path(pokemon.image_path, 8))
    for pokemon in pokemons:
        print(f"Pokemon: {pokemon.name}")
        print(f"Color complexity: {pkmn_color_complexities[pokemon.number - 1]}")
    return pkmn_color_complexities


if __name__ == "__main__":
    calculate_gen_one()
