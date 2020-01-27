import requests
from bs4 import BeautifulSoup

def main():
    """
    in url.txt only add links on every line for the show episode
    """
    f = open('output.txt', 'a+')
    with open('url.txt', 'r') as et:
        for episode in et:
            r = requests.get(episode.strip())
            r_html = r.text
            soup = BeautifulSoup(r_html,'html.parser')
            title = soup.find("h2", class_='title')
            f.write("\n=====================================\n")
            if not title:
                f.write('\n\nPrint for unknown title\n\n')
            else:
                f.write("\n\nGetting transcript for {}\n\n".format(title.text))
            data = soup.find("div", class_="entrytext")
            children = data.findChildren("p", class_='MsoNormal')
            for child in children:
                spanThis = child.findChildren('span')
                for span in spanThis:
                    """
                    TBD : The following print statement can be written to a file and the file can be named for every episode by using the
                    title variable above.
                    """
                    # print(span.text)
                    temp = str(span.text) + '\n'
                    f.write(temp)

if __name__ == '__main__':
    main()
