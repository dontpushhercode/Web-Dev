from classes import MagicEntity, Fairy, Witch

def main():
    fairy = Fairy("Tinkerbell", 10, 100, 5)
    witch = Witch("Yennefer", 15, 120, 10)
    magicEntity = MagicEntity("Generic Entity", 5, 80)

    magical = [magicEntity, fairy, witch]

    for entity in magical:
        print(entity)
        entity.speak()
        print()

if __name__ == "__main__":
    main()