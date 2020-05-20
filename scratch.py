import json
import wikipediaapi


class WikiCountry:
    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        print(self.file)
        self.json = json.load(self.file)
        self.start = start
        print(self.start)
        self.wiki = wikipediaapi.Wikipedia('en')


    def __iter__(self):
        return self

    def __next__(self):
        print(self.start)
        self.start += 1
        if self.start == len(self.json):
            raise StopIteration
        country = self.json[self.start]['name']['common']
        country_page = self.wiki.page(country)
        country_link = country_page.fullurl
        #print(country, country_page, country_link)
        return country, country_link, self.start


if __name__ == '__main__':
        output_file = open('countries_link.txt', 'w')
        for country, item, num in WikiCountry('countries.json',0):
            try:
                print(country,item)
                output_file.write(str(num) + "." + str(country) + ' - ' + str(item) + '\n')
            except:
                print("Ошибка")
        output_file.close()