from typer import Typer

app = Typer()

@app.command()
def hello_world():
    """Hello Typer!"""
    print("Hello, Typer!")

if __name__ == "__main__":
    app()
