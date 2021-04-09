from dataclasses import dataclass
from enum import Enum


muscle = {
    "calories_burned_per_resting_hour": 0.25,
    "calories_burned_per_active_hour": .5
}

fat = {
    "calories_burned_per_resting_hour": 0.08,
    "calories_burned_per_active_hour": 0.08
}


@dataclass
class Weight:
    muscle: float  # in KG
    fat: float  # in KG


@dataclass
class Activity:
    hours_moving: float
    hours_resting: float


def get_bmr(age: int, weight: float, height: float) -> float:
    return 5 + 10 * weight + 6.25 * height - 5 * age


ActivityLevel = {
    "xs": 1.2,  # sedentary (little to no exercise)
    "s": 1.375,  # lightly active (light exercise 1–3 days per week)
    "m": 1.55,  # moderately active (moderate exercise 3–5 days per week)
    "l": 1.725,  # very active (hard exercise 6–7 days per week)
    "xl": 1.9,  # extra active (very hard exercise, training, or a physical job)
}


def calories_burned_per_day(bmr: BMR, activity_level: float) -> float:
    return bmr.ratio * activity_level


def calories_burned_resting_per_hour(weight: Weight) -> float:
    fat_burned_per_hour: float = weight.fat * fat["calories_burned_per_resting_hour"]
    muscle_burned_per_hour: float = weight.muscle * muscle["calories_burned_per_resting_hour"]
    return fat_burned_per_hour + muscle_burned_per_hour


def calories_burned_active_per_hour(weight: Weight) -> float:
    fat_burned_per_hour: float = weight.fat * fat["calories_burned_per_active_hour"]
    muscle_burned_per_hour: float = weight.muscle * muscle["calories_burned_per_active_hour"]
    return fat_burned_per_hour + muscle_burned_per_hour


def calories_burned_per_day(weight: Weight, activity: Activity):
    calories_burned_resting = calories_burned_resting_per_hour(weight) * activity.hours_resting
    calories_burned_moving = calories_burned_resting_per_hour(weight) * activity.hours_moving
    return calories_burned_resting + calories_burned_moving


def main():
    weight = 93  # in KG
    height = 183  # in cm
    fat_weight = body_weight * 0.19  # in KG
    weight = Weight(muscle=muscle_weight, fat=fat_weight)
    activity = Activity(hours_resting=20, hours_moving=4)
    print('how many calories do I burn per day? -> ', calories_burned_per_day(weight, activity))


if __name__ == '__main__':
    main()
