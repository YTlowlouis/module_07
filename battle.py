from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("\nTesting factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    for c in [base, evolved]:
        print(c.describe())
        print(c.attack())


def test_battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("\nTesting battle")
    c1 = f1.create_base()
    c2 = f2.create_base()

    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    try:
        flame_fact = FlameFactory()
        aqua_fact = AquaFactory()

        test_factory(flame_fact)
        test_factory(aqua_fact)
        test_battle(flame_fact, aqua_fact)
    except Exception as e:
        print(f"An error occurred: {e}")
