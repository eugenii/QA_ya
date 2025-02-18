# Работа с завершёнными и незавершёнными задачами.

new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Удалить 005 из списка задач и перенести в завершённые
completed_tasks.append(new_tasks.pop())

# Удалить из списка задач 007.
new_tasks.remove('task_007')

# Вывести на экран последнюю задачу из списка задач.
print(new_tasks[-1])

# Код для промежуточной проверки.
# print(new_tasks)
# print(completed_tasks)