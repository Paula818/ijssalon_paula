def presenteer(mijn_dict=None, totaal=None):
    if mijn_dict is None:
        mijn_dict = {
    'vis': 10,
    'vlees': 25,
    'overig': 15
        }
    if totaal is None:
        totaal = 50

    for k, v in mijn_dict.items():
        print(f"{k}: {v} euro")

    print("========================")
    print(f"Totaal: {totaal} euro")

#presenteer()