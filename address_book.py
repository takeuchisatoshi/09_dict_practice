def main():
    address_books = [{"name": "株式会社NEXT REVOLUTION",
                      "location": "岩手県八幡平市大更第35地割62番地",
                      "zipcode": "0287111"},

                     {"name": "ペンションあんとる・ど・めえる",
                      "location": "岩手県八幡平市松尾寄木第１地割６１８−１２",
                      "zipcode": "0287111"},

                     {"name": "なかやま荘",
                      "location": "岩手県八幡平市松尾寄木2-512",
                      "zipcode": "0287302"},
                     ]

    # print(address_books[0]["name"])
    # print(f"所在地: 〒{address_books[0]['zipcode']} {address_books[0]['location']}")
    #
    # print(address_books[1]["name"])
    # print(f"所在地: {address_books[1]['location']}")
    #
    # print(address_books[2]["name"])
    # print(f"所在地: {address_books[2]['location']}")

    for address in address_books:
        name = address["name"]
        print(name)
        location = address["location"]
        print(location)
        zipcode = address["zipcode"]
        print(zipcode)


if __name__ == "__main__":
    main()
