import json
from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.classic import Classic

classics = Blueprint('classics', 'classics')


@classics.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  classic = Classic(**data)
  db.session.add(classic)
  db.session.commit()
  return jsonify(classic.serialize()), 201

@classics.route('/',methods=["GET"])
def index():
    classics = Classic.query.all()
    return jsonify([classic.serialize() for classic in classics]),200

@classics.route('/<id>',methods=["GET"])
def show(id):
  classic = Classic.query.filter_by(id=id).first()
  classic_data = classic.serialize()
  return jsonify(classic=classic_data),200

@classics.route('/<id>',methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  classic = Classic.query.filter_by(id=id).first()

  if classic.profile_id != profile["id"]:
    return 'Forbidden', 403
  
  db.session.delete(classic)
  db.session.commit()
  return jsonify(message="Success Deleted"),200