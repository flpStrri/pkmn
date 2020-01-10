from domain.pokemon import Pokemon
from service.pkmn_image_manager import PkmnImageManager


def calculate_gen_one():
    pokemons = [Pokemon(i) for i in range(1, 151)]
    paths = [pokemon.image_path for pokemon in pokemons]
    pkmn_color_complexities = [PkmnImageManager.get_complexity_from_path(path) for path in paths]
    for pokemon in pokemons:
        print(f"Pokemon: {pokemon.name}")
        print(f"Color complexity: {pkmn_color_complexities[pokemon.number - 1]}")


if __name__ == "__main__":
    calculate_gen_one()
