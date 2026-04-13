from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyError
)


def conduct_tournament(name: str,
                       opponents_data: List[Tuple[CreatureFactory,
                                                  BattleStrategy]]) -> None:
    print(name)
    formatted_opponents = [
        f"({f.__class__.__name__.replace('Factory', '')}"
        f"+{s.__class__.__name__.replace('Strategy', '')})"
        for f, s in opponents_data
    ]
    print(f"[ {', '.join(formatted_opponents)} ]")

    print("*** Tournament ***")
    print(f"{len(opponents_data)} opponents involved")

    opponents = [(f.create_base(), s) for f, s in opponents_data]

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            c1, s1 = opponents[i]
            c2, s2 = opponents[j]

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    conduct_tournament("Tournament 0 (basic)", [
        (flame, normal), (heal, defensive)
    ])

    print("")
    conduct_tournament("Tournament 1 (error)", [
        (flame, aggressive), (heal, defensive)
    ])

    print("")
    conduct_tournament("Tournament 2 (multiple)", [
        (aqua, normal), (heal, defensive), (trans, aggressive)
    ])
