import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and keep only Date and Text columns
df = pd.read_csv(r"C:/Users/acer/Documents/New folder/Whatsapp_chat.csv", header=None).iloc[:, :2]
df.columns = ['Date', 'Text']


print("\nTotal messages analyzed:", len(df))


# 2. Filter rows with valid dates and clean special characters
df = df[df['Date'].str.match(r'\d{2}-\d{2}', na=False)].copy()
df['Text'] = df['Text'].str.replace('â€¯', ' ') # Fixes the PM/AM space

# 3. Split Text into Time, User, and Message
df[['Time', 'Msg']] = df['Text'].str.split(' - ', n=1, expand=True)
df[['User', 'Msg']] = df['Msg'].str.split(': ', n=1, expand=True)

# 4. Convert to Datetime and Drop empty messages
df['DT'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['DT', 'Msg'])

# 5. Visualizations
# Bar chart of Top 5 Users
df['User'].value_counts().head(5).plot(kind='bar', color='skyblue')
plt.title("Top 5 Users")
plt.show()

# Line chart of Messages by Hour
df['DT'].dt.hour.value_counts().sort_index().plot(kind='line', marker='o')
plt.title("Messages by Hour")
plt.show()
