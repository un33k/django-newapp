from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from ... import defaults as defs


class Command(BaseCommand):
    help = 'Command to print hello world'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--say',
            action='store_true',
            dest='say',
            default=False,
            help='Say Hello World!')

    def handle(self, *args, **options):
        if not options['say']:
            raise CommandError("Option `--say` must be specified.")
            return
        count = 0
        if defs.NEWAPP_HELLO_WOLD:
            self.stdout.write(self.style.SUCCESS('We said {}'.format(defs.NEWAPP_HELLO_WOLD)))
        else:
            self.stdout.write(self.style.WARNING('We said hello'))
