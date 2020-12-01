from azureml.core import Workspace, Experiment, Environment
import click


@click.command()
@click.option("-e", "--environment", type=str, default="PyTorch-1.7-GPU",
              help="The name of the environment to build")
@click.option('-v', "--version", type=int, help="The version of the environment to build.")
def main(environment: str, version: int):
    ws = Workspace.from_config()

    pt_env = Environment.get(ws, environment, version)
    
    print('===============================')
    print('     BUILDING ENVIRONMENT      ')
    print('===============================')
    print(f'Building environment:') 
    print(f'\tName: {pt_env.name}')
    print(f'\tVersion {pt_env.version}')
    print('===============================')

    build = pt_env.build(ws)
    build.wait_for_completion(show_output=True)

if __name__ == "__main__":
    main()