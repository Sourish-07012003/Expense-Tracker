💸 Expense Tracker
A simple, responsive, and feature-rich Expense Tracker web application built using Flask for the backend and Streamlit for the frontend. It allows users to add, view, filter, analyze, and delete expenses, with data stored in a CSV file.

🚀 Features
✅ Add new expenses with date, category, amount, and note

🗑️ Delete individual expenses by index

📋 View all expenses in a well-structured table

🔍 Filter expenses by category or note text

📊 Visual analytics (category-wise pie chart, monthly bar graph)

💾 Download all expenses as a CSV file

💡 Real-time feedback messages (success/error)

🖼️ Clean and stylish Streamlit UI

🛠 Tech Stack
Layer	Tech
Backend	Flask (Python)
Frontend	Streamlit (Python)
Database	CSV File
Visuals	Plotly

📁 Project Structure
bash
Copy
Edit
expense-tracker/
│
├── app.py                # Flask backend
├── app_frontend.py       # Streamlit frontend
├── expenses.csv          # CSV file for storing expense data (auto-created)
├── README.md             # This file
🧑‍💻 Installation & Run
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
2. Install Dependencies
Make sure you have Python 3.8+ and pip installed.

bash
Copy
Edit
pip install flask streamlit pandas requests plotly
3. Run the Flask Backend
bash
Copy
Edit
python app.py
4. Run the Streamlit Frontend
In another terminal:

bash
Copy
Edit
streamlit run app_frontend.py
📷 Screenshots
Add Expense	View Table	Analytics

(You can create a /screenshots folder and add sample images.)

🔧 Future Improvements
🌐 User authentication (login/signup)

🧾 Switch from CSV to SQLite/MySQL database

☁️ Deploy to Streamlit Cloud or Render

📱 Mobile-friendly PWA support

📃 License
MIT License. Free to use and modify.