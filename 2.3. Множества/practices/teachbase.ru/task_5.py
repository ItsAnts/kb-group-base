day1_visitors: set[str] = {"user1", "user2", "user3", "user4"}
day2_visitors: set[str] = {"user3", "user4", "user5", "user6"}

unique_visitors: set[str] = day1_visitors.union(day2_visitors)
print(f"Уникальные посетили за два дня: {unique_visitors}")
visitors_first_day_and_second_day: set[str] = day1_visitors.intersection(day2_visitors)
print(f"Посетители в первый и второй день: {visitors_first_day_and_second_day}")
visitors_only_second_day: set[str] = day2_visitors.difference(day1_visitors)
print(f"Посетили, которые були только во второй дент: {visitors_only_second_day}")
