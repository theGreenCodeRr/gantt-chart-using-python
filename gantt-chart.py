import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Define the data for the Gantt chart
tasks_data = {
    "Task": ["Literature Review", "Prototyping", "Testing", "Enhancing",
            "Conference Publication","Additional Functionality", "Seminar", "Testing 2nd round", "Enhancing 2nd round",
             "Thesis Writing", "Pre-defense", "Final Defense"],

    "Start": ["2024-04-01", "2024-07-01", "2024-09-01", "2024-09-01", "2024-12-01",
              "2025-03-01", "2025-07-01", "2025-08-01", "2025-09-01", "2025-07-01", "2025-11-01", "2026-02-01"],
              
    "Finish": ["2024-06-30", "2024-08-31", "2024-11-30", "2024-10-31", 
                "2025-02-28", "2025-06-30", "2025-07-31", "2025-10-31", "2025-10-31", "2025-11-30", "2025-11-30", "2026-02-28"]
}

# Create a DataFrame
df = pd.DataFrame(tasks_data)
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

# Define a deeper shade of green
deeper_green = "#228B22"  # Forest Green

# Plotting
fig, ax = plt.subplots(figsize=(25, 8))  # Width increased for a wider chart

# Create a Gantt chart with deeper green bars and larger text for labels
for i, task in enumerate(df['Task']):
    start = df.loc[i, 'Start']
    finish = df.loc[i, 'Finish']
    ax.barh(task, finish - start, left=start, color=deeper_green)

# Formatting with larger font size for the task labels
ax.set_yticks(range(len(df['Task'])))
ax.set_yticklabels(df['Task'], fontsize=20)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45, fontsize=16)
plt.title('Research Plan and Future Goals', fontsize=22)
plt.tight_layout()

# Show plot
plt.show()
