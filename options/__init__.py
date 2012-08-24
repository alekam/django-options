# major, minor, patch
VERSION = (0, 1, 1)


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version


def get_option(name, default=None, store=True):
    from .models import Option
    qs = Option.objects.filter(name=name)
    if not qs.exists():
        if store:
            set_option(name, default)
        return default
    elif qs.count() == 1:
        return qs.get().get_value()
    else:
        data = []
        for opt in qs:
            val = opt.get_value()
            if val is not None:
                data.append(val)
        return data


def set_option(name, value=None):
    if isinstance(value, list):
        if len(value) == 0:
            set_option(name, None)
            set_option(name, None)
        else:
            for val in value:
                set_option(name, val)
    else:
        from .models import Option
        opt = Option.objects.create(name=name)
        opt.set_value(value)
