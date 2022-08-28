#/src/views/BlogpostView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.BlogpostModel import BlogpostModel, BlogpostSchema
from marshmallow import ValidationError

blogpost_api = Blueprint('blogpost_api', __name__)
blogpost_schema = BlogpostSchema()


@blogpost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Blogpost Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  # try catch block 
  try:
     data= blogpost_schema.load(req_data)
  #handle marshmallow validation errors
  except ValidationError as err:
    return custom_response(err.messages, 400)
 
 
  post = BlogpostModel(data)
  post.save()
  data = blogpost_schema.dump(post)
  return custom_response(data, 201)

@blogpost_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Blogposts
  """
  posts = BlogpostModel.get_all_blogposts()
  data = blogpost_schema.dump(posts, many=True)
  return custom_response(data, 200)



@blogpost_api.route('/<int:blogpost_id>', methods=['GET'])
def get_one(blogpost_id):
  """
  Get A Blogpost
  """
  post = BlogpostModel.get_one_blogpost(blogpost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = blogpost_schema.dump(post)
  return custom_response(data, 200)


@blogpost_api.route('/<int:blogpost_id>', methods=['PUT'])
@Auth.auth_required
def update(blogpost_id):
  """
  Update A Blogpost
  """
  req_data = request.get_json()
  post = BlogpostModel.get_one_blogpost(blogpost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = blogpost_schema.dump(post)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  # try catch block 
  try:
    data=blogpost_schema.load(req_data, partial=True)
  #handle marshmallow validation errors
  except ValidationError as err:
    return custom_response(err.messages, 400)
  post.update(data)
  
  data = blogpost_schema.dump(post)
  return custom_response(data, 200)


@blogpost_api.route('/<int:blogpost_id>', methods=['DELETE'])
@Auth.auth_required
def delete(blogpost_id):
  """
  Delete A Blogpost
  """
  post = BlogpostModel.get_one_blogpost(blogpost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = blogpost_schema.dump(post)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

