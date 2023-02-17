from django_auth_ldap.backend import LDAPBackend


class LDAPBackendSecondary(LDAPBackend):
    settings_prefix = "AUTH_LDAP_SECONDARY_"
    # Do any additional overloaded method to meet requirements.