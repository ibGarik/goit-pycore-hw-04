import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_directory_structure(path: Path, indent: str = ""):

    for item in sorted(path.iterdir()):
        
        if item.name.lower() == "venv":
            continue

        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            print_directory_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")


def main():

    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: потрібно вказати шлях до директорії!{Style.RESET_ALL}")
        print("Приклад використання:")
        print(r"    python hw03.py i:\GoIT\Projects\vscode-basics\goit-pycore-hw-04\module6\visual")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    
    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: вказаний шлях не існує!{Style.RESET_ALL}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: це не директорія!{Style.RESET_ALL}")
        sys.exit(1)

    
    print(f"{Fore.CYAN}Структура директорії: {dir_path.resolve()}{Style.RESET_ALL}\n")

    
    print_directory_structure(dir_path)


if __name__ == "__main__":
    main()
