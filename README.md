

## 🍽️ Recipes Web App
### This is a full-stack application where users can view recipes. The backend is built using FastAPI and MySQL, and the frontend is built with React.js (vite + react)


## 📂 Project Structure
 
#### RECIPES/
#### ├── backend/      → FastAPI backend with MySQL
#### ├── frontend/     → React frontend

## 🧰 Tech Stack
#### Backend: Python, FastAPI
#### Database: MySQL
#### Frontend: React (Vite + React)
#### Styling: CSS, Tailwind CSS

## ⚙️ Backend Setup
1. Create and activate virtual environment:
#### cd backend
#### python -m venv env
#### source env/bin/activate - Linux/Mac
#### env\Scripts\activate    - Windows
2. Install dependencies:
#### pip install -r requirements.txt
3. Set up MySQL
Make sure you have MySQL installed and running.
Create a database named recipes_db.
In MySQL shell or GUI:
#### CREATE DATABASE recipes_db;
4. Update your connection URL in database.py:
#### DATABASE_URL = "mysql+pymysql://root@localhost:3306/recipes_db" - replace with your database url
5. Run the backend server:
#### uvicorn main:app --reload

### 📡 API Testing 

📄 GET http://127.0.0.1:8000/api/recipes: 
Returns a list of all stored recipes.
- GET http://127.0.0.1:8000/api/recipes?page=1&limit=10 
##### returns recipes from 1 to 10 

📄 GET http://127.0.0.1:8000/api/recipes/search  :
Returns a list of all stored recipes by filtering in each category (calories , title, cuisine, total time , rating)
- GET http://127.0.0.1:8000/api/recipes/search?title=Pie&rating=4.5
##### returns recipes titled with pie and having rating above or equal to 4.5



### 🖥️ Frontend Setup
1. Open another terminal and go to the frontend folder:
cd frontend
2. Install dependencies:
npm install
3. Run the development server:
npm run dev
This will start the app at http://localhost:5173.

### 🔗 Connecting Frontend to Backend
In your React components (like recipedetails.jsx), you can fetch data like this:
#### fetch('http://localhost:8000/recipes/')
#### .then(res => res.json())
#### .then(data => console.log(data));

