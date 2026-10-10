pyetjet = [
    {
        "pyetja": "1. Çfarë do të thotë 'EdTech'?",
        "opsionet": [
            "A) Educational Technology",
            "B) Editing Technology",
            "C) Economic Technology",
        ],
        "përgjigja": "A",
    },
    {
        "pyetja": "2. Cila nga këto është një platformë për mësimin online?",
        "opsionet": ["A) Photoshop", "B) Moodle", "C) Excel"],
        "përgjigja": "B",
    },
    {
        "pyetja": "3. Cila gjuhë programimi përdoret gjerësisht në inteligjencën artificiale?",
        "opsionet": ["A) Python", "B) HTML", "C) CSS"],
        "përgjigja": "A",
    },
    {
        "pyetja": "4. Cila është mënyra më e mirë për të mësuar programim?",
        "opsionet": [
            "A) Leximi i librit",
            "B) Shkrimi i kodit",
            "C) Njohja e koncepteve",
        ],
        "përgjigja": "B",
    },
    {
        "pyetja": "5. Çfarë do të thotë shkurtesa AI?",
        "opsionet": [
            "A) Artificial Intelligence",
            "B) Arsimi Internacional",
            "C) Arritje Inteligjente",
        ],
        "përgjigja": "A",
    },
]


def zhvillo_kuizin():
    pikët = 0
    print("=== MIRË SE ERDHËT NË KUIZIN E EDTECH ===\n")

    for item in pyetjet:
        print(item["pyetja"])

        for opsioni in item["opsionet"]:
            print(opsioni)

        pergjigja_perdoruesit = (
            input("Zgjidhni përgjigjen tuaj (A, B, apo C): ").upper().strip()
        )

        if pergjigja_perdoruesit == item["përgjigja"]:
            print("Saktë!\n")
            pikët += 1
        else:
            print(f"E gabuar! Përgjigja e saktë ishte: {item['përgjigja']}\n")

    print(f"Lojë e përfunduar! Ju morët {pikët} nga {len(pyetjet)} pikë.")


zhvillo_kuizin()


