from app import accountControllerNamespace
from flask_restplus import fields

userResponseModel = accountControllerNamespace.model('User response model', {
    'firstName': fields.String('First name'),
    'lastName': fields.String('Last name'),
    'email': fields.String('User email'),
    'imageId': fields.Integer('User image id')
})

userRegistrationDetailsModel = accountControllerNamespace.model('User Details model', {
    'imageId': fields.Integer('Id of user image'),
    'firstName' : fields.String('User first name'),
    'lastName' : fields.String('User last name'),
    'email' : fields.String('User email')
})

userRegistrationModel = accountControllerNamespace.model('Registration model', {
    'password': fields.String("User password"),
    'confirmPassword' : fields.String("Confirmation password"),
    'details' : fields.Nested(userRegistrationDetailsModel)
})

userLoginModel = accountControllerNamespace.model('Login model', {
    'email' : fields.String('User email.'),
    'password' : fields.String('User password')
})

token_model = accountControllerNamespace.model('Token model', {
    'message': fields.String('Message'),
    'access_token': fields.String('Token')
})