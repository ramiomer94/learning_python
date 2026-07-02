from user import User
from admin import Admin

admin_user = Admin('steve', 'jobs', 56, 'california')
admin_user.privileges.show_privileges()