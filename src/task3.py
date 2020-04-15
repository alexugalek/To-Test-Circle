# LINE_OFFSET is the number of line we will start to read information
# about 250 films with the highest rating.
LINE_OFFSET = 29


def file_handler(file_name, data):
    """File saver function

    :param file_name: name of file to save data
    :param data: data to save
    :return: None
    """
    with open('data5/{}'.format(file_name), 'w') as file:
        file.write('\n'.join(data))


def doc_parser():
    """Function of parsing data from IMDB statistic

    :return: None
    """
    ratings_gist = {}
    years_gist = {}
    films_names = []
    line_offset = 1

    try:
        with open('data5/ratings.list', 'r') as file:

            for line in file:
                if line_offset < LINE_OFFSET:
                    line_offset += 1
                    continue

                data_to_split, year = line.split(' (')
                year = year[:4]
                distribution, votes, rating, *title = data_to_split.split()

                films_names.append(' '.join(title))
                ratings_gist[rating] = ratings_gist.get(rating, 0) + 1
                years_gist[year] = years_gist.get(year, 0) + 1

                if len(films_names) == 250:
                    break

    except IOError as error:
        print(error)
        return

    ratings_data = [
        '{} - {}'.format(rank, value) for rank, value in ratings_gist.items()
    ]

    years_gist_items = sorted(years_gist.items())
    years_data = [
        '{}:{}'.format(year, value) for year, value in years_gist_items
    ]

    file_handler('top250_movies.txt', films_names)
    file_handler('ratings.txt', ratings_data)
    file_handler('years.txt', years_data)


if __name__ == '__main__':
    doc_parser()
