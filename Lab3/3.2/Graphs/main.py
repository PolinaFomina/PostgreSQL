import psycopg2
import matplotlib.pyplot as plt


def getNumber(line):
    i = 0

    while not line[i].isdigit():
        i = i + 1

    numberString = ""
    while line[i] != " ":
        numberString = numberString + line[i]
        i = i + 1

    return float(numberString)


connection = psycopg2.connect(
    database="IMDB",
    user="admin",
    password="1234",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM imdbdata")
result1 = cursor.fetchall()

plt.figure()
plt.xlabel("size KB")
plt.ylabel("time sec")
plt.xlim([0, 10])
plt.ylim([0, 0.5])

for id in range(0, result1[0][0], 10):
    print(id)
    cursor.execute("EXPLAIN (ANALYZE, Timing) SELECT data->>\'roles\' FROM imdbdata WHERE data->>\'id\' = \'{0}\'".format(id))
    time = getNumber(cursor.fetchall()[-1][0]) / 1000
    cursor.execute("SELECT pg_column_size(data)/1024 FROM imdbdata WHERE data->>'id' = \'{0}\'".format(id))
    size = cursor.fetchall()[0][0]
    plt.scatter(size, time, color='#0093f0', s=2)

plt.show()
