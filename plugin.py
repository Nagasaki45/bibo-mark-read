import datetime

import bibo
import pybibs
import click


@click.command('mark-read', short_help='Mark an entry as read.')
@click.argument('search_term')
@click.pass_context
def mark_read(ctx, search_term):
    data = ctx.obj['data']
    entry = bibo.query.get(data, search_term)

    entry['fields']['readdate'] = str(datetime.date.today())
    tags_field = entry['fields'].get('tags')
    if tags_field:
        tags = (t.strip() for t in tags.split(','))
        updated = ','.join([t for t in tags if t.lower() != 'to read'])
        entry['fields']['tags'] = tags

    pybibs.write_file(data, ctx.obj['database'])
