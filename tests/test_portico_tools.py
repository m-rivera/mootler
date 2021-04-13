import mootler.src.portico_tools as pt

def test_get_emails():
    """Read Portico student csv and get emails"""
    df = pt.get_emails("data/portico_divination.csv")
    df=df.rename(columns = {11:'Email'})
    print(df)
    assert True
