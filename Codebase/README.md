 Attendance Percentage Predictor

 1. Introduction
The Attendance Percentage Predictor is a Python-based project that calculates students' weekly attendance percentages and predicts future attendance using basic machine learning techniques.

This project helps students monitor their attendance and understand whether they are maintaining the minimum required attendance of 75%.

 2. Objective
The main objectives of this project are:
- To calculate weekly attendance percentages.
- To store and display attendance data in tabular form.
- To predict future attendance using Linear Regression.
- To identify whether attendance is SAFE or WARNING based on the 75% threshold.
- To understand the practical applications of Python libraries.

 3. Technologies Used
- **Python:** Main programming language.
- **NumPy:** Used for numerical calculations and week numbering.
- **Pandas:** Used to organize and display attendance data in tabular form.
- **Linear Regression:** Used to estimate future attendance trends.

 4. Features
- Accepts weekly attendance percentage as input.
- Validates user input.
- Creates an attendance table using Pandas.
- Predicts future attendance using `numpy.polyfit()`.
- Checks the predicted attendance against the 75% threshold.
- Displays SAFE or WARNING status.

 5. Project Structure

```text
Attendance-Percentage-Predictor/
│
├── main.py
├── README.md
└── testcases/
    ├── Test Case 1.png
    ├── Test Case 2.png
    ├── Test Case 3.png
    └── Test Case 4.png
```

 6. Installation and Requirements

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install numpy pandas
```

 7. How to Run the Project

1. Download or clone the repository.
2. Open the project folder.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

5. Enter the weekly attendance percentages when prompted.
6. View the attendance table, predicted attendance, and final status.

## 8. Prediction Method

This project uses Linear Regression to estimate future attendance.

The `numpy.polyfit()` function is used to calculate the best-fit line based on previous weekly attendance data.

The predicted attendance is compared with the minimum attendance requirement of 75%.

- **SAFE:** Predicted attendance is 75% or above.
- **WARNING:** Predicted attendance is below 75%.

 9. Test Cases

Different test cases are used to check the correctness of the program.

Screenshots of the program outputs are available in the `testcases` folder.

10. Learning Outcomes

Through this project, I learned:
- Basic Python programming.
- Input validation.
- Working with NumPy arrays.
- Creating tables using Pandas.
- Understanding Linear Regression.
- Predicting future values using historical data.
- Using GitHub and GitHub Codespaces.

11. Conclusion

The Attendance Percentage Predictor is a simple educational project that demonstrates how Python and its libraries can be used to analyze attendance data and predict future trends.

This project helped me improve my programming, problem-solving, and data analysis skills.

---

Project Type: First-Year BTech CSE Python Project  
Developed Using: Python, NumPy and Pandas
