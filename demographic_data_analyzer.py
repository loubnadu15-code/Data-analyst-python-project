import pandas as pd


def calculate_demographic_data(print_data=True):
    # Lire les données depuis le fichier CSV
    df = pd.read_csv("adult.data.csv")

    # 1. Combien de personnes de chaque race sont représentées dans ce jeu de données ?
    race_count = df['race'].value_counts()

    # 2. Quel est l'âge moyen des hommes ?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Quel est le pourcentage de personnes ayant un diplôme de Bachelor ?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Pourcentage des personnes ayant une éducation avancée (Bachelor, Master ou Doctorat) qui gagnent plus de 50K 
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[advanced_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Pourcentage des personnes sans éducation avancée qui gagnent plus de 50K
    lower_education_rich = round(
        (df[~advanced_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Nombre minimum d'heures travaillées par semaine
    min_work_hours = df['hours-per-week'].min()

    # 7. Pourcentage des personnes qui travaillent le minimum d'heures et qui gagnent plus de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Pays ayant le pourcentage le plus élevé de personnes gagnant plus de 50K
    country_rich_percentage = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts() / df['native-country'].value_counts() * 100
    )

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. Métier le plus populaire en Inde parmi les personnes qui gagnent plus de 50K
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
