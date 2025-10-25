def total_salary(path):

    total_sum = 0
    developer_count = 0
    
    try:
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    
                    name, salary_str = line.strip().split(',')
                    salary = int(salary_str)
                    
                   
                    total_sum += salary
                    developer_count += 1
                except (ValueError, IndexError):
                  
                    print(f"Попередження: Некоректний формат рядка, пропускаємо: '{line.strip()}'")

    except FileNotFoundError:

        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    
   
    if developer_count == 0:
        return (0, 0)
    
    average_salary = total_sum / developer_count
    
    return (total_sum, int(average_salary))

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
