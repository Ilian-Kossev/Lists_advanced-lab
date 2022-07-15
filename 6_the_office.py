employee_happiness_list = input().split()
happiness_factor = int(input())
happiness_factor_adjusted_happiness_list = list(map(lambda x: int(x) * happiness_factor, employee_happiness_list))
average_happiness_value = sum(happiness_factor_adjusted_happiness_list) / len(happiness_factor_adjusted_happiness_list)
final_list = list(filter(lambda x: x >= average_happiness_value, happiness_factor_adjusted_happiness_list))
if len(final_list) >= len(employee_happiness_list) / 2:
    print(f"Score: {len(final_list)}/{len(employee_happiness_list)}. Employees are happy!")
else:
    print(f"Score: {len(final_list)}/{len(employee_happiness_list)}. Employees are not happy!")