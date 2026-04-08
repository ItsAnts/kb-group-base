projects = {
    "Сайт компании": {
        "budget": 150000,
        "status": "В работе"
    },
    "Мобильное приложение": {
        "budget": 300000,
        "status": "Планирование"
    }
}

print(f"СТАТУС преокта 'Сайт компании': {projects["Сайт компании"]["status"]}")
# project["Сайт компании"] -> {"budget": 150000, "status": "В работе"}
# project["Сайт компании"]["status"] -> "В работе"
projects["Мобильное приложение"]["budget"] += 50000

projects.update({"Телеграм Бот": {"budget": 30000, "status": "Планирование"}})
print(projects)

iteratio: int = 0
keys: list[str] = list(projects.keys())
while iteratio != len(keys):
    # projects[keys[iteratio]]["budget"] -> projects["Сайт компании"]["budget"]
    # keys[iteratio]] -> iteratio = 0 -> keys[0] -> "Сайт компании"
    if projects[keys[iteratio]]["budget"] > 300000:
        print(f"Данный проект больше 300000: {keys[iteratio]}")
    iteratio += 1