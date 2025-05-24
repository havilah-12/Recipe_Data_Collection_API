from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Integer, text
from typing import Optional
import re

from database import SessionLocal
from models import Recipe
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- PAGINATED RECIPE LIST ---
@app.get("/api/recipes")
def get_recipes(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    query = db.query(Recipe).order_by(Recipe.rating.desc())
    total = query.count()
    recipes = query.offset(offset).limit(limit).all()
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": [r.__dict__ for r in recipes]
    }

# --- FILTERED SEARCH WITH OPERATOR SUPPORT ---
@app.get("/api/recipes/search")
def search_recipes(
    db: Session = Depends(get_db),
    title: Optional[str] = None,
    cuisine: Optional[str] = None,
    calories: Optional[str] = None,
    total_time: Optional[str] = None,
    rating: Optional[str] = None,
    page: int = 1,
    limit: int = 10
):
    query = db.query(Recipe)

    # Helper to extract operator and value from string
    def parse_op_val(param: str):
        pattern = r"^(>=|<=|>|<|=)?\s*(\d+(\.\d+)?)$"
        match = re.match(pattern, param.strip())
        if not match:
            raise HTTPException(status_code=400, detail=f"Invalid filter format: {param}")
        op = match.group(1) or "="
        val = float(match.group(2))
        return op, val

    # Applying filters
    if title:
        title = re.sub(r"\s+", " ", title.strip().lower())
        query = query.filter(func.lower(Recipe.title).ilike(f"%{title}%"))

    if cuisine:
        query = query.filter(Recipe.cuisine.ilike(f"%{cuisine}%"))

    if calories:
        op, val = parse_op_val(calories)
        calories_expr = cast(
            text("CAST(REPLACE(JSON_UNQUOTE(nutrients->'$.calories'), ' kcal', '') AS UNSIGNED)"),
            Integer
        )
        if op == ">":
            query = query.filter(calories_expr > val)
        elif op == ">=":
            query = query.filter(calories_expr >= val)
        elif op == "<":
            query = query.filter(calories_expr < val)
        elif op == "<=":
            query = query.filter(calories_expr <= val)
        else:
            query = query.filter(calories_expr == val)

    if total_time:
        op, val = parse_op_val(total_time)
        col = Recipe.total_time
        if op == ">":
            query = query.filter(col > val)
        elif op == ">=":
            query = query.filter(col >= val)
        elif op == "<":
            query = query.filter(col < val)
        elif op == "<=":
            query = query.filter(col <= val)
        else:
            query = query.filter(col == val)

    if rating:
        op, val = parse_op_val(rating)
        col = Recipe.rating
        if op == "=":
            query = query.filter(func.round(col, 1) == val)
        elif op == ">":
            query = query.filter(col > val)
        elif op == ">=":
            query = query.filter(col >= val)
        elif op == "<":
            query = query.filter(col < val)
        elif op == "<=":
            query = query.filter(col <= val)

    total = query.count()
    offset = (page - 1) * limit
    results = query.offset(offset).limit(limit).all()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": [r.__dict__ for r in results]
    }
