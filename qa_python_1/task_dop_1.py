# Доп задание 1.

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 


def drop_duplicates(tickets):
    """Drop duplicated tickets from tickets list."""
    non_dubbles = set()
    for level in tickets:
        for ticket in tickets[level]:
            if ticket not in non_dubbles:
                non_dubbles.add(ticket)
                continue
            tickets[level].remove(ticket)


def sort_tickets_by_type(types, tickets):
    """Sort tickets by type."""
    drop_duplicates(tickets)
    result = {}
    for i in range(1, len(types) + 1):
        result[types[i]] = tickets[i]
    return result


tickets_by_type = sort_tickets_by_type(types, tickets)

print(tickets_by_type)           
# tickets_by_type = {
#     'Блокирующий': ['API_45', 'API_76', 'E2E_4'],
#     'Критический': ['UI_19', 'API_65', 'E2E_45'],
#     'Значительный': ['E2E_2'],
#     'Незначительный': ['E2E_9'],
#     'Тривиальный': ['API_61']
# } 