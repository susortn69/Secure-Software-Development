# app/api.py
from flask import Blueprint, request, jsonify
from . import db
from .models import Course
from bleach import clean

api = Blueprint("api", __name__)

@api.get("/health")
def health():
    return {"ok": True}

@api.get("/courses")
def list_courses():
    items = Course.query.order_by(Course.code).all()
    return jsonify([{"id": c.id, "code": c.code, "title": c.title} for c in items])

@api.post("/courses")
def create_course():
    data = request.get_json(silent=True) or {}
    code = clean((data.get("code") or "").strip())
    title = clean((data.get("title") or "").strip())
    if not code or not title:
        return {"error": "code and title required"}, 400
    if Course.query.filter_by(code=code).first():
        return {"error": "course exists"}, 409
    c = Course(code=code, title=title)
    db.session.add(c)
    db.session.commit()
    return {"id": c.id, "code": c.code, "title": c.title}, 201
