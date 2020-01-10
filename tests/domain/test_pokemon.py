from domain.pokemon import Pokemon, Gen


def test_we_gotta_catch_em_all():
    assert Pokemon.do_we_gotta_catch_em_all()


def test_instance_image_path():
    pikachu = Pokemon(25)
    assert isinstance(pikachu.image_path, str)


def test_class_image_path():
    path = Pokemon.get_image_path(25)
    assert isinstance(path, str)


def test_instance_generation():
    pikachu = Pokemon(25)
    assert isinstance(pikachu.generation, Gen)
    assert pikachu.generation == Gen.ONE


def test_class_generation():
    generation = Pokemon.get_generation(278)
    assert isinstance(generation, Gen)
    assert generation == Gen.THREE
