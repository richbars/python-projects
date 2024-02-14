
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


def main():
    quantidade = 0
    url = "https://www.unip.br/"  # Link da Documentação
    visited_urls = set()
    allLinksToVisite = [url]
    linkForaDominio = set()
    linkDentroDominio = set()
    link_404 = set()

    while allLinksToVisite:
        current_url = allLinksToVisite.pop(0)

        if current_url in visited_urls:
            continue



        try:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.content, "html.parser")

            visited_urls.add(current_url)

            # Extrair todos os links da página
            links = [
                urljoin(current_url, link["href"])
                for link in soup.find_all("a", href=True)
            ]

            # Adicionar os links encontrados para visitar posteriormente
            for link in links:
                if urlparse(link).netloc != urlparse(url).netloc:
                    linkForaDominio.add(link)  # Adiciona links fora do domínio apenas uma vez
                else:
                    linkDentroDominio.add(link)

            #quantidade += 1

            # # Limpa o print atual
            # print(f"{len(links)}")
            # print(links)
        except requests.exceptions.RequestException as e:
            # print(f"Erro ao acessar o link {current_url}: {e}")
            continue



    try:
        for link in linkDentroDominio:
            response = requests.get(link)
            if response.status_code != 200:
                link_404.add(link)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o link {link}: {e}")

    try:
        for link in linkForaDominio:
            response = requests.get(link)
            if response.status_code != 200:
                link_404.add(link)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o link {link}: {e}")

    # print(
    #     f"Links dentro do dominio: {len(linkDentroDominio)}\n"
    #     f"Links fora do dominio: {len(linkForaDominio)}\n"
    #     f"Quantidade de links scaneados: {quantidade}\n"
    # )

    if len(link_404) == 0:
        print("Nenhum link quebrado!")
    else:
        for link in link_404:
            print(f"\n - {link}")

    print(f"\nLinks dentro do Dominio:\n")
    for link in linkDentroDominio:
        print(f"\n- {link}")

    print(f"\nLinks fora do Dominio:\n")
    for link in linkForaDominio:
        print(f"\n- {link}")


if __name__ == "__main__":
    main()
