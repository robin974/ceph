distro = None
release = None
codename = None


def choose_init():
    """Select a init system

    Returns the name of a init system (upstart, sysvinit ...).
    """
    if distro.lower() == 'ubuntu' or distro.lower() == 'linuxmint':
        return 'upstart'
    return 'sysvinit'
