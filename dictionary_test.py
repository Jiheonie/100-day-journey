student_scores = {
    "Harry": 81, 
    "Ron": 78,
    "Hermione": 99
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)


travel_log = {
    "France":{
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits": 12
    }
}

travel_log_list = [
    {
        "country":"France",
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits": 12
    }
]

def add_new_country(country, cities, visits):
    new_dic = {}
    new_dic["country"] = country
    new_dic["cities_visited"] = cities
    new_dic["total_visits"] = visits
    travel_log_list.append(new_dic)

add_new_country("Russia", ["Moscow","Saint Petersburg"], 2)
print(travel_log_list)