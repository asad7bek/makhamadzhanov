from cheast import Item, Cheast
from лабораторная_9.cheast import Cheast

if __name__ == "__main__":
    cheast: Cheast = Cheast("Старый, потрепанный временем ящик.")

    cheast.addd(Item("Меч", 50))
    cheast.add(Item("Зелье", 20))
    cheast.add_item(Item("Золото", 100))

    cheast.show_content()  # Сундук закрыт

    cheast.open_cheast()
    cheast.show_content()

    received_item = cheast.get_item()
    if received_item:
        print(f"Вы получили: {received_item.get_name()}")
    else:
        print("Сундук пуст или закрыт.")

    cheast.показать_содержимое()