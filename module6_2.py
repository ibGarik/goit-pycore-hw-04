def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    parts = line.strip().split(',')
                    cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
                    cats_list.append(cat_info)  
                except Exception:
                    continue
    except FileNotFoundError:
        print(f"Error: File at path '{path}' not found.")
        return []
    return cats_list

cats_info = get_cats_info("cats_file.txt")
print(cats_info)