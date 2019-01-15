from flask_restplus import Resource, reqparse, fields, marshal_with

class AccountControllerParsers():

    userLoginParser = reqparse.RequestParser(bundle_errors=True)
    userLoginParser.add_argument('email', help = 'Email is required', required = True, location = 'json')
    userLoginParser.add_argument('password', help = 'Password is required', required = True, location = 'json')

    userRegisterParser = reqparse.RequestParser(bundle_errors=True)
    userRegisterParser.add_argument('password', dest = 'password', help = 'Password is required', required = True, location = 'json')
    userRegisterParser.add_argument('confirmPassword', dest = 'confirmPassword', help = 'Confirm password is required', required = True, location = 'json')
    userRegisterParser.add_argument('details', help = "User details is required", required = True, type = dict)

    userDetailsParser = reqparse.RequestParser(bundle_errors=True)
    userDetailsParser.add_argument('imageId', type = int, required = False, location=('details',))
    userDetailsParser.add_argument('firstName', help = "First name is required", required = True, location=('details',))
    userDetailsParser.add_argument('lastName', help = "Last name is required", required = True, location=('details',))
    userDetailsParser.add_argument('email', help = "Email is required", required = True, location=('details',))