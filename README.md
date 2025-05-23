

## 🍽️ Recipes Web App
This is a full-stack application where users can view recipes. The backend is built using FastAPI and MySQL, and the frontend is built with React.js.


### Project Structure
## RECIPES/
## ├── backend/      → FastAPI backend with MySQL
## ├── frontend/     → React frontend

⚙️ Backend Setup
1. Create and activate virtual environment:
cd backend
python -m venv env
source env/bin/activate      # on Linux/Mac
env\Scripts\activate         # on Windows
2. Install dependencies:
pip install -r requirements.txt
3. Set up MySQL
Make sure you have MySQL installed and running.
Create a database named recipes_db.
In MySQL shell or GUI:
CREATE DATABASE recipes_db;
4. Update your connection URL in database.py:
DATABASE_URL = "mysql+pymysql://root@localhost:3306/recipes_db" - replace with your database url
5. Run the backend server:
uvicorn main:app --reload

### 📡 API Endpoints

📄 GET /recipes/  : 
Returns a list of all stored recipes.

📄 GET /recipes/search  :
Returns a list of all stored recipes by filtering in each category (calories , title, cuisine, total time , rating)


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
fetch('http://localhost:8000/recipes/')
  .then(res => res.json())
  .then(data => console.log(data));
