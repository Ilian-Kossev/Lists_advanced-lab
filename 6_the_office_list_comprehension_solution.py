employee_happiness_list = input().split()
happiness_factor = int(input())
happiness_factor_adjusted_happiness_list = [int(el) * happiness_factor for el in employee_happiness_list]
average_happiness_value = sum(happiness_factor_adjusted_happiness_list) / len(happiness_factor_adjusted_happiness_list)
final_list = [el for el in happiness_factor_adjusted_happiness_list if el >= average_happiness_value]
if len(final_list) >= len(employee_happiness_list) / 2:
    print(f"Score: {len(final_list)}/{len(employee_happiness_list)}. Employees are happy!")
else:
    print(f"Score: {len(final_list)}/{len(employee_happiness_list)}. Employees are not happy!")
