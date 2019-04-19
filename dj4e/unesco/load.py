import csv
from unesco.models import Category, Site, States, Region, Iso

fh = open('whc-sites-2018-small.csv')
rows = csv.reader(fh)

Category.objects.all().delete()
Site.objects.all().delete()
States.objects.all().delete()
Region.objects.all().delete()
Iso.objects.all().delete()

i = 0
for row in rows:
    if len(row[0]) < 1 : continue
    print(row[0])
    i = i + 1
    if i > 5 : break

    try:
        a = Category.objects.get(name=row[0])
    except:
        print("Inserting name",row[0])
        a = Category(name=row[0])
        a.save()

    try:
        b = States.objects.get(description=row[1])
    except:
        print("Inserting description",row[1])
        b = States(description=row[1])
        b.save()

    try:
        c = States.objects.get(justification=row[2])
    except:
        print("Inserting justification",row[2])
        c = States(justification=row[2])
        c.save()

    try:
        d = int(row[3])
    except:
        d = None

    # try:
    #     e = Region.objects.get(description=row[4])
    # except:
    #     print("Inserting longitude",row[4])
    #     e = Region(longitude=row[4])
    #     e.save()

    try:
        e = int(row[4])
    except:
        e = None

    # try:
    #     f = Region.objects.get(latitude=row[5])
    # except:
    #     print("Inserting latitude",row[5])
    #     f = Region(latitude=row[5])
    #     f.save()

    try:
        f = int(row[5])
    except:
        f = None

    # try:
    #     g = Region.objects.get(area_hectares=row[6])
    # except:
    #     print("Inserting area_hectares",row[6])
    #     g = Region(area_hectares=row[6])
    #     g.save()

    try:
        g = int(row[6])
    except:
        g = None

    try:
        h = States.objects.get(category=row[7])
    except:
        print("Inserting category",row[7])
        h = States(category=row[7])
        h.save()

    try:
        j = States.objects.get(states=row[8])
    except:
        print("Inserting states",row[8])
        j = States(states=row[8])
        j.save()

    try:
        k = Region.objects.get(region=row[9])
    except:
        print("Inserting region",row[9])
        k = Region(region=row[9])
        k.save()

    try:
        l = Site.objects.get(iso=row[10])
    except:
        print("Inserting iso",row[10])
        l = Site(iso=row[10])
        l.save()

    m = Site(name=a,description=b, justification=c, year=d, longitude=e, latitude=f, area_hectares=g, category=h, states=j, region=k, iso=l)
    m.save()