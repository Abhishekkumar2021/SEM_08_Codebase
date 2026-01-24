import matplotlib.pyplot as plt
import seaborn as sns
import random as rd

# Global plotting theme
sns.set_theme(style="whitegrid")

# Bar graph data (Showing marks obtained in different subjects)
x = ['Computer Science', 'Mathematics', 'Physics', 'Biology']
y = [85, 90, 78, 88]

# Create bar graph
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='skyblue')
plt.title('Marks Obtained in Different Subjects', fontsize=16)
plt.xlabel('Subjects', fontsize=14)
plt.ylabel('Marks', fontsize=14)
plt.ylim(0, 100)
plt.show()

# generate 1000 random numbers between 0 to 100 and then will divide those into 5 categories
# numbers = []
# for _ in range(1000):
#     numbers.append(rd.randint(0, 100))
    
numbers = [rd.randint(0, 100) for _ in range(1000)]
categories = ['0-20', '21-40', '41-60', '61-80', '81-100']
frequency = [0, 0, 0, 0, 0]

def get_category_index(number):
    if 0 <= number <= 20:
        return 0
    elif 21 <= number <= 40:
        return 1
    elif 41 <= number <= 60:
        return 2
    elif 61 <= number <= 80:
        return 3
    elif 81 <= number <= 100:
        return 4

for number in numbers:
    idx = get_category_index(number)
    frequency[idx] += 1

# Create bar graph for frequency distribution
plt.figure(figsize=(12, 6))
plt.bar(categories, frequency, color='lightgreen')
plt.title('Frequency Distribution of Random Numbers', fontsize=16)
plt.xlabel('Categories', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.ylim(0, max(frequency) + 50)
plt.show()