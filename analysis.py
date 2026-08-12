import pandas as pd
df=pd.read_csv("Student_Performance.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.shape)
print("Average Final Marks:",df["G3"].mean())
print("Highest Final Marks:",df["G3"].max())
print("Lowest Final Marks:",df["G3"].min())
print("Average Absences:",
      df["absences"].mean())
high = df[df["G3"]>15]
print("Student scoring above 15:")
print(high["G3"])
#BAR GRAPH
import matplotlib.pyplot as plt
plt.bar(df.index,df["G3"])
plt.title("Final Marks of Students")
plt.xlabel("Student")
plt.ylabel("Final Marks")
plt.show()
#HISTOGRAM
plt.hist(df["G3"],bins=10)
plt.title("Distribution of Final Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
#PIE CHART
passed = len(df[df["G3"]>=10])
failed = len(df[df["G3"]<10])
plt.pie([passed,failed],
        labels=["Passed","Failed"],
        autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()
#SCATTER PLOT
import matplotlib.pyplot as plt
plt.scatter(df["absences"],df["G3"])
plt.title("Attendance (Absences) vs Final Marks")
plt.xlabel("Absences")
plt.ylabel("Final Marks")
plt.show()