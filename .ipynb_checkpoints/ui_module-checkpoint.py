# -*- coding: utf-8 -*-
"""ui_module.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p_xm-vr5ZVgsZ7pi2ag2g3FL4KbtMd-O
"""

from query_module import*

def display_menu():
    print("\n=== Stroke Data Analytics ===")
    print("1. Smokers with hypertension and stroke")
    print("2. Heart disease with stroke")
    print("3. Hypertension by gender")
    print("4. Smoking habits (stroke vs. no stroke)")
    print("5. Urban vs. rural with stroke")
    print("6. Dietary habits")
    print("7. Individuals with hypertension and stroke")
    print("8. Hypertension (stroke vs. no stroke)")
    print("9. Individuals with heart disease and stroke")
    print("10. Descriptive statistics for a feature")
    print("11. Average sleep hours")
    print("12. Quit")

def start_ui():
    """Start the interactive UI."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            result = querySmokeHypertensionAndStroke()
            print("Results:", result)
        elif choice == '2':
            result = queryHeartDiseaseAndStroke()
            print("Results:", result)
        elif choice == '3':
            result = queryHypertensionAndStroke()
            print("Results:", result)
        elif choice == '4':
            result = querySmokingHabitsAndStroke()
            print("Results:", result)
        elif choice == '5':
            result = queryResidencyType()
            print("Results:", result)
        elif choice == '6':
            result = queryDietaryHabits()
            print("Stroke habits:", result['Stroke'][:5], "...")
            print("No stroke habits:", result['No Stroke'][:5], "...")
        elif choice == '7':
            result = queryHypertensionStroke()
            print("First 5 records:", result[:5])
        elif choice == '8':
            result = query_hypertension_all()
            print("Stroke (first 5):", result['Stroke'][:5])
            print("No Stroke (first 5):", result['No Stroke'][:5])
        elif choice == '9':
            result = query_heart_disease_stroke_individuals()
            print("First 5 records:", result[:5])
        elif choice == '10':
            result = query_descriptive_stats()
            print("Results:", result)
        elif choice == '11':
            result = query_sleep_hours()
            print("Results:", result)
        elif choice == '12':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
        cont = input("Continue? (y/n): ").lower()
        if cont != 'y':
            print("Goodbye!")
            break