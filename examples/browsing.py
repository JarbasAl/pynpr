from pynpr import NRPBrowser

NPR = NRPBrowser()
for p in NPR.podcast_categories():
    print(p.name, p.url)

for p in NPR.get_featured_podcasts():
    print(p.name, p.url)

for show in NPR.get_shows():
    print(show.name, show.url, show.show_type)
