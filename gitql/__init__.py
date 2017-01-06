__version__ = '1.0.0'

# Supported tables and fields.
PossibleTables = {
    'commits': [
        'hash',
        'date',
        'author',
        'author_email',
        'committer',
        'committer_email',
        'summary',
        'message',
    ],
    'refs': [
        'name',
        'full_name',
        'type',
        'hash',
    ],
    'remotes': [
        'name',
        'url',
        'push_url',
        'owner',
    ],
    'tags': [
        'name',
        'full_name',
        'hash',
    ],
    'branches': [
        'name',
        'full_name',
        'hash',
    ],
}


def get_possible_fields(table):
    return PossibleTables.get(table.lower(), [])


def show_all_tables():
    for table, fields in PossibleTables.items():
        print('{}'.format(table))
        print('    {}'.format(' . '.join(fields)))
