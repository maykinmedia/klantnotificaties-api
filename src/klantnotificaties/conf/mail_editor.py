from django.utils.translation import gettext_lazy as _


MAIL_EDITOR_CONF = {
    "default": {
        "name": _("Default Email"),
        "description": _("This is the default email template."),
        "subject_default": "{{subject}}",
        "body_default": """
            {{content}}
        """,
        "subject": [{
            "name": "site_name",
            "description": _("This is the name of the site. From the sites"),
        }],
        "body": [{
            "name": "content",
            "description": _("This is the content of the message"),
        }]
    }
}
