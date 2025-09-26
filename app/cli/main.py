from typer import Typer

app = Typer()

@app.command()
def hello_typer():
    """Hello Typer!"""
    print("Hello, Typer!")

if __name__ == "__main__":
    app()
