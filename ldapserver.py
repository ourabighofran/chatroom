import ldap
import hashlib
from ldap3 import Server, Connection, ALL, MODIFY_ADD, ObjectDef, AttrDef, Entry
def hash_password(password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed_password
class LDAPServer:
    ou_dn = 'ou=users,dc=tekup,dc=com'

    def __init__(self):
        self.ldap_connection = None

    def ldap_initialize(self):
        ldap_server = 'ldap://192.168.26.134'
        ldap_base_dn = 'dc=tekup,dc=tekup'
        ldap_admin_dn = 'cn=admin,dc=tekup,dc=tekup'
        ldap_admin_password = 'ubuntu'
        with Connection(ldap_server, user=admin_dn, password=admin_password, auto_bind=True) as connect:
            # Define the LDAP entry for the new user
            user_entry = Entry.from_definition(
                connect,  # Use the connection to retrieve the schema
                'inetOrgPerson',
                {
            'cn': username,
            'givenName': given_name,
            'sn': surname,
            'mail': email,
            'userPassword': password,
            })
            # Add the user to the LDAP server
            connect.add(user_entry)
            print(f"User'{username}' added successfully.")
            ldap_server = Server('ldap://192.168.26.134:389', get_info=ALL)

# Define the user details
username = 'ghofran'
password = 'ghofran123'
given_name = 'ghofran'
surname = 'ourabi'
email = 'ourabighofran01@gmail.com'

# Bind to the LDAP server (replace 'cn=admin,dc=example,dc=com' and 'admin_password' with your admin credentials)
admin_dn = 'cn=admin,dc=tekup,dc=com'
admin_password = 'ubuntu'
print(f"User '{username}' added successfully.")


