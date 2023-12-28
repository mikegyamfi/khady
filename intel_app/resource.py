from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import CustomUser

class CustomUserResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='id')
    password = fields.Field(attribute='password', column_name='password')
    last_login = fields.Field(attribute='last_login', column_name='last_login')
    is_superuser = fields.Field(attribute='is_superuser', column_name='is_superuser')
    groups = fields.Field(attribute='groups', column_name='groups')
    user_permissions = fields.Field(attribute='user_permissions', column_name='user_permissions')
    is_staff = fields.Field(attribute='is_staff', column_name='is_staff')
    is_active = fields.Field(attribute='is_active', column_name='is_active')
    date_joined = fields.Field(attribute='date_joined', column_name='date_joined')
    first_name = fields.Field(attribute='first_name', column_name='first_name')
    last_name = fields.Field(attribute='last_name', column_name='last_name')
    username = fields.Field(attribute='username', column_name='username')
    email = fields.Field(attribute='email', column_name='email')
    phone = fields.Field(attribute='phone', column_name='phone')
    wallet = fields.Field(attribute='wallet', column_name='wallet')
    status = fields.Field(attribute='status', column_name='status')
    password1 = fields.Field(attribute='password1', column_name='password1')
    password2 = fields.Field(attribute='password2', column_name='password2')

    class Meta:
        model = CustomUser
        skip_unchanged = True
        report_skipped = False
        clean_model_instances = True