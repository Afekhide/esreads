from marshmallow import Schema, fields


class PostSchema(Schema):
    order = True
    id = fields.Int()
    title = fields.String()
    content = fields.String()
    user_email = fields.String()
    date_posted = fields.DateTime()


class UserSchema(Schema):
    order = True
    id = fields.Integer()
    role_id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    password = fields.Str()
    api_key = fields.Str()
    job = fields.Str()
    ip_address = fields.Str()
    img_data = fields.Raw()
    posts = fields.List(fields.Nested(PostSchema))


class RoleSchema(Schema):
    id = fields.Int()
    name = fields.String()
    users = fields.List(fields.Pluck(UserSchema, 'email'))


post_schema = PostSchema()
posts_schema = PostSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)


