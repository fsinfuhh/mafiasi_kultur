# Mafiasi Kulturgenießer

**TODO: Fill out a proper project description**

## Configuration Details

The application is intended to be configured via environment variables.
The following variables are defined:

| Name                              | Default                           | Required? | Description                                                                                                                  |
|-----------------------------------|-----------------------------------|:---------:|------------------------------------------------------------------------------------------------------------------------------|
| `APP_MODE`                        | `prod` in docker, `dev` otherwise |    yes    | The mode in which mafiasi_kultur operates.<br>**Changing this may affect the defaults of other variables.** |
| `DJANGO_DEBUG`                    | `False` except in `dev` mode      |    no     | Whether djangos debug mode is enabled ([django debug reference](https://docs.djangoproject.com/en/dev/ref/settings/#std-setting-DEBUG)) |
| `DJANGO_SECRET_KEY`               | *unset* except in `dev` mode      |    yes    | The django secret key used for cryptographic operations ([django secret key reference](https://docs.djangoproject.com/en/dev/ref/settings/#std-setting-SECRET_KEY)) |
| `DJANGO_ALLOWED_HOSTS`            | *unset* except in `dev` mode      |    yes    | The hostnames that are allowed to connec to the django server ([django allowed hosts reference](https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts)) |
| `DJANGO_DB`                       | *unset* except in `dev` mode      |    yes    | A database url for django to connect to ([db url format reference](https://github.com/jazzband/dj-database-url/#url-schema)) |
| `DJANGO_CACHE`                    | `locmem://default`                |    no     | A cache url for django to use ([cache url format reference](https://github.com/epicserve/django-cache-url#supported-caches)) |
| `DJANGO_ALLOWED_CORS_ORIGINS`     | `[]` except in `dev` mode         |    no     | List of HTTP origins that are allowed to do CORS requests against the django api |
| `DJANGO_TRUST_REVERSE_PROXY`      | `False`                           |    no     | Whether `X-Forwarded-For` headers are to be trusted (enable this if django is running behind a reverse proxy) |
| `DJANGO_OPENID_CLIENT_ID`         | *unset* except in `dev` mode      |    yes    | The openid client id which django uses to validate authentication tokens |
| `DJANGO_OPENID_CLIENT_SECRET`     | *unset* except in `dev` mode      |    yes    | The openid client secret for the configured client id |
| `OPENID_ISSUER`                   | *mafiasi-identity*                |    no     | The openid issuer that authors access tokens and which should be consulted for validation |
| `DJANGO_ANY_OPENID_USER_IS_ADMIN` | `False`                           |    no     | Whether any user that logs in via openid should be made a django superuser |
| `DJANGO_SUPERUSER_GROUPS`         | `[]`                              |    no     | A list of group names whose members should be made django superusers |
| `DJANGO_ALLOWED_METRICS_NETS`     | `127.0.0.0/0`, `::/64`            |    no     | List of IP networks which are allowed to access the /metrics endpoint                                                                     |
| `NUXT_PUBLIC_API_BASE`            | *unset* except in `dev`           |    yes    | The base url of the django application (e.g. `https://api.mafiasi_kultur.com`) |
| `NUXT_PUBLIC_OPENID_CLIENT_ID`    | `dev-client`                      |    no     | The openid client id which the frontend uses for authentication |
| `NUXT_PUBLIC_OPENID_ISSUER`       | *mafiasi-identity*                |    no     | The openid issuer which the frontend uses for authentication (should be the same as the one in configured for django) |

For the configuration of these variables in `dev` mode, see the configuration in [.env.dev](./.env.dev).
