"""
Задача 3

Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

def pack_backpack(items, max_capacity):
    def helper(items_list, target, current_items):
        if target == 0:
            return [current_items]
        if not items_list:
            return []

        results = []
        for i in range(len(items_list)):
            if items_list[i][1] <= target:
                results.extend(helper(items_list[i+1:], target - items_list[i][1],
                                      current_items + [items_list[i][0]]))
        return results

    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    return helper(sorted_items, max_capacity, [])

items = {
    "палатка": 4.0,
    "спальник": 1.5,
    "котелок": 0.5,
    "еда": 2.0,
    "фонарик": 0.3,
    "аптечка": 0.7
}

max_capacity = 6.0

all_backpacks = pack_backpack(items, max_capacity)
print("Все возможные варианты комплектации рюкзака:")
for backpack in all_backpacks:
    print(backpack)