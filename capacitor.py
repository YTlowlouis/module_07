from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    for label, creature in [("base", factory.create_base()),
                            ("evolved", factory.create_evolved())]:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        print(creature.heal())


def test_transform() -> None:
    print("\nTesting Creature with transform capability")
    factory = TransformCreatureFactory()

    for label, creature in [("base", factory.create_base()),
                            ("evolved", factory.create_evolved())]:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


if __name__ == "__main__":
    test_healing()
    test_transform()
