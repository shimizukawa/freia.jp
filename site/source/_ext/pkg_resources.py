from importlib.metadata import version, entry_points


class Require:
    def __init__(self, distribution_name):
        self.distribution_name = distribution_name
        self.version = version(distribution_name)


def iter_entry_points(group, name):
    return entry_points(group=group, name=name)


def require(distribution_name):
    return [Require(distribution_name)]
