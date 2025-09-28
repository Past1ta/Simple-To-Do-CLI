import json
import os
from colorama import init, Fore, Style

# Инициализация colorama (обязательно для Windows)
init(autoreset=True)

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def show_tasks(tasks):
    if not tasks:
        print(f"\n{Fore.GREEN}Список задач пуст. 🎉{Style.RESET_ALL}")
        return
    print(f"\n{Fore.CYAN}Ваши задачи:{Style.RESET_ALL}")
    for i, task in enumerate(tasks, 1):
        status = f"{Fore.GREEN}✅{Style.RESET_ALL}" if task["done"] else f"{Fore.RED}❌{Style.RESET_ALL}"
        title = task['title']
        if task["done"]:
            title = f"{Fore.GREEN}{title}{Style.RESET_ALL}"
        else:
            title = f"{Fore.YELLOW}{title}{Style.RESET_ALL}"
        print(f"{Fore.WHITE}{i}.{Style.RESET_ALL} {status} {title}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    print(f"\n{Fore.GREEN}Задача '{title}' добавлена! ✅{Style.RESET_ALL}")

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"\n{Fore.GREEN}Задача '{tasks[index]['title']}' отмечена как выполненная! ✅{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}Неверный номер задачи! ❌{Style.RESET_ALL}")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"\n{Fore.MAGENTA}Задача '{removed['title']}' удалена! 🗑️{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}Неверный номер задачи! ❌{Style.RESET_ALL}")

def main():
    tasks = load_tasks()
    while True:
        print(f"\n{Fore.BLUE}{'='*40}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}📝  Менеджер задач{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'='*40}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}1.{Style.RESET_ALL} Показать задачи")
        print(f"{Fore.WHITE}2.{Style.RESET_ALL} Добавить задачу")
        print(f"{Fore.WHITE}3.{Style.RESET_ALL} Отметить задачу как выполненную")
        print(f"{Fore.WHITE}4.{Style.RESET_ALL} Удалить задачу")
        print(f"{Fore.WHITE}5.{Style.RESET_ALL} Выйти")
        choice = input(f"\n{Fore.CYAN}Выберите действие (1-5): {Style.RESET_ALL}").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input(f"{Fore.CYAN}Введите название задачи: {Style.RESET_ALL}").strip()
            if title:
                add_task(tasks, title)
                save_tasks(tasks)
            else:
                print(f"{Fore.RED}Название не может быть пустым!{Style.RESET_ALL}")
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    idx = int(input(f"{Fore.CYAN}Введите номер задачи для завершения: {Style.RESET_ALL}")) - 1
                    complete_task(tasks, idx)
                    save_tasks(tasks)
                except ValueError:
                    print(f"{Fore.RED}Пожалуйста, введите число.{Style.RESET_ALL}")
        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                try:
                    idx = int(input(f"{Fore.CYAN}Введите номер задачи для удаления: {Style.RESET_ALL}")) - 1
                    delete_task(tasks, idx)
                    save_tasks(tasks)
                except ValueError:
                    print(f"{Fore.RED}Пожалуйста, введите число.{Style.RESET_ALL}")
        elif choice == "5":
            print(f"\n{Fore.CYAN}До свидания! 👋{Style.RESET_ALL}")
            break
        else:
            print(f"\n{Fore.RED}Неверный выбор. Попробуйте снова.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()