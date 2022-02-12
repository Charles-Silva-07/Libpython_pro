import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no github
    :param usuário str: com o nome do usuário no github
    :return str com o link do usuário
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar(input('Digite Seu usuário do github para ver seu avatar:')))
