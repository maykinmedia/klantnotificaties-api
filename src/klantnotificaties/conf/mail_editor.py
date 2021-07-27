from django.utils.translation import gettext_lazy as _


MAIL_EDITOR_CONF = {
    "activation": {
        "name": _("Activation Email"),
        "description": _("This email is used when people need to activate their account."),
        "subject_default": "Activeer uw account voor {{site_name}}",
        "body_default": """
            <h1>Hallo {{ name }},</h1>

            <p>Welkom! Je hebt je geregistreerd voor een {{ site_name }} account.</p>

            <p>{{ activation_link }}</p>
        """,
        "subject": [{
            "name": "site_name",
            "description": _("This is the name of the site. From the sites"),
        }],
        "body": [{
            "name": "name",
            "description": _("This is the name of the user"),
        }, {
            "name": "site_name",
            "description": _("This is the name of the site. From the sites"),
        }, {
            "name": "activation_link",
            "description": _("This is the link to activate their account."),
        }]
    }
}
