from actions import Action, ActionMethod, show_action_list, get_action
from manager import BookManager

FILE_PATH = 'books.json'


def main():
    show_action_list()
    action = get_action()
    with BookManager(FILE_PATH) as manager:

        match action:
            case Action.ALL.value:
                ActionMethod.get_all_books(manager)

            case Action.CREATE.value:
                while True:
                    ActionMethod.create_book(manager)
                    if input("Хотите продолжить? (y/n): ") != 'y':
                        break

            case Action.DELETE.value:
                while True:
                    ActionMethod.delete_book(manager)
                    if input("Хотите продолжить? (y/n): ") != 'y':
                        break

            case Action.UPDATE_STATUS.value:
                while True:
                    ActionMethod.update_status(manager)
                    if input("Хотите продолжить? (y/n): ") != 'y':
                        break

            case Action.SEARCH.value:
                while True:
                    ActionMethod.search_book(manager)
                    if input("Хотите продолжить? (y/n): ") != 'y':
                        break

            case _:
                print("Действие не найдено")
    main()


if __name__ == "__main__":
    main()
