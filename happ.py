def calculate_ctr(ranking, searches):
    ctr = (1 / ranking) * (searches / 100)
    return ctr

if __name__ == "__main__":
    ranking = int(input("Enter the website's search engine ranking: "))
    searches = int(input("Enter the number of searches for the keyword: "))
    ctr = calculate_ctr(ranking, searches)
    print(f"CTR: {ctr}")
