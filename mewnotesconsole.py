import json
import os

DATA_FILE = "notes.json"

CATEGORY_LABELS = {
    "1": "Личное",
    "2": "Работа",
    "3": "Идеи",
    "4": "Важное"
}

def get_category_label(cat):
    return CATEGORY_LABELS.get(cat, f"неизвестная ({cat})")

def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

def add_note(notes):
    title = input("Название заметки: ")
    description = input("Описание: ")
    category = input("Категория (1 - Личное, 2 - Работа, 3 - Идеи, 4 - Важное): ")
    new_note = {
        "title": title,
        "description": description,
        "category": category
    }
    notes.append(new_note)

def view_notes(notes):
    if not notes:
        print("Нет заметок.")
        return
    for number, note in enumerate(notes, start=1):
        print(f"{number}. Название: {note['title']}")
        print(f"   Описание: {note['description']}")
        print(f"   Категория: {get_category_label(note['category'])}")
        print("---")

def edit_note(notes):
    view_notes(notes)
    if not notes:
        return
    try:
        index = int(input("Номер для редактирования: ")) - 1
        if index < 0 or index >= len(notes):
            print("Плохой номер.")
            return
        note = notes[index]
        new_title = input(f"Новое название ({note['title']}): ")
        if new_title:
            note["title"] = new_title
        new_desc = input(f"Новое описание ({note['description']}): ")
        if new_desc:
            note["description"] = new_desc
        new_cat = input(f"Новая категория ({get_category_label(note['category'])}): ")
        if new_cat:
            note["category"] = new_cat
    except ValueError:
        print("Введите корректный номер.")

def delete_note(notes):
    view_notes(notes)
    if not notes:
        return
    try:
        index = int(input("Номер для удаления: ")) - 1
        if 0 <= index < len(notes):
            notes.pop(index)
        else:
            print("Плохой номер.")
    except ValueError:
        print("Введите корректный номер.")

def search_note(notes):
    search = input("Что искать: ")
    found = False
    for number, note in enumerate(notes, start=1):
        if search.lower() in note["title"].lower() or search.lower() in note["description"].lower():
            print(f"{number}. {note['title']}: {note['description']}")
            found = True
    if not found:
        print("Ничего нет.")

# сортировка заметок
def sort_notes_by_category(notes):
    personal = []
    work = []
    ideas = []
    important = []
    other = []
    for note in notes:
        if note["category"] == "1":
            personal.append(note)
        elif note["category"] == "2":
            work.append(note)
        elif note["category"] == "3":
            ideas.append(note)
        elif note["category"] == "4":
            important.append(note)
        else:
            other.append(note)
    sorted_notes = personal + work + ideas + important + other
    for number, note in enumerate(sorted_notes, start=1):
        print(f"{number}. {note['title']} - {get_category_label(note['category'])}")

def main():
    notes = load_notes()
    while True:
        print("\n MewNotes Меню ")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Поиск заметок")
        print("6. Сортировать по категории")
        print("7. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            edit_note(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            search_note(notes)
        elif choice == "6":
            sort_notes_by_category(notes)
        elif choice == "7":
            save_notes(notes)
            print("До встречи в MewNotes")
            break
        else:
            print("Неверный выбор. Попробуйте снова!")

if __name__ == "__main__":
    main()
