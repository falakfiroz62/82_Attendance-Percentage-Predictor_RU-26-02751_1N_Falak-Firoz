import numpy as np
import pandas as pd

print("========Attendance Percentage Predictor========")

data = input("Enter weekly attendance percentages seperated by commas : ")

try:
    attendance = [float(x.strip()) for x in data.split(",")] 

    if len(attendance) < 2:
        print("\nAt least 2 weeks of data are required.")

    elif any(x<0 or x>100 for x in attendance):
        print("Attendance must be between 0 and 100.") 

    else:
        weeks = np.arange(1,len(attendance) + 1)

        df = pd.DataFrame({"Weeks": weeks, "Attendance(%)": attendance})

        slope, intercept= np.polyfit(weeks, attendance, 1)

        future_week = int(input("Enter a future week number:"))

        if future_week <= len(attendance):
            print("please enter a future week number.")
        else:
            prediction = slope * future_week + intercept
            prediction = np.clip(prediction,0,100)

  
        print(f"Slope: {slope:.2f} | Intercept: {intercept:.2f}")

        print("Predicted attendance for week", future_week,":",f"{prediction:.2f}%")
     
        if prediction >= 75:
            print("Safe")
        else:
            print("Warning: below 75%")


except ValueError:
    print("Invalid input! Please enter numbers only.")        
