

# 🍽️ Recipes Web App

A full-stack application where users can view and search recipes. The backend is built using **FastAPI** and **MySQL**, and the frontend uses **React.js** (Vite + React).



## 📂 Project Structure

```

RECIPES/
├── backend/      → FastAPI backend with MySQL
├── frontend/     → React frontend

````



## 🧰 Tech Stack

- **Backend**: Python, FastAPI  
- **Database**: MySQL  
- **Frontend**: React (Vite)  
- **Styling**: CSS, Tailwind CSS  



## ⚙️ Backend Setup

1. **Create and activate virtual environment**:
   ```bash
   cd backend
   python -m venv env
   source env/bin/activate      # Linux/Mac
   env\Scripts\activate         # Windows


2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL**:

   * Ensure MySQL is installed and running
   * Create a database:

     ```sql
     CREATE DATABASE recipes_db;
     ```

4. **Update connection URL** in `database.py`:

   ```python
   DATABASE_URL = "mysql+pymysql://root@localhost:3306/recipes_db"
   ```

5. **Run the FastAPI server**:

   ```bash
   uvicorn main:app --reload
   ```


## 📡 API Endpoints

### 🔹 GET All Recipes (Paginated)

```http
GET /api/recipes?page=1&limit=10
```

Returns recipes in descending order of rating.

### 🔹 GET Filtered Recipes

```http
GET /api/recipes/search?title=Pie&rating=4.5
```

Searches recipes with flexible filters:

* `title` → partial match (case-insensitive)
* `rating`, `calories`, `total_time` → supports comparison operators (`>`, `<`, `>=`, `<=`, `=`)
* `cuisine` → exact match



## 🖥️ Frontend Setup

1. Open a new terminal and navigate:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run the React app:

   ```bash
   npm run dev
   ```

   App runs on: [http://localhost:5173](http://localhost:5173)



## 🔗 Connecting Frontend to Backend

In your React component (e.g., `RecipeDetails.jsx`):

```js
axios.get(`http://localhost:8000/api/recipes?page=${page}&limit=${limit}`)
     .then(res => console.log(res.data.data));
```



## 🧠 Logics Used

Refer to [`python_logics.txt`](./backend/python_logics.txt) for detailed backend logic, including:

* SQLAlchemy model definition
* JSON parsing and database insertion
* Pagination and search filters with operators
* Nutrient extraction from JSON fields using SQL functions


### ✨ Happy Cooking & Coding!


