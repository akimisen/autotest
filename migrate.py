import sys, os
import click
from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import User, Task, CaseInfo, Department, 

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
  return dict(db=db, User=User, CaseInfo=CaseInfo, Task=Task, Department=Department)

@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, help='Run tests under code coverage.')
@click.argument('test_names', nargs=-1)
def test(coverage, test_names):
  """Run the unit tests."""
  if coverage and not os.environ.get('FLASK_COVERAGE'):
    import subprocess
    os.environ['FLASK_COVERAGE'] = '1'
    sys.exit(subprocess.call(sys.argv))

@app.cli.command()
@click.option('--length', default=25,
              help='Number of functions to include in the profiler report.')
@click.option('--profile-dir', default=None,
              help='Directory where profiler data files are saved.')
def profile(length, profile_dir):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length], profile_dir=profile_dir)
    app.run()

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

    # create or update user roles
    .insert_roles()

    # ensure all users are following themselves
    User.add_self_follows()